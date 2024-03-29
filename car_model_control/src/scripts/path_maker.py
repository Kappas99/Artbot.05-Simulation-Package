#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

path = Path()

def odom_cb(data):
    global path
    path.header = data.header
    pose = PoseStamped()
    pose.header = data.header
    pose.pose = data.pose.pose
    path.poses.append(pose)
    path_pub.publish(path)

rospy.init_node('path_node')

odom_sub = rospy.Subscriber('car_model/mobile_base_controller/odom', Odometry, odom_cb)
path_pub = rospy.Publisher('/path', Path, queue_size=100)

if __name__ == '__main__':
    rospy.spin()
