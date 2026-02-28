#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def main():
    rospy.init_node('circle_mover', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    vel = Twist()
    radius = 1.0
    linear_speed = 1.0
    angular_speed = linear_speed / radius
    
    vel.linear.x = linear_speed
    vel.angular.z = angular_speed
    
    rospy.loginfo("Circle mover started: radius=%.1fm", radius)
    
    while not rospy.is_shutdown():
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
