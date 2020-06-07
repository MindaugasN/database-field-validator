class CharField:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        
    def __set_name__(self, instance, property_name):
        self.property_name = property_name
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f'{self.property_name} must be a type of string.')
        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(f'{self.property_name} cannot be less than {self.min_value} char length.')
        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(f'{self.property_name} cannot be greater than {self.max_value} char length.')
        instance.__dict__[self.property_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)
