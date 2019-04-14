from voccourse import VocationalCourse
from nonvoccourse import NonVocationalCourse
import menu
from member import Member
from schedulcourse import ScheduledCourse
import datetime


class Cooperative:
    def __init__(self):
        self._courses = {}
        self._scheduledCourses = {}
        self._members = {}

    def addMember(self, member):
        if member in self._members:
            raise CooperativeException("Duplicate member id"+member.mid)
            pass
        else:
            self._members[member.mid] = member
            return True
        pass

    def addCourse(self, course):
        if self.getCourse(course.courseCode):
            raise CooperativeException("Duplicate member id"+course.courseCode)
            pass
        else:
            self._courses[course.courseCode] = course
            return True
        pass

    def addScheduledCourse(self, scheduledCourse):
        if not self.getCourse(scheduledCourse.course.courseCode):
            raise CooperativeException("No course with code " + str(scheduledCourse.course.courseCode))
        if self.getScheduledCourse(scheduledCourse.course.courseCode, scheduledCourse.schedule_date):
            raise CooperativeException("Duplicate schedule. Course with code {} has  already  been  scheduled  on  {})"
                                       .format(scheduledCourse.course.courseCode, scheduledCourse.schedule_date))
            pass
        else:
            self._scheduledCourses[str(scheduledCourse.course.courseCode)+str(scheduledCourse.schedule_date)] = scheduledCourse
            return True
        pass

    def getMember(self, mid):
        try:
            return self._members[mid]
        except KeyError:
            return None
        pass

    def getCourse(self, code):
        try:
            return self._courses[code]
        except KeyError:
            return None

    def getScheduledCourse(self, code, scheduledDate):
        try:
            return self._scheduledCourses[str(code)+str(scheduledDate)]
        except KeyError:
            return None
        pass

    def getMemberCourseAndScheduledCourse(self, mid, code, sceduleDate):
        if not self.getMember(mid):
            raise CooperativeException("No member with member id {}".format(mid))
            pass
        elif not self.getCourse(code):
            raise CooperativeException("No course with code {}".format(code))
            pass
        elif not self.getScheduledCourse(code, sceduleDate):
            pass
            raise CooperativeException("No schedule for course  with  code  {}  on {} ".format(code, sceduleDate))
        else:
            return self.getMember(mid), self.getCourse(code), self.getScheduledCourse(code, sceduleDate)


    def enroll(self, mid, code, scheduleDate):
        try:
            member, course, scheduleCourse = self.getMemberCourseAndScheduledCourse(mid, code, scheduleDate)
            scheduleCourse.addParticipant(member)
        except CooperativeException:
            pass

    def cancelEnrollment(self, mid, code, scheduleDate):
        try:
            member, course, scheduleCourse = self.getMemberCourseAndScheduledCourse(mid, code, scheduleDate)
            if scheduleCourse.searchParticipant(member):
                scheduleCourse.removeParticipant(member)
                days = scheduleDate-datetime.date.today()
                return course.cancellationPenalty(member.monthlyIncome(), member.age(datetime.date.today()),days)
            else:
                return -1
        except Exception as e:
            print("Error Penalty rate:", e)

    def membersStr(self):
        out_str = ''
        for item in self._members:
            out_str += str(self._members[item]) +'\n'
        return out_str


    def coursesStr(self):
        out_str = ''
        for item in self._courses:
            out_str += str(self._courses[item]) + '\n'
        return out_str

    def scheduledCoursesStr(self):
        out_str = ''
        for item in self._scheduledCourses:
            out_str += str(self._scheduledCourses[item]) + '\n'
        return out_str


class CooperativeException(Exception):
    pass


if __name__ == "__main__":
    cooperative = Cooperative()
    cooperative.addMember(Member("Helen", 111111111, datetime.date(1964, 1, 1), 1000.0))
    cooperative.addMember(Member("Irene", 222222222222, datetime.date(1949, 10, 1)))
    cooperative.addMember(Member("Jackson", 333333333, datetime.date(1959, 3, 1), 2500.0))
    cooperative.addMember(Member("Kendrick", 444444444, datetime.date(1979, 11, 1), 1000.0))
    cooperative.addCourse(NonVocationalCourse("C001", "Gluten-free diet fees", "How to start...", 100.00))
    cooperative.addCourse(VocationalCourse("C002", "Eng in business", "Development...", 10000.00, "Engineering"))
    cooperative.addScheduledCourse(ScheduledCourse(NonVocationalCourse("C001", "Gluten-free diet fees",
                                                                       "How to start...", 100.00),
                                   datetime.date(2019, 10, 12)))
    cooperative.addScheduledCourse(ScheduledCourse(VocationalCourse("C002", "Eng in business", "Development...",
                                                                    10000.00, "Engineering"),
    datetime.date(2019, 10, 12)))
    menu_test = menu.Menu()
    menu_test.menu_start(cooperative)



