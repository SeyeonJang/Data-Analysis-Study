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
    "products": "../../Dacon_KPI/products.csv"
}

# 데이터 불러오기
data = {}
for name, file in files.items():
    data[name] = pd.read_csv(file)

# 주문 시간을 날짜 형식으로 변환
data["orders"]["Order_purchase_timestamp"] = pd.to_datetime(data["orders"]["Order_purchase_timestamp"])

# 2018년 01월 이후의 데이터 필터링
data["orders"] = data["orders"][data["orders"]["Order_purchase_timestamp"] >= "2018-01-01"]

# orders와 order_items 합치기
merged_data = pd.merge(data["orders"], data["order_items"], on="Order_id")

# Customer_id 별로 총 주문액 구하기
customer_total_order_value = merged_data.groupby("Customer_id")["Price"].sum()

# Customer_id 별로 주문건수 구하기
customer_order_counts = merged_data.groupby("Customer_id")["Order_id"].nunique()

# merged_data와 products 데이터 합치기
complete_data = pd.merge(merged_data, data["products"], on='Product_id')

# 평균 주문 가치(AOV) 계산
average_order_value_per_customer = customer_total_order_value / customer_order_counts

# AOV를 기준으로 각 고객을 평균보다 낮은 그룹과 높은 그룹으로 분류
low_aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 10) & (average_order_value_per_customer < 60)]
high_aov_group = average_order_value_per_customer[(average_order_value_per_customer >= 200) & (average_order_value_per_customer < 300)]

# 고객 ID별로 평균보다 낮은 그룹과 높은 그룹에서 주문된 상품 카테고리별로 판매량을 계산
low_group_sales = complete_data[complete_data['Customer_id'].isin(low_aov_group.index)].groupby('Product_category_name')['Order_id'].count().sort_values(ascending=False).head(10)
high_group_sales = complete_data[complete_data['Customer_id'].isin(high_aov_group.index)].groupby('Product_category_name')['Order_id'].count().sort_values(ascending=False).head(10)

# 원 그래프로 표현
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

ax[0].pie(low_group_sales, labels=low_group_sales.index, autopct='%1.1f%%', startangle=140)
ax[0].set_title('AOV가 10~60인 상위 10개 판매 카테고리')

ax[1].pie(high_group_sales, labels=high_group_sales.index, autopct='%1.1f%%', startangle=140)
ax[1].set_title('AOV가 200~300인 상위 10개 판매 카테고리')

plt.tight_layout()
plt.show()
