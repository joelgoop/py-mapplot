"""Helper functions to use with mapplot for convenience"""
import operator

def eq(key,value):
    """Return function that compares item to value."""
    return lambda x: x[key]==value

def prop(key):
    """Return function that gets item by key."""
    return operator.itemgetter(key)

def on_val(func):
    """Return function that applies func to value in dict."""
    return lambda (k,v): (k,func(v))

def get(idx):
    """Return function to get index idx."""
    return lambda x: x[idx]
