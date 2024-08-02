from pydantic import BaseModel, Field
from typing import Union


class ProductPageQuery(BaseModel):
    """Please, gather information about this H&M product page."""

    product_name: str
    pricing: float
    total_reviews: Union[float, None]
    product_description: str = Field(description="Either return existing description if it is short, or if it is too large (100 words+) generate it yourself up to 100 words.")
    product_details: str = Field(description="Provide here any additonal details you have found, if not -- you may generate it yourself based on page content.")