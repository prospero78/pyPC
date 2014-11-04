from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext
import Cython.Compiler.Options as cOptions


cOptions.annotate = True

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("cmodVideo", ["cmodVideo.pyx"])]
)
