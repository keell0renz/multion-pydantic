"""
In this file we explore the usecase defined in https://www.reddit.com/r/webscraping/comments/m5hh4l/how_to_extract_product_data_from_hm_with_google/
reddit post, which asks for a way to scrape H&M products.

One of the benefits of pydantic-based query is that this query is defined in declarative way, and can be used to type return values
in frameworks like FastAPI or other systems which heavily rely on Pydantic DTOs and Pydantic-based typing.

One of the challenges is that AI does not always adhere to types and can output None, due to the nature of my prototype: it is just a wrapper.

In future I would like to implement this feature closer to the back end and force model output defined types, and also I will introduce proper type display of Union-like types to account for None output.
"""

from fastapi import FastAPI
from .multion_pydantic import MultiOn, MultiOnPydantic
from .queries import ProductPageQuery, SearchPageQuery, SearchResponse


app = FastAPI()

# I know it is bad to leave API keys like this, but this is just a toy example.
client: MultiOnPydantic = MultiOn(api_key="05ab569bdefe479aaa6077a59c06cf6c")  # type: ignore


@app.get("/scrape_product_page")
async def scrape_product_page(
    link: str,
) -> ProductPageQuery:  # Can be used to define output result of scraping.
    """Retrieve data about product page."""

    # In this example I have made this function accept a generic output_schema, which properly displays output Pydantic schema.
    response: ProductPageQuery = client.retrieve_with_model(
        url=link, output_schema=ProductPageQuery
    )

    return response


# https://www2.hm.com/nl_nl/search-results.html?q=jeans
# This can jam sometimes, because, as I have said -- it is possible to define only a WRAPPER without having access to MultiOn internals, so if it fails -- try again.
@app.get("/scrape_search_page")
async def scrape_search_page(
    link: str,
) -> SearchResponse:  # Different output schema, but child of SearchPageQuery
    """Retrieve results and their number."""

    response: SearchPageQuery = client.retrieve_with_model(
        url=link, output_schema=SearchPageQuery
    )

    # Construct SearchResponse from SearchPageQuery
    search_response = SearchResponse(
        results_links=response.results_links, results_num=len(response.results_links)
    )

    return search_response
