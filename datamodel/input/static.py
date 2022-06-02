import logging
from pydantic import root_validator

from datamodel.input.staticbase import *

class General(GeneralBase):

    @root_validator
    def stop_is_after_start(cls, data):
        start = data.get("timestamp_start")
        stop = data.get("timestamp_stop")
        if (start is not None) and (stop is not None) and (stop <= start):
            msg = "fails {} < {}. {}: {}, {}: {}".format(
                "timestamp_stop", "timestamp_start", "timestamp_stop", stop, "timestamp_start", start)
            raise ValueError(msg)
        return data

    pass

class ViolationCostsParameters(ViolationCostsParametersBase): pass

class Bus(BusBase): pass

class Shunt(ShuntBase): pass

class DispatchableDevices_SimpleProducingConsumingDevices(DispatchableDevices_SimpleProducingConsumingDevicesBase): pass

class ACTransmissionLine(ACTransmissionLineBase): pass

class TwoWindingTransformer(TwoWindingTransformerBase): pass

class DCLine(DCLineBase): pass

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase): pass

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase): pass

