def add_time(start_hours, start_minutes, start_seconds, added_hours, added_minutes, added_seconds):
    total_hours = start_hours + added_hours
    total_minutes = start_minutes + added_minutes
    total_seconds = start_seconds + added_seconds
    return total_hours, total_minutes, total_seconds

def subtract_time(start_hours, start_minutes, start_seconds, end_hours, end_minutes, end_seconds):
    