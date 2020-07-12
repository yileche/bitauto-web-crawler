import pandas as pd

df = pd.read_csv(r'/Users/cheyile/PycharmProjects/SScrapy/bitauto/bitauto/bitauto4.csv', low_memory=False)
df.drop_duplicates(keep='first', inplace=True)
df.to_csv(r'/Users/cheyile/PycharmProjects/SScrapy/bitauto/bitauto4quchong.csv')