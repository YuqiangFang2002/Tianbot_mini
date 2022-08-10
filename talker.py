#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import ColorRGBA

def talker():
    pub = rospy.Publisher('tianbot_mini/led', ColorRGBA, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        led_color_cmd = ColorRGBA()
        led_color_cmd.r = 64
        led_color_cmd.g = 0
        led_color_cmd.b = 0
        led_color_cmd.a = 10       
        rospy.loginfo(led_color_cmd)
        pub.publish(led_color_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
