"task1"
def sieve(lst):
    return tuple(sorted(set(lst), reverse=True))
"task2"
def uniquenumbers(a, b):
    return [x for x in range(a, b+1) if len(set(str(x))) == len(str(x))]