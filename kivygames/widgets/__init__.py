from inspect import currentframe
from os import extsep
from os.path import splitext, exists
from kivy.lang.builder import Builder

def loadKv():
    filename = currentframe().f_back.f_code.co_filename
    f = extsep.join((splitext(filename)[0], 'kv'))
    if exists(f) and f not in Builder.files:
        Builder.load_file(f)
