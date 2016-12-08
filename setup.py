#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.
    """
    output = []
    for filename in filenames:
        f = codecs.open(filename, encoding='utf-8')
        try:
            output.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(output)


setup(
    name='flask-countries',
    version='1.0',
    description='Provides a country field for a flask application',
    long_description=read_files('README.rst', 'CHANGES.rst'),
    author='Florent Messa',
    author_email='florent.messa@gmail.com',
    url='https://github.com/ulule/flask-countries/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
)
