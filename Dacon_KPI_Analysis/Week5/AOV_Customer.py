import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 파일을 읽기
orders = pd.read_csv('../../Dacon_KPI/orders.csv')
order_items = pd.read_csv('../../Dacon_KPI/order_items.csv')

# orders에서 2018년 01월 이후 데이터 필터링
orders['Order_purchase_timestamp'] = pd.to_datetime(orders['Order_purchase_timestamp'])
filtered_orders = orders[orders['Order_purchase_timestamp'] >= '2018-01-01']

# orders와 order_items 합치기
merged_data = pd.merge(filtered_orders, order_items, on='Order_id')

# Customer_id 별로 총 주문액 구하기
customer_total_order_value = merged_data.groupby('Customer_id')['Price'].sum()

# Customer_id 별로 주문건수 구하기
customer_order_counts = merged_data.groupby('Customer_id')['Order_id'].nunique()

# 평균 주문 가치(AOV) 계산
average_order_value_per_customer = customer_total_order_value / customer_order_counts

# average_order_value_per_customer을 구간별로 나누기 (예: 1000원 단위로 끊기)
aov_bins = pd.cut(average_order_value_per_customer, bins=range(0, int(average_order_value_per_customer.max()) + 10, 10))

# 구간별 인원수 세기
aov_bins_counts = aov_bins.value_counts().sort_index()

# 고객 당 평균 구매 가치(AOV)의 평균 계산
avg_aov_mean = average_order_value_per_customer.mean()

# 계산된 평균 출력
print(f"고객 당 평균 구매 가치(AOV)의 평균: {avg_aov_mean:.2f}원")

# 바 그래프 그리기
plt.figure(figsize=(12, 6))
aov_bins_counts.head(30).plot(kind='bar')
plt.title('고객 당 평균 구매 가치(AOV)')
plt.xlabel('평균 구매 금액')
plt.ylabel('고객 수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
