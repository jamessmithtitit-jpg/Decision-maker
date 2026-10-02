from datetime import datetime , time

def current_time():
    current_time = datetime.now()

    return current_time.hour() 



print(current_time())

