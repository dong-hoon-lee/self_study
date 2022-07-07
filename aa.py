import pandas as pd

class Test:
    global df
    df = pd.read_csv('./Kmooc/stock_pricing/data/snp500.csv')

    def __init__(self):
        self.a = None

    def df_to_dict(self):
        self.aa = df
        return self.aa

# t = Test(df)
# print(t.df_to_dict())