import logging
from pydantic import root_validator, validator
from datamodel.input.database import *

class InputDataFile(InputDataFileBase):

    # todo uids_not_repeated not sure we can do this as a validator

    # @root_validator
    # def uids_not_repeated(cls, data):
    # #def uids_not_repeated(self, data): # not permitted

    #     #uids = cls.get_uids()
    #     uids = self.get_uids() # not permitted
    #     uids_sorted = sorted(uids)
    #     uids_set = set(uids_sorted)
    #     uids_num = {u:0 for i in uids_set}
    #     for u in uids:
    #         uids_num[u] += 1
    #     uids_num_max = max([0] + uids_num)
    #     if uids_num_max > 1:
    #         msg = "fails uid uniqueness. repeated uids, with number of reps: {}".format(
    #             {k: v for k, v in uids_num.items() if v > 1})
    #         raise ValueError(msg)
    #     return data

    # def get_uids(cls, data):

    #     uids = []
    #     network = data.get("network")
    #     if network is not None:
    #         uids += network.get_uids()
    #     reliability = self.get("reliability")
    #     if reliability is not None:
    #         uids += reliability.get_uids()
    #     return uids

    def uids_not_repeated(self):

        uids = self.get_uids()
        uids_sorted = sorted(uids)
        uids_set = set(uids_sorted)
        uids_num = {i:0 for i in uids_set}
        for i in uids:
            uids_num[i] += 1
        uids_num_max = max([0] + list(uids_num.values()))
        if uids_num_max > 1:
            msg = "fails uid uniqueness. repeated uids, with numbers of occurrences: {}".format(
                {k: v for k, v in uids_num.items() if v > 1})
            raise ValueError(msg)

    def get_uids(self):

        return self.network.get_uids() + self.reliability.get_uids()

    def ctg_dvc_uids_in_domain(self):

        domain = (
            self.network.get_ac_line_uids() +
            self.network.get_two_winding_transformer_uids() +
            self.network.get_dc_line_uids())
        domain = set(domain)
        num_ctg = len(self.reliability.contingency)
        ctg_comp_not_in_domain = [
            list(set(self.reliability.contingency[i].components).difference(domain))
            for i in range(num_ctg)]
        ctg_idx_comp_not_in_domain = [
            i for i in range(num_ctg)
            if len(ctg_comp_not_in_domain[i]) > 0]
        ctg_comp_not_in_domain = [
            (i, self.reliability.contingency[i].uid, ctg_comp_not_in_domain[i])
            for i in ctg_idx_comp_not_in_domain]
        if len(ctg_idx_comp_not_in_domain) > 0:
            msg = "fails contingency outaged devices in branches. failing contingencies (index, uid, failing devices): {}".format(
                ctg_comp_not_in_domain)
            raise ValueError(msg)
