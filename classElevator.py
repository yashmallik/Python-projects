# The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    def __str__(self):
        return (f"Current floor: {self.current}")
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current<10 and self.current >= -1:
            self.current = self.current+1
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1 and self.current <= 10:
            self.current = self.current-1
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""    
        self.current = floor
        pass


elevator = Elevator(-1, 10, 0)

# This class is pretty empty and doesn't do much.  To test whether your *Elevator* class is working correctly, run the code blocks below.

elevator.up() 
elevator.current #should output 1
1

elevator.down() 
elevator.current #should output 0
0

elevator.go_to(10) 
elevator.current #should output 10
# 10

# If you get a NameError message, be sure to run the Elevator class definition code block first. If you get an AttributeError message, be sure to initialize self.current in your Elevator class.

# Once you've made the above methods output 1, 0 and 10, you've successfully coded the Elevator class and its methods. Great work!

# For the up and down methods, did you take into account the top and bottom floors? Keep in mind that the elevator shouldn't go above the top floor or below the bottom floor. To check that out, try the code below and verify if it's working as expected. If it's not, then go back and modify the methods so that this code behaves correctly.

# Go to the top floor. Try to go up, it should stay. Then go down.

elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
# 9
# 1

# Now add the str method to your Elevator class definition above so that when printing the elevator using the print( ) method, we get the current floor together with a message. For example, in the 5th floor it should say "Current floor: 5"

elevator.go_to(5)
print(elevator)
# Current floor: 5