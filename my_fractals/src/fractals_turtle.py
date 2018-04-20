#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
# import the library
import threading, time

#from appjar import gui


class fractas_turtles():
  #PI = 0 #3.1415926535897

  def __init__(self):
       #Creating our node,publisher and subscriber
       rospy.init_node('fractals_turtle', anonymous=True)
       self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
       self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
       self.pose = Pose()
       self.rate = rospy.Rate(10)
       self.PI = 3.1415926535897

   #Callback function implementing the pose value received
  def callback(self, data):
       self.pose = data
       self.pose.x = round(self.pose.x, 4)
       self.pose.y = round(self.pose.y, 4)
 
  def move(self, notForward, dist):
        #velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
       vel_msg = Twist()
       
       #print("Let's move your robot")
       speed = 3 #1 #input("Input your speed:")
       distance = dist #input("Type your distance:")
       #isForward = 1 #input("Foward?: ")#True or False
       
       #Checking if the movement is forward or backwards
       if(notForward == 0):
           vel_msg.linear.x = abs(speed)
       else:
           vel_msg.linear.x = -abs(speed)
       #Since we are moving just in x-axis
       vel_msg.linear.y = 0
       vel_msg.linear.z = 0
       vel_msg.angular.x = 0
       vel_msg.angular.y = 0
       vel_msg.angular.z = 0
       
           #Setting the current time for distance calculus
       t0 = rospy.Time.now().to_sec()
       current_distance = 0

       #Loop to move the turtle in an specified distance
       while(current_distance < distance):
           #Publish the velocity
           self.velocity_publisher.publish(vel_msg)
           #Takes actual time to velocity calculus
           t1=rospy.Time.now().to_sec()
           #Calculates distancePoseStamped
           current_distance= speed*(t1-t0)
       #After the loop, stops the robot
       vel_msg.linear.x = 0
       #Force the robot to stop
       self.velocity_publisher.publish(vel_msg)

  def rotate(self, notClockwise, ang):
        #velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
       vel_msg = Twist()
   
       # Receiveing the user's input
       #print("Let's rotate your robot")
       speed = 100 #30 #input("Input your speed (degrees/sec):")
       angle = ang #75 
       clockwise = 0 #input("Clockwise?: ") #True or false
   
       #Converting from angles to radians
       angular_speed = speed*2*self.PI/360
       relative_angle = angle*2*self.PI/360
   
       #We wont use linear components
       vel_msg.linear.x=0
       vel_msg.linear.y=0
       vel_msg.linear.z=0
       vel_msg.angular.x = 0
       vel_msg.angular.y = 0
   
       # Checking if our movement is CW or CCW
       if notClockwise == 0:
           vel_msg.angular.z = -abs(angular_speed)
       else:
           vel_msg.angular.z = abs(angular_speed)
       # Setting the current time for distance calculus
       t0 = rospy.Time.now().to_sec()
       current_angle = 0
   
       while(current_angle < relative_angle):
           self.velocity_publisher.publish(vel_msg)
           t1 = rospy.Time.now().to_sec()
           current_angle = angular_speed*(t1-t0)
   
   
       #Forcing our robot to stop
       vel_msg.angular.z = 0
       self.velocity_publisher.publish(vel_msg)
       #rospy.spin()


if __name__ == '__main__':
   try:
       obj = fractas_turtles()
       obj.rotate(0, 75)
       obj.move(1, 4)
       obj.rotate(0, 75)
       obj.rotate(0, 75)
       obj.move(1, 4)
       obj.rotate(0, 75)
       obj.rotate(0, 75)
       obj.move(1, 4)
       obj.rotate(0, 75)
       obj.rotate(0, 75)
       obj.move(1, 3)
       obj.rotate(0, 120)
       #obj.rotate(0)
       obj.move(1, 3)



       #try: x = turtlebot()
    	#gui_run()

    	
   except rospy.ROSInterruptException: pass

