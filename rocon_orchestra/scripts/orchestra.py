#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_orchestration/rocon_orchestra/LICENSE
#
##############################################################################
# Imports
##############################################################################

import roslib
roslib.load_manifest('rocon_orchestra')
import rospy
import rocon_orchestra

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    rospy.init_node('orchestration')  # , log_level=rospy.DEBUG)
    orchestration = rocon_orchestra.Orchestration()
    rospy.spin()
