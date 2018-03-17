# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='DotsAndBoxes',
    version='1.0.2',
    description=(
        '点格棋对弈软件'
    ),
    long_description=open('README.rst', 'rb').read().decode('utf8'),
    author='高铭',
    author_email='gaomingshsf@hotmail.com',
    maintainer='高铭',
    maintainer_email='gaomingshsf@hotmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Everyb0dyLies/Dots-and-Boxes',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=[
        'PyQt5'
    ]
)

