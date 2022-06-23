class Validator:

    def __init__(self, gender: int, realty: int, count_children: int, income_type: int, family_status: int,
                 time_employed: float, email: int, family_members: int):
        self.gender = gender
        self.realty = realty
        self.count_children = count_children
        self.income_type = income_type
        self.family_status = family_status
        self.time_employed = time_employed
        self.email = email
        self.family_members = family_members

    def isValid(self) -> bool:

        if self.gender != 0 and self.gender != 1:
            return False

        if self.realty != 0 and self.realty != 1:
            return False

        if self.count_children < 0 or self.count_children is None:
            return False

        if self.income_type < 0 or self.income_type > 4 or self.income_type is None:
            return False

        if self.time_employed < 0 or self.time_employed is None:
            return False

        if self.email != 0 and self.email != 1:
            return False

        if self.family_members < 0 or self.family_members is None:
            return False

        return True



