# You are given a list of appointments, where each appointment has following properties:
#   int start_time
#   int end_time
#   bool has_conflict = false
#
# list<appointment>
#
#
# # [(3,5),(6,8)]
# # (4,6)
# # if there exists tuple where (x,y) where x<k<y where k is new appt (k,l)
class Appointment:
    def __init__(self, start, end):
        self.start_time = start
        self.end_time = end
        self.has_conflict = False


class Appointments:
    def __init__(self):
        self.appointments = []

    def addAppointment(self, appointments):
        self.appointments = appointments;

    def fixConflicts(self):

        i = 1
        maxEndTime = 0

        while i < len(self.appointments):
            if self.appointments[i].start_time < maxEndTime:
                self.appointments[i].has_conflict = True
            if self.appointments[i].end_time > maxEndTime:
                maxEndTime = self.appointments[i].end_time

            i += 1
