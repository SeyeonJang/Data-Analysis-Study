import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 파일 로드
customers = pd.read_csv('../../Dacon_KPI/customers.csv')
orders = pd.read_csv('../../Dacon_KPI/orders.csv')
order_items = pd.read_csv('../../Dacon_KPI/order_items.csv')

# 2018-01-01 이후 데이터 필터링
orders["Order_purchase_timestamp"] = pd.to_datetime(orders["Order_purchase_timestamp"])
filtered_orders = orders[orders["Order_purchase_timestamp"] >= "2018-01-01"]

# 주문 아이템 정보 합치기
merged_order_items = pd.merge(filtered_orders[["Order_id", "Customer_id"]], order_items, on="Order_id")

# Customer_id 별로 각 구매에서 몇 개의 제품을 구입했는지
item_counts_per_purchase = merged_order_items.groupby(["Customer_id", "Order_id"]).size()

# Customer_id 별 구매 별 제품 구입 개수의 평균
average_items_per_customer = item_counts_per_purchase.groupby(level=0).mean()

# 바 그래프 시각화
plt.figure(figsize=(10, 6))
average_items_per_customer.value_counts().sort_index().plot(kind='bar')
plt.title('Customer 평균 구매 제품 수')
plt.xlabel('평균 구매 제품 수')
plt.ylabel('사람 수')
plt.show()
