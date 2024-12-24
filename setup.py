from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    Removes '-e .' if present, which is typically used for editable installs.
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters and whitespace
        requirements = [req.strip() for req in requirements]
        # Remove '-e .' if it exists
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ML_Pipeline_project',
    version='0.0.1',
    description='Machine Learning pipeline project',
    author='jsharma212',
    author_email='jsharma212@gmail.com',
    packages=find_packages(),  # Automatically find all packages in your project
    install_requires=get_requirements("requirements.txt")  # Install dependencies
)


