from validator import Validator
import re

class PhoneValidator(Validator):
    def _validate(self, data):
        phone = data.get("phone", "")
        if not re.match(r"^\d{8}$", phone):
            raise ValueError("Telefoonnummer moet 8 cijfers bevatten.")