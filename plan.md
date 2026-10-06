# Decision Maker: Project Specification & Roadmap

## 1. Vision & Core Concept
**Decision Maker** is an accountability and focus-oriented task manager CLI. It helps users commit to focused work sessions and introduces deliberate friction mechanics to curb distraction (clock-watching cooldowns, low-probability break rolls, and mandatory reflection on task abortion).

---

## 2. Application State Machine

The application alternates between two primary operating states:

```
+-------------------------------------------------------+
|                    STATE: IDLE                        |
|  (No task running / Planning & Queue Management)      |
+-------------------------------------------------------+
   | 1. Add Task (Name, Description, Start, Duration)
   | 2. Remove Task
   | 3. What to do (Decision Maker / Selection)
   |
   v [Task start time arrives / Task started]
+-------------------------------------------------------+
|                   STATE: ACTIVE                       |
|           (Task currently in progress)                |
+-------------------------------------------------------+
   | 1. Check time remaining (15-min cooldown)
   | 2. Roll dice for break (1% win rate, 30-min cooldown)
   | 3. Abort task (Mandatory reason prompt)
   | 4. Task completes when end time is reached
```

---

## 3. Feature Breakdown

### A. Idle State (Menu 1)
* **Add Task**:
  * Inputs: Task Name, Description, Scheduled Start Time ($H:M:S$), Duration ($H:M:S$).
  * Computes: Projected End Time ($H:M:S$).
* **Remove Task**:
  * Deletes a scheduled or queued task before it begins.
* **What to do**:
  * Decision engine to guide the user on which task to tackle next.

### B. Active State (Menu 2)
* **Check Time Left**:
  * Displays remaining duration in $H:M:S$.
  * **Cooldown**: 15 minutes between checks to prevent compulsive clock-watching.
* **Roll for Break**:
  * Gamified break request: 99% probability of failure, 1% success.
  * **Cooldown**: 30 minutes between attempts.
* **Abort Task**:
  * Ends the task prematurely.
  * Prompts user for a mandatory reason (logged for discipline and post-analysis).
* **Automatic Completion**:
  * Detects when the timer reaches zero and transitions back to Idle.

---

## 4. Mathematical Logic: Time & Midnight Rollover

1. **Total Seconds Conversion**:
   $$\text{total\_seconds} = (\text{hours} \times 3600) + (\text{minutes} \times 60) + \text{seconds}$$

2. **End Time Calculation**:
   $$\text{end\_total\_seconds} = \text{start\_seconds} + \text{duration\_seconds}$$

3. **24-Hour Clock Wrap-Around (Midnight Crossing)**:
   $$\text{normalized\_end\_seconds} = \text{end\_total\_seconds} \pmod{86400}$$

4. **Conversion back to $H:M:S$**:
   * $\text{hours} = \lfloor\text{seconds} / 3600\rfloor$
   * $\text{minutes} = \lfloor(\text{seconds} \pmod{3600}) / 60\rfloor$
   * $\text{remaining\_seconds} = \text{seconds} \pmod{60}$

---

## 5. Architectural Review & Identified Gaps

To bring this plan from concept to a production implementation, the following gaps need resolution:

### Gap 1: Execution Model & Non-Blocking Menu
* **Challenge**: If the app is in the "Active State" menu waiting for user input (`input("> ")`), the terminal blocks.
* **Question**: How does the app check if the task has naturally ended or reached its start time while waiting for user keystrokes?
* **Options**:
  1. Check timestamps dynamically whenever the user presses Enter.
  2. Use a background loop / non-blocking input thread.

### Gap 2: Date Awareness vs. Pure Time
* **Challenge**: Working only with $H:M:S$ creates ambiguity when a task crosses midnight or spans multiple calendar days (e.g., started at 23:30, 2-hour duration ends tomorrow at 01:30).
* **Solution**: Internally store actual timestamps (`datetime`), while presenting $H:M:S$ to the user.

### Gap 3: Data Persistence
* **Challenge**: If the terminal is closed or the computer restarts, active tasks and cooldown states in memory are lost.
* **Solution**: A lightweight JSON store (`tasks.json`) to persist task queue, active session, cooldown timestamps, and abort logs.

### Gap 4: Cooldown State Tracking
* **Challenge**: Need exact tracking for:
  * `last_checked_time`: timestamp of last check
  * `last_dice_roll_time`: timestamp of last roll
* **Validation**:
  * If $\text{current\_time} - \text{last\_checked} < 15 \text{ min}$, reject and display remaining cooldown.

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
