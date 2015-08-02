import os
import sys
import json
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.test import test


README = open(os.path.join(os.path.dirname(__file__), 'python/README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# append the python directory to our path so we can import utils
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'python'))


def build_fixture(input_path, output_path):
    from utils import translate_django_fixture

    contents = None
    with open(input_path) as infile:
        contents = json.loads(infile.read())
        print BASE_DIR

    contents = translate_django_fixture(contents)

    with open(output_path, 'w') as outfile:
        outfile.write(json.dumps(contents))


class BuildPy(build_py):

    # adapted from:
    # http://www.digip.org/blog/2011/01/generating-data-files-in-setup.py.html
    def run(self):
        # honor the --dry-run flag
        if not self.dry_run:
            target_dir = os.path.join(self.build_lib, 'django_fantasy/fixtures')

            # mkpath is a distutils helper to create directories
            self.mkpath(target_dir)

            input_path = os.path.join(BASE_DIR, 'data.json')
            output_path = os.path.join(target_dir, 'fantasy-database.json')

            build_fixture(input_path, output_path)

        # distutils uses old-style classes, so no super()
        build_py.run(self)


class Test(test):
    user_options = [
        ('test-labels=', 'l', "Test labels to pass to runner.py test"),
        ('djtest-args=', 'a', "Arguments to pass to runner.py test"),
    ]

    def initialize_options(self):
        test.initialize_options(self)
        self.test_labels = 'tests'
        self.djtest_args = ''

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from tests.runner import main

        # We still need to build the fixture manually during test, since
        # setuptools runs tests on PY2 'in place'.
        target_dir = os.path.join(BASE_DIR, 'python/django_fantasy/fixtures')
        build_fixture(
            os.path.join(BASE_DIR, 'data.json'),
            os.path.join(target_dir, 'fantasy-database.json')
        )

        test_labels = self.test_labels.split()
        djtest_args = self.djtest_args.split()
        main(['runner.py', 'test'] + test_labels + djtest_args)


setup(
    name='fantasy-database',
    version='2.0.1',
    license='MIT',

    description='A database with a few fantasy books in it for testing query builders, orms, rest frameworks, etc.',
    long_description=README,
    url='https://github.com/tkellen/fantasy-database',
    author='Tyler Kellen',
    author_email='tyler@sleekcode.net',
    package_dir={'': 'python'},
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
