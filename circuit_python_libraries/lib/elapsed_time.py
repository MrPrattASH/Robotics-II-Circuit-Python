import time

class ElapsedTime:
    def __init__(self):
        """Creates a timer and starts it immediately."""
        self._start_time = time.monotonic()

    def reset(self):
        """Resets the timer to zero."""
        self._start_time = time.monotonic()

    def seconds(self) -> float:
        """Returns the number of seconds since the last reset."""
        return time.monotonic() - self._start_time

    def milliseconds(self) -> float:
        """Returns the number of milliseconds since the last reset."""
        return (time.monotonic() - self._start_time) * 1000

    def start_time(self) -> float:
        """Returns the point in time (monotonic) when the timer was started/reset."""
        return self._start_time