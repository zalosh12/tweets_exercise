import pandas as pd

from src.data_analyzer import DataAnalyzer

df = pd.read_csv(r"C:\Users\eliwa\PycharmProjects\tweets_project\data\tweets_dataset.csv")

from src.cleaner import Cleaner

cg = Cleaner(df)
print(cg.df)
# from src import data_analyzer
# m = DataAnalyzer(df)
# # m.add_word_count()
# print(m.df.columns)
# print(m.count_by_category())
# print(m.get_average_len())
# print(m.get_common_words())
# print(m.get_upper_words())
# m.three_longest_tweets()
# print(m.result.keys())