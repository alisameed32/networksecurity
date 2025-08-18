'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    reuirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                reuirement = line.strip()
                ## ignore empty lines and -e .
                if reuirement and reuirement != '-e .':
                    reuirements_lst.append(reuirement)
    except FileExistsError:
        print("requirements.txt file not found.")                


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ali Sameed",
    author_email="alisameed.ds@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)