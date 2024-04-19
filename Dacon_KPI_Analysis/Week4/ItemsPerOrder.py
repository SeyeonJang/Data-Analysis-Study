# 동일한 주문에 포함된 품목 수로 그룹화

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 경로
order_items = "../../Dacon_KPI/order_items.csv"

# CSV 파일을 읽어와 DataFrame으로 변환
df = pd.read_csv(order_items)

# 주문별 품목 수 계산
item_counts = df.groupby('Order_id')['Order_item_id'].max()

# 품목 수 별로 그룹화하고, 각 그룹의 판매량(주문 수) 집계
sales_per_item_count = item_counts.value_counts().sort_index()

# 결과 시각화
plt.figure(figsize=(10, 6))
sales_per_item_count.plot(kind='bar')
plt.title('품목 수 별 주문 수')
plt.xlabel('구매 품목 수')
plt.ylabel('주문 수')
plt.xticks(rotation=0)
plt.grid(axis='y')

plt.show()

print(sales_per_item_count)