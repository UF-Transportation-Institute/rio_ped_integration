#!/usr/bin/env python

## RIO Integration that listens to String published
## to the 'counts' topic

import rospy
from std_msgs.msg import String

import socket


class RioIntegration:

    def callback(self, msg):
        print(msg)
        try:
            self._bsm_publisher.sendto(msg.data, (self.ip, self.port))
        except Exception:
            # ok to ignore some counts
            pass

    def __init__(self):
        rospy.Subscriber('ped_counter/counts', String, self.callback)
        self.ip = rospy.get_param("rio_integration_node/server_ip")
        self.port = rospy.get_param("rio_integration_node/server_port")

        self._bsm_publisher = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._bsm_publisher.setblocking(0)


if __name__ == '__main__':
    rospy.init_node('rio_integration_node', anonymous=True)

    integration = RioIntegration()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
