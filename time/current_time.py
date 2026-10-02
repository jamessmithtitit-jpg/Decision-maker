from datetime import datetime 

def current_time():
    hours = datetime.now("%H")
    minutes = datetime.now("%M")
    seconds = datetime.now("%S") 

    return  hours , minutes , seconds 



current_time()

