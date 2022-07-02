"""
Download the Latest RIDB Configuration File
"""

import logging
import os
from pathlib import Path

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

_this_file = spec_file_path = Path(__file__).resolve()
helpers_dir = _this_file.parent
github_dir = helpers_dir.parent
project_dir = github_dir.parent

yaml_file_path = project_dir.joinpath("openapi.yaml")

session = requests.Session()
swagger_url = os.getenv(
    "SWAGGER_URL", "https://ridb.recreation.gov/ridb/dist/assets/swagger/ridb.yaml"
)

response = session.get(swagger_url)
fixed = response.content.decode("utf-8").replace(
    "RIDB_HOST", "https://ridb.recreation.gov"
)
yaml_file_path.write_text(fixed)
