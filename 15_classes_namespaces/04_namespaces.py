var = 'var'

def scope_test():
    def do_local():
        var = "this only stays in do_local scope"
        return var

    def do_nonlocal():
        nonlocal var
        var = "this goes one level above (scope_test has access to it)"

    def do_global():
        global var
        var = "this goes only to global scope (out of scope_test function)"

    var = "defined in scope test"
    do_local()
    print("After local assignment:", var)
    do_nonlocal()
    print("After nonlocal assignment:", var)
    do_global()
    print("After global assignment:", var)

scope_test()
print("In global scope:", var)