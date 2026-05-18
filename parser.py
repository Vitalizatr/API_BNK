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
            r.raise_for_status()

            df = pd.read_csv(StringIO(r.text),sep=";")
            df.columns = ["data", "depo", "base_rate", "repo_rate", "loan"]
            
            # Удалил служебные даные таблицы
            df = df.iloc[:-3]

            df["data"] = pd.to_datetime(df["data"],format="%d.%m.%Y")

            
            return df
        except Exception as e:
            print(e)
            return None
    
    
    @staticmethod
    def convert_to_json_all(df):
        try:
            df["data"] = df["data"].dt.strftime("%d.%m.%Y")
            array = df.to_dict(orient="records")
            array_json = json.dumps(array)
            
            return array_json
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def add_half(df):
        try:
            df["half"] = (
                df["data"].dt.year.astype(str)
                + ": "
                + (
                    df["data"].dt.month <= 6
                ).map({
                    True: "H1",
                    False: "H2"
                })
            )

            
            return df.drop_duplicates(subset=["half"])
        except Exception as e:
            print(e)
            return None

    