import datetime


class Member:
    _nextId = 1

    def __init__(self, name, contact, dob, monthlyIncome = None):
        self._mid = Member._nextId
        Member._nextId += 1
        self._name = name
        self._contact = contact
        self._dob = dob
        self._monthlyIncome = monthlyIncome

    def age(self, onThisDate):
        delta = onThisDate - self._dob
        year = int(delta.days/365)
        return str(year)

    @property
    def mid(self):
        return self._mid
        pass

    @property
    def monthlyIncome(self):
        return self._monthlyIncome
        pass

    def __str__(self):
        if self.monthlyIncome:
            return "Id: {} Name: {}\t Contact: {} Monthly Income:${} Date of birth: {} Age: {}".format(self.mid, self._name,
                                                                                          self._contact,
                                                                                          self.monthlyIncome, self._dob,
                                                                                                       self.age(datetime.date.today()))
        else:
            return "Id: {} Name: {}\t Contact: {} Monthly Income: Undisclosed Date of birth: {} Age: {}".format(self.mid,
                                                                                                        self._name,
                                                                                               self._contact,
                                                                                               self._dob,
                                                                                            self.age(datetime.date.today()))
        pass


if __name__ == "__main__":
    member = Member("Helen", 111111111, datetime.date(1964, 1, 1), 1000.0)
    member1 = Member("Irene", 222222222222, datetime.date(1949, 10, 1))
    age = member1.age(datetime.date.today())
    print(str(member))
    print(str(member1))


