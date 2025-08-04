import re, string


class Cleaner:
    def __init__(self,df):
        self.df = df

    def get_clean_dat(self):
        self.clean_punctuation_marks()
        self.convert_to_lower_case()
        self.drop_unclassified_tweets()
        return self.df

    def drop_unnecessary_columns(self,important_columns):
        unnecessary_columns = [col for col in self.df.columns if col not in important_columns]
        self.df.drop(columns=[unnecessary_columns],inplace=True)

    def clean_punctuation_marks(self):
        clean_string = lambda x: re.sub(rf"[{string.punctuation}]", "", str(x))
        self.df['Text'] = self.df['Text'].apply(clean_string)

    def convert_to_lower_case(self):
        self.df['Text'] = self.df['Text'].str.lower()

    def drop_unclassified_tweets(self):
        self.df.dropna(subset="Biased",inplace=True)

