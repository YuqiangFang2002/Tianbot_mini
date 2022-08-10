import rospy
from std_msgs.msg import String
from rosecho.msg import ttsActionGoal

def main():
    rospy.init_node('pub_template_node',anonymous=False)
    pub=rospy.Publisher('/rosecho/tts/goal',ttsActionGoal,queue_size=10)
    while not rospy.is_shutdown():
        tts=ttsActionGoal()
        tts.goal.text="一箭三连"
        pub.publish(tts)
        rospy.sleep(4)
    pass

if __name__=='__main__':
    main()


