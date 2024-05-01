# 주문 상태 출력

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
orders_df = pd.read_csv('../../Dacon_KPI/orders.csv')
order_items_df = pd.read_csv('../../Dacon_KPI/order_items.csv')

# 주문 시간에서 월 정보 추출
orders_df['Order_purchase_timestamp'] = pd.to_datetime(orders_df['Order_purchase_timestamp'])
orders_df['month'] = orders_df['Order_purchase_timestamp'].dt.to_period('M')

# orders와 order_items 병합
merged_df = pd.merge(orders_df, order_items_df, on='Order_id')

# 월별 매출액 계산
monthly_sales = merged_df.groupby('month')['Price'].sum()

# 가장 매출이 높은 월을 찾습니다.
max_sales_value = monthly_sales.max()  # 최대 매출액
max_sales_month = monthly_sales.idxmax()  # 최대 매출액을 기록한 월

print(f"가장 매출이 높은 월: {max_sales_month}, 매출액: {max_sales_value}")


# 매출액 바 그래프로 시각화
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='bar')
plt.title('월별 매출액')
plt.xlabel('월')
plt.ylabel('매출액')
plt.xticks(rotation=45)
plt.show()


# 월별 총 매출액을 총 주문 건수로 나눈 값 (평균 주문 가치)

# 월별 주문 건수 계산
monthly_order_count = merged_df.groupby('month')['Order_id'].nunique()
# 월별 평균 주문 가치 계산
monthly_avg_order_value = monthly_sales / monthly_order_count
# 평균 주문 가치 바 그래프로 시각화
plt.figure(figsize=(10,6))
monthly_avg_order_value.plot(kind='bar', color='orange')
plt.title('월별 평균 주문 가치')
plt.xlabel('월')
plt.ylabel('평균 주문 가치')
plt.xticks(rotation=45)
plt.show()