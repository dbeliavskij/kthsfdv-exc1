#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16


def node_a():
    pub = rospy.Publisher('/Beliavskij', UInt16, queue_size = 10)
    rospy.init_node('node_a', anonymous = True)
    rate = rospy.Rate(20)
    k = 1
    while not rospy.is_shutdown():
        rospy.loginfo(k)
        pub.publish(k)
        k += 4
        rate.sleep()

if __name__ == '__main__':
    try:
        node_a()
    except rospy.ROSInterruptException:
        pass
