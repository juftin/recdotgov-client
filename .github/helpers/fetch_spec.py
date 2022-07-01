"""
Download the Latest RIDB Configuration File
"""

import os
from pathlib import Path
import zipfile

import requests

_this_file = spec_file_path = Path(__file__).resolve()
scripts_dir = _this_file.parent
project_dir = scripts_dir.parent
assets_dir = project_dir.joinpath("assets")
assets_dir.mkdir(exist_ok=True)

spec_file = assets_dir.joinpath("openapi.yaml")
zip_file_path = assets_dir.joinpath("recdotgov_client.zip")

session = requests.Session()

swagger_url = os.getenv("SWAGGER_URL",
                        "https://ridb.recreation.gov/ridb/dist/assets/swagger/ridb.yaml")
response = session.get(swagger_url)
spec_file.write_bytes(response.content)

client_response = session.post("https://generator3.swagger.io/api/generate",
                               headers={"content-type": "application/json"},
                               json={
                                   "specURL": swagger_url,
                                   "lang": "python",
                                   "options": {
                                       "additionalProperties": {
                                           "packageName": "recdotgov_client",
                                           "projectName": "recdotgov-client",
                                           "packageVersion": "0.1.0",
                                           "packageUrl": "https://github.com/juftin/recdotgov-client",
                                           "library": "requests",
                                       },
                                   },
                                   "type": "CLIENT",
                                   "codegenVersion": "V3"
                               })
zip_file_path.write_bytes(client_response.content)

zipped_data = zipfile.ZipFile(zip_file_path, mode="r")
zipped_data.extractall(path=project_dir)
