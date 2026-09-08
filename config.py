import os
from dotenv import load_dotenv

load_dotenv()

# API URLs
BASE_URL = "https://jsonplaceholder.typicode.com"
DUMMYJSON_URL = "https://dummyjson.com"

# UI environment
ENVIRONMENT = os.getenv("TEST_ENV", "qa")

ENV_URLS = {
    "qa": "https://www.saucedemo.com",
    "staging": "https://www.saucedemo.com",
}

UI_BASE_URL = ENV_URLS[ENVIRONMENT]

# Playwright
HEADLESS = (
    os.getenv("HEADLESS", "false").lower() == "true"
    or os.getenv("CI", "false").lower() == "true"
)



