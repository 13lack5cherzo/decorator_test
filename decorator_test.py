class Decorator:
    """ class to decorate a function """

    def __init__(self, **_decorator_kwargs):
        """
        magic init function for decorator
        :param _decorator_kwargs: dict() of arguments passed into the decorator
        """
        self._decorator_kwargs = _decorator_kwargs

    def __call__(self, _func):
        """
        magic call function for decorator
        :param _func: decorated function to get feature value
        :return: feature value put into dict() using cls.set_ft_value
        """

        def _func_wrapper(*func_args, **func_kwargs):
            """ function to wrap decorated function """
            # call decorated function
            func_output = _func(*func_args, **func_kwargs)
            # modify decorated function output
            wrapper_output = Decorator.modify_function(x=func_output, **self._decorator_kwargs)
            return wrapper_output

        return _func_wrapper

    @staticmethod
    def modify_function(x, **kwargs):
        """ function to modify decorated function """
        print(f"modify decorated function with {kwargs}")
        return x


@Decorator(decorator_param1="decorator_param1")
def decorated_function(x=1, y=1):
    return x + y


def main():
    print(decorated_function(x=1, y=1))

    exit(0)


if __name__ == '__main__':
    main()

