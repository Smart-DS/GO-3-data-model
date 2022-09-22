import logging
from datamodel.output.sectionsbase import *

class TimeSeriesOutput(TimeSeriesOutputBase):

    def get_bus_uids(self):

        return [i.uid for i in self.bus]

    def get_shunt_uids(self):

        return [i.uid for i in self.shunt]

    def get_simple_dispatchable_device_uids(self):

        return [i.uid for i in self.simple_dispatchable_device]

    def get_ac_line_uids(self):

        return [i.uid for i in self.ac_line]

    def get_dc_line_uids(self):

        return [i.uid for i in self.dc_line]

    def get_two_winding_transformer_uids(self):
        
        return [i.uid for i in self.two_winding_transformer]

    def get_uids(self):

        uids = (
            self.get_bus_uids() +
            self.get_shunt_uids() +
            self.get_simple_dispatchable_device_uids() +
            self.get_ac_line_uids() +
            self.get_dc_line_uids() +
            self.get_two_winding_transformer_uids())
        return uids

