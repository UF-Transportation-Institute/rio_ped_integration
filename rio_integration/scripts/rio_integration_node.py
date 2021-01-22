#!/usr/bin/env python

## RIO Integration that listens to String published
## to the 'counts' topic
import rospy
from std_msgs.msg import String


class RioIntegration:

    def callback(self, data):
      print(data)


    def __init__(self):
        rospy.Subscriber('ped_counter/counts', String, self.callback)


if __name__ == '__main__':
    rospy.init_node('rio_integration_node', anonymous=True)

    integration = RioIntegration()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
