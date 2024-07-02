from setuptools import find_packages,setup
from typing import List


var='-e .'

def get_requirements(file_path:str)->List[str]:
    # this function returns the list of requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if var in requirements:
            requirements.remove(var)
    
    return requirements

setup(
name='Student performance prediction',
version='0.0.1',
author='Sachin negi',
author_email='negi.sachin1906@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)