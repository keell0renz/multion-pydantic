"""
Queries are declared in a declarative way and can be used as output schemas both for FastAPI and MultiOn scraper.

Also, later user may define different FastAPI output schemas based on queries, for returning additional values received at FastAPI level.
"""

from pydantic import BaseModel, Field


class ProductPageQuery(BaseModel):
    """Please, gather information about this H&M product page."""

    product_name: str
    pricing: float
    total_reviews: float | None
    product_description: str = Field(
        description="Either return existing description if it is short, or if it is too large (100 words+) generate it yourself up to 100 words."
    )
    product_details: str = Field(
        description="Provide here any additonal details you have found, if not -- you may generate it yourself based on page content."
    )


class SearchPageQuery(BaseModel):
    """Please, return the list of links of the search result page you are seeing."""

    results_links: list[str]

# Here you can see where in case output of FastAPI is different to MultiOn API output we can define a child response schema, avoiding duplications.
class SearchResponse(SearchPageQuery):
    results_num: int
