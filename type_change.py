def cast(typ):
    def decorator(func):
        def wrapper(args, **kwargs):
            result = func(args, **kwargs)
            try:
                result = typ(result)
            except:
                pass
            return result
        return wrapper
    return decorator
@cast(str)
def transformation(value):
    return value

result = transformation(579)
print(type(result))
print(result)

