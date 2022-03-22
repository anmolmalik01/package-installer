import os
import json


def create_json():
      """ Creates a json file and adds essential info to it """
      
      os.system('touch package.json')

      lst ={
            'project-name': '',
            'project-description': '',
            'version': '',
            'author': {
                  'name': '',
                  'email': '',
                  'url': '',
            },
            'keywords': [],
      }

      filename = 'package.json'

      # Writing json
      with open(filename, mode='w') as f:
          json.dump(lst, f)

      os.system('echo "JSON created"')
 