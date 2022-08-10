#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry 
from geometry_msgs.msg import Twist

# def callback(data):
#  rospy.loginfo(data.pose.pose.orientation.w)
#  pub = rospy.Publisher('tianbot_mini/cmd_vel', Twist, queue_size=10)
#  tianbot_move_cmd = Twist()

# if data.pose.pose.orientation.w>-0.66:
#    tianbot_move_cmd.angular.z=0.8
#    pub.publish(tianbot_move_cmd) 
# else:
#     if data.pose.pose.orientation.w<-0.76:
#        tianbot_move_cmd.angular.z=0.8
#        pub.publish(tianbot_move_cmd)

def callback(data):
 rospy.loginfo(data.pose.pose.orientation.w)
 pub = rospy.Publisher('tianbot_mini/cmd_vel', Twist, queue_size=10)
 tianbot_move_cmd = Twist()
 if data.pose.pose.orientation.w>-0.66:
    tianbot_move_cmd.angular.z=0.8
    pub.publish(tianbot_move_cmd)   
 else:
    if data.pose.pose.orientation.w<-0.76:
       tianbot_move_cmd.angular.z=-0.8
       pub.publish(tianbot_move_cmd)   #自定义的
 
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("tianbot_mini/odom", Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
