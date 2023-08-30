def validator(cmp, exc):
    def decorator(setter):  # a decorator for the setter
        def wrapper(self, value):  # the wrapper around your setter
            if cmp(value):  # if cmp function returns True, raise the passed exception
                raise exc
            setter(self, value)  # otherwise just call the setter to do its job

        return wrapper

    return decorator


def str_validator(setter):
    """
    Validates a string value to raise a ValueError if it is blank or None
    """
    def wrapper(self, value):
        if value == "" or value is None:
            raise ValueError(f"'{setter.__name__}' can't be blank or None")
        setter(self, value)

    return wrapper


def int_validator(setter):
    """
    Validates an integer value to raise a ValueError if it is less than 0
    """
    def wrapper(self, value):
        if value < 0:
            raise ValueError(f"'{setter.__name__}' can't be less than 0")
        setter(self, value)

    return wrapper
