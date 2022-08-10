import rospy 
from std_msgs.msg import String

def cb(msg):
    print(msg.data)

rospy.init_node('tbm_asr_decode')
rospy.Subscriber("tianbot_mini/asr",String, cb)
rospy.spin()
