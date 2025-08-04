import pandas as pd
from collections import Counter

class DataAnalyzer:
    # Investigate data of tweets from Twitter
    def __init__(self,tweets_df):
        self.df = tweets_df.copy()
        self.result = {}

        self.add_category_column()
        self.count_tweets_by_category()
        self.get_average_len()
        self.three_longest_tweets()
        self.get_upper_words()
        self.get_common_words()

    def add_category_column(self):
        """function to  create new column to categorize data"""
        categories = {1:"antisemitic",0:"non_antisemitic"}
        self.df["category"] = self.df['Biased'].apply(
            lambda x: categories.get(x,"unspecified")
        )



    def count_tweets_by_category(self):
        """function to analyze How many tweets are there from each category
             (by category, unspecified, and total) """
        category_dict = self.df['category'].value_counts().to_dict()
        category_dict['total'] = self.df['category'].count()
        self.result['total_tweets'] = category_dict


    def get_average_len(self):
        # add a column to The DataFrame to hold len of tweet by word
        self.df['text_length'] = self.df['Text'].apply(
                    lambda x: len(x.split()))

        # the average len by all Data frame
        total_mean = self.df['text_length'].mean()

        #analyze average len by category
        mean_by_category = self.df.groupby('category')['text_length'].mean().to_dict()
        mean_by_category['total'] = total_mean

        self.result['average_length'] = mean_by_category
        return mean_by_category

    def three_longest_tweets(self) :

        self.df['char_sum'] = self.df['Text'].str.replace(" ", "").str.len()

        top_3_tweets = self.df.groupby('category', group_keys=False).apply(
            lambda x : x.nlargest(3, 'char_sum')
        ).reset_index(drop=True)

        top_3_dict = top_3_tweets.groupby('category')['Text'].apply(list).to_dict()
        self.result["longest_3_tweets"] = top_3_dict

    def get_common_words(self):
        # analyze the most common words in the data
        words = ",".join(self.df['Text'].values).lower()
        words_counter = Counter(words.split())
        top_10_common = words_counter.most_common(10)
        self.result["common_words"] = {'total':[i[0] for i in top_10_common]}
        return top_10_common

    def get_upper_words(self):
        self.df['upper_words'] = self.df['Text'].apply(
            lambda x: sum([1 if w.isalpha() and w.isupper() else 0 for w in str(x).split()])
        )
        upper_words_counter = self.df.groupby('Biased')['upper_words'].sum().to_dict()
        upper_words_counter['total'] = self.df['upper_words'].sum()
        self.result["uppercase_words"] = upper_words_counter
        return upper_words_counter











