
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, SetPen
import math

class ANBARWriter:
    def __init__(self):
        rospy.init_node('anbar_writer', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(100)
        
        # Wait for services
        rospy.wait_for_service('/turtle1/teleport_absolute')
        rospy.wait_for_service('/turtle1/set_pen')
        self.teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        self.set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        
    def pen_up(self):
        self.set_pen(255, 255, 255, 2, 1)
        
    def pen_down(self):
        self.set_pen(0, 0, 0, 2, 0)
        
    def move_to(self, x, y, theta=0):
        self.pen_up()
        self.teleport(x, y, theta)
        rospy.sleep(0.1)
        
    def draw_line(self, distance, speed=2.0):
        self.pen_down()
        vel = Twist()
        vel.linear.x = speed
        
        duration = abs(distance / speed)
        start = rospy.Time.now()
        
        while rospy.Time.now() - start < rospy.Duration(duration):
            self.pub.publish(vel)
            self.rate.sleep()
            
        self.pub.publish(Twist())
        self.pen_up()
        
    def rotate(self, angular_speed, angle):
        vel = Twist()
        vel.angular.z = angular_speed
        
        duration = abs(angle / angular_speed)
        start = rospy.Time.now()
        
        while rospy.Time.now() - start < rospy.Duration(duration):
            self.pub.publish(vel)
            self.rate.sleep()
            
        self.pub.publish(Twist())
        
    def draw_A(self, start_x, start_y, size=1.5):
        # Left leg up
        self.move_to(start_x, start_y, math.pi/3)
        self.draw_line(size)
        
        # Right leg down
        self.move_to(start_x + size*0.5, start_y + size*0.866, -math.pi/3)
        self.draw_line(size)
        
        # Middle bar
        mid_x = start_x + size*0.25
        mid_y = start_y + size*0.433
        self.move_to(mid_x, mid_y, 0)
        self.draw_line(size*0.5)
        
    def draw_N(self, start_x, start_y, size=1.5):
        # Left vertical
        self.move_to(start_x, start_y, math.pi/2)
        self.draw_line(size)
        
        # Diagonal down-right
        self.move_to(start_x, start_y + size, -math.pi/6)
        self.draw_line(size*1.15)
        
        # Right vertical down
        self.move_to(start_x + size*0.5, start_y + size, -math.pi/2)
        self.draw_line(size)
        
    def draw_B(self, start_x, start_y, size=1.5):
        # Left vertical
        self.move_to(start_x, start_y, math.pi/2)
        self.draw_line(size)
        
        # Top curve (simplified as two lines)
        self.move_to(start_x, start_y + size, 0)
        self.draw_line(size*0.4)
        self.move_to(start_x + size*0.4, start_y + size, -math.pi/2)
        self.draw_line(size*0.25)
        
        # Middle bar
        self.move_to(start_x, start_y + size*0.5, 0)
        self.draw_line(size*0.4)
        
        # Bottom curve (simplified)
        self.move_to(start_x, start_y, 0)
        self.draw_line(size*0.4)
        
    def draw_R(self, start_x, start_y, size=1.5):
        # Left vertical
        self.move_to(start_x, start_y, math.pi/2)
        self.draw_line(size)
        
        # Top horizontal
        self.move_to(start_x, start_y + size, 0)
        self.draw_line(size*0.4)
        
        # Right vertical down
        self.move_to(start_x + size*0.4, start_y + size, -math.pi/2)
        self.draw_line(size*0.4)
        
        # Middle horizontal
        self.move_to(start_x + size*0.4, start_y + size*0.6, math.pi)
        self.draw_line(size*0.4)
        
        # Diagonal leg
        self.move_to(start_x + size*0.2, start_y + size*0.6, -math.pi/4)
        self.draw_line(size*0.6)
        
    def write_ANBAR(self):
        rospy.loginfo("Writing ANBAR...")
        
        # Clear and center
        self.teleport(5.5, 5.5, 0)
        rospy.sleep(0.5)
        
        letter_size = 1.2
        spacing = 1.8
        start_y = 4.0
        
        # A (position 0)
        self.draw_A(2.0, start_y, letter_size)
        
        # N (position 1)
        self.draw_N(2.0 + spacing, start_y, letter_size)
        
        # B (position 2)
        self.draw_B(2.0 + spacing*2, start_y, letter_size)
        
        # A (position 3)
        self.draw_A(2.0 + spacing*3, start_y, letter_size)
        
        # R (position 4)
        self.draw_R(2.0 + spacing*4, start_y, letter_size)
        
        rospy.loginfo("ANBAR complete!")
        
        # Hide turtle at end
        self.pen_up()
        self.teleport(11, 5.5, 0)

if __name__ == '__main__':
    try:
        writer = ANBARWriter()
        rospy.sleep(1)
        writer.write_ANBAR()
    except rospy.ROSInterruptException:
        pass
