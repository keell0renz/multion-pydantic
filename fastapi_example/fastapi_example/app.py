from fastapi import FastAPI
from .multion_pydantic import MultiOn, MultiOnPydantic


app = FastAPI()

client: MultiOnPydantic = MultiOn(api_key="05ab569bdefe479aaa6077a59c06cf6c")  # type: ignore

@app.get("/scrape_product_page")
async def scrape_product_page():
    pass
