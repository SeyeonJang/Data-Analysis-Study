# 고객 ID와 고객 주문 ID가 다른가?

import pandas as pd

# CSV 파일 경로
customers = "../../Dacon_KPI/customers.csv"
df = pd.read_csv(customers)

customer_id_count = df['Customer_id'].nunique()
customer_unique_id_count = df['Customer_unique_id'].nunique()

print("고객 ID의 개수:", customer_id_count)
print("고객 고유 ID의 개수:", customer_unique_id_count)