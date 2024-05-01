# 주문 상태 출력

import pandas as pd

orders = "../../Dacon_KPI/orders.csv"
df = pd.read_csv(orders)

order_statuses = df['Order_status'].unique()
for status in order_statuses:
    print(status)