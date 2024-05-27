import os 

import py_doe_settings
from dynardo_py_algorithms import DOETYPES
from py_os_criterion import DesignStatus, PyOSCriterion, PyOSCriterionContainer
from py_os_parameter import PyParameter

obj = actors.ParametricSystemActor('Pv Calculator')
obj.auto_save_mode = AS_ACTOR_FINISHED
add_actor(obj)

example_system = obj
cwd = os.getcwd()
exec(open(f'{cwd}\\create_pv_calculator.py').read())
obj = example_system