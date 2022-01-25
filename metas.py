class FloatFieldMeta(type):
    """
    FloatFieldMeta type class
    """

    def __call__(cls, label, value):
        if not isinstance(label, str):
            raise TypeError('label must be a string')

        if not isinstance(value, float):
            raise TypeError('value must be a float')
        elif not value >= 0:
            raise TypeError('value must be greater than or equal 0')

        return super().__call__(label, value)


class IntegerFieldMeta(type):
    """
    IntegerFieldMeta type class
    """

    def __call__(cls, label, value):
        if not isinstance(label, str):
            raise TypeError('label must be a string')

        if not isinstance(value, int):
            raise TypeError('value must be a integer')
        elif not (0 <= value <= 150):
            raise TypeError('value must be in between 0 and 150')

        return super().__call__(label, value)


class StringFieldMeta(type):
    """
    IntegerFieldMeta type class with animal habit list
    """

    _animal_habitat: list = ['air', 'land', 'water']

    def __call__(cls, label, value):
        if not isinstance(label, str):
            raise TypeError('label must be a string')

        if not isinstance(value, str):
            raise TypeError('value must be a string')

        if label == 'The habitat' and value not in cls._animal_habitat:
            raise TypeError('value must be in between: {}'.format(cls._animal_habitat))

        return super().__call__(label, value)


class RecordMeta(type):
    """
    IntegerFieldMeta type class
    """

    def __new__(mcs, cls_name, bases, attrs):
        # Implement the class creation by manipulating the attr dictionary
        return super(RecordMeta, mcs).__new__(mcs, cls_name, bases, attrs)
