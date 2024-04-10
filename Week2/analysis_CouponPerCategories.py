import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")

# CSV 파일 경로
csv_file_path = "../Onlinesales_info.csv"

# CSV 파일을 읽어와 DataFrame으로 변환
df = pd.read_csv(csv_file_path)

# 제품 카테고리별 쿠폰 사용 횟수 계산
coupon_counts = df.groupby('제품카테고리')['쿠폰상태'].value_counts().unstack().fillna(0)
# ['쿠폰상태'].value_counts : 쿠폰 상태 별로 개수 세기
# unstack : 다중 인덱스를 가진 결과를 다시 데이터프레임 형태로 변환
# fillna(0) : 결측값(NaN)을 0으로 채움

# 쿠폰 사용 횟수에서 비율로 변환
coupon_ratios = coupon_counts.div(coupon_counts.sum(axis=1), axis=0)
# coupon_counts.sum(axis=1) : 제품 카테고리별로 쿠폰 사용 횟수의 총합을 계산
# coupon_counts.div(coupon_counts.sum(axis=1), axis=0) : 각 셀의 값을 해당 행의 합으로 나누어 쿠폰 사용 비율을 계산

# 결과 출력
print("[제품 카테고리별 쿠폰 사용 비율]")
print(coupon_ratios)

coupon_ratios.plot.bar(stacked=True)
plt.show()