from datetime import datetime

from apscheduler.scheduler import Scheduler
from Loader import Loader


class ScheduledLoad():
    def __init__(self, store):
        self.loader = Loader(store)
        self.sched = Scheduler()
        self.sched.start()

    def load(self):
        print 'Kicking off scheduled load'
        self.sched.add_interval_job(self.loader.load, minutes=5)

