import os
import sys
import glob


base = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# add test eggs to path
eggs = os.path.join(base, "*.egg")
sys.path += glob.glob(eggs)

# also add parent directory to path (to find tests)
pkg_base = os.path.join(base, 'python')
sys.path.append(pkg_base)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


def main(argv):
    from django.core.management import execute_from_command_line
    execute_from_command_line(argv)


if __name__ == '__main__':
    args = sys.argv
    args.insert(1, 'test')

    main(args)
