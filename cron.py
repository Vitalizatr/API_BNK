import os
import json
from parser import Parser
from dotenv import load_dotenv
import requests



"""Обычное измененние"""

url = os.environ["SOME_SECRET"]

def cron():
    P = Parser("https://bnm.md/en/official_exchange_rates?get_xml=1&date=19.06.2026")
    df = P.parse_data_from_url()
    df_year_half = P.add_half(df)

    data = P.convert_to_json_all(df_year_half)
    
    with open("data/rates.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print(cron())
    r = requests.get("https://bnm.md/ru/export-base-rates?limit=1000", timeout=30)
    print(r.status_code)
    print(r.text[:200])
    load_dotenv()
