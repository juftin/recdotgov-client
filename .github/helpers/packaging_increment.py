"""
Project Version Management
"""

from argparse import ArgumentParser
from pathlib import Path

from packaging.version import Version

_this_file = Path(__file__).resolve()
version_file = _this_file.parent.parent.joinpath("VERSION")
version = Version(version_file.read_text())

increment_dict = dict(
    major=Version(f"{version.major + 1}.{version.minor}.{version.micro}"),
    minor=Version(f"{version.major}.{version.minor + 1}.{version.micro}"),
    patch=Version(f"{version.major}.{version.minor}.{version.micro + 1}"),
    none=version,
)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--increment", "-i", default="none", dest="increment")
    args, _ = parser.parse_known_args()
    new_version = str(increment_dict[args.increment])
    version_file.write_text(new_version + "\n")
    print(new_version)
