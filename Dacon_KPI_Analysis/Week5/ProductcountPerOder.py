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
    "customers": "../../Dacon_KPI/customers.csv"  # 고객 데이터 파일 경로 추가
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
aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 10) & (average_order_value_per_customer < 60)]

# # AOV가 0에서 10 사이인 고객의 고유 ID 필터링
# aov_customers = aov_group.index
#
# # AOV 조건에 맞는 고객 데이터 필터링
# filtered_orders = merged_data[merged_data['Customer_unique_id'].isin(aov_customers)]
#
# # 주문당 상품 개수 계산
# order_product_counts = filtered_orders.groupby('Order_id')['Order_item_id'].count()
#
# # 주문당 상품 개수별로 주문 수 계산
# product_count_distribution = order_product_counts.value_counts().sort_index()
#
# # 바 그래프 생성
# plt.figure(figsize=(10, 6))
# product_count_distribution.plot(kind='bar')
# plt.title('주문당 상품 개수별 주문 수')
# plt.xlabel('구매 개수')
# plt.ylabel('해당 구매 개수의 주문 수')
# plt.xticks(rotation=0) # x축 라벨 회전
# plt.show()

# AOV 그룹에 속하는 고객의 주문 데이터 필터링
filtered_data = merged_data[merged_data["Customer_unique_id"].isin(aov_group.index)]

# 주문당 상품 개수 계산
order_product_counts = filtered_data.groupby("Order_id").size()

# 상품 개수별 주문 수 집계
product_count_distribution = order_product_counts.value_counts().sort_index()

# 전체 주문 대비 상품 개수별 주문의 비율 계산
order_percentage = (product_count_distribution / product_count_distribution.sum()) * 100
print(order_percentage)

# 바 그래프 시각화
order_percentage.plot(kind='bar')
plt.xlabel('상품 개수')
plt.ylabel('주문 비율 (%)')
plt.title('주문당 평균 상품 개수 비율')
plt.show()