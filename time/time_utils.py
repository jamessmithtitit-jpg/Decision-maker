from datetime import datetime 

class time:
    def __init__(self):
        self.hours = 0 
        self.minutes = 0 
        self.seconds = 0 
        self.current_hours = int(datetime.now().strftime("%H")) 
        self.current_minutes = int(datetime.now().strftime("%M")) 
        self.current_seconds = int(datetime.now().strftime("%S")) 
    def get_time_input(self):
        self.input_hours = int(input("Hours(24Hr Format is taken here): "))
        self.input_minutes = int(input("Minutes(24Hr Format is taken here): "))
        self.input_seconds = int(input("Seconds(24Hr Format is taken here): "))
    def calculate_time(self):
        
        


                            

        
