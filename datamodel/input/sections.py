import logging
from datamodel.input.sectionsbase import *

class Network(NetworkBase):

    # todo bus UIDs unique
    # etc

    def get_bus_uids(self):

        return [i.uid for i in self.bus]

    def get_shunt_uids(self):

        return [i.uid for i in self.shunt]

    def get_simple_dispatchable_device_uids(self):

        return [i.uid for i in self.simple_dispatchable_device]

    def get_ac_line_uids(self):

        return [i.uid for i in self.ac_line]

    def get_two_winding_transformer_uids(self):

        return [i.uid for i in self.two_winding_transformer]

    def get_dc_line_uids(self):

        return [i.uid for i in self.dc_line]

    def get_active_zonal_reserve_uids(self):

        return [i.uid for i in self.active_zonal_reserve]

    def get_reactive_zonal_reserve_uids(self):

        return [i.uid for i in self.reactive_zonal_reserve]

    def get_uids(self):

        uids = (
            self.get_bus_uids() +
            self.get_shunt_uids() +
            self.get_simple_dispatchable_device_uids() +
            self.get_ac_line_uids() +
            self.get_two_winding_transformer_uids() +
            self.get_dc_line_uids() +
            self.get_active_zonal_reserve_uids() +
            self.get_reactive_zonal_reserve_uids())
        return uids

    def shunt_bus_uids_in_domain(self):

        domain = self.get_bus_uids()
        domain = set(domain)
        num_shunt = len(self.shunt)
        shunt_idx_bus_not_in_domain = [
            i for i in range(num_shunt)
            if not (self.shunt[i].bus in domain)]
        shunt_bus_not_in_domain = [
            (i, self.shunt[i].uid, self.shunt[i].bus)
            for i in shunt_idx_bus_not_in_domain]
        if len(shunt_idx_bus_not_in_domain) > 0:
            msg = "fails shunt bus in buses. failing shunts (index, uid, bus uid): {}".format(
                shunt_bus_not_in_domain)
            raise ValueError(msg)

class TimeSeriesInput(TimeSeriesInputBase): pass

class Reliability(ReliabilityBase):

    def get_contingency_uids(self):

        return [i.uid for i in self.contingency]

    def get_uids(self):

        return self.get_contingency_uids()
