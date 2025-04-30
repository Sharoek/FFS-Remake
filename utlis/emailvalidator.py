from validator import Validator
import re

class EmailValidator(Validator):
    def _validate(self, data):
        email = data.get("email", "")
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email):
            raise ValueError("Ongeldig e-mailadres.")