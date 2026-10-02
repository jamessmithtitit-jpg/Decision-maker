from datetime import datetime 

def get_current_time():
    hours = datetime.now("%H")
    minutes = datetime.now("%M")
    seconds = datetime.now("%S") 

    return hours, minutes, seconds 



get_current_time()
