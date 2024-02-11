from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirments
    '''
    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n',"")for req in requirement]

    return requirement

setup(
name = 'ml_project',
version = '0.0.1',
author = 'Rohit',

author_email = 'rg99939@gmail.com',
packages = find_packages(),

install_requires = get_requirements('requirment.txt')

)