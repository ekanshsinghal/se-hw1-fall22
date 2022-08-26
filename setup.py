from setuptools import setup, find_packages

setup(
    name='Basic Calculator',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',
    description='A basic calculator for addition, subtraction, multiplication, division, and modulus operations',
    author='Supriya, Gowtham, Rahul, Ekansh',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
