from pkg_resources import load_entry_point
import sys
import sys_path
sys_path.test_imports()
if __name__ == '__main__':
    sys.exit(load_entry_point('pytest', 'console_scripts', 'py.test')())
