#!/usr/bin/env python2
# -*- coding: utf-8 -*-
PI = 3.1415926535897

import rospy
from time import sleep
#import actionlib
#from ogretici_paket.msg import task_situationAction, task_situationFeedback, task_situationResult
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBot():
    def __init__(self):
        rospy.init_node("motion_controller")
        self.hedef_konum_x = int(input("x degerini giriniz: "))
        self.hedef_konum_y = int(input("y degerini giriniz: "))
        self.guncel_konum_x=0
        self.guncel_konum_y=0
        self.guncel_konum_theta=0
        self.kontrol= True
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.poz_guncelle)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.rate = rospy.Rate(5)
        while self.kontrol:
            self.dondur()
    
    def angle(self):
        radyan= atan2(self.hedef_konum_y - self.guncel_konum_y, self.hedef_konum_x - self.guncel_konum_x)
        self.rate.sleep()
        return radyan-self.guncel_konum_theta

    def dondur(self):
        turn_angle = self.angle()
        angular_velocity=Twist()
        if (round(turn_angle,1) != 0.0):
            angular_velocity.angular.z=0.2
            self.velocity_publisher.publish(angular_velocity)
            turn_angle=self.angle()
        else:
            angular_velocity.angular.z=0.0
            self.velocity_publisher.publish(angular_velocity)
            self.kontrol=False

    def poz_guncelle(self,mesaj):
        self.guncel_konum_x = mesaj.x
        self.guncel_konum_y = mesaj.y
        self.guncel_konum_theta = mesaj.theta

    def mesafe(self):
        mesafe= sqrt(pow((self.hedef_konum_x-self.guncel_konum_x),2)+pow((self.hedef_konum_y-self.guncel_konum_y),2))
        return mesafe

    def hareket(self):
        vel_msg= Twist()
        yerdegistirme=0
        mesafe=self.mesafe()
        print("Hedef konum ve mevcut konum arasindaki mesafe:",mesafe)
        t0 = rospy.Time.now().to_sec()
        while yerdegistirme<mesafe:
            vel_msg.linear.x=0.5
            self.velocity_publisher.publish(vel_msg)
            sleep(0.1)
            t1 = rospy.Time.now().to_sec()
            yerdegistirme = vel_msg.linear.x*(t1-t0)
        vel_msg.linear.x=0.0
        self.velocity_publisher.publish(vel_msg)
        print("Hedefe varildi !")
        print("Turtle icin yeni konum x=",self.guncel_konum_x,         "y=",self.guncel_konum_y)

try:
    x=TurtleBot()
    x.hareket()
except rospy.ROSInterruptException:
    print("Dugum sonlandi!!!")


