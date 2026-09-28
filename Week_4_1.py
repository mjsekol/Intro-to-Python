# Functions
import time # This will import the time module, which provides various time-related functions
#! Functions without Parameters
#? NASA Themed Examples
def launch_countdown():
    print("T-minus 10 seconds and counting...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1) # This will pause the program for 1 second to simulate the countdown
    print("Liftoff! The rocket has launched into space.")

launch_countdown() # This will call the launch_countdown function and execute the code within it    

#On Monday NASA Launches Rockete 1
launch_countdown() # This will call the launch_countdown function and execute the code within it

#On Thursday NASA Launches Rocket 2
launch_countdown() # This will call the launch_countdown function and execute the code within it