import logging
from pydantic import root_validator, validator

from datamodel.input.timeseriesbase import *

class General(GeneralBase):

    @root_validator
    def time_periods_eq_len_interval_duration(cls, data):

        time_periods = data.get("time_periods")
        interval_duration = data.get("interval_duration")
        if (time_periods is not None) and (interval_duration is not None):
            if not(len(interval_duration) == time_periods):
                msg = "fails len(interval_duration) == time_periods. len(interval_duration): {}, time_periods: {}".format(
                    len(interval_duration), time_periods)
                raise ValueError(msg)
        return data

    @validator("interval_duration")
    def interval_duration_gt_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] <= 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries > 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

class DispatchableDevices_SimpleProducingConsumingDevices(DispatchableDevices_SimpleProducingConsumingDevicesBase):
    
    pass

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase):

    pass

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase):

    pass

