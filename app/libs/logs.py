import logging


log_struct = "%(asctime)s | %(levelname)-8s | %(message)s"
log_date = "%d-%m-%Y %H:%M:%S"


def show_variables(global_variables, to_show):
    for variable in to_show:
        value = global_variables.get(variable, "no such variable")
        logging.info(f"Variable {variable.replace('_', ' ')} = {value}")


def log_vars(var_dict):
    for var, val in var_dict.items():
        logging.info(f"Variable {var} = {val}")


def log_primitives(global_variables):
    magic_mark = "__"
    val_types = (str, int, float)
    for var, val in global_variables.items():
        if magic_mark not in var and isinstance(val, val_types):
            logging.info(f"Variable {var} = {val}")
