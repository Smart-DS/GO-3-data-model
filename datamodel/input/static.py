import logging
from pydantic import root_validator, validator

from datamodel.input.staticbase import *

class General(GeneralBase):

    print('hello world 1')

    @root_validator
    def stop_is_after_start(cls, data):
        print('hello world 5')
        start = data.get("timestamp_start")
        stop = data.get("timestamp_stop")
        print('hello world 2')
        raise ValueError('hello world 6')
        if (start is not None) and (stop is not None) and not (start < stop):
            msg = "fails {} < {}. {}: {}, {}: {}".format(
                "timestamp_start", "timestamp_stop", "timestamp_start", start, "timestamp_stop", stop)
            raise ValueError(msg)
        return data

class ViolationCostsParameters(ViolationCostsParametersBase): pass

class Bus(BusBase):
    
    print('hello world 3')

    @root_validator
    def vm_lb_le_ub(cls, data):

        lb = data.get("vm_lb")
        ub = data.get("vm_ub")
        print('hello world 4')
        if (lb is not None) and (ub is not None) and not (lb <= ub):
            msg = "fails {} <= {}. {}: {}, {}: {}".format(
                "lb", "ub", "vm_lb", lb, "vm_ub", ub)
            raise ValueError(msg)
        return data
    pass

class Shunt(ShuntBase): pass

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

