from setuptools import find_packages,setup
from typing import List

E_DOT='-e .'
def get_requirenments(file_path:str)->List[str]:
    '''
    this function will return the list of requirnmnsts

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements


setup(
    name='mlproject1',
    version='0.0.1',
    author='Yash',
    author_email='yashgcode@gmail.com',
    packages=find_packages(),
    install_requires=get_requirenments('requirements.txt'),

)