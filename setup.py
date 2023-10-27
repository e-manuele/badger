from cx_Freeze import setup, Executable

base = None

executables = [Executable("logger.py", base=base, target_name = 'Badger',icon="icon.ico")]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "rfid_test",
    options = options,
    version = "1.0",
    description = 'test',
    executables = executables
)
# python setup.py build
