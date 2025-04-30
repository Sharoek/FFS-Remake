from validator import Validator

class AgeValidator(Validator):
    def _validate(self, data):
        age = data.get("age", 0)
        if not isinstance(age, int) or not (0 < age < 120):
            raise ValueError("Ongeldige leeftijd.")