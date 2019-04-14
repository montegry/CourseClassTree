from voccourse import VocationalCourse
from nonvoccourse import NonVocationalCourse
from member import Member
import datetime


class ScheduledCourse:

    def __init__(self, course, schedule_date):
        self._course = course
        self._schedule_date = schedule_date
        self._participant_list = []

    @property
    def course(self):
        return self._course

    @property
    def schedule_date(self):
        return self._schedule_date

    @property
    def participant_list(self):
        return self._participant_list

    def searchParticipant(self, member):
        for item in self.participant_list:
            if member == item.mid or member == item:
                return item
            else:
                return None

    def addParticipant(self, member):
        if self.searchParticipant(member):
            return False
        else:
            self._participant_list.append(member)
            return True

    def removeParticipant(self, member):
        if self.searchParticipant(member):
            self.participant_list.remove(member)
            return True
        else:
            return False

    def __str__(self):
        first_block = "Scheduled date: {}\n".format(self.schedule_date)
        second_block = str(self.course)+ '\n'
        third_block = "Participant List: \n"
        for participant in self.participant_list:
            third_block += str(participant) + '\n'
        fourth_block = "Number of participant: {}\n".format(len(self.participant_list))
        return first_block+second_block+third_block+fourth_block


if __name__ == "__main__":
    v_course = VocationalCourse("C001", "Gluten-free diet fees", "How to start...", 10000.00, "Engineering")
    nv_course = NonVocationalCourse("C003", "joy how to fly", "How to start...", 100.00)
    sh_course = ScheduledCourse(v_course, datetime.date(2019, 10, 12))
    sh_course_1 = ScheduledCourse(nv_course, datetime.date(2019, 10, 12))
    sh_course_1.addParticipant(Member("Helen", 1000101, datetime.date(1964, 1, 1), 1200.0))
    sh_course_1.addParticipant(Member("Zeus", 10111929, datetime.date(1959, 1, 1), 2100.0))

    print(str(sh_course))
    print(str(sh_course_1))
