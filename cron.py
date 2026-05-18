import os
import json
from parser import Parser
from dotenv import load_dotenv

load_dotenv()

"""Обычное измененние"""

url = os.environ["SOME_SECRET"]

def cron():
    P = Parser(url)
    df = P.parse_data_from_url()
    df_year_half = P.add_half(df)

    data = P.convert_to_json_all(df_year_half)
    
    with open("data/rates.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print(cron())