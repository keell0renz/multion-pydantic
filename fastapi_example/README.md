# FastAPI Example with MultiOn and Pydantic

This project demonstrates how to use FastAPI in conjunction with MultiOn and Pydantic to scrape product data from H&M. The example is based on a use case defined in a [Reddit post](https://www.reddit.com/r/webscraping/comments/m5hh4l/how_to_extract_product_data_from_hm_with_google/).

## Overview

The project consists of three main components:

1. **app.py**: Defines the FastAPI application and endpoints.
2. **multion_pydantic.py**: Extends the MultiOn client to support Pydantic models.
3. **queries.py**: Defines Pydantic models for the queries and responses.

## app.py

This file sets up the FastAPI application and defines two endpoints for scraping product and search pages.

- **Endpoint: `/scrape_product_page`**
  - **Method**: GET
  - **Parameters**: `link` (str) - The URL of the product page to scrape.
  - **Response**: `ProductPageQuery` - A Pydantic model containing the scraped product data.
  - **Description**: This endpoint retrieves data about a product page using the `retrieve_with_model` method from the MultiOn client.

- **Endpoint: `/scrape_search_page`**
  - **Method**: GET
  - **Parameters**: `link` (str) - The URL of the search results page to scrape.
  - **Response**: `SearchResponse` - A Pydantic model containing the list of result links and the number of results.
  - **Description**: This endpoint retrieves search results and constructs a `SearchResponse` from the `SearchPageQuery`.

## multion_pydantic.py

This file extends the MultiOn client to support Pydantic models. It defines a method `retrieve_with_model` that takes an output schema (a Pydantic model) and retrieves data accordingly.

- **Class: `MultiOnPydantic`**
  - Inherits from `MultiOn`.
  - **Method: `retrieve_with_model`**
    - **Parameters**: `output_schema` (Type[T]), `*args`, `**kwargs`
    - **Returns**: An instance of the output schema.
    - **Description**: This method constructs a command based on the schema's JSON representation and retrieves data from the MultiOn API. It then validates the response against the schema.

## queries.py

This file defines the Pydantic models used for the queries and responses.

- **Class: `ProductPageQuery`**
  - **Fields**:
    - `product_name` (str)
    - `pricing` (float)
    - `total_reviews` (float | None)
    - `product_description` (str)
    - `product_details` (str)
  - **Description**: This model represents the data to be scraped from a product page.

- **Class: `SearchPageQuery`**
  - **Fields**:
    - `results_links` (list[str])
  - **Description**: This model represents the data to be scraped from a search results page.

- **Class: `SearchResponse`**
  - Inherits from `SearchPageQuery`.
  - **Fields**:
    - `results_num` (int)
  - **Description**: This model extends `SearchPageQuery` to include the number of results.

## How to Run

1. Install the required dependencies:

   ```bash
   poetry install
   ```

2. Run the FastAPI application:

   ```bash
   poetry run uvicorn fastapi_example.app:app
   ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This example demonstrates how to integrate FastAPI with MultiOn and Pydantic to create a web scraping service. By defining queries and responses using Pydantic models, we ensure type safety and validation, making the API more robust and reliable.
