from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_validator):
        self._next = next_validator
        return next_validator  

    def validate(self, data):
        self._validate(data)
        if self._next:
            self._next.validate(data)

    @abstractmethod
    def _validate(self, data):
        pass