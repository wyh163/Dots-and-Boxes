# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='DotsAndBoxes',
    version=1.0,
    description=(
        '点格棋对弈软件'
    ),
    long_description=open('README.rst').read(),
    author='高铭',
    author_email='gaomingshsf@hotmail.com',
    maintainer='高铭',
    maintainer_email='gaomingshsf@hotmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Everyb0dyLies/Dots-and-Boxes',
    classifiers=[
        'Development Status :: 1',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'PyQt5'
    ]

)