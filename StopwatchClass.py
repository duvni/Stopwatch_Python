from datetime import datetime, timedelta


class Stopwatch:
    """Provides a set of methods and properties that you can use to accurately measure elapsed time."""

    def __init__(self):
        """Initializes a new instance of the Stopwatch class.

        The returned Stopwatch instance is stopped, and the elapsed time property of the instance is zero.
        Use the start method to begin measuring elapsed time with the new Stopwatch instance.
        Use the start_new method to initialize a new Stopwatch instance and immediately start it."""
        self._start = None  # type: datetime
        self._elapsed = timedelta(0)
        self._running = False

    @property
    def elapsed(self) -> timedelta:
        """Gets the total elapsed time measured by the current instance."""
        if not self.is_running:
            return self._elapsed
        cur_timedelta = (datetime.utcnow()-self._start)
        return cur_timedelta + self._elapsed

    @property
    def elapsed_milliseconds(self) -> int:
        """"Gets the total elapsed time measured by the current instance, in milliseconds."""
        return int(self.elapsed.total_seconds() * 1000)

    @property
    def is_running(self) -> bool:
        """Gets a value indicating whether the Stopwatch timer is running."""
        return self._running

    def reset(self):
        """Stops time interval measurement and resets the elapsed time to zero."""
        self._elapsed = timedelta(0)
        self._running = False

    def restart(self):
        """Stops time interval measurement, resets the elapsed time to zero, and starts measuring elapsed time."""
        self.reset()
        self.start()

    def start(self):
        """Starts, or resumes, measuring elapsed time for an interval."""
        if self.is_running:
            return
        self._start = datetime.utcnow()
        self._running = True

    def stop(self):
        """Stops measuring elapsed time for an interval."""
        self._elapsed = self.elapsed
        self._running = False

    @staticmethod
    def start_new() -> 'Stopwatch':
        """Initializes a new Stopwatch instance, sets the elapsed time property to zero,
        and starts measuring elapsed time."""
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch

    def __str__(self):
        return '{} milliseconds have elapsed so far'.format(self.elapsed_milliseconds)

    def __repr__(self):
        elapsed_interval = self.elapsed
        return 'Stopwatch has been running for {} days, {} seconds and {} microseconds'.format(
               elapsed_interval.days, elapsed_interval.seconds, elapsed_interval.microseconds)
