from abc import ABCMeta, abstractmethod, abstractproperty


class Course:
    __metaclass__ = ABCMeta
    _baseCancellationPenaltyRate = 0.3

    def __init__(self, courseCode, title, description, fees):
        self._courseCode = courseCode
        self._title = title
        self._description = description
        self._fees = fees

    @classmethod
    def getDaseCancellationPenaltyRate(cls):
        return Course._baseCancellationPenaltyRate
        pass

    @classmethod
    def setBaseCancellationPenaltyRate(cls, baseCancellationPenatlyRate):
        Course._baseCancellationPenaltyRate = baseCancellationPenatlyRate
        pass

    @abstractmethod
    def getSubsidy(self, income, age):
        pass

    def cancellationPenaltyRate(self, days):
        days = int(days.days)
        if days > 7:
            return 0
        elif 7 > days > 4:
            return Course._baseCancellationPenaltyRate/2
        else:
            return Course._baseCancellationPenaltyRate
        pass

    def cancellationPenalty(self, income, age, days):
        cpr = self.cancellationPenaltyRate(days)
        subsidy = self.getSubsidy(income, age)
        fee = self.fees - subsidy
        return fee*cpr
        
    @property
    def courseCode(self):
        return self._courseCode
        pass

    @property
    def fees(self):
        return self._fees
        pass

    def __str__(self):
        return 'Course code: {}, Title: {}, Fees: {}, Description: {}'.format(self.courseCode, self._title, self._fees,
                                                                              self._description)
        pass


if __name__ == "__main__":
    course = Course("E012", "Engineering  In  Business", "Development  and  implementation  of  business  solutions",
                    "$10000.0")
    print(str(course))