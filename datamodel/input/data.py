import logging
from pydantic import root_validator, validator
from datamodel.input.database import *

class InputDataFile(InputDataFileBase):

    def get_uids(self):

        return self.network.get_uids() + self.reliability.get_uids()
