import pandas as pd

csv_file_path = '../Customer_info.csv'

df = pd.read_csv(csv_file_path)

# DataFrame 출력
print(df)