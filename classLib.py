class Process:
    def __init__(self, number: int, execution_time: int = 1, time_left: int = 1, status=None,
                 complete: bool = False):
        if status is None:
            status = []
        self.number = number
        self.time_left = time_left
        self.execution_time = execution_time
        self.status = status
        self.complete = complete

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_time_left(self):
        return self.time_left

    def set_time_left(self, time_left):
        self.time_left = time_left

    def get_execution_time(self):
        return self.execution_time

    def set_execution_time(self, execution_time):
        self.execution_time = execution_time

    def get_status(self):
        return self.status

    # Setter for status
    def update_status(self, status):
        self.status.append(status)

    def get_complete(self):
        return self.complete

    def set_complete(self, complete):
        self.complete = complete

    def decrement_time_left(self, time_ran=1):
        self.time_left -= time_ran

    def update_complete(self):
        if self.time_left == 0:
            self.complete = True
        # No else because this is to check if the process have been completed once

def style_status(val):
    style_running = "color: #418fda"
    style_ready = "color: #aadcee"
    style_complete = "color: #4631ac"
    style_waiting = "color: gray"

    if "Running" in val:
        return style_running
    elif "Ready" in val:
        return style_ready
    elif "Ran and Got Completed" in val:
        return style_complete
    elif "Waiting" in val:
        return style_waiting
    else:
        return ""