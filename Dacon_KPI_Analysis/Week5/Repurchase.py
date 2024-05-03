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
# print(payment_counts)


### 새코드
# 고객 ID 별로 주문 날짜를 정렬하여, 각 고객의 주문 횟수 및 날짜 차이 계산
low_aov_customers_orders = data["orders"][data["orders"]["Customer_id"].isin(aov_group.index)].sort_values(by=["Customer_id", "Order_purchase_timestamp"])

# 고객별 주문 횟수 계산
customer_reorder_counts = low_aov_customers_orders.groupby("Customer_id").size()

# 재구매한 고객만 필터링
reordered_customers = customer_reorder_counts[customer_reorder_counts > 1].index

# 재구매한 고객과 그렇지 않은 고객의 비율 계산
reordered_ratio = len(reordered_customers) / len(aov_group) * 100
not_reordered_ratio = 100 - reordered_ratio

print('재구매한 인원 수')
print(len(reordered_customers))

# 원 그래프로 재구매한 사람과 하지 않은 사람의 비율 표시
plt.figure(figsize=(10, 7))
plt.pie([reordered_ratio, not_reordered_ratio], labels=["재구매한 고객", "재구매하지 않은 고객"], autopct='%1.1f%%', startangle=140)
plt.title('AOV가 0~10인 고객의 재구매율')
plt.show()

# 재구매한 고객들의 첫 구매와 두 번째 구매 날짜 차이 계산 및 출력
for customer_id in reordered_customers:
    customer_orders = low_aov_customers_orders[low_aov_customers_orders["Customer_id"] == customer_id]
    first_order_date = pd.to_datetime(customer_orders.iloc[0]["Order_purchase_timestamp"])
    second_order_date = pd.to_datetime(customer_orders.iloc[1]["Order_purchase_timestamp"])
    date_diff = (second_order_date - first_order_date).days
    print(f"고객 ID: {customer_id}, 첫 구매와 두 번째 구매 사이의 날짜 차이: {date_diff}일")



# # 원 그래프로 표시
# plt.figure(figsize=(10, 10))
# plt.pie(payment_counts['count'], labels=payment_counts['Payment_type'], autopct='%1.1f%%', startangle=140)
# plt.title('AOV가 0~10인 고객의 결제 방법별 시퀀스 분포')
# plt.show()
