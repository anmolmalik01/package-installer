import os
import json
import sys


# function to convert json file into array
def convert_arr_to_dic(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct       


def build():
    """ Add modules to json file """

    # getting library name in project
    os.system('echo "Collecting all the modules included in project"')
    os.system('pipreqs ./ --force')

    # ========================== array maniputaion ===============================
    # creating a array having 
    txt_file = open('./requirements.txt')
    requirements_array = txt_file.readlines()
    txt_file.close()

    # stoping if the array is empty is empty
    if len(requirements_array) == 0 or requirements_array==['\n']:
        sys.exit("This project doesn't include any module.")

    # spliting the arary
    splited_array = []
    for i in range(len(requirements_array)):
        splited_array.append(requirements_array[i].split("=="))
    
    # creating final array and storing it in final_array
    final_array = []
    for i in range(len(requirements_array)):
        for j in range(2):
            final_array.append( splited_array[i][j].strip() )

    # =========================== json manipulation ==================================
    # opening python-package.json for reading
    json_file = open('package.json', 'r')
    json_object = json.load(json_file)
    json_file.close()

    json_object["packages"] = convert_arr_to_dic(final_array)

    f = open('package.json', 'w')
    json.dump(json_object, f, ensure_ascii = False, indent=6)
    f.close()

    os.system('echo "JSON updated"')