import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")

onlinesales_info = pd.read_csv('../Onlinesales_info.csv')
customer_info = pd.read_csv('../Customer_info.csv')

# 고객ID를 기준으로 두 데이터프레임을 조인
merged_data = pd.merge(customer_info, onlinesales_info, on='고객ID')

# 거래날짜를 월별로 변환하여 새로운 열을 생성
merged_data['거래월'] = pd.to_datetime(merged_data['거래날짜']).dt.to_period('M')

# 고객의 지역에 따른 월별 매출을 계산
monthly_sales_by_region = merged_data.groupby(['거래월','고객지역'])['평균금액'].sum().unstack(fill_value=0)
print(monthly_sales_by_region)

monthly_sales_by_region.plot.bar()

plt.show()