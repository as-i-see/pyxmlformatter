from distutils.core import setup
import xmlformatter

setup(
    name = 'pyxmlformatter',
    version = '1.0',
    py_modules = ['xmlformatter'],
    scripts = ['bin/xmlformat'],
)
