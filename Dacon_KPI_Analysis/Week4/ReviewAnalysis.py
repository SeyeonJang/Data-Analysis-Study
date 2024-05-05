# 리뷰를 분석해보자!

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 경로
reviews = "../../Dacon_KPI/reviews.csv"
df = pd.read_csv(reviews)


# [분석] 모든 리뷰에 생성시간과 답변시간이 있는가?
print("리뷰 생성 시간이 있는지 여부:", not df['Review_creation_date'].isnull().any())
print("리뷰 답변 시간이 있는지 여부:", not df['Review_answer_timestamp'].isnull().any())


# [분석] 리뷰의 생성 시간과 답변 시간의 차이는?
df['Review_creation_date'] = pd.to_datetime(df['Review_creation_date'])
df['Review_answer_timestamp'] = pd.to_datetime(df['Review_answer_timestamp'])
# 생성 시간과 답변 시간의 차이 계산 (시간 단위)
df['Response_time_hours'] = (df['Review_answer_timestamp'] - df['Review_creation_date']) / pd.Timedelta(hours=1)
# 생성 시간과 답변 시간의 차이를 기준으로 그룹화하고, 각 그룹의 개수 계산
response_time_grouped = df['Response_time_hours'].round().astype(int).value_counts().sort_index()
# 그래프 그리기
plt.figure(figsize=(10, 6))
response_time_grouped.plot(kind='bar')
plt.title('리뷰 답변 시간 차이에 따른 그룹화')
plt.xlabel('생성시간과 답변 시간의 차이 (시간)')
plt.ylabel('리뷰 개수')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()