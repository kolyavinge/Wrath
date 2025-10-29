import ctypes

from termcolor import colored


def warn(message):
    print(colored(f"Warning: {message}", "yellow"))


def convertListToLPLPChar(lst):
    c_char_p_array = (ctypes.c_char_p * len(lst))()
    for i, s in enumerate(lst):
        c_char_p_array[i] = s.encode("utf-8")
    LP_LP_c_char = ctypes.POINTER(ctypes.POINTER(ctypes.c_char))
    result = ctypes.cast(c_char_p_array, LP_LP_c_char)

    return result
