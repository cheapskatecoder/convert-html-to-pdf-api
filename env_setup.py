import os
import importlib
# getting dependencies
try:
    importlib.import_module('flask')
    importlib.import_module('pdfkit')
    importlib.import_module('wkhtmltopdf')
    print("GOOD TO GO")
except ImportError:
    print("Getting the required files \n this may take some time...")
    os.system("python3 -m pip install flask")
    os.system("python3 -m pip install pdfkit")
    os.system("python3 -m pip install wkhtmltopdf")
    os.system("apt install wkhtmltopdf")
    print("Getting Dependencies")
# end getting dependecines
