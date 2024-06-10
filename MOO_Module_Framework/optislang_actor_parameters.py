import os
import json
from check_json_files import check_parameters_json

def actor_parameters_to_csv():
    '''
    Use Case:
        This function generates a csv file which is required for inputting in a parametric system
        It reads in 02_Model/parameters.json and generates optislang_actor_parameters.csv'

    Args:
        No arguments are provided for this function

    Returns:
    '''
    #Reads parameters.json file
    cwd = os.getcwd()
    parameters_json = check_parameters_json('MOO_M_ARRHENIUS')
    with open(parameters_json,'r') as file:
        json_data = json.load(file)

    #Define csv columns
    csv_columns = ["Param_Type", "Reference_value", "Constant", "Modifiable", "Unit", "Removeable", "Operation", "Det_Type", "Det_Kind", "Det_Range",
             "Ran_Type", "Ran_Has_CoV", "Ran_CoV", "Ran_Params", "Ran_Moments"]

    csv_name = "optislang_actor_parameters.csv"

    #Writing column values 
    with open(csv_name, "w") as outfile:
        outfile.write("Name,Param_Type,Reference_value,Constant,Modifiable,Unit,Removeable,Operation,Det_Type,Det_Kind,Det_Range,Ran_Type,Ran_Has_CoV,Ran_CoV,Ran_Params,Ran_Moments\n")
        
        for module in json_data.keys():
            for param_name in json_data[module]["parameters"].keys():
                outfile.write("\"" + param_name + "\",")
                i = 1
                for columns in csv_columns:
                    data = json_data[module]["parameters"][param_name][columns]
                    if isinstance(data, str):
                        outfile.write("\"" + data + "\"")
                    else:
                        outfile.write(str(data))

                    if i < len(csv_columns):
                        outfile.write(",")
                    i += 1
                outfile.write("\n")
                print(f'Successfully created {csv_name}')


if __name__ == '__main__':
    actor_parameters_to_csv()