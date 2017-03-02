# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_littleb', [dirname(__file__)])
        except ImportError:
            import _littleb
            return _littleb
        if fp is not None:
            try:
                _mod = imp.load_module('_littleb', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _littleb = swig_import_helper()
    del swig_import_helper
else:
    import _littleb
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _littleb.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _littleb.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _littleb.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _littleb.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _littleb.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _littleb.SwigPyIterator_equal(self, x)

    def copy(self):
        return _littleb.SwigPyIterator_copy(self)

    def next(self):
        return _littleb.SwigPyIterator_next(self)

    def __next__(self):
        return _littleb.SwigPyIterator___next__(self)

    def previous(self):
        return _littleb.SwigPyIterator_previous(self)

    def advance(self, n):
        return _littleb.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _littleb.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _littleb.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _littleb.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _littleb.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _littleb.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _littleb.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _littleb.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_littleb.SHARED_PTR_DISOWN_swigconstant(_littleb)
SHARED_PTR_DISOWN = _littleb.SHARED_PTR_DISOWN

_littleb.SUCCESS_swigconstant(_littleb)
SUCCESS = _littleb.SUCCESS

_littleb.ERROR_FEATURE_NOT_IMPLEMENTED_swigconstant(_littleb)
ERROR_FEATURE_NOT_IMPLEMENTED = _littleb.ERROR_FEATURE_NOT_IMPLEMENTED

_littleb.ERROR_FEATURE_NOT_SUPPORTED_swigconstant(_littleb)
ERROR_FEATURE_NOT_SUPPORTED = _littleb.ERROR_FEATURE_NOT_SUPPORTED

_littleb.ERROR_INVALID_CONTEXT_swigconstant(_littleb)
ERROR_INVALID_CONTEXT = _littleb.ERROR_INVALID_CONTEXT

_littleb.ERROR_INVALID_DEVICE_swigconstant(_littleb)
ERROR_INVALID_DEVICE = _littleb.ERROR_INVALID_DEVICE

_littleb.ERROR_INVALID_BUS_swigconstant(_littleb)
ERROR_INVALID_BUS = _littleb.ERROR_INVALID_BUS

_littleb.ERROR_NO_RESOURCES_swigconstant(_littleb)
ERROR_NO_RESOURCES = _littleb.ERROR_NO_RESOURCES

_littleb.ERROR_MEMEORY_ALLOCATION_swigconstant(_littleb)
ERROR_MEMEORY_ALLOCATION = _littleb.ERROR_MEMEORY_ALLOCATION

_littleb.ERROR_SD_BUS_CALL_FAIL_swigconstant(_littleb)
ERROR_SD_BUS_CALL_FAIL = _littleb.ERROR_SD_BUS_CALL_FAIL

_littleb.ERROR_UNSPECIFIED_swigconstant(_littleb)
ERROR_UNSPECIFIED = _littleb.ERROR_UNSPECIFIED
class BlProperties(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlProperties, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BlProperties, name)
    __repr__ = _swig_repr
    __swig_setmethods__["paired"] = _littleb.BlProperties_paired_set
    __swig_getmethods__["paired"] = _littleb.BlProperties_paired_get
    if _newclass:
        paired = _swig_property(_littleb.BlProperties_paired_get, _littleb.BlProperties_paired_set)
    __swig_setmethods__["trusted"] = _littleb.BlProperties_trusted_set
    __swig_getmethods__["trusted"] = _littleb.BlProperties_trusted_get
    if _newclass:
        trusted = _swig_property(_littleb.BlProperties_trusted_get, _littleb.BlProperties_trusted_set)
    __swig_setmethods__["connected"] = _littleb.BlProperties_connected_set
    __swig_getmethods__["connected"] = _littleb.BlProperties_connected_get
    if _newclass:
        connected = _swig_property(_littleb.BlProperties_connected_get, _littleb.BlProperties_connected_set)

    def __init__(self):
        this = _littleb.new_BlProperties()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _littleb.delete_BlProperties
    __del__ = lambda self: None
BlProperties_swigregister = _littleb.BlProperties_swigregister
BlProperties_swigregister(BlProperties)

class BleCharactersitic(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BleCharactersitic, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BleCharactersitic, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _littleb.new_BleCharactersitic(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _littleb.delete_BleCharactersitic
    __del__ = lambda self: None

    def getPath(self):
        return _littleb.BleCharactersitic_getPath(self)

    def getUuid(self):
        return _littleb.BleCharactersitic_getUuid(self)
BleCharactersitic_swigregister = _littleb.BleCharactersitic_swigregister
BleCharactersitic_swigregister(BleCharactersitic)

class BleService(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BleService, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BleService, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _littleb.new_BleService()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _littleb.delete_BleService
    __del__ = lambda self: None

    def init(self, bleService):
        return _littleb.BleService_init(self, bleService)

    def getPath(self):
        return _littleb.BleService_getPath(self)

    def getUuid(self):
        return _littleb.BleService_getUuid(self)

    def getPrimary(self):
        return _littleb.BleService_getPrimary(self)

    def getCharacteristics(self):
        return _littleb.BleService_getCharacteristics(self)
BleService_swigregister = _littleb.BleService_swigregister
BleService_swigregister(BleService)


def parseUartServiceMessage(message):
    return _littleb.parseUartServiceMessage(message)
parseUartServiceMessage = _littleb.parseUartServiceMessage

def parseDBusMessage(message):
    return _littleb.parseDBusMessage(message)
parseDBusMessage = _littleb.parseDBusMessage
class Device(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Device, name)
    __repr__ = _swig_repr

    def __init__(self, device):
        this = _littleb.new_Device(device)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _littleb.delete_Device
    __del__ = lambda self: None

    def connect(self):
        return _littleb.Device_connect(self)

    def disconnect(self):
        return _littleb.Device_disconnect(self)

    def pair(self):
        return _littleb.Device_pair(self)

    def unpair(self):
        return _littleb.Device_unpair(self)

    def getBleCharacteristicByPath(self, path):
        return _littleb.Device_getBleCharacteristicByPath(self, path)

    def getBleCharacteristicByUuid(self, uuid):
        return _littleb.Device_getBleCharacteristicByUuid(self, uuid)

    def getBleServiceByPath(self, path):
        return _littleb.Device_getBleServiceByPath(self, path)

    def getBleServiceByUuid(self, uuid):
        return _littleb.Device_getBleServiceByUuid(self, uuid)

    def getBleDeviceServices(self):
        return _littleb.Device_getBleDeviceServices(self)

    def writeToCharacteristic(self, uuid, size, value):
        return _littleb.Device_writeToCharacteristic(self, uuid, size, value)

    def readFromCharacteristic(self, uuid):
        return _littleb.Device_readFromCharacteristic(self, uuid)

    def getDeviceProperties(self):
        return _littleb.Device_getDeviceProperties(self)

    def registerChangeStateEvent(self, propertyChangeCallback, userdata):
        return _littleb.Device_registerChangeStateEvent(self, propertyChangeCallback, userdata)

    def getName(self):
        return _littleb.Device_getName(self)

    def getAddress(self):
        return _littleb.Device_getAddress(self)

    def getNumOfServices(self):
        return _littleb.Device_getNumOfServices(self)

    def registerCharacteristicReadEvent(self, uuid, call_func, userdata):
        return _littleb.Device_registerCharacteristicReadEvent(self, uuid, call_func, userdata)

    def registerCallbackReadEvent(self, uuid, python_func_ptr):
        return _littleb.Device_registerCallbackReadEvent(self, uuid, python_func_ptr)

    def registerCallbackStateEvent(self, python_func_ptr):
        return _littleb.Device_registerCallbackStateEvent(self, python_func_ptr)
Device_swigregister = _littleb.Device_swigregister
Device_swigregister(Device)

class DeviceManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DeviceManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DeviceManager, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["getInstance"] = lambda x: _littleb.DeviceManager_getInstance
    if _newclass:
        getInstance = staticmethod(_littleb.DeviceManager_getInstance)

    def getBlDevices(self, seconds=5):
        return _littleb.DeviceManager_getBlDevices(self, seconds)

    def getDeviceByName(self, name):
        return _littleb.DeviceManager_getDeviceByName(self, name)
    __swig_destroy__ = _littleb.delete_DeviceManager
    __del__ = lambda self: None
DeviceManager_swigregister = _littleb.DeviceManager_swigregister
DeviceManager_swigregister(DeviceManager)

def DeviceManager_getInstance():
    return _littleb.DeviceManager_getInstance()
DeviceManager_getInstance = _littleb.DeviceManager_getInstance

class uintVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, uintVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, uintVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _littleb.uintVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _littleb.uintVector___nonzero__(self)

    def __bool__(self):
        return _littleb.uintVector___bool__(self)

    def __len__(self):
        return _littleb.uintVector___len__(self)

    def __getslice__(self, i, j):
        return _littleb.uintVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _littleb.uintVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _littleb.uintVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _littleb.uintVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _littleb.uintVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _littleb.uintVector___setitem__(self, *args)

    def pop(self):
        return _littleb.uintVector_pop(self)

    def append(self, x):
        return _littleb.uintVector_append(self, x)

    def empty(self):
        return _littleb.uintVector_empty(self)

    def size(self):
        return _littleb.uintVector_size(self)

    def swap(self, v):
        return _littleb.uintVector_swap(self, v)

    def begin(self):
        return _littleb.uintVector_begin(self)

    def end(self):
        return _littleb.uintVector_end(self)

    def rbegin(self):
        return _littleb.uintVector_rbegin(self)

    def rend(self):
        return _littleb.uintVector_rend(self)

    def clear(self):
        return _littleb.uintVector_clear(self)

    def get_allocator(self):
        return _littleb.uintVector_get_allocator(self)

    def pop_back(self):
        return _littleb.uintVector_pop_back(self)

    def erase(self, *args):
        return _littleb.uintVector_erase(self, *args)

    def __init__(self, *args):
        this = _littleb.new_uintVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _littleb.uintVector_push_back(self, x)

    def front(self):
        return _littleb.uintVector_front(self)

    def back(self):
        return _littleb.uintVector_back(self)

    def assign(self, n, x):
        return _littleb.uintVector_assign(self, n, x)

    def resize(self, *args):
        return _littleb.uintVector_resize(self, *args)

    def insert(self, *args):
        return _littleb.uintVector_insert(self, *args)

    def reserve(self, n):
        return _littleb.uintVector_reserve(self, n)

    def capacity(self):
        return _littleb.uintVector_capacity(self)
    __swig_destroy__ = _littleb.delete_uintVector
    __del__ = lambda self: None
uintVector_swigregister = _littleb.uintVector_swigregister
uintVector_swigregister(uintVector)

class intVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _littleb.intVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _littleb.intVector___nonzero__(self)

    def __bool__(self):
        return _littleb.intVector___bool__(self)

    def __len__(self):
        return _littleb.intVector___len__(self)

    def __getslice__(self, i, j):
        return _littleb.intVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _littleb.intVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _littleb.intVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _littleb.intVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _littleb.intVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _littleb.intVector___setitem__(self, *args)

    def pop(self):
        return _littleb.intVector_pop(self)

    def append(self, x):
        return _littleb.intVector_append(self, x)

    def empty(self):
        return _littleb.intVector_empty(self)

    def size(self):
        return _littleb.intVector_size(self)

    def swap(self, v):
        return _littleb.intVector_swap(self, v)

    def begin(self):
        return _littleb.intVector_begin(self)

    def end(self):
        return _littleb.intVector_end(self)

    def rbegin(self):
        return _littleb.intVector_rbegin(self)

    def rend(self):
        return _littleb.intVector_rend(self)

    def clear(self):
        return _littleb.intVector_clear(self)

    def get_allocator(self):
        return _littleb.intVector_get_allocator(self)

    def pop_back(self):
        return _littleb.intVector_pop_back(self)

    def erase(self, *args):
        return _littleb.intVector_erase(self, *args)

    def __init__(self, *args):
        this = _littleb.new_intVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _littleb.intVector_push_back(self, x)

    def front(self):
        return _littleb.intVector_front(self)

    def back(self):
        return _littleb.intVector_back(self)

    def assign(self, n, x):
        return _littleb.intVector_assign(self, n, x)

    def resize(self, *args):
        return _littleb.intVector_resize(self, *args)

    def insert(self, *args):
        return _littleb.intVector_insert(self, *args)

    def reserve(self, n):
        return _littleb.intVector_reserve(self, n)

    def capacity(self):
        return _littleb.intVector_capacity(self)
    __swig_destroy__ = _littleb.delete_intVector
    __del__ = lambda self: None
intVector_swigregister = _littleb.intVector_swigregister
intVector_swigregister(intVector)

class BleServicePtrVec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BleServicePtrVec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BleServicePtrVec, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _littleb.BleServicePtrVec_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _littleb.BleServicePtrVec___nonzero__(self)

    def __bool__(self):
        return _littleb.BleServicePtrVec___bool__(self)

    def __len__(self):
        return _littleb.BleServicePtrVec___len__(self)

    def __getslice__(self, i, j):
        return _littleb.BleServicePtrVec___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _littleb.BleServicePtrVec___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _littleb.BleServicePtrVec___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _littleb.BleServicePtrVec___delitem__(self, *args)

    def __getitem__(self, *args):
        return _littleb.BleServicePtrVec___getitem__(self, *args)

    def __setitem__(self, *args):
        return _littleb.BleServicePtrVec___setitem__(self, *args)

    def pop(self):
        return _littleb.BleServicePtrVec_pop(self)

    def append(self, x):
        return _littleb.BleServicePtrVec_append(self, x)

    def empty(self):
        return _littleb.BleServicePtrVec_empty(self)

    def size(self):
        return _littleb.BleServicePtrVec_size(self)

    def swap(self, v):
        return _littleb.BleServicePtrVec_swap(self, v)

    def begin(self):
        return _littleb.BleServicePtrVec_begin(self)

    def end(self):
        return _littleb.BleServicePtrVec_end(self)

    def rbegin(self):
        return _littleb.BleServicePtrVec_rbegin(self)

    def rend(self):
        return _littleb.BleServicePtrVec_rend(self)

    def clear(self):
        return _littleb.BleServicePtrVec_clear(self)

    def get_allocator(self):
        return _littleb.BleServicePtrVec_get_allocator(self)

    def pop_back(self):
        return _littleb.BleServicePtrVec_pop_back(self)

    def erase(self, *args):
        return _littleb.BleServicePtrVec_erase(self, *args)

    def __init__(self, *args):
        this = _littleb.new_BleServicePtrVec(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _littleb.BleServicePtrVec_push_back(self, x)

    def front(self):
        return _littleb.BleServicePtrVec_front(self)

    def back(self):
        return _littleb.BleServicePtrVec_back(self)

    def assign(self, n, x):
        return _littleb.BleServicePtrVec_assign(self, n, x)

    def resize(self, *args):
        return _littleb.BleServicePtrVec_resize(self, *args)

    def insert(self, *args):
        return _littleb.BleServicePtrVec_insert(self, *args)

    def reserve(self, n):
        return _littleb.BleServicePtrVec_reserve(self, n)

    def capacity(self):
        return _littleb.BleServicePtrVec_capacity(self)
    __swig_destroy__ = _littleb.delete_BleServicePtrVec
    __del__ = lambda self: None
BleServicePtrVec_swigregister = _littleb.BleServicePtrVec_swigregister
BleServicePtrVec_swigregister(BleServicePtrVec)

class BleCharactersiticPtrVec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BleCharactersiticPtrVec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BleCharactersiticPtrVec, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _littleb.BleCharactersiticPtrVec_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _littleb.BleCharactersiticPtrVec___nonzero__(self)

    def __bool__(self):
        return _littleb.BleCharactersiticPtrVec___bool__(self)

    def __len__(self):
        return _littleb.BleCharactersiticPtrVec___len__(self)

    def __getslice__(self, i, j):
        return _littleb.BleCharactersiticPtrVec___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _littleb.BleCharactersiticPtrVec___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _littleb.BleCharactersiticPtrVec___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _littleb.BleCharactersiticPtrVec___delitem__(self, *args)

    def __getitem__(self, *args):
        return _littleb.BleCharactersiticPtrVec___getitem__(self, *args)

    def __setitem__(self, *args):
        return _littleb.BleCharactersiticPtrVec___setitem__(self, *args)

    def pop(self):
        return _littleb.BleCharactersiticPtrVec_pop(self)

    def append(self, x):
        return _littleb.BleCharactersiticPtrVec_append(self, x)

    def empty(self):
        return _littleb.BleCharactersiticPtrVec_empty(self)

    def size(self):
        return _littleb.BleCharactersiticPtrVec_size(self)

    def swap(self, v):
        return _littleb.BleCharactersiticPtrVec_swap(self, v)

    def begin(self):
        return _littleb.BleCharactersiticPtrVec_begin(self)

    def end(self):
        return _littleb.BleCharactersiticPtrVec_end(self)

    def rbegin(self):
        return _littleb.BleCharactersiticPtrVec_rbegin(self)

    def rend(self):
        return _littleb.BleCharactersiticPtrVec_rend(self)

    def clear(self):
        return _littleb.BleCharactersiticPtrVec_clear(self)

    def get_allocator(self):
        return _littleb.BleCharactersiticPtrVec_get_allocator(self)

    def pop_back(self):
        return _littleb.BleCharactersiticPtrVec_pop_back(self)

    def erase(self, *args):
        return _littleb.BleCharactersiticPtrVec_erase(self, *args)

    def __init__(self, *args):
        this = _littleb.new_BleCharactersiticPtrVec(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _littleb.BleCharactersiticPtrVec_push_back(self, x)

    def front(self):
        return _littleb.BleCharactersiticPtrVec_front(self)

    def back(self):
        return _littleb.BleCharactersiticPtrVec_back(self)

    def assign(self, n, x):
        return _littleb.BleCharactersiticPtrVec_assign(self, n, x)

    def resize(self, *args):
        return _littleb.BleCharactersiticPtrVec_resize(self, *args)

    def insert(self, *args):
        return _littleb.BleCharactersiticPtrVec_insert(self, *args)

    def reserve(self, n):
        return _littleb.BleCharactersiticPtrVec_reserve(self, n)

    def capacity(self):
        return _littleb.BleCharactersiticPtrVec_capacity(self)
    __swig_destroy__ = _littleb.delete_BleCharactersiticPtrVec
    __del__ = lambda self: None
BleCharactersiticPtrVec_swigregister = _littleb.BleCharactersiticPtrVec_swigregister
BleCharactersiticPtrVec_swigregister(BleCharactersiticPtrVec)



import ctypes

# a ctypes callback prototype



def registerCallbackEventRead(dev, uuid, py_callback_ev):
    py_callback_type_re = ctypes.CFUNCTYPE(ctypes.c_int,  ctypes.py_object, ctypes.py_object)
# wrap the python callback with a ctypes function pointer
    func_er = py_callback_type_re(py_callback_ev)

# get the function pointer of the ctypes wrapper by casting it to void* and taking its value
    func_er_ptr = ctypes.cast(func_er, ctypes.c_void_p).value
    dev.registerCallbackReadEvent(uuid, func_er_ptr)

def registerCallbackChangeState(dev, py_callback_cs):
    py_callback_type_cs = ctypes.CFUNCTYPE(ctypes.c_int,  ctypes.py_object)
    f_cs = py_callback_type_cs(py_callback_cs)
    f_cs_ptr = ctypes.cast(f_cs, ctypes.c_void_p).value
    dev.registerCallbackStateEvent(f_cs_ptr)

# This file is compatible with both classic and new-style classes.


