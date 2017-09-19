import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap-datepicker',
    packages=['bootstrap_datepicker'],
    include_package_data=True,
    version='1.0',
    description='Bootstrap 3 and 4 compatible datepicker for Django projects.',
    long_description=long_description,
    author='Nakahara Kunihiko/Samuel Colvin/Jack Weatherilt',
    author_email='nakahara.kunihiko@gmail.com/s@muelcolvin.com/jackweatherilt@outlook.com',
    url='https://github.com/jackweath/django-bootstrap3-datepicker-2',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
