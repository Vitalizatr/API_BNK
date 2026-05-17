import os
from parser import Parser
from dotenv import load_dotenv

load_dotenv()

url = os.environ["URL"]

def cron():
    P = Parser(url)
    df = P.parse_data_from_url()

    return P.convert_to_json_all(df)