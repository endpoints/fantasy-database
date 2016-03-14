import os
import sys
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'python/README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# append the python directory to our path so we can import utils
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'python'))


def get_commands():
    from setup_commands import Test, BuildPy
    return Test, BuildPy

Test, BuildPy = get_commands()


setup(
    name='fantasy-database',
    version='2.0.3-post.1',
    license='MIT',

    description='A database with a few fantasy books in it for testing query builders, orms, rest frameworks, etc.',
    long_description=README,
    url='https://github.com/tkellen/fantasy-database',
    author='Tyler Kellen',
    author_email='tyler@sleekcode.net',
    package_dir={'': 'python'},
    py_modules=['setup_commands', 'utils'],
    packages=find_packages('python', exclude=['tests']),

    tests_require=['django>=1.7'],

    cmdclass={
        'build_py': BuildPy,
        'test': Test,
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
