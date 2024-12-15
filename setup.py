from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='deeplearning',
    version='0.0.1',
    author='sudheer',
    author_email='yalavarthisudheer678@gmail.com',
    install_requires=get_requirements(r'C:\Users\Sudheer\deeplearningproject\requirements.txt'),
    package=find_packages()
)
