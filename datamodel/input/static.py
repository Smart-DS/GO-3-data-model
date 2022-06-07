import logging
from pydantic import root_validator

from datamodel.input.staticbase import *

class General(GeneralBase):

    @root_validator
    def stop_is_after_start(cls, data):
        start = data.get("timestamp_start")
        stop = data.get("timestamp_stop")
        if (start is not None) and (stop is not None) and not (start < stop):
            msg = "fails {} < {}. {}: {}, {}: {}".format(
                "timestamp_start", "timestamp_stop", "timestamp_start", start, "timestamp_stop", stop)
            raise ValueError(msg)
        return data

class ViolationCostsParameters(ViolationCostsParametersBase): pass

class Bus(BusBase):
    
    @root_validator
    def vm_lb_le_ub(cls, data):

        lb = data.get("vm_lb")
        ub = data.get("vm_ub")
        if (lb is not None) and (ub is not None) and not (lb <= ub):
            msg = "fails {} <= {}. {}: {}, {}: {}".format(
                "lb", "ub", "vm_lb", lb, "vm_ub", ub)
            raise ValueError(msg)
        return data
    pass

class Shunt(ShuntBase): pass

class DispatchableDevices_SimpleProducingConsumingDevices(DispatchableDevices_SimpleProducingConsumingDevicesBase): pass

class ACTransmissionLine(ACTransmissionLineBase):
    
    @root_validator
    def mva_ub_nom_le_em(cls, data):

        nom = data.get("mva_ub_nom")
        em = data.get("mva_ub_em")
        if (nom is not None) and (em is not None) and not (nom <= em):
            msg = "fails {} <= {}. {}: {}, {}: {}".format(
                "mva_ub_nom", "mva_ub_em", "mva_ub_nom", nom, "mva_ub_em", em)
            raise ValueError(msg)
        return data

class TwoWindingTransformer(TwoWindingTransformerBase): pass

class DCLine(DCLineBase): pass

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase): pass

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase): pass

