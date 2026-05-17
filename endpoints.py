import services
from fastapi import FastAPI
from basemodels import SCount

app = FastAPI(
    title="BNP API",
    description="API для Национального Банка Молдовы",
    version="0.1.0"
)

@app.get("/base_rate/{count}")
async def get_base_rate(count:SCount):
    return services.get_data_column("base_rate",count)

@app.get("/depo/{count}")
async def get_depo(count:SCount):
    return services.get_data_column("depo",count)

@app.get("/repo_rate/{count}")
async def get_repo_rate(count:SCount):
    return services.get_data_column("repo_rate",count)

@app.get("/loan/{count}")
async def get_loan(count:SCount):
    return services.get_data_column("loan",count)
