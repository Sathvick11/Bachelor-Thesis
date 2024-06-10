'''
NOTE: This python script will be running in Optislang's Python interpreter
      Therefore, calling or importing other files might not work inside here
'''
import os
from pathlib import Path
from py_os_design import PyOSDesignEntry
import json

cwd = os.getcwd()

def create_parametric_actor(actor_name:str):
    '''
    Use Case:
        This function creates a parametric actor in Optislang using Optislang Python API
        Here, the parametric system consists only of a single module

    Args:
        actor_name(str): Name of the actor to be defined in Optislang

    Returns:
        A Python actor connected with it's input and output, defined parameters for the actor
    '''
    #Create a Python actor in the parametric system
    actor = actors.PythonActor(actor_name)
    parametric_system.add_actor(actor)

    #Connecting the python actor
    connect(parametric_system, 'IODesign', actor, 'IDesign')
    connect(actor, 'ODesign', parametric_system, 'IIDesign')

    #Defining the path of the algorithm
    actor.path = Path(cwd,'MOO_M_ARRHENIUS\\02_Model\\arrhenius.py')

    #Importing the parameters from the csv file
    params = parametric_system.parameter_manager
    params.import_from_csv(os.path.join(cwd,'',','))
    parametric_system.parameter_manager = params
    return actor_name

def read_parameters(json_file:str = Path(cwd,'MOO_M_ARRHENIUS\\02_Model\\parameters.json')):
    '''
    Use case:
        This function reads parameters.json file which contains optislang parameters

    Args:
        json_file(str): Path of 'parameters.json' file. -----> (The path for it is pre defined in the function)

    Returns:
        A json file in read mode
    '''
    with open(json_file,'r') as file:
        data_from_json = json.load(file)
    return data_from_json


def write_parameters():
    '''
    Use case:
        This function reads the parameters from 'parameters.json' and writes it into 'optislang_parameters.py'

    Args:
        None

    Returns:
        None
    '''
    param_path = Path(cwd,'optislang_parameters.py')
    if param_path.exists():
        os.remove(param_path)
    with open(param_path, 'w') as outfile:
        outfile.write('from py_os_design import PyOSDesignEntry\n')
        data_json = read_parameters()
        for module in data_json:
            for param_name,param in data_json[module]['parameters'].items():
                param_value = param['Reference_value']

                if isinstance(param_value,str):
                    param_value = f"'{param_value}'"
                elif isinstance(param_value,int):
                    param_value = f"{float(param_value)}"

                outfile.write(f"actor.add_parameter('{param_name}', PyOSDesignEntry({param_value}))\n")

if __name__ == '__main__':
    write_parameters()
    create_parametric_actor('Arrhenius')
    exec(Path(cwd,'optislang_parameters.py'))