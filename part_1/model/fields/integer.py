from numbers import Integral


class IntegerField:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        
    def __set_name__(self, instance, property_name):
        self.property_name = property_name
        
    def __set__(self, instance, value):
        if not isinstance(value, Integral):
            raise ValueError(f'{self.property_name} must be a type of int.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.property_name} cannot be less than {self.min_value}.')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.property_name} cannot be greater than {self.max_value}.')
        instance.__dict__[self.property_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)
