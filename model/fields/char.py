from model.base import BaseValidator


class CharField(BaseValidator):
    def __init__(self, min_value=None, max_value=None):
        min_value = max(min_value or 0, 0)
        super().__init__(min_value, max_value)
        
    def __set_name__(self, instance, property_name):
        self.property_name = property_name
        
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a type of string.')
        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(f'{self.property_name} cannot be less than {self.min_value} char length.')
        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(f'{self.property_name} cannot be greater than {self.max_value} char length.')
