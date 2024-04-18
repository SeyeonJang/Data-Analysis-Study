# 활동 고객과 휴면 고객의 매출액

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 파일명과 경로를 각각의 변수에 저장합니다.
customer_info_file = "../Customer_info.csv"
online_sales_file = "../Onlinesales_info.csv"

customer_info_df = pd.read_csv(customer_info_file)
online_sales_df = pd.read_csv(online_sales_file)

online_sales_df['거래날짜'] = pd.to_datetime(online_sales_df['거래날짜'])
recent_transaction_date = online_sales_df.groupby('고객ID')['거래날짜'].max().reset_index()

current_date = recent_transaction_date['거래날짜'].max()

# 휴면 고객
dormant_customers = recent_transaction_date[
    (current_date - recent_transaction_date['거래날짜']).dt.days >= 90]
# 활동 고객
active_customers = recent_transaction_date[
    (current_date - recent_transaction_date['거래날짜']).dt.days < 90]

# 각 고객의 매출을 계산
online_sales_with_customer = pd.merge(online_sales_df, customer_info_df, on='고객ID', how='inner')
dormant_sales = online_sales_with_customer[online_sales_with_customer['고객ID'].isin(dormant_customers['고객ID'])]['평균금액'].sum()
active_sales = online_sales_with_customer[online_sales_with_customer['고객ID'].isin(active_customers['고객ID'])]['평균금액'].sum()

# 휴면 고객과 활동 고객의 매출을 합산
total_sales = dormant_sales + active_sales

# 매출 비율을 계산
dormant_sales_ratio = dormant_sales / total_sales * 100
active_sales_ratio = active_sales / total_sales * 100

print("휴면 고객 매출:", dormant_sales)
print("활동 고객 매출:", active_sales)

plt.figure(figsize=(10, 6))
plt.pie([active_sales_ratio, dormant_sales_ratio], labels=['활동 고객', '휴면 고객'], autopct='%1.1f%%', startangle=140)
plt.title('활동 고객과 휴면 고객 매출 비율')
plt.axis('equal')
plt.show()
