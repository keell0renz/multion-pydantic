from fastapi import FastAPI
from .multion_pydantic import MultiOn, MultiOnPydantic


app = FastAPI()


@app.get("/scrape_product_page")
async def scrape_product_page():
    pass
