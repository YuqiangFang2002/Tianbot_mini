#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

target_w = 0

def callback(data):
    rospy.loginfo(data.pose.pose.orientation.w)
    pub = rospy.Publisher('tianbot_mini/cmd_vel', Twist, queue_size=10)   #仿真机器人名字
    tianbot_move_cmd = Twist()
    global target_w

    if data.header.frame_id == "tianlaoshi/odom":         #实体机器人名字
        target_w = data.pose.pose.orientation.w
    else:
        if data.pose.pose.orientation.w > target_w-0.1 :
            tianbot_move_cmd.angular.z = 0.8
            pub.publish(tianbot_move_cmd)
        else:
            if data.pose.pose.orientation.w < target_w+0.1 :
                tianbot_move_cmd.angular.z = -0.8
                pub.publish(tianbot_move_cmd)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('jianzhengqiji_huibuhuifanche', anonymous=True)

    rospy.Subscriber("tianbot_mini/odom", Odometry, callback)                          #仿真机器人名字
    rospy.Subscriber("tianlaoshi/odom", Odometry, callback)                           #实体机器人名字

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
