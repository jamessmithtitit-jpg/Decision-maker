"""The Menu will be if currently no task is going on:  
1. Add Task 
2. Remove Task 
3. What to do 


The menu if currently a task is going on(will activate automatically when that time comes):
1. Check how much time left(15 minutes cooldown)
2. Roll the dice to take a break(99% probability to fail , 30 minutes cooldown)
3. Abort Task. (Reason will be asked ) 


Now working on time module so if I kinda wanna calculate time I will be needing to know that what time is there and what time will be the task end 
If I put a task with 2 hours 3 minutes and 3 seconds then the task will end after 2 * 3600 + 3 * 60 + 3 seconds 

so if I press add task and then there should appear name and description of task as inputs and then the time it should start and then how much time should it be there like if it should start at 
6 hr 15 min 0 sec and happen for 2 hours 3 minutes and 3 seconds then it should be calculated with 6 * 3600 + 15 * 60 + 0 + 2 * 3600 + 3 * 60 + 3 this sum should be divided by 3600(questent will be taken as hours) and the reminder should be divided 60(Questent will be taken as minutes ) and the remaining reminder is seconds and should be shown as H : M : S up This is the ending time  
So now I gotta make multiple functions for calculating time like :
1. At what time will the task end at 
2. How much time left for the task deadline to end 

First calculate the all the seconds if they exceed 60 then they will be divided by 60 and the quotent will be added to minutes and the reminder will be seconds and if the minutes exceed 60 then again minutes will be divided by 60 and then the quotent will be taken added to hours and the reminder will be minutes and then if the hours will be 24 or exceed 24 then they will be minu by 24 
"""

import random # Importing random
# Lets make one normal  version first 

# So in this version I will only have like add task which will ask for the tasks again and again like with probability 
# So now I would need one more thing that is a screen asking for preset or custom inputs 
initial_input = input("""
                        Do you want to use:
                        1.Preset 
                        2.Custom
                        Enter the value here for the input: """)




def preset():
    selection : str = input("""Which preset you want to use ? 
                      1.JEE / Coding Preset(90/10) when JEE is not completed
                      2.JEE/Coding Preset(10/90) when JEE is completed for the day 
                      3.JEE/Break(50/50)When JEE Session is completed chance to draw a break when the session is completed and if break does not come out then study JEE for just more 15 minutes No biggie man
                      4.JEE/Break(99/1)When JEE is not completed should only use in between cooldown of 30 minutes 
                      5.Coding/Break(30/70)When Coding session(set hours) is completed and project is not and when project is completed then enjoy 
                      6.Coding/break(99/1)when coding seession is not completed 
                      """)  
    if selection == "1":
        answer = random.choices(population=['JEE Task' , 'Coding Task'] , weights=[90,10] , k=100)
        print(answer[random.randint(0,99)])
    if selection == "2":
            answer = random.choices(population=['JEE Task' , 'Coding Task'] , weights=[10,90] , k=100)
            print(answer[random.randint(0,99)])
    if selection == "3":
            answer = random.choices(population=['JEE Task' , 'Break'] , weights=[50,50] , k=100)
            print(answer[random.randint(0,99)])
    if selection == "4":
            answer = random.choices(population=['JEE Task' , 'Break'] , weights=[99 , 1] , k=100)
            print(answer[random.randint(0,99)])
    if selection == "5":
            answer = random.choices(population=['Coding' , 'Break'] , weights=[30,70] , k=100)
            print(answer[random.randint(0,99)])
            
    if selection == "6":
            answer = random.choices(population=['Coding' , 'Break'] , weights=[99,1] , k=100)
            print(answer[random.randint(0,99)])
        
        
        
def custom(): 
    tasks : list[str  ] = [] # Making list because it is defaultly taken in random.choices 

    percentage : list[int] = [] # Same as above
    while True: # Want multiple inputs 
        try: # Chances of ValueError are there 
            task = input("task: ")# Taking the input input for adding task in list
            probability = int(input("percentage(All the percentage should equal to 100): "))# Taking percentage upto 100 because k is equal to 100 which is like the total of all the weights 
            tasks.append(task)
            percentage.append(probability)
            task = input("task: ")# Repeat of previous code because atleast two inputs are needed 
            probability = int(input("percentage(All the percentage should equal to 100): "))
            tasks.append(task)
            percentage.append(probability)
            
            feedback = input("Do you want to add more inputs: ")# asking whether want more inputs or thats all  
            if feedback == 'n':# If n given then the loop breaks and can go to calculating the answer 
                print("Be ready to put the input")
                break 
            else:
                print("Give more input")
            if not task or not probability:
                print(tasks)
                break
        except ValueError:
            print(tasks)
            break 

        answer = random.choices(population=tasks , weights=percentage , k=100)
        print(answer[random.randint(0, 99)])

if initial_input == "1":
    preset()
elif initial_input == "2":
    custom()
else:
    raise ValueError("Only the appropriate choices are selected here")