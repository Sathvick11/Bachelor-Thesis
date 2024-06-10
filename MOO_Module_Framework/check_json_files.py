import os
from pathlib import Path
from clone_module import module_dir_path

def json_file_exists(json_path:Path):
    '''
    Use case:
        A functions which checks if a json file exists in the given path or not

    Args:
        json_path(Path): Path to verify the existence of the json file

    Returns:
        - 
    '''
    if Path(json_path).exists():
        print(f'File found in {json_path }')
    else:
        print(f'File {json_path} not found/ does not exist')

def check_module_config_json(module_name:str)->Path:
    '''
    Use Case:
        This functions check if 01_Specification/module_config.json is present in the module defined module_name

    Args:
        module_name(str): Name of the module

    Returns:
        Path of the json file
    '''
    module_config_json_path = Path(module_dir_path(module_name),'01_Specification','module_config.json')
    #Checks if module_config.json is present
    json_file_exists(module_config_json_path)

#function to define directory

def check_parameters_json(module_name:str)->Path:
    '''
    Use Case:
        This functions check if 02_Model/parameters.json is present in the module defined module_name

    Args:
        module_name(str): Name of the module

    Returns:
        Path of the json file
    '''

    parameters_json_path = Path(module_dir_path(module_name),'02_Model','parameters.json')

    try:
        json_file_exists(parameters_json_path)
        return parameters_json_path
    except FileNotFoundError as e:
        print(f'parameters.json not found/does not exist\nError:{e}')


if __name__ == '__main__':
    check_module_config_json('MOO_M_ARRHENIUS')
    check_parameters_json('MOO_M_ARRHENIUS')