import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
plt.close("all")

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
sales_df = pd.read_csv("../Onlinesales_info.csv")

# 거래 날짜를 날짜 형식으로 변환
sales_df['거래날짜'] = pd.to_datetime(sales_df['거래날짜'])

# 각 고객의 구매 간격 계산
purchase_intervals = sales_df.groupby('고객ID')['거래날짜'].apply(lambda x: x.diff().mean()).reset_index()
purchase_intervals.columns = ['고객ID', '평균구매주기']

# 평균 구매 주기를 일(day)로 변환
purchase_intervals['평균구매일수'] = purchase_intervals['평균구매주기'].dt.days

# 고객별 평균 구매 주기가 NaN인 경우를 제거
purchase_intervals = purchase_intervals.dropna()

# 일(day) 단위로 그룹화하여 평균 구매 주기 계산
average_purchase_interval = purchase_intervals.groupby('평균구매일수').size().reset_index(name='고객수')
print(average_purchase_interval)
# 그래프 그리기
plt.bar(average_purchase_interval['평균구매일수'], average_purchase_interval['고객수'])
plt.xlabel('평균 구매 일수')
plt.ylabel('고객 수')
plt.title('평균 구매 주기별 고객 수')
plt.xticks(rotation=70)
plt.show()