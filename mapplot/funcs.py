"""Helper functions to use with mapplot for convenience"""


def eq(key, value):
    """Return function that compares item to value."""
    return lambda x: x[key] == value


def on_val(func):
    """Return function that applies func to value in dict."""
    return lambda (k, v): (k, func(v))
