# -*- coding: utf-8 -*-
from statsd import statsd

from celery.events.snapshot import Polaroid


class Instax(Polaroid):
    clear_after = True

    def handle_task(self, (uuid, task), worker=None):
        name, state = task.name.lower(), task.state.lower()
        statsd.incr("celery.tasks.{0}.{1}".format(name, state), 1)
        if task.runtime:
            statsd.timing("celery.tasks.{0}".format(name),
                task.runtime * 1000)

    def on_shutter(self, state):
        if not state.event_count:
            # No new events since last snapshot.
            return
        statsd.incr("celery.tasks.total", state.task_count)
        statsd.gauge("celery.workers.total", len(state.workers))
        statsd.gauge("celery.workers.alive.count",
            sum(1 for _, worker in state.workers.items() if worker.alive))
        statsd.gauge("celery.workers.dead.count",
            sum(1 for _, worker in state.workers.items() if not worker.alive))
        map(self.handle_task, state.tasks.items())
