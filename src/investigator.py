import pandas as pd
from collections import Counter

class Investigator:
    # Investigate data of tweets from Twitter
    def __init__(self,tweets_df):
        self.df = tweets_df.copy()

    def count_by_category(self):
        # count total tweets and tweets by category
        category_dict = self.df['Biased'].values_count.to_dict()
        total = self.df['Biased'].count()
        return {
            "total":total,
            "category_dict":category_dict
        }

    # def add_word_count(self):
    #     #add column to data frame to hold len of the tweet
    #     self.df['text_length'] = self.df['Text'].apply(
    #         lambda x: len(x.split()))

    def get_average_len(self):
        # add a column to The DataFrame to hold len of tweet by word
        self.df['text_length'] = self.df['Text'].apply(
                    lambda x: len(x.split()))

        # the average len by all Data frame
        total_mean = self.df['text_length'].mean()

        #analyze average len by category
        mean_by_category = self.df.groupby('Biased')['text_length'].mean().to_dict()
        mean_by_category['total'] = total_mean

        return mean_by_category

    def three_longest_tweets(self):
        pass

    def get_common_words(self):
        # analyze the most common words in the data
        words = ",".join(self.df['Text'].values).lower()
        words_counter = Counter(words.split())
        top_10_common = words_counter.most_common(10)
        return top_10_common

    def get_upper_words(self):
        total_words = ",".join(self.df['Text'].values)


        pass






