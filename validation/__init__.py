def validator(cmp, exc):
    def decorator(setter):  # a decorator for the setter
        def wrapper(self, value):  # the wrapper around your setter
            if cmp(value):  # if cmp function returns True, raise the passed exception
                raise exc
            setter(self, value)  # otherwise just call the setter to do its job

        return wrapper

    return decorator
