import schedule
import time
from datetime import datetime

def minute_task():
    # Implement your task here
    print("Task executed at:", datetime.now())

# Schedule the task to run every one minute
schedule.every(2).minutes.do(minute_task)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)


'''import schedule
import time
from datetime import datetime

def saturday_morning_task():
    # Implement your task here
    print("Task executed at:", datetime.now())

# Schedule the task to run every Saturday at 6 AM
schedule.every().saturday.at("06:00").do(saturday_morning_task)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)

'''