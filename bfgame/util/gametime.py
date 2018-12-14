class GameTime(object):
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.days = 0

    def pass_turns(self, turns=1):
        minute_updated = False
        hours_updated = False
        days_updated = False

        seconds = turns * 6
        self.seconds += seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
            minute_updated = True

        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
            hours_updated = True

        if self.hours >= 24:
            self.hours -= 24
            self.days += 1
            days_updated = True

        return TimeUpdateResult(minute_updated, hours_updated, days_updated)


class TimeUpdateResult(object):
    __slots__ = ["minute_updated", "hours_updated", "days_updated"]

    def __init__(self, minute_updated=False, hours_updated=False, days_updated=False):
        self.minute_updated = minute_updated
        self.hours_updated = hours_updated
        self.days_updated = days_updated
