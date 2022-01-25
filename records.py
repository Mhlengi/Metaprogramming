from metas import FloatFieldMeta, IntegerFieldMeta, StringFieldMeta, RecordMeta


class FloatField(metaclass=FloatFieldMeta):
    """
    FloatField with label & value
    """

    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __float__(self):
        return self.value

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value


class IntegerField(metaclass=IntegerFieldMeta):
    """
    IntegerField with label & value
    """

    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __int__(self):
        return self.value

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value


class StringField(metaclass=StringFieldMeta):
    """
    StringField with label & value
    """

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value

    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __str__(self):
        return self.value


class Record(metaclass=RecordMeta):
    """
    Record class with meta
    """
    pass


class Person(Record):
    """
    Person record with name, age, income
    """

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @property
    def income(self):
        return self._income

    def __init__(self, name, age, income):
        self._name = StringField(label="The name", value=name)
        self._age = IntegerField(label="The person's age", value=age)
        self._income = FloatField(label="The person's income", value=income)

    def __str__(self):
        return f"{self.__class__.__name__}( \n  # {self.name.label} \n  name='{self.name.value}' " \
               f"\n\n  # {self.age.label}  \n  age={self.age.value} \n\n  # {self.income.label}  " \
               f"\n  income={self.income.value} \n)"


class Named(Record):
    """
    A base class for things with names
    """

    def __init__(self, name):
        # super(Named, self).__init__()
        self._name = StringField(label="The name", value=name)

    @property
    def name(self):
        return self._name


class Animal(Named):
    """
    An animal
    """

    def __init__(self, name, habitat, weight):
        super(Animal, self).__init__(name)
        self._habitat = StringField(label="The habitat", value=habitat)
        self._weight = FloatField(label="The animals weight (kg)", value=weight)

    @property
    def habitat(self):
        return self._habitat

    @property
    def weight(self):
        return self._weight


class Dog(Animal):
    """
    A type of animal
    """

    def __init__(self, name, habitat, weight, bark):
        super(Dog, self).__init__(name, habitat, weight)
        self._bark = StringField(label="Sound of bark", value=bark)

    @property
    def bark(self):
        return self._bark
