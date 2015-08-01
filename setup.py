import os
import sys
import json
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


README = open(os.path.join(os.path.dirname(__file__), 'django/README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# append the django directory to our path so we can import utils
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'django'))


def build_fixture():
    from utils import translate_fixture

    contents = None
    with open(os.path.join(BASE_DIR, 'data.json')) as f:
        contents = json.loads(f.read())

    contents = translate_fixture(contents)

    with open(os.path.join(BASE_DIR, 'django/fantasy/fixtures/fantasy-database.json'), 'w') as f:
        f.write(json.dumps(contents))


class Develop(develop):

    def run(self):
        develop.run(self)
        build_fixture()


class Install(install):

    def run(self):
        install.run(self)
        build_fixture()


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

    cmdclass={
        'develop': Develop,
        'install': Install,
    },

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
