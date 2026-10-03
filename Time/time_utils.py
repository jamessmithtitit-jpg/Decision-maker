from datetime import datetime 

class Time:
    def __init__(self):
        self.hours = 0 
        self.minutes = 0 
        self.seconds = 0 
        self.current_hours = int(datetime.now().strftime("%H")) 
        self.current_minutes = int(datetime.now().strftime("%M")) 
        self.current_seconds = int(datetime.now().strftime("%S")) 
    def get_time_input(self):
        try: 
            self.input_hours = int(input("Hours(24Hr Format is taken here): "))
            self.input_minutes = int(input("Minutes(24Hr Format is taken here): "))
            self.input_seconds = int(input("Seconds(24Hr Format is taken here): "))
        except ValueError:
            print("Write the inputs in integer only ")
    def show_ending_time(self ):
            self.total_hours = self.current_hours + self.input_hours
            self.total_minutes = self.current_minutes + self.input_minutes
            self.total_seconds = self.current_seconds + self.input_seconds
            if self.total_seconds >= 60:
                self.total_minutes = self.total_minutes + self.total_seconds // 60 
                self.total_seconds = self.total_seconds % 60 
            if self.total_minutes >= 60:
                 self.total_hours = self.total_hours + self.total_minutes // 60
                 self.total_minutes = self.total_minutes % 60 
            if self.total_hours >= 24: 
                 self.total_hours = self.total_hours - 24 
            print(f"{self.total_hours}:{self.total_minutes}:{self.total_seconds}")




            
             

        


                            

        
