
import random # Importing random
from flask import Flask , render_template , request
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
    if sum(percentage) != 100:
        raise ValueError("The sum of the percentage should be 100")
    answer = random.choices(population=tasks , weights=percentage , k=100)
    print(answer[random.randint(0, 99)])

if initial_input == "1":
    preset()
elif initial_input == "2":
    custom()
else:
    raise ValueError("Only the appropriate choices are selected here")