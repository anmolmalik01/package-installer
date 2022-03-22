import os
import json

def install():
    """Install added libraries."""

    json_file = open('package.json')
    json_object = json.load(json_file)
    json_file.close()

    # data store list created from json_object
    data = list(json_object["packages"].items())

    os.system("echo 'Initilaizing modules installation'")
    
    index = 0
    while index != (len(data)):
        print(f"pip install {data[index][0]}=={data[index][1]} ")
        os.system("pip install "+data[index][0]+"=="+data[index][1]+" ")
        index += 1    

    os.system("echo 'Installation completed'")
