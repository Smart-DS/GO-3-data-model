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

    @validator("p_lb")
    def p_lb_ge_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] < 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries >= 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("cost")
    def cost_entry_1_ge_0(cls, data):

        num_t = len(data)
        t_num_h = [len(data[i]) for i in range(num_t)]
        errs = [(i,j,data[i][j][1]) for i in range(num_t) for j in range(t_num_h[i]) if data[i][j][1] < 0.0]
        if len(errs) > 0:
            msg = "fails entries[i][j][1] >= 0. failures (i, j, entry): {}".format(errs)
            raise ValueError(msg)
        return data

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase):

    @validator("RAMPING_RESERVE_UP")
    def ramping_reserve_up_ge_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] < 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries >= 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("RAMPING_RESERVE_DOWN")
    def ramping_reserve_down_ge_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] < 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries >= 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase):

    @validator("REACT_UP")
    def react_up_ge_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] < 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries >= 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("REACT_DOWN")
    def react_down_ge_0(cls, data):

        num_t = len(data)
        idx_err = [i for i in range(num_t) if data[i] < 0.0]
        errs = [(i, data[i]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails entries >= 0. failures (index, entry): {}".format(errs)
            raise ValueError(msg)
        return data

