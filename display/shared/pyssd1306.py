# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


"""
SSD1306 Interface
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyssd1306', [dirname(__file__)])
        except ImportError:
            import _pyssd1306
            return _pyssd1306
        if fp is not None:
            try:
                _mod = imp.load_module('_pyssd1306', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyssd1306 = swig_import_helper()
    del swig_import_helper
else:
    import _pyssd1306
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def init(*args):
  """init(char * i2c_bus, int16_t w, int16_t h)"""
  return _pyssd1306.init(*args)

def blit(*args):
  """blit(char * data)"""
  return _pyssd1306.blit(*args)

def set_pixel(*args):
  """set_pixel(int16_t x, int16_t y, uint16_t color)"""
  return _pyssd1306.set_pixel(*args)

def invert(*args):
  """invert(bool i)"""
  return _pyssd1306.invert(*args)

def clear():
  """clear()"""
  return _pyssd1306.clear()

def update():
  """update()"""
  return _pyssd1306.update()
# This file is compatible with both classic and new-style classes.


