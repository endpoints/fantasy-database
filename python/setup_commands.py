
import os
import sys
import json
from setuptools.command.build_py import build_py
from setuptools.command.test import test

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def build_fixture(input_path, output_path):
    from utils import translate_django_fixture

    contents = None
    with open(input_path) as infile:
        contents = json.loads(infile.read())

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

    # This is almost a direct copy of the original method. The difference is
    # that this method only performs a non-'inplace' build.
    def with_project_on_sys_path(self, func):
        from pkg_resources import (
            normalize_path, working_set, add_activation_listener, require
        )

        # Ensure metadata is up-to-date
        self.reinitialize_command('build_py', inplace=0)
        self.run_command('build_py')
        bpy_cmd = self.get_finalized_command("build_py")
        build_path = normalize_path(bpy_cmd.build_lib)

        # Build extensions
        self.reinitialize_command('egg_info', egg_base=build_path)
        self.run_command('egg_info')

        self.reinitialize_command('build_ext', inplace=0)
        self.run_command('build_ext')

        ei_cmd = self.get_finalized_command("egg_info")

        old_path = sys.path[:]
        old_modules = sys.modules.copy()

        try:
            sys.path.insert(0, normalize_path(ei_cmd.egg_base))
            working_set.__init__()
            add_activation_listener(lambda dist: dist.activate())
            require('%s==%s' % (ei_cmd.egg_name, ei_cmd.egg_version))
            func()
        finally:
            sys.path[:] = old_path
            sys.modules.clear()
            sys.modules.update(old_modules)
            working_set.__init__()

    def run_tests(self):
        from tests.runner import main

        test_labels = self.test_labels.split()
        djtest_args = self.djtest_args.split()
        main(['runner.py', 'test'] + test_labels + djtest_args)
