from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

extcython = Extension("cyupdate", ["03_cython_update.pyx"],
    include_dirs = [numpy.get_include()])
    
extcythonfast = Extension("cyupdate_fast", ["04_cythonfast_update.pyx"],
    include_dirs = [numpy.get_include()])
    
                
setup(ext_modules=[extcython, extcythonfast],
      cmdclass = {'build_ext': build_ext})

from numpy.distutils.core import setup, Extension        
setup(
  ext_modules = [Extension( 'f2py_update', ['05_f2py_update.f90'] )],
)
