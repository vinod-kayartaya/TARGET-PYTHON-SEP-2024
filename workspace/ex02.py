def say_hello(name:str, city:str="Bangalore") -> str:
    """
    This is an example function to accept couple of paramters
    and return a value corresponding to the same
    """

    if type(name) is not str or type(city) is not str:
        raise TypeError("name/city must be <str>")

    return f"Hello {name}, how is weather in {city}?"
