"""
This module facilitates the creation of DiTTo layerstacks (https://github.com/Smart-DS/layerstack).
"""

from __future__ import absolute_import, division, print_function
from builtins import super, range, zip, round, map

import logging

logger = logging.getLogger(__name__)

from layerstack.layer import ModelLayerBase
from datamodel.base import BidDSJsonBaseModel
import datamodel.input.data as data


class BidDSLayerBase(ModelLayerBase):

    @classmethod
    def _check_model_type(cls, model):
        # Check to make sure model is of the proper type
        pass

    @classmethod
    def _load_model(cls, model_path):
        # Method to load model
        # Creates an InputDataFile which inherits BidDSJsonBaseModel
        # This is what is set as the initial model
        bidds_model = data.InputDataFile.load(model_path)
        return bidds_model

        logger.error(
            "Bid-DS models cannot be loaded. Start your stack with a load-model layer."
        )
        raise ("Bid-DS models cannot be loaded.")

    @classmethod
    def _save_model(cls, model_path):
        # Method to save model
        json_model = self.model.save(model_path)
        logger.error(
            "Bid-DS models cannot be saved. End your stack with a save-model layer."
        )
        raise ("Bid-DS models cannot be saved.")
