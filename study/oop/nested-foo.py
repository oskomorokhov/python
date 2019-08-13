def checkio(f, g):

    def h(*args, **kwargs):

        try:
            a = f(*args, **kwargs)
            print("f ok", f(*args, **kwargs))
            if a is None:
                raise ValueError

        except:
            status = "f_error"
            try:
                b = g(*args, **kwargs)
                print("g ok", g(*args, **kwargs))
                if b is None:
                    raise ValueError
            except:
                status = "both_error"
                return (None, status)
            else:
                return (g(*args, **kwargs), status)

        else:
            try:
                if a == g(*args, **kwargs):
                    return (a, 'same')
                else:
                    if g(*args, **kwargs) is None:
                        raise ValueError
                    return (a, 'different')
            except:
                print("g not ok")
                return (a, "g_error")

    return h


'''assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"'''


def f(x): return abs(x)


def g(x):
    if x > 0:
        return x
    elif x < 0:
        return -x


c = checkio(f, g)
result = c(0)
print(result)

# assert checkio(f,g)(0) = (0,'g_error')

print("Checks done!")
