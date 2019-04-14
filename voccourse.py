from course import Course


class VocationalCourse(Course):
    _cancellationPenaltyAddRate = 0.1
    _specialisedIndustries = ["Engineering", "Electronics", "Computing"]

    def __init__(self, courseCode, title, description, fees, industry):
        Course.__init__(self, courseCode, title, description, fees)
        self._industry = industry

    def getSubsidy(self, income, age):
        if income:
            if self._industry in VocationalCourse._specialisedIndustries:
                industry_cost = 0.1
            else:
                industry_cost = 0
            age = int(age)
            if age > 60:
                subsidy = self.fees * (0.95 - industry_cost)
            elif 60 > age > 55:
                subsidy = self.fees * (0.9 - industry_cost)
            else:
                subsidy = self.fees * (0.8 - industry_cost)
            if subsidy < 0:
                subsidy = 0
        else:
            subsidy = 0

        return int(subsidy)

    def cancellationPenaltyRate(self, days):
        return super(VocationalCourse, self).cancellationPenaltyRate(days) + VocationalCourse._cancellationPenaltyAddRate

    def __str__(self):
        return 'Vocational course code: {}, Title: {}, Fees: ${}, Description: {}, Industry: {}'.format(self.courseCode,
                                                                                                       self._title,
                                                                                                       self._fees,
                                                                                                       self._description,
                                                                                                       self._industry)


if __name__ == "__main__":
    v_course = VocationalCourse("C001", "Gluten-free diet fees", "How to start...", 100.00, "Engineering")
    print(str(v_course))
