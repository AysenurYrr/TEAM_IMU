#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class IHACam():
    def __init__(self):
        rospy.init_node("kamera")
        rospy.Subscriber("webcam/image_raw",Image,self.kameraCallback)
        self.bridge = CvBridge()
        rospy.spin()

    def kameraCallback(self,mesaj):
        self.foto = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.imshow("Ucak Kamerasi",self.foto)
        cv2.waitKey(1)

nesne = IHACam()
