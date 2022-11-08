from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

with open(here / "README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="GO-3-data-model",
    version="1.0.2",
    description="Repository for model formulation of Grid Optimization Competition #3",
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
