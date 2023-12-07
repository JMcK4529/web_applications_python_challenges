import re

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        return re.match(
            r"^[a-z]{1,2}\d[a-z|\d]?\s*\d[a-z]{2}$",
            postcode,
            re.IGNORECASE) is not None
