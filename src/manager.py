import pandas as pd
from data_analyzer import DataAnalyzer
from json_writer import JsonWriter
from cleaner import Cleaner

class Manager:
    def __init__(self,file_src):
        self.file_src = file_src

    def run(self):

            #load data from a file
            data = pd.read_csv(self.file_src)

            #analyze the data
            analyzer = DataAnalyzer(data)

            #the results of analyzing
            results = analyzer.result

            #convert results to basic python data types
            converted_results = JsonWriter.convert_to_native(results)

            #write results to json file
            JsonWriter.write_to_json(converted_results)


            cleaner = Cleaner(data)

            #get cleaned data
            clean_data = cleaner.get_clean_dat()

            #write clened dat to csv file
            clean_data.to_csv("../results/cleaned_data.csv")





