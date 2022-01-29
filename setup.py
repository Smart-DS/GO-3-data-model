from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

with open(here / "README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="Bid-DS-data-model",
    version="0.1.0",
    description="Pydantic model of Bid-DS json format. Support for loading, validation, editing, saving.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="NREL",
    packages=find_packages(),
    package_dir={"datamodel": "datamodel"},
    scripts = [],
    include_package_data=True,
    install_requires=[
        "pydantic"
    ]
)
