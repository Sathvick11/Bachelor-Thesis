import os

from py_os_design import PyOSDesignEntry

pv_calculator = actors.MatlabActor('Pv_calculator')
example_system.add_actor(pv_calculator)

connect(example_system, 'IODesign', pv_calculator, 'IDesign')
connect(pv_calculator, 'ODesign', example_system, 'IIDesign')

cwd = os.getcwd()

pv_calculator.file_path = Path(os.path.join(cwd, "MOO_M_PV_CALCULATOR\\02_Model\\main_Pv_Calculator.m"))

params = example_system.parameter_manager
params.import_from_csv('G:\My Drive\Bachelor_Thesis\Bachelor_Thesis_Sathvick\Pv_calculator_python\optislang_input_parameters.csv', ',')
example_system.parameter_manager = params

pv_calculator.add_parameter('nameLC', PyOSDesignEntry(''))
pv_calculator.add_parameter('nameFET', PyOSDesignEntry(''))
pv_calculator.add_parameter('Tj', PyOSDesignEntry(''))
pv_calculator.add_parameter('commutationtype', PyOSDesignEntry(''))
pv_calculator.add_parameter('time_tracker', PyOSDesignEntry(1.0))
pv_calculator.add_parameter('flgTjFk', PyOSDesignEntry('false'))