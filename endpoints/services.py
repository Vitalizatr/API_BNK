import os
from parser import Parser
from dotenv import load_dotenv

load_dotenv()

url = os.environ["URL"]

P = Parser(url)
dataframe = P.parse_data_from_url()

def get_data_column(str,count):
    global dataframe
    try:
        if str not in df.columns:
            raise FileNotFoundError
        
        df = dataframe.iloc[0:count]
        return P.convert_to_json_all(df[["data",str]])
    except Exception as E:
        print(E)
        return None