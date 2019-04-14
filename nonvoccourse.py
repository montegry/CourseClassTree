from course import Course


class NonVocationalCourse(Course):
    def __init__(self, courseCode, title, description, fees):
        Course.__init__(self, courseCode, title, description, fees)

    def getSubsidy(self, income, age):
        if income and income > 1200:
            subsidy = 0.5
        else:
            subsidy = 0
        subsidy = subsidy * self.fees
        return subsidy

    def __str__(self):
        return 'Non Vocational course code: {}, Title: {}, Fees: ${}, Description: {}'.format(self.courseCode,
                                                                                             self._title,
                                                                                             self._fees,
                                                                                             self._description
                                                                                             )


if __name__ == "__main__":
    nv_course = NonVocationalCourse("C001", "Gluten-free diet fees", "How to start...", 100.00)
    print(str(nv_course))
