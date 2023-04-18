import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from pprint import pprint

TEST_DIR = 'tests'


def run_tests():
    test_dir = Path(TEST_DIR)
    test_results = defaultdict(dict)
    succeeded = True
    for module_dir in sorted(test_dir.iterdir()):
        if not module_dir.is_dir():
            continue

        module_name = module_dir.name
        for test_file in sorted(module_dir.glob('**/test*.py')):
            base_module, test_module = str(test_file.parent), test_file.stem
            base_module = base_module.replace('/', '.')
            try:
                command = f'python -m unittest {base_module}.{test_module}'
                print(f'[Execute] {command}')
                subprocess.check_output(command, shell=True)
                test_results[module_name][test_module] = 'succeeded'
            except subprocess.CalledProcessError:
                test_results[module_name][test_module] = 'failed'
                succeeded = False
    return test_results, succeeded


def main():
    test_results, succeeded = run_tests()
    if succeeded:
        print('All tests succeeded.')
    else:
        print('Some tests failed. Failed tests:')
        failed_tests = test_results.copy()
        for module_name, test_modules in test_results.items():
            for test_module, result in test_modules.items():
                if result != 'failed':
                    failed_tests[module_name].pop(test_module)
        pprint(failed_tests, width=20, indent=2)
        sys.exit(1)


if __name__ == '__main__':
    main()
