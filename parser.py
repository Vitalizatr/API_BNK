import httpx
import pandas as pd
from io import StringIO
import json

class Parser():
    def __init__(self,_url):
        self.url = _url

    def parse_data_from_url(self):
        try:
            r = httpx.get(self.url)
            r_json= r.json()

            df = pd.read_html(StringIO(r_json[1]['data']))[0]
            df.columns = ["data", "depo", "base_rate", "repo_rate", "loan"]

            return df
        except Exception as e:
            print(e)
            return None
    
    
    @staticmethod
    def convert_to_json_all(df):
        try:
            array = df.to_dict(orient="records")
            array_json = json.dumps(array)
            
            return array_json
        except Exception as e:
            print(e)
            return None
    
    