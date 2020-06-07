from numbers import Integral

from model.base import BaseValidator


class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, Integral):
            raise ValueError(f'{self.property_name} must be a type of int.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.property_name} cannot be less than {self.min_value}.')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.property_name} cannot be greater than {self.max_value}.')
