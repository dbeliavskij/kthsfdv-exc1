#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import Float32

rospy.init_node('node_b', anonymous=True)

def callback(msg):
    out = Float32()
    out = msg.data / 0.15
    rospy.loginfo(out)
    pub.publish(out)

sub = rospy.Subscriber('/Beliavskij', UInt16, callback)
pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)

rospy.spin()