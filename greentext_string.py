import ctypes

pythonapi = ctypes.pythonapi


class PyNumberMethods(ctypes.Structure):
    _fields_ = [
        ('nb_add', ctypes.c_void_p),
        ('nb_subtract', ctypes.c_void_p),
        ('nb_multiply', ctypes.c_void_p),
        ('nb_remainder', ctypes.c_void_p),
        ('nb_divmod', ctypes.c_void_p),
        ('nb_power', ctypes.c_void_p),
        ('nb_negative', ctypes.c_void_p),
        ('nb_positive', ctypes.c_void_p),
        ('nb_absolute', ctypes.c_void_p),
        ('nb_bool', ctypes.c_void_p),
        ('nb_invert', ctypes.c_void_p)
    ]


class PyTypeObject(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('ob_type', ctypes.POINTER(ctypes.py_object)),
        ('ob_size', ctypes.c_ssize_t),
        ('tp_name', ctypes.c_char_p),
        ('tp_basicsize', ctypes.c_ssize_t),
        ('tp_itemsize', ctypes.c_ssize_t),
        ('tp_dealloc', ctypes.c_void_p),
        ('tp_vectorcall_offset', ctypes.c_ssize_t),
        ('tp_getattr', ctypes.c_void_p),
        ('tp_setattr', ctypes.c_void_p),
        ('tp_as_async', ctypes.c_void_p),
        ('tp_repr', ctypes.c_void_p),
        ('tp_as_number', ctypes.POINTER(PyNumberMethods))
    ]


str_addr = id(str)

str_type = ctypes.cast(str_addr, ctypes.POINTER(PyTypeObject))


@ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
def greentext_string(self):
    print('\033[92m>' + self)
    return self


str_type.contents.tp_as_number.contents.nb_invert = ctypes.cast(greentext_string, ctypes.c_void_p)

~'Be me'
~'Mess with Python unstable API'
~'Feels good man'
