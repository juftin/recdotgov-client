"""
Download the Latest RIDB Configuration File
"""

import os
from pathlib import Path
import zipfile

import requests

_this_file = spec_file_path = Path(__file__).resolve()
helpers_dir = _this_file.parent
github_dir = helpers_dir.parent
project_dir = github_dir.parent
build_dir = project_dir.joinpath("build")
build_dir.mkdir(exist_ok=True)

zip_file_path = build_dir.joinpath("recdotgov_client.zip")

session = requests.Session()
swagger_url = os.getenv("SWAGGER_URL",
                        "https://ridb.recreation.gov/ridb/dist/assets/swagger/ridb.yaml")

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
