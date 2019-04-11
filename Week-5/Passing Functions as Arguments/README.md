Passing Functions as Arguments


Like everything else in Python, functions are objects. Since they are objects, they can be supplied as arguments to other functions.

We can test this concept by creating an example function that simply runs other functions:
def function_runner(f):
    """ (function) -> NoneType

    Call f.
    """

    f()

We can test this concept by having it call one of two other functions:
def function_1():
    print("function_1 was called.")

def function_2():
    print("function_2 was called.")

If we call function_runner passing it the name of function_1,
function_runner(function_1)

we get the results:
function_1 was called.

If we call it using function_2
function_runner(function_2)

we see the following:
function_2 was called.