class InvalidDateError(Exception):
    pass

class Calendar:
    def __init__(self):
        self.events = {}

    def validate_date(self, date):
        try:
            parts = date.split("-")
            if len(parts) != 3:
                raise InvalidDateError("Date must be in the format YYYY-MM-DD.")
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= month <= 12):
                raise InvalidDateError("Month must be between 1 and 12.")
            if not (1 <= day <= 31):
                raise InvalidDateError("Day must be between 1 and 31.")
        except (ValueError, InvalidDateError) as e:
            raise InvalidDateError(f"Invalid date: {e}")

    def add_event(self, date, event):
        try:
            self.validate_date(date)
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]
            print(f"Event '{event}' added to {date}.")
        except InvalidDateError as e:
            print(e)

    def update_event(self, date, old_event, new_event):
        try:
            self.validate_date(date)
            if date in self.events and old_event in self.events[date]:
                self.events[date].remove(old_event)
                self.events[date].append(new_event)
                print(f"Event '{old_event}' updated to '{new_event}' on {date}.")
            else:
                print(f"Event '{old_event}' not found on {date}.")
        except InvalidDateError as e:
            print(e)

    def delete_event(self, date, event):
        try:
            self.validate_date(date)
            if date in self.events and event in self.events[date]:
                self.events[date].remove(event)
                if not self.events[date]:
                    del self.events[date]
                print(f"Event '{event}' deleted from {date}.")
            else:
                print(f"Event '{event}' not found on {date}.")
        except InvalidDateError as e:
            print(e)

    def display_events_for_day(self, date):
        try:
            self.validate_date(date)
            if date in self.events:
                print(f"Events on {date}: {', '.join(self.events[date])}")
            else:
                print(f"No events found on {date}.")
        except InvalidDateError as e:
            print(e)

    def display_all_events(self):
        if not self.events:
            print("No events in the calendar.")
        else:
            print("Calendar Events:")
            for date, events in self.events.items():
                print(f"{date}: {', '.join(events)}")