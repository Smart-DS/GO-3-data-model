# GO-3-data-model

[![PyPI](https://img.shields.io/pypi/v/GO-3-data-model.svg)](https://pypi.org/project/GO-3-data-model/)

Pydantic models for the [GO Competition Challenge 3](https://gocompetition.energy.gov/challenges/challenge-3) [json format](https://gocompetition.energy.gov/challenges/challenge-3/data_format). Support for loading, validation, editing, saving. 

Should often be used in conjunction with [C3DataUtilities](https://github.com/GOCompetition/C3DataUtilities).

## Install

```
pip install GO-3-data-model
```

## Use

To load GO-3 input data files:

```
from datamodel.input.data import InputDataFile
problem_data = InputDataFile.load(problem_data_file_name)
```

If no errors are raised, then validation succeeded and problem_data is a Pydantic model containing the problem data. All fields may be edited, and the resulting modified model can be saved:

```
problem_data.save(filename)
```

The output data structure is encoded in `datamodel.input.data.OutputDataFile`, and json schemas are available in `datamodel/schemas`.

## Developer Instructions

If the json format changes, please:

1. Create a new folder named YYYYMMDD (with today's current date) under GO-3-data-model/input
2. Copy and paste the .tex files of the new version into the folder
3. Commit and push

If you want to work on automatically generating the Pydantic model, you'll first want to create a conda/Python environment and install this package in developer mode:

```
conda activate YOUR_ENV_NAME
cd GO-3-data-model
pip install -e .
```

Then you'll want to modify code in `GO-3-data-model/datamodel/create.py` and run it from the command line as in:

```
cd GO-3-data-model
python datamodel/create.py 20220128
```

If any of the files prefixed with `__` change, you might need to hand-port those changes into the files with the same names but not prefixed with `__`. (The latter sometimes contain hand-written validators and therefore are not overwritten by `create.py`.)
