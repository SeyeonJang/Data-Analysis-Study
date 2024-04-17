import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
sales_info = pd.read_csv("../Onlinesales_info.csv")
customer_info = pd.read_csv("../Customer_info.csv")
discount_info = pd.read_csv("../Discount_info.csv")
marketing_info = pd.read_csv("../Marketing_info.csv")
tax_info = pd.read_csv("../Tax_info.csv")

# 필요한 정보를 병합
merged_sales_customer = pd.merge(sales_info, customer_info, on="고객ID")

# 거래날짜 컬럼을 datetime 형식으로 변환
merged_sales_customer['거래날짜'] = pd.to_datetime(merged_sales_customer['거래날짜'])

# 월별 매출을 계산하기 위해 월 정보 컬럼 추가
merged_sales_customer['년/월'] = merged_sales_customer['거래날짜'].dt.to_period('M')

# 카테고리별로 그룹화하여 월별 매출 계산
monthly_sales_by_category = merged_sales_customer.groupby(['년/월', '제품카테고리'])['평균금액'].sum().unstack().fillna(0)

# 시각화
plt.figure(figsize=(12, 6))
monthly_sales_by_category.plot(kind='bar', stacked=True)
plt.title('월별 카테고리별 매출')
plt.xlabel('년/월')
plt.ylabel('매출량')
plt.xticks(rotation=45)
plt.legend(title='카테고리', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 카테고리별로 월별 매출 합계 계산
monthly_sales_sum = merged_sales_customer.groupby(['년/월', '제품카테고리'])['평균금액'].sum()

# 각 년/월에 대해 매출이 가장 높은 상위 3개 카테고리 선택
top_3_categories_per_month = monthly_sales_sum.groupby(level=0).nlargest(3).reset_index(level=0, drop=True).unstack().reset_index()

# 각 년/월에 대해 상위 3개의 카테고리와 매출액을 새로운 열로 추가
top_3_categories_per_month[['상위1_카테고리', '상위1_매출액', '상위2_카테고리', '상위2_매출액', '상위3_카테고리', '상위3_매출액']] = top_3_categories_per_month.apply(lambda row: pd.Series(row.values), axis=1)

# 컬럼 이름 변경
# 컬럼 이름 변경
top_3_categories_per_month.columns = ['년/월',
                                      '상위1_카테고리', '상위1_매출액',
                                      '상위2_카테고리', '상위2_매출액',
                                      '상위3_카테고리', '상위3_매출액']


# 결과 출력
print("년/월마다 매출이 가장 높은 상위 3개 카테고리와 매출액:")
print(top_3_categories_per_month)
