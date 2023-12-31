import sys
from cx_Freeze import setup, Executable

company_name = 'Metalmed'
product_name = 'RFID_logger'

bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    # 'includes': ['atexit', 'PySide.QtNetwork'], # <-- this causes error
    }

# GUI applications require a different base on Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(script='logger.py',
                 base=base,
                 icon='icon.ico',
                )

setup(name=product_name,
      version='1.0.0',
      description='blah',
      executables=[exe],
      options={'bdist_msi': bdist_msi_options})

# python setup.py bdist_msi
