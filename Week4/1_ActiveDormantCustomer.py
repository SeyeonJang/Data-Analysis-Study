import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

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

# 휴면 고객과 활동 고객의 수
dormant_count = len(dormant_customers)
active_count = len(active_customers)
print("휴면 고객 수:", dormant_count)
print("활동 고객 수:", active_count)

plt.figure(figsize=(10, 6))
plt.pie([active_count, dormant_count], labels=['활동 고객', '휴면 고객'], autopct='%1.1f%%', startangle=140)
plt.title('활동 고객과 휴면 고객 비율')
plt.axis('equal')  
plt.show()
