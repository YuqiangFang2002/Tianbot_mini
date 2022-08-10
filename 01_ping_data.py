import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def main():
 rospy.init_node('tbm_sonar_sensor_node',anonymous=False)
 rospy.Subscriber('tianbot_mini/cmd_rxd', String,cb,queue_size=10)

 while not rospy.is_shutdown():
   pass
 pass

def cb(data):
    pub = rospy.Publisher("tianbot_mini/cmd_vel", Twist, queue_size=10)
    dist=float(data.data)/100.0
    cmd = Twist()
    if dist>0.1 and dist<0.6:
        cmd.linear.x=0.2
    else:
        cmd.linear.x=0
    pub.publish(cmd)
    rospy.loginfo("distance:"+str(dist))

if __name__=='__main__':
    main()
