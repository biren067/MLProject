from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT = '-e .'
def get_requirement(filepath:str)->list[str]:
    '''
        This function will return a list of packages
    '''
    requirement = []
    with open(filepath,'r') as f:
        content = f.readlines()
        requirement = [x.replace(r"\n","") for x in content]

    if HYPE_E_DOT in requirement:
        requirement.remove(HYPE_E_DOT)

    
    return requirement


setup(name='mlproject',version='0.0.1',author='biren',
      author_email='birendra@xmoney.in',packages=find_packages(),
      install_requires=get_requirement('requirements.txt'))