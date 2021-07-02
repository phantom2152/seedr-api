from setuptools import find_packages, setup
setup(
    name='seedr',
    packages=['seedr'],
    version='0.1.0',
    description='A python Unofficial seedr api to control seedr.cc accounts',
    author='Ns-AnoNymouS',
    license='MIT',
    install_requires=['aiohttp'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
)
