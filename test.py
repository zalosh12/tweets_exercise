import pandas as pd
df = pd.read_csv(r"C:\Users\eliwa\PycharmProjects\tweets_project\data\tweets_dataset.csv")
print(df.head())

from src import investigator
m = investigator.Investigator(df)
# m.add_word_count()
print(m.df.columns)
print(m.get_average_len())
print(m.get_common_words())