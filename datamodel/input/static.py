import logging
from pydantic import root_validator, validator

from datamodel.input.staticbase import *

class General(GeneralBase):

    #print('hello world 1')

    @root_validator
    def stop_is_after_start(cls, data):
        #print('hello world 5')
        start = data.get("timestamp_start")
        stop = data.get("timestamp_stop")
        #print('hello world 2')
        #raise ValueError('hello world 6')
        if (start is not None) and (stop is not None) and not (start < stop):
            msg = "fails {} < {}. {}: {}, {}: {}".format(
                "timestamp_start", "timestamp_stop", "timestamp_start", start, "timestamp_stop", stop)
            raise ValueError(msg)
        return data

class ViolationCostsParameters(ViolationCostsParametersBase):

    @validator("p_bus_vio_cost")
    def p_bus_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "p_bus_vio_cost", "p_bus_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("q_bus_vio_cost")
    def q_bus_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "q_bus_vio_cost", "q_bus_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("s_vio_cost")
    def s_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "s_vio_cost", "s_vio_cost", data)
            raise ValueError(msg)
        return data            

class Bus(BusBase):
    
    @validator("vm_lb")
    def vm_lb_gt_0(cls, data):

        if not (data > 0):
            msg = "fails {} > 0. {}: {}".format(
                "vm_lb", "vm_lb", data)
            raise ValueError(msg)
        return data            

    @root_validator
    def vm_lb_le_init(cls, data):

        lb = data.get("vm_lb")
        init = data.get("initial_status")
        if (lb is not None) and (init is not None):
            #v0 = init.get("vm") # why does data.get() work but init.get() does not work?
            v0 = init.vm
            #if (v0 is not None) and not (lb <= v0):
            if not (lb <= v0):
                msg = "fails {} <= {}. {}: {}, {}: {}".format(
                    "vm_lb", "(initial_status -> vm)", "vm_lb", lb, "(initial_status -> vm)", v0)
                raise ValueError(msg)
        return data

    @root_validator
    def vm_init_le_ub(cls, data):

        ub = data.get("vm_ub")
        init = data.get("initial_status")
        if (ub is not None) and (init is not None):
            v0 = init.vm
            if not (v0 <= ub):
                msg = "fails {} <= {}. {}: {}, {}: {}".format(
                    "(initial_status -> vm)", "vm_ub", "(initial_status -> vm)", v0, "vm_ub", ub)
                raise ValueError(msg)
        return data

class Shunt(ShuntBase):
        # "step_ub": 2,
        # "step_lb": 0.5,
        # "initial_status": {
        #   "step": 1
        # }

    # todo: note this does not work. Parsing converts non-int float to int before validator is called
    # perhaps we could type the step_ub field as pydantic.StrictInt instead of as int in datamodel.input.staticbase
    # if we do that then we do not need this validator anyway
    @validator("step_ub")
    def step_ub_int(cls, data):

        if not (data == round(data)):
            msg = "fails {} integer. {}: {}".format(
                "step_ub", "step_ub", data)
            raise ValueError(msg)
        #raise ValueError('hello world shunt. data: {}'.format(data))
        return data

    @validator("step_lb")
    def step_lb_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >=0. {}: {}".format(
                "step_lb", "step_lb", data)
            raise ValueError(msg)
        return data

    @root_validator
    def step_lb_le_init(cls, data):

        lb = data.get("step_lb")
        init = data.get("initial_status")
        if (lb is not None) and (init is not None):
            u0 = init.step
            if not (lb <= u0):
                msg = "fails {} <= {}. {}: {}, {}: {}".format(
                    "step_lb", "(initial_status -> step)", "step_lb", lb, "(initial_status -> step)", u0)
                raise ValueError(msg)
        return data

    @root_validator
    def step_init_le_ub(cls, data):

        ub = data.get("step_ub")
        init = data.get("initial_status")
        if (ub is not None) and (init is not None):
            u0 = init.step
            if not (u0 <= ub):
                msg = "fails {} <= {}. {}: {}, {}: {}".format(
                    "(initial_status -> step)", "step_ub", "(initial_status -> step)", u0, "step_ub", ub)
                raise ValueError(msg)
        return data

class DispatchableDevices_SimpleProducingConsumingDevices(DispatchableDevices_SimpleProducingConsumingDevicesBase): pass

class ACTransmissionLine(ACTransmissionLineBase):

    @validator("mva_ub_nom")
    def mva_ub_nom_gt_0(cls, data):

        if not (data > 0):
            msg = "fails {} > 0. {}: {}".format(
                "mva_ub_nom", "mva_ub_nom", data)
            raise ValueError(msg)
        return data            

    @validator("mva_ub_em")
    def mva_ub_em_gt_0(cls, data):

        if not (data > 0):
            msg = "fails {} > 0. {}: {}".format(
                "mva_ub_em", "mva_ub_em", data)
            raise ValueError(msg)
        return data            
    
    @root_validator
    def mva_ub_nom_le_em(cls, data):

        nom = data.get("mva_ub_nom")
        em = data.get("mva_ub_em")
        if (nom is not None) and (em is not None) and not (nom <= em):
            msg = "fails {} <= {}. {}: {}, {}: {}".format(
                "mva_ub_nom", "mva_ub_em", "mva_ub_nom", nom, "mva_ub_em", em)
            raise ValueError(msg)
        return data
    
    @root_validator
    def r_ne_0_or_x_ne_0(cls, data):

        r = data.get("r")
        x = data.get("x")
        if (r is not None) and (x is not None) and not (abs(r) + abs(x) > 0):
            msg = "fails abs(r) + abs(x) > 0. r: {}, x: {}".format(r, x)
            raise ValueError(msg)
        return data

class TwoWindingTransformer(TwoWindingTransformerBase): pass

class DCLine(DCLineBase): pass

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase): pass

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase): pass

