from validator import Validator

class NameValidator(Validator):
    def _validate(self, data):
        name = data.get("first_name", "")
        if not name.isalpha() or len(name) < 2:
            raise ValueError("Ongeldige voornaam: alleen letters en minstens 2 tekens.")