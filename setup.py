from setuptools import find_packages, setup
setup(
    name='seedr',
    packages=find_packages(include=['seedr']),
    version='0.1.0',
    description='Added web preview for links in copy method in pyrogram',
    author='Anonymous',
    license='MIT',
    install_requires=['aiohttp[speedups]'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
)
