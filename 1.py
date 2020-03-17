class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.calendar = Calendar()

    def setAvailableTime(self, slot):
        return self.calendar.setAvailableTime(slot)


class Calendar(object):
    def __init__(self):
        self.entries = {}

    def setAvailableTIme(self, slot):
        return slot not in self.entries

    def add_entry(self, slot, record):
        if not self.setAvailableTime(slot):
            raise DoubleslotException
        self.entries[slot] = record

    def __str__(self):
        return str(self.entries)


class DoubleslotException(Exception):
    pass


class learner(Person):
    def __init__(self, first_name, last_name, ssn):
        super(learner, self).__init__(first_name, last_name)
        self.ssn = ssn
        self.learner_id = self.first_name[:1] + self.last_name + ssn


class mentor(Person):
    def __init__(self, first_name, last_name, expertise):
        super(mentor, self).__init__(first_name, last_name)
        self.expertise = expertise

    def addStacks(self):
        record = super(mentor, self).addStacks()
        record['expertise'] = self.expertise
        return record


def getmentor(mentor, learner, slot):

    def make_appointment(self, slot, record):
        self.calendar.add_entry(slot, record)

    if not mentor.setAvailableTime(slot):
        print('Cannot slot, mentor is not available:', mentor)
        return

    mentor.make_appointment(slot, learner.addStacks())
