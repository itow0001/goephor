'''
Created on Apr 29, 2016

@author: iitow
'''
from setuptools import setup, find_packages

SRCDIR = './goephor'


def readme():
    ''' Spits out README.rst for our long_description
    with open('README.rst', 'r') as fobj:
        return fobj.read()
    '''


setup(
    name='goephor',
    version='1.0.6',
    description="Build automation tool",
    long_description=readme(),
    author='ian.itow',
    author_email='ian.itow@isilon.com',
    url='',
    license='',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': SRCDIR},
    packages=find_packages(SRCDIR, exclude=['examples']),
    zip_safe=False,
    install_requires=[
        'requests==2.7.0',
        'PyYAML==3.10'
    ],
    entry_points={
        'console_scripts': ['goephor = goephor.goephor:main']
    },
    include_package_data=True,
)