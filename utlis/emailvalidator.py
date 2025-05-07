from validator import Validator
import re

class EmailValidator(Validator):
    def _validate(self, data):
        email = data.get("email", "")

        email_regex = re.compile(
            r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+"
            r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
            r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|'
            r'\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@'
            r"(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
            r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|"
            r"\[(?:(?:(2(5[0-5]|[0-4][0-9])|"
            r"1[0-9][0-9]|[1-9]?[0-9]))\.){3}"
            r"(?:(2(5[0-5]|[0-4][0-9])|"
            r"1[0-9][0-9]|[1-9]?[0-9])|"
            r"[a-z0-9-]*[a-z0-9]:"
            r"(?:[\x01-\x08\x0b\x0c\x0e-\x1f"
            r"\x21-\x5a\x53-\x7f]|"
            r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",
            re.IGNORECASE
        )
        
        if not re.match(email_regex, email):
            raise ValueError("Ongeldig e-mailadres.")