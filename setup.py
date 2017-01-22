#! /usr/bin/env python
import os
from setuptools import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules']

setup(
    name='settings-test',
    author='Mira',
    author_email='moony19@gmail.com',
    description='test travis settings',
    url='https://github.com/szewczykmira/settings-test',
    packages=['sets'],
    include_package_data=True,
    classifiers=CLASSIFIERS,
    install_requires=['Django>=1.8', 'requests', 'dj-database-url', 'psycopg2',
                      'pytest-django'],
    platforms=['any'],
    test_suite='settings-test.tests',
    tests_require=['pytest'],
    zip_safe=False)

