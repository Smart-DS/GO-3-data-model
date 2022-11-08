import logging
from pydantic import root_validator, validator

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

    @validator("e_vio_cost")
    def e_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "e_vio_cost", "e_vio_cost", data)
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

class DispatchableDevices_SimpleProducingConsumingDevices(DispatchableDevices_SimpleProducingConsumingDevicesBase):

    ### This one is incorrect
    # @validator("startup_states")
    # def startup_states_entry0_ge_0(cls, data):

    #     num_states = len(data)
    #     idx_err = [i for i in range(num_states) if data[i][0] < 0.0]
    #     errs = [(i, data[i][0]) for i in idx_err]
    #     if len(idx_err) > 0:
    #         msg = "fails states have entry 0 >= 0. failures (index, entry 0): {}".format(errs)
    #         raise ValueError(msg)
    #     return data

    @validator("startups_ub")
    def startups_ub_entry0_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][0] < 0.0]
        errs = [(i, data[i][0]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 0 >= 0. failures (index, entry 0): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("startups_ub")
    def startups_ub_entry1_ge_entry0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][1] < data[i][0]]
        errs = [(i, data[i][0], data[i][1]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 1 >= entry 0. failures (index, entry 0, entry 1): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("startups_ub")
    def startups_ub_entry2_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][2] < 0]
        errs = [(i, data[i][2]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 2 >= 0. failures (index, entry 2): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_ub")
    def energy_req_ub_entry0_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][0] < 0.0]
        errs = [(i, data[i][0]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 0 >= 0. failures (index, entry 0): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_ub")
    def energy_req_ub_entry1_ge_energy0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][1] < data[i][0]]
        errs = [(i, data[i][0], data[i][1]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 1 >= entry 0. failures (index, entry 0, entry 1): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_ub")
    def energy_req_ub_entry2_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][2] < 0.0]
        errs = [(i, data[i][2]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 2 >= 0. failures (index, entry 2): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_lb")
    def energy_req_lb_entry0_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][0] < 0.0]
        errs = [(i, data[i][0]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 0 >= 0. failures (index, entry 0): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_lb")
    def energy_req_lb_entry1_ge_energy0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][1] < data[i][0]]
        errs = [(i, data[i][0], data[i][1]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 1 >= entry 0. failures (index, entry 0, entry 1): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("energy_req_lb")
    def energy_req_lb_entry2_ge_0(cls, data):

        num_constrs = len(data)
        idx_err = [i for i in range(num_constrs) if data[i][2] < 0.0]
        errs = [(i, data[i][2]) for i in idx_err]
        if len(idx_err) > 0:
            msg = "fails constraints have entry 2 >= 0. failures (index, entry 2): {}".format(errs)
            raise ValueError(msg)
        return data

    @validator("in_service_time_lb")
    def min_uptime_ge_0(cls, data):

        if data < 0:
            msg = "fails min uptime >= 0. min uptime: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("down_time_lb")
    def min_downtime_ge_0(cls, data):

        if data < 0:
            msg = "fails min downtime >= 0. min downtime: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_up_ub")
    def ramp_up_rate_ge_0(cls, data):

        if data < 0:
            msg = "fails ramp up rate >= 0. ramp up rate: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_down_ub")
    def ramp_down_rate_ge_0(cls, data):

        if data < 0:
            msg = "fails ramp down rate >= 0. ramp down rate: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_startup_ramp_ub")
    def startup_ramp_rate_ge_0(cls, data):

        if data < 0:
            msg = "fails startup ramp rate >= 0. startup ramp rate: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_shutdown_ramp_ub")
    def shutdown_ramp_rate_ge_0(cls, data):

        if data < 0:
            msg = "fails shutdown ramp rate >= 0. shutdown ramp rate: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_reg_res_up_ub")
    def p_reg_res_up_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_reg_res_up_ub >= 0. p_reg_res_up_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_reg_res_down_ub")
    def p_reg_res_down_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_reg_res_down_ub >= 0. p_reg_res_down_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_syn_res_ub")
    def p_syn_res_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_syn_res_ub >= 0. p_syn_res_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_nsyn_res_ub")
    def p_nsyn_res_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_nsyn_res_ub >= 0. p_nsyn_res_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_res_up_online_ub")
    def p_ramp_res_up_online_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_ramp_res_up_online_ub >= 0. p_ramp_res_up_online_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_res_down_online_ub")
    def p_ramp_res_down_online_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_ramp_res_down_online_ub >= 0. p_ramp_res_down_online_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_res_up_offline_ub")
    def p_ramp_res_up_offline_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_ramp_res_up_offline_ub >= 0. p_ramp_res_up_offline_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @validator("p_ramp_res_down_offline_ub")
    def p_ramp_res_down_offline_ub_ge_0(cls, data):

        if data < 0:
            msg = "fails p_ramp_res_down_offline_ub >= 0. p_ramp_res_down_offline_ub: {}".format(data)
            raise ValueError(msg)
        return data

    @root_validator
    def q_linear_or_bound_cap_but_not_both(cls, data):

        linear = data.get("q_linear_cap")
        bound = data.get("q_bound_cap")
        if (linear is not None) and (bound is not None) and (linear > 0) and (bound > 0):
            msg = "fails q_linear_cap == 0 or q_bound_cap == 0. q_linear_cap: {}, q_bound_cap: {}".format(
                linear, bound)
            raise ValueError(msg)
        return data
    
class ACTransmissionLine(ACTransmissionLineBase):
    
    @root_validator
    def fbus_ne_tbus(cls, data):

        fr = data.get("fr_bus")
        to = data.get("to_bus")
        if (fr is not None) and (to is not None) and (fr == to):
            msg = "fails fr_bus != to_bus. fr_bus: {}, to_bus: {}".format(fr, to)
            raise ValueError(msg)
        return data

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

class TwoWindingTransformer(TwoWindingTransformerBase):
    
    @root_validator
    def fbus_ne_tbus(cls, data):

        fr = data.get("fr_bus")
        to = data.get("to_bus")
        if (fr is not None) and (to is not None) and (fr == to):
            msg = "fails fr_bus != to_bus. fr_bus: {}, to_bus: {}".format(fr, to)
            raise ValueError(msg)
        return data

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
    
    @root_validator
    def tm_le_tm_ub(cls, data):

        tm_ub = data.get("tm_ub")
        initial_status = data.get("initial_status")
        if (tm_ub is not None) and (initial_status is not None):
            tm = initial_status.tm
            if not (tm <= tm_ub):
                msg = "fails initial_status.tm <= tm_ub. initial_status.tm: {}, tm_ub: {}".format(tm, tm_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def tm_ge_tm_lb(cls, data):

        tm_lb = data.get("tm_lb")
        initial_status = data.get("initial_status")
        if (tm_lb is not None) and (initial_status is not None):
            tm = initial_status.tm
            if not (tm >= tm_lb):
                msg = "fails initial_status.tm >= tm_lb. initial_status.tm: {}, tm_lb: {}".format(tm, tm_lb)
                raise ValueError(msg)
        return data
    
    @root_validator
    def ta_le_ta_ub(cls, data):

        ta_ub = data.get("ta_ub")
        initial_status = data.get("initial_status")
        if (ta_ub is not None) and (initial_status is not None):
            ta = initial_status.ta
            if not (ta <= ta_ub):
                msg = "fails initial_status.ta <= ta_ub. initial_status.ta: {}, ta_ub: {}".format(ta, ta_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def ta_ge_ta_lb(cls, data):

        ta_lb = data.get("ta_lb")
        initial_status = data.get("initial_status")
        if (ta_lb is not None) and (initial_status is not None):
            ta = initial_status.ta
            if not (ta >= ta_lb):
                msg = "fails initial_status.ta >= ta_lb. initial_status.ta: {}, ta_lb: {}".format(ta, ta_lb)
                raise ValueError(msg)
        return data

    @root_validator
    def tm_or_ta_lb_eq_ub(cls, data):
        
        tm_ub = data.get("tm_ub")
        tm_lb = data.get("tm_lb")
        ta_ub = data.get("ta_ub")
        ta_lb = data.get("ta_lb")
        if (tm_ub is not None) and (tm_lb is not None) and (ta_ub is not None) and (ta_lb is not None):
            if (tm_lb < tm_ub) and (ta_lb < ta_ub):
                msg = "fails tm_ub == tm_lb or ta_ub == ta_lb. tm_ub: {}, tm_lb: {}, ta_ub: {}, ta_lb: {}".format(
                    tm_ub, tm_lb, ta_ub, ta_lb)
                raise ValueError(msg)
        return data

    @validator("tm_lb")
    def tm_lb_gt_0(cls, data):

        if not (data > 0):
            msg = "fails {} > 0. {}: {}".format(
                "tm_lb", "tm_lb", data)
            raise ValueError(msg)
        return data            

class DCLine(DCLineBase):
    
    @root_validator
    def fbus_ne_tbus(cls, data):

        fr = data.get("fr_bus")
        to = data.get("to_bus")
        if (fr is not None) and (to is not None) and (fr == to):
            msg = "fails fr_bus != to_bus. fr_bus: {}, to_bus: {}".format(fr, to)
            raise ValueError(msg)
        return data
    
    @root_validator
    def pdc_fr_le_pdc_ub(cls, data):

        pdc_ub = data.get("pdc_ub")
        initial_status = data.get("initial_status")
        if (pdc_ub is not None) and (initial_status is not None):
            pdc_fr = initial_status.pdc_fr
            if not (pdc_fr <= pdc_ub):
                msg = "fails initial_status.pdc_fr <= pdc_ub. initial_status.pdc_fr: {}, pdc_ub: {}".format(
                    pdc_fr, pdc_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def pdc_fr_ge_minus_pdc_ub(cls, data):

        pdc_ub = data.get("pdc_ub")
        initial_status = data.get("initial_status")
        if (pdc_ub is not None) and (initial_status is not None):
            pdc_fr = initial_status.pdc_fr
            if not (pdc_fr >= -pdc_ub):
                msg = "fails initial_status.pdc_fr >= -pdc_ub. initial_status.pdc_fr: {}, pdc_ub: {}".format(
                    pdc_fr, pdc_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def qdc_fr_le_qdc_fr_ub(cls, data):

        qdc_fr_ub = data.get("qdc_fr_ub")
        initial_status = data.get("initial_status")
        if (qdc_fr_ub is not None) and (initial_status is not None):
            qdc_fr = initial_status.qdc_fr
            if not (qdc_fr <= qdc_fr_ub):
                msg = "fails initial_status.qdc_fr <= qdc_fr_ub. initial_status.qdc_fr: {}, qdc_fr_ub: {}".format(
                    qdc_fr, qdc_fr_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def qdc_fr_ge_qdc_fr_lb(cls, data):

        qdc_fr_lb = data.get("qdc_fr_lb")
        initial_status = data.get("initial_status")
        if (qdc_fr_lb is not None) and (initial_status is not None):
            qdc_fr = initial_status.qdc_fr
            if not (qdc_fr >= qdc_fr_lb):
                msg = "fails initial_status.qdc_fr >= qdc_fr_lb. initial_status.qdc_fr: {}, qdc_fr_lb: {}".format(
                    qdc_fr, qdc_fr_lb)
                raise ValueError(msg)
        return data
    
    @root_validator
    def qdc_to_le_qdc_to_ub(cls, data):

        qdc_to_ub = data.get("qdc_to_ub")
        initial_status = data.get("initial_status")
        if (qdc_to_ub is not None) and (initial_status is not None):
            qdc_to = initial_status.qdc_to
            if not (qdc_to <= qdc_to_ub):
                msg = "fails initial_status.qdc_to <= qdc_to_ub. initial_status.qdc_to: {}, qdc_to_ub: {}".format(
                    qdc_to, qdc_to_ub)
                raise ValueError(msg)
        return data
    
    @root_validator
    def qdc_to_ge_qdc_to_lb(cls, data):

        qdc_to_lb = data.get("qdc_to_lb")
        initial_status = data.get("initial_status")
        if (qdc_to_lb is not None) and (initial_status is not None):
            qdc_to = initial_status.qdc_to
            if not (qdc_to >= qdc_to_lb):
                msg = "fails initial_status.qdc_to >= qdc_to_lb. initial_status.qdc_to: {}, qdc_to_lb: {}".format(
                    qdc_to, qdc_to_lb)
                raise ValueError(msg)
        return data

    @validator("qdc_fr_ub")
    def qdc_fr_ub_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "qdc_fr_ub", "qdc_fr_ub", data)
            raise ValueError(msg)
        return data            

    @validator("qdc_fr_lb")
    def qdc_fr_lb_le_0(cls, data):

        if not (data <= 0):
            msg = "fails {} <= 0. {}: {}".format(
                "qdc_fr_lb", "qdc_fr_lb", data)
            raise ValueError(msg)
        return data            

    @validator("qdc_to_ub")
    def qdc_to_ub_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "qdc_to_ub", "qdc_to_ub", data)
            raise ValueError(msg)
        return data            

    @validator("qdc_to_lb")
    def qdc_to_lb_le_0(cls, data):

        if not (data <= 0):
            msg = "fails {} <= 0. {}: {}".format(
                "qdc_to_lb", "qdc_to_lb", data)
            raise ValueError(msg)
        return data            

class ActiveZonalReserveRequirementsViolationCosts(ActiveZonalReserveRequirementsViolationCostsBase):

    @validator("REG_UP")
    def reg_up_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REG_UP", "REG_UP", data)
            raise ValueError(msg)
        return data            

    @validator("REG_DOWN")
    def reg_down_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REG_DOWN", "REG_DOWN", data)
            raise ValueError(msg)
        return data            

    @validator("SYN")
    def syn_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "SYN", "SYN", data)
            raise ValueError(msg)
        return data            

    @validator("NSYN")
    def nsyn_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "NSYN", "NSYN", data)
            raise ValueError(msg)
        return data            

    @validator("REG_UP_vio_cost")
    def reg_up_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REG_UP_vio_cost", "REG_UP_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("REG_DOWN_vio_cost")
    def reg_down_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REG_DOWN_vio_cost", "REG_DOWN_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("SYN_vio_cost")
    def syn_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "SYN_vio_cost", "SYN_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("NSYN_vio_cost")
    def nsyn_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "NSYN_vio_cost", "NSYN_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("RAMPING_RESERVE_UP_vio_cost")
    def ramping_reserve_up_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "RAMPING_RESERVE_UP_vio_cost", "RAMPING_RESERVE_UP_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("RAMPING_RESERVE_DOWN_vio_cost")
    def ramping_reserve_down_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "RAMPING_RESERVE_DOWN_vio_cost", "RAMPING_RESERVE_DOWN_vio_cost", data)
            raise ValueError(msg)
        return data            

class ReactiveZonalReserveRequirementsViolationCosts(ReactiveZonalReserveRequirementsViolationCostsBase):

    @validator("REACT_UP_vio_cost")
    def react_up_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REACT_UP_vio_cost", "REACT_UP_vio_cost", data)
            raise ValueError(msg)
        return data            

    @validator("REACT_DOWN_vio_cost")
    def react_down_vio_cost_ge_0(cls, data):

        if not (data >= 0):
            msg = "fails {} >= 0. {}: {}".format(
                "REACT_DOWN_vio_cost", "REACT_DOWN_vio_cost", data)
            raise ValueError(msg)
        return data            
