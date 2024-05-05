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
    "customers": "../../Dacon_KPI/customers.csv",
    "payments": "../../Dacon_KPI/payments.csv"
}

# 데이터 불러오기
data = {}
for name, file in files.items():
    data[name] = pd.read_csv(file)

# orders와 customers 데이터 합치기 (Customer_id 기준)
orders_customers_merged = pd.merge(data["orders"], data["customers"], on="Customer_id")

# orders_customers_merged와 order_items 데이터 합치기 (Order_id 기준)
merged_data = pd.merge(orders_customers_merged, data["order_items"], on="Order_id")

# Customer_unique_id 별로 총 주문액 구하기
customer_total_order_value = merged_data.groupby("Customer_unique_id")["Price"].sum()

# Customer_unique_id 별로 주문건수 구하기
customer_order_counts = merged_data.groupby("Customer_unique_id")["Order_id"].nunique()

# 평균 주문 가치(AOV) 계산
average_order_value_per_customer = customer_total_order_value / customer_order_counts

# AOV가 0에서 10 사이인 고객 그룹 필터링
aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 200) & (average_order_value_per_customer < 300)]

# AOV 그룹의 Customer_unique_id를 기반으로 필터링된 주문 데이터를 payments 데이터와 결합
aov_orders = merged_data[merged_data['Customer_unique_id'].isin(aov_group.index)]
payments_filtered = pd.merge(aov_orders, data["payments"], on="Order_id")

print('주문 수 :',len(aov_orders))

# 할부 개월수별로 주문 수 집계
installments_counts = payments_filtered['Payment_installments'].value_counts().sort_index()
print('할부 개월 수 별 주문 수')
print(installments_counts)

# 바 그래프로 시각화
plt.figure(figsize=(10, 6))
installments_counts.plot(kind='bar')
plt.title('AOV가 200에서 300 사이인 고객 그룹의 할부 개월수별 주문 수')
plt.xlabel('할부 개월수')
plt.ylabel('주문 수')
plt.xticks(rotation=0)
plt.show()