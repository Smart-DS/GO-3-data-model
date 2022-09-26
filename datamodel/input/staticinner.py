import logging
from pydantic import root_validator, validator

from datamodel.input.staticinnerbase import *

class BusInitialStatus(BusInitialStatusBase): pass

class ShuntInitialStatus(ShuntInitialStatusBase): pass

class DispatchableDevices_SimpleProducingConsumingDevicesInitialStatus(DispatchableDevices_SimpleProducingConsumingDevicesInitialStatusBase):
    
    @validator("accu_down_time")
    def shutdown_accu_down_time_ge_0(cls, data):

        if data < 0:
            msg = "fails accu_down_time >= 0. accu_down_time: {}".format(data)
            raise ValueError(msg)
        return data
    
    @validator("accu_up_time")
    def shutup_accu_up_time_ge_0(cls, data):

        if data < 0:
            msg = "fails accu_up_time >= 0. accu_up_time: {}".format(data)
            raise ValueError(msg)
        return data

    @root_validator
    def accu_up_or_down_time_eq_0(cls, data):

        up = data.get("accu_up_time")
        down = data.get("accu_down_time")
        if (up is not None) and (down is not None) and not ((up <= 0.0) or (down <= 0.0)):
            msg = "fails (accu_up_time <= 0.0) or (accu_down_time <= 0.0). accu_up_time: {}, accu_down_time: {}".format(
                up, down)
            raise ValueError(msg)
        return data

    @root_validator
    def if_prior_on_then_accu_up_gt_0(cls, data):

        on = data.get("on_status")
        up = data.get("accu_up_time")
        if (on is not None) and (up is not None) and (on > 0) and (up <= 0.0):
            msg = "fails (on_status > 0 implies accu_up_time > 0.0). on_status: {}, accu_up_time: {}".format(
                on, up)
            raise ValueError(msg)
        return data

    @root_validator
    def if_prior_off_then_accu_down_gt_0(cls, data):

        on = data.get("on_status")
        down = data.get("accu_down_time")
        if (on is not None) and (down is not None) and (on < 1) and (down <= 0.0):
            msg = "fails (on_status < 1 implies accu_down_time > 0.0). on_status: {}, accu_down_time: {}".format(
                on, down)
            raise ValueError(msg)
        return data

    # may not want these two, due to startup trajectories

    # @root_validator
    # def if_prior_on_then_p_eq_0(cls, data):

    #     on = data.get("on_status")
    #     p = data.get("p")
    #     if (on is not None) and (p is not None) and (on <= 0) and (p != 0.0):
    #         msg = "fails (on_status == 0 implies p == 0.0). on_status: {}, p: {}".format(
    #             on, p)
    #         raise ValueError(msg)
    #     return data

    # @root_validator
    # def if_prior_on_then_q_eq_0(cls, data):

    #     on = data.get("on_status")
    #     q = data.get("q")
    #     if (on is not None) and (q is not None) and (on <= 0) and (q != 0.0):
    #         msg = "fails (on_status == 0 implies q == 0.0). on_status: {}, q: {}".format(
    #             on, q)
    #         raise ValueError(msg)
    #     return data

    # if on0 > 0.0 then accu_up > 0.0
    # if on0 < 1.0 then accu_down > 0.0

class ACTransmissionLineInitialStatus(ACTransmissionLineInitialStatusBase): pass

class TwoWindingTransformerInitialStatus(TwoWindingTransformerInitialStatusBase): pass

class DCLineInitialStatus(DCLineInitialStatusBase): pass

