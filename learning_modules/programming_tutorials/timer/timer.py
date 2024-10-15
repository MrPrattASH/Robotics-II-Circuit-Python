import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def set_timer(self, start_time: float, stop_time: float):
        """Set the start and stop times for the timer."""
        self.start_time = start_time
        self.stop_time = stop_time

    def check_timer(self) -> bool:
        """Check if the current monotonic time has exceeded the stop time."""
        if self.start_time is None or self.stop_time is None:
            raise ValueError("Timer has not been set.")
        
        current_time = time.monotonic()
        return current_time >= self.stop_time