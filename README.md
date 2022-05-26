# Bid-DS-data-model

Pydantic model of Bid-DS json format. Support for loading, validation, editing, saving.

🚧🚧 Under Construction 🚧🚧

Current work is to set up the Pydantic model for the json format. If the json format changes, please:

1. Create a new folder named YYYYMMDD (with today's current date) under Bid-DS-data-model/input
2. Copy and paste the .tex files of the new version into the folder
3. Commit and push

If you want to work on automatically generating the Pydantic model, you'll first want to create a conda/Python environment and install this package in developer mode:

```
conda activate YOUR_ENV_NAME
cd Bid-DS-data-model
pip install -e .
```

Then you'll want to add code to Bid-DS-data-model/datamodel/create.py and run it from the command line as in:

```
cd Bid-DS-data-model
python datamodel/create.py 20220128
```

To use the created Pydantic model for reading and validating, do:

```
from datamodel.input.data import InputDataFile
problem_data = InputDataFile.load(problem_data_file_name)
```

If no errors are raised, then validation succeeded and problem_data is a Pydantic model containing the problem data.
