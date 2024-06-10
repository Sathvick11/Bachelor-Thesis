from pathlib import Path
import os
import shutil
import subprocess

#Define global variables
cwd = os.getcwd()

def module_dir_path(module_name:str)->Path:
    '''
    Use case:
        This function gets the absolute path to the directory of the module

    Argument:
        module_path(str): Name of the module
    
    Returns:
        absolute path of the module_name's directory

    '''
    return Path(cwd,module_name)


def clone_module(module_name:str,module_branch:str):
    '''
    UseCase:
        This functions clones a Git repository from the provided URL and branch into the current working directory.

        If the module is already present, it will throw a log stating indicating that it already exists.
        If the module does not exist, the function will clone the provided module and stores it in the current working directory.

    Arguments to be provided:
        module_name(str): Name of the directory where the module is stored in GitHub
        module_url(str): URL of the module's GitHub repository -------> Decide if this needs to be added to the code
        module_branch(str): A specific branch of the module's GitHub to clone

    Raises:
        Exception if an error occurs while cloning the repository
    '''
    command = f'git clone https://github.boschdevcloud.com/rbpoe/{module_name}.git --branch {module_branch}'
    if not module_dir_path(module_name).exists():
        try:
            subprocess.run(command)
            echo = f'Successfully cloned module {module_name} from https://github.boschdevcloud.com/rbpoe/{module_name}.git branch {module_branch}'
            print(echo)

        except Exception as e:
            print(f'Failed to clone module {module_name} from https://github.boschdevcloud.com/rbpoe/{module_name}.git branch {module_branch}\n')
            print(f' Error : {e}')
            
            
    else:
        print(f'{module_name} folder already exists in {cwd} \n')
        print(f'Deleting {module_name}')

        try:
            shutil.rmtree(module_dir_path(module_name))
            print(f'Trying to clone {module_name}')
            subprocess.run(command)

        except PermissionError as e:
            print(f'Failed to execute\n Error: {e}')


if __name__ == '__main__':
    clone_module('MOO_M_ARRHENIUS','main_m_v1.0')