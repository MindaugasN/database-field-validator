class BaseValidator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        
    def __set_name__(self, instance, property_name):
        self.property_name = property_name
               
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def validate(self, value):
        """Implement validation method separately for each class"""
        pass
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.property_name] = value
