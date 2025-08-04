import pandas as pd
from data_analyzer import DataAnalyzer
from json_writer import JsonWriter
from cleaner import Cleaner

def run():
    data = pd.read_csv("../data/tweets_dataset.csv")

    analyzer = DataAnalyzer(data)

    results = analyzer.result

    converted_results = JsonWriter.convert_to_native(results)

    JsonWriter.write_to_json(converted_results)

    cleaner = Cleaner(data)

    cleaner.df.to_csv("../results/cleaned_data.csv")





