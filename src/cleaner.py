import re, string


class Cleaner:
    def __init__(self,df):
        self.df = df

    def get_clean_dat(self):
        self.drop_unnecessary_columns()
        self.clean_punctuation_marks()
        self.convert_to_lower_case()
        self.drop_unclassified_tweets()
        return self.df

    def drop_unnecessary_columns(self,important_columns=('Text','Biased')):
        unnecessary_columns = [col for col in self.df.columns if col not in important_columns]
        self.df.drop(unnecessary_columns,axis=1,inplace=True)

    def clean_punctuation_marks(self):
        clean_string = lambda x: re.sub(rf"[{string.punctuation}]", "", str(x))
        self.df['Text'] = self.df['Text'].apply(clean_string)

    def convert_to_lower_case(self):
        self.df['Text'] = self.df['Text'].str.lower()

    def drop_unclassified_tweets(self):
        self.df.dropna(subset="Biased",inplace=True)

