from voccourse import VocationalCourse
from nonvoccourse import NonVocationalCourse
from cooperative import Cooperative
from member import Member
from schedulcourse import ScheduledCourse
import datetime


class Menu:
    def __init__(self):
        self.menu = "Menu:\n1. List Members\n2. List Courses\n3. List Schedules \n4. Add Member\n5. Add Course\n6. Add Schedule\n" \
           "7. Enroll  Member\n8. Cancel  Enrollment\n0. Exit"
        self.choice = None

    def menu_start(self, coop):
        while self.choice != 0:
            print(self.menu)

            correct_choice = False
            while not correct_choice:
                self.choice = input("Enter choice:")
                try:
                    self.choice = int(self.choice)
                    if 9 > self.choice >= 0:
                        correct_choice = True
                    else:
                        raise ValueError
                except ValueError:
                    print("Enter a number from 0 to 8")
            if self.choice == 1:
                self.option_one(coop)
            elif self.choice == 2:
                self.option_two(coop)
            elif self.choice == 3:
                self.option_three(coop)
            elif self.choice == 4:
                self.option_four(coop)
            elif self.choice == 5:
                self.option_five(coop)
            elif self.choice == 6:
                self.option_six(coop)
            elif self.choice == 7:
                self.option_seven(coop)
            elif self.choice == 8:
                self.option_eight(coop)



    def option_one(self, coop):
        print(coop.membersStr())

    def option_two(self, coop):
        print(coop.coursesStr())

    def option_three(self, coop):
        print(coop.scheduledCoursesStr())

    def option_four(self, coop):
        try:
            name = input("Enter name:")
        except ValueError:
            print("Error in input name")
            return 0
        try:
            contact = int(input("Enter contact:"))
        except ValueError:
            print("Error in input contact")
            return 0
        date = self.correct_date('day of birth')
        try:
            money = input("Enter monthly income to nearest whole number or <Enter> if not disclosing: ")
            if money == '':
                money = None
            else:
                money = int(money)

        except ValueError:
            print("Error in input monthly income")
            return 0
        try:

            coop.addMember(Member(name, contact, date, money))
            print(coop.membersStr())
            print("Add member operation successful")
        except UnboundLocalError:
            print("Operation is not successful")


    def option_five(self, coop):
        type_course_correct = False
        while not type_course_correct:
            try:
                type_course = input("Enter V or N for Vocational or Non Vocational course: ")
                if type_course == "V" or type_course == "N":
                    type_course_correct = True
                else:
                    raise TypeError
            except TypeError:
                print("Type of Course should be N or V")
                type_course_correct = False
        code = input("Enter course code: ")
        if coop.getCourse(code):
            print("Error in Add course operation. This Course is already in Cooperative")
            return 0
        title = input("Enter a title: ")
        description = input("Enter description: ")
        fees_correct = False
        while not fees_correct:
            try:
                fees = int(input("Enter Fees: "))
                fees_correct =True
            except ValueError:
                fees_correct = False
        if type_course == "V":
            industry = input("Enter Industry: ")
            coop.addCourse(VocationalCourse(code, title, description, fees, industry))
        else:
            coop.addCourse(NonVocationalCourse(code, title, description, fees))
        print("Add Course successful")

    def option_six(self, coop):
        code = input("Enter course code: ")
        date = self.correct_date("schedule")
        if coop.getScheduledCourse(code, date) :
            print("Error in Add course operation. This Course is already scheduled")
            return 0
        elif not coop.getCourse(code):
            print("Error in Add course operation. This Course is not in course list")
            return 0
        else:
            coop.addScheduledCourse(ScheduledCourse(coop.getCourse(code), date))
            print("Add Scheduled Course successful")
        pass

    def option_seven(self, coop):
        user_data = self.correct_enroll(coop)
        if user_data == 0:
            return 0
        mid = user_data[0]
        code = user_data[1]
        date = user_data[2]
        coop.enroll(mid, code, date)
        print(coop.getMember(mid))
        fee = coop.getCourse(code).fees
        subsidy = coop.getCourse(code).getSubsidy(coop.getMember(mid).monthlyIncome, coop.getMember(mid).age(datetime.date.today()))
        payment = fee - subsidy
        course_to_enroll = coop.getScheduledCourse(code, date)
        result = course_to_enroll.addParticipant(coop.getMember(mid))
        if not result:
            print("Participant is already up to course")
            return 0
        print("Course fee: {} Subsidy: {} Payment:{}".format(fee, subsidy, payment))

    def option_eight(self, coop):
        user_data = self.correct_enroll(coop)
        if user_data == 0:
            return 0
        mid = user_data[0]
        code = user_data[1]
        date = user_data[2]
        date_cancel = self.correct_date("cancellation")
        days = date - date_cancel
        mon_income = coop.getMember(mid).monthlyIncome
        age = coop.getMember(mid).age(datetime.date.today())
        penalty = coop.getCourse(code).cancellationPenalty(mon_income, age, days)
        penalty_rate = coop.getCourse(code).cancellationPenaltyRate(days)
        print("Cancellation penalty for {} days {}".format(days.days, penalty_rate))
        print(coop.getMember(mid))
        fee = coop.getCourse(code).fees
        subsidy = coop.getCourse(code).getSubsidy(coop.getMember(mid).monthlyIncome,
                                                  coop.getMember(mid).age(datetime.date.today()))
        payment = fee - subsidy
        print("Course fee: {} Subsidy: {} Payment:{}".format(fee, subsidy, payment))
        print("Penalty rate: {}% Penalty amount: {}$".format(penalty_rate, penalty))
        course_to_offroll = coop.getScheduledCourse(code, date)
        result = course_to_offroll.removeParticipant(coop.getMember(mid))
        if not result:
            print("Participant is not in list. Operation unsuccessful")
            return 0
        else:
            print("Cancellation successful.")
        pass


    def correct_date(self, name):
        date_correct = False
        while not date_correct:
            try:
                date = input("Enter {} date in format d/m/yyyy:".format(name)).split('/')
                date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
                date_correct = True
            except (ValueError, IndexError):
                print("Please  enter  date  in  d/m/yyyy format")
                date_correct = False
        return date

    def correct_enroll(self, coop):
        mid = input("Enter member id:")
        try:
            mid = int(mid)
        except ValueError:
            print("Incorrect member id")
            return 0
        if not coop.getMember(mid):
            print("There is no member with such id")
            return 0
        code = input("Enter course code:")
        if not coop.getCourse(code):
            print("There is no course with such code")
            return 0
        date = self.correct_date("scheduled")
        if not coop.getScheduledCourse(code, date):
            print("There is no scheduled course on this date")
            return 0
        return [mid, code, date]


if __name__ == "__main__":
    coop = Cooperative()
    menu = Menu().menu_start(coop)