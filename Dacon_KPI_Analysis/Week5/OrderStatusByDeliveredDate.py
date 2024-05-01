# 주문 상태 출력

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

orders = "../../Dacon_KPI/orders.csv"
df = pd.read_csv(orders)

# 필요한 컬럼을 datetime 타입으로 변환
df['Order_delivered_customer_date'] = pd.to_datetime(df['Order_delivered_customer_date'])
df['Order_estimated_delivery_date'] = pd.to_datetime(df['Order_estimated_delivery_date'])

# 주문 상태가 'canceled'인 데이터 필터링
canceled_orders = df[df['Order_status'] == 'canceled']
# Pandas 출력 옵션 설정
pd.set_option('display.max_columns', None)  # 모든 열을 보기 위한 설정
pd.set_option('display.max_rows', None)  # 모든 행을 보기 위한 설정

# 원하는 컬럼 선택하여 출력
print(canceled_orders[['Order_id', 'Order_status', 'Order_purchase_timestamp', 'Order_delivered_carrier_date', 'Order_delivered_customer_date', 'Order_estimated_delivery_date']])


# # 기대 배송 날짜보다 실제 배송 날짜가 앞일 때의 데이터 필터링
# earlier_than_expected = df[df['Order_delivered_customer_date'] < df['Order_estimated_delivery_date']]
#
# # 기대 배송 날짜보다 실제 배송 날짜가 뒤일 때의 데이터 필터링
# later_than_expected = df[df['Order_delivered_customer_date'] > df['Order_estimated_delivery_date']]
#
# # 함수 정의: 원 그래프 그리기
# def plot_pie(dataframe, title):
#     status_counts = dataframe['Order_status'].value_counts()
#     plt.figure(figsize=(8, 8))
#     plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
#     plt.title(title)
#     plt.show()
#
# # 기대 배송 날짜보다 실제 배송 날짜가 앞일 때의 원 그래프
# plot_pie(earlier_than_expected, '기대 배송 날짜보다 실제 배송 날짜가 앞인 주문의 상태')
#
# # 기대 배송 날짜보다 실제 배송 날짜가 뒤일 때의 원 그래프
# plot_pie(later_than_expected, '기대 배송 날짜보다 실제 배송 날짜가 뒤인 주문의 상태')
