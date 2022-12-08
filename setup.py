from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List(str) =[]
    # with open('requirements.txt',mode='r')as file:
    #     requirement_list = [line.rstrip() for line in file]
    return requirement_list
# print(get_requirements())   

setup(
    name="sensor",
    version="0.0.1",
    author="Niraj Tarway",
    author_email="ds.tarway.niraj@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)