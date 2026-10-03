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