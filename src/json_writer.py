import json
import numpy as np

class JsonWriter:
    @staticmethod
    def write_to_json(result_dict):
        with open('../results/results.json', 'w', encoding='utf-8') as f :
            json.dump(result_dict, f, ensure_ascii=False, indent=4)

    @staticmethod
    def convert_to_native(obj):
        """ function to convert numpy objects yo
        native python objects"""
        if isinstance(obj, dict) :
            return {JsonWriter.convert_to_native(k) : JsonWriter.convert_to_native(v) for k, v in obj.items()}
        elif isinstance(obj, list) :
            return [JsonWriter.convert_to_native(i) for i in obj]
        elif isinstance(obj, np.integer) :
            return int(obj)
        elif isinstance(obj, np.floating) :
            return float(obj)
        elif isinstance(obj, np.bool_) :
            return bool(obj)
        else:
            return obj


