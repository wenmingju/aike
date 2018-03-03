import os, yaml
def read_data(filename):
    filepath = os.getcwd() + os.sep + 'YML_data' + os.sep + filename + '.yml'
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.load(f)
