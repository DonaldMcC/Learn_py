# This will introduce the simplest of maths functions as everyone understands
# them.  Obviously there is no actual requirement to create these functions
# as python has them and many others built in.
# However it should provide the key features of functions in that they accept
# parameters and return a value.
# We will keep the add function super-clean but improve further ones with
# docstrings and options

def func_add(a, b):
    return a + b
    
    
def func_subtract(a, b):
    """
        :param a:
        :param b:
        :return a - b:

        >>> func_subtract(10, 7)
        3
        >>> func_subtract(5, 3)
        2
        """
    return a - b

    
def func_multiply(a, b):
    return a * b

    
def func_divide(a, b):
    return a / b


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    'Can run with -v option if you want to confirm tests were run'
    _test()
