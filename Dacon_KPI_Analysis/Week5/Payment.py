# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import rc
#
# # 한글 폰트 설정
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False
#
# # 데이터 파일 경로
# files = {
#     "order_items": "../../Dacon_KPI/order_items.csv",
#     "orders": "../../Dacon_KPI/orders.csv",
#     "products": "../../Dacon_KPI/products.csv",
#     "payments": "../../Dacon_KPI/payments.csv"
# }
#
# # 데이터 불러오기
# data = {}
# for name, file in files.items():
#     data[name] = pd.read_csv(file)
#
# # 주문 시간을 날짜 형식으로 변환
# data["orders"]["Order_purchase_timestamp"] = pd.to_datetime(data["orders"]["Order_purchase_timestamp"])
# # 2018년 01월 이후의 데이터 필터링
# data["orders"] = data["orders"][data["orders"]["Order_purchase_timestamp"] >= "2018-01-01"]
# # orders와 order_items 합치기
# merged_data = pd.merge(data["orders"], data["order_items"], on="Order_id")
# # Customer_id 별로 총 주문액 구하기
# customer_total_order_value = merged_data.groupby("Customer_id")["Price"].sum()
# # Customer_id 별로 주문건수 구하기
# customer_order_counts = merged_data.groupby("Customer_id")["Order_id"].nunique()
# # 평균 주문 가치(AOV) 계산
# average_order_value_per_customer = customer_total_order_value / customer_order_counts
#
# # AOV가 0에서 10 사이인 고객 그룹 필터링
# aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 0) & (average_order_value_per_customer < 10)]
#
# # merged_data와 payments 데이터 합치기
# complete_payments_data = pd.merge(merged_data, data["payments"], on='Order_id')
# # 평균 AOV가 0에서 10 사이인 고객 그룹에 대한 결제 데이터 필터링
# low_aov_payments = complete_payments_data[complete_payments_data['Customer_id'].isin(aov_group.index)]
# # 결제 시퀀스가 1보다 큰 데이터 필터링
# multiple_payments = low_aov_payments[low_aov_payments['Payment_sequential'] > 1]
#
# # 다수의 결제 방법을 사용한 시퀀스별 카운트 계산
# multiple_payment_counts = multiple_payments['Payment_sequential'].value_counts().sort_index()
#
# # 바 그래프로 표시
# plt.figure(figsize=(10, 6))
# multiple_payment_counts.plot.bar()
# plt.title('AOV가 0~10인 고객의 다수 결제 시퀀스 분포')
# plt.xlabel('결제 시퀀스')
# plt.ylabel('카운트')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# 이미 주어진 조건과 같이 한글 폰트 설정
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 파일 경로
files = {
    "order_items": "../../Dacon_KPI/order_items.csv",
    "orders": "../../Dacon_KPI/orders.csv",
    "payments": "../../Dacon_KPI/payments.csv"
}

# 데이터 불러오기
data = {}
for name, file in files.items():
    data[name] = pd.read_csv(file)

# orders와 order_items 합치기
merged_data = pd.merge(data["orders"], data["order_items"], on="Order_id")

# Customer_id 별로 총 주문액 구하기
customer_total_order_value = merged_data.groupby("Customer_id")["Price"].sum()

# Customer_id 별로 주문건수 구하기
customer_order_counts = merged_data.groupby("Customer_id")["Order_id"].nunique()

# 평균 주문 가치(AOV) 계산
average_order_value_per_customer = customer_total_order_value / customer_order_counts

# AOV가 0에서 10 사이인 고객 그룹 필터링
aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 0) & (average_order_value_per_customer < 10)]

# merged_data와 payments 데이터 합치기
complete_payments_data = pd.merge(merged_data, data["payments"], on='Order_id')

# 평균 AOV가 0에서 10 사이인 고객 그룹에 대한 결제 데이터 필터링
low_aov_payments = complete_payments_data[complete_payments_data['Customer_id'].isin(aov_group.index)]

# 결제 방법 & 시퀀스를 함께 고려하여 카운트 계산
payment_counts = low_aov_payments.groupby(['Payment_type', 'Payment_sequential']).size().reset_index(name='count')

# Payment_type으로 다시 그룹화하여 카운트 계산
payment_counts = payment_counts.groupby('Payment_type')['count'].sum().reset_index()
print(payment_counts)

# 원 그래프로 표시
plt.figure(figsize=(10, 10))
plt.pie(payment_counts['count'], labels=payment_counts['Payment_type'], autopct='%1.1f%%', startangle=140)
plt.title('AOV가 0~10인 고객의 결제 방법별 시퀀스 분포')
plt.show()
