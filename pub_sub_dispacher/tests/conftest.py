def pytest_addoption(parser):
    parser.addoption('--l', '--live', dest='live', help='run live unit tests', nargs=0)