import os
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'django/README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='fantasy-database',
    version='2.0.0',
    license='BSD License',

    description='A database with a few fantasy books in it for testing query builders, orms, rest frameworks, etc.',
    long_description=README,
    url='https://github.com/tkellen/fantasy-database',
    author='Tyler Kellen',
    package_dir={'': 'django'},
    packages=find_packages(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
