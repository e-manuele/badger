import sys
from cx_Freeze import setup, Executable



base = "Win32GUI" if sys.platform == "win32" else None

packages = ["idna","os","sys","logging","serial","csv","time","datetime","io","serial.tools.list_ports"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name="Badger",
    options = options,
    version="1.0",
    description="rfid logger",
    executables=[Executable("logger_badge.py", base=base, icon="icon_3.ico")],
)
#python setup.py build