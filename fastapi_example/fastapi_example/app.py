from fastapi import FastAPI


app = FastAPI()


@app.get("/scrape_product_page")
async def scrape_product_page():
    pass
