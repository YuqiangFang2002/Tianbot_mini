

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('rospy_sub_msgs_node',anonymous=False)
    rospy.Subscriber('/rosecho/asr',String,cb)
    while not rospy.is_shutdown():
        pass
    pass

def cb(data):
    rospy.loginfo(data.data)

if __name__=='__main__':
    main()
