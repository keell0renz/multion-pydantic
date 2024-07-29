# MultiOn x Pydantic: The Holy Grail of Data Extraction?

In this Jupyter notebook, we present a small proof-of-concept regarding the idea of a Pydantic-based query approach for web data extraction. Due to the lack of access to the source code and internals of MultiOn, we created a software-level abstraction that adds a new method, `retrieve_with_model`, which can accept Pydantic models as queries.

## Overview

The notebook demonstrates how to use Pydantic models to structure and validate data extracted from web pages using the MultiOn API. This approach allows for more robust and type-safe data extraction, leveraging Pydantic's powerful data validation capabilities.

## Market Demand

Here I provide found articles and projects about web scraping using Pydantic, to demonstrate that some users are in need of this solution.

[Medium Article](https://medium.com/@prabhavithreddy/llm-lang-chain-and-pydantic-a-powerful-trio-for-object-oriented-web-data-extraction-12098ebe4733)

[Example implemented with LangChain and BeautifulSoup](https://dzone.com/articles/enhancing-web-scraping-with-large-language-models)

Also, there is a general purpose library which connects AI models and Pydantic:

[Instructor](https://python.useinstructor.com/)

## Key Components

### MultiOnPydantic Class

We define a `MultiOnPydantic` class to provide type hinting for the `MultiOn` object. This class includes the `retrieve_with_model` method, which is designed to accept Pydantic models as output schemas.
