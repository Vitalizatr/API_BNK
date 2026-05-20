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
            df.columns = ["date", "depo", "base_rate", "repo_rate", "loan"]
            df = df.where(pd.notnull(df), None)
            # Удалил служебные даные таблицы
            df = df.iloc[:-3]
            
            df["date"] = pd.to_datetime(df["date"],format="%d.%m.%Y")

            
            return df
        except Exception as e:
            print(e)
            return None
    
    
    @staticmethod
    def convert_to_json_all(df):
        try:
            df["date"] = df["date"].dt.strftime("%d.%m.%Y")
            array_json = df.to_dict(orient="records")
            
            return array_json
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def add_half(df):
        try:
            df["half"] = (
                df["date"].dt.year.astype(str)
                + ": "
                + (
                    df["date"].dt.month <= 6
                ).map({
                    True: "H1",
                    False: "H2"
                })
            )

            
            return df.drop_duplicates(subset=["half"])
        except Exception as e:
            print(e)
            return None

    
