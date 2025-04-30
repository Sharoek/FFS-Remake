import re
from validator import Validator

class ZipCodeValidator(Validator):
    def _validate(self, data):
        zip_code = data.get("zip_code", "")
        if not re.match(r"^\d{4}[A-Z]{2}$", zip_code):
            raise ValueError("Ongeldige postcode. Verwacht: 1234AB.")