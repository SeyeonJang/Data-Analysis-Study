# 거래량이 많은 카테고리

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

online_sales_file = "../Onlinesales_info.csv"
online_sales_df = pd.read_csv(online_sales_file)
online_sales_df['거래날짜'] = pd.to_datetime(online_sales_df['거래날짜'])

recent_sales_date = online_sales_df['거래날짜'].max()  # 데이터 안에서 가장 최근의 거래 날짜를 구합니다.
recent_year_sales = online_sales_df[online_sales_df['거래날짜'] >= recent_sales_date - pd.DateOffset(years=1)]

category_sales_count = recent_year_sales['제품카테고리'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
category_sales_count.plot(kind='bar')
plt.title('최근 1년 간 거래 횟수가 높은 카테고리')
plt.xlabel('카테고리')
plt.ylabel('거래량')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
