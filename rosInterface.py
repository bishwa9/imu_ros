import rospy
import std_msgs.msg
from sensor_msgs.msg import Imu

class rosInterface:
    def __init__(self, imu_name):
        self.imuPub = rospy.Publisher(imu_name, Imu, queue_size=100)
        rospy.Timer(rospy.Duration(0.2), self.timer_cb)
        self.imu_data = list()
        self.R_a = list()
        self.R_g = list()

    def new_data(self, R_a_, R_g_, imu_data_):
        self.imu_data = imu_data_
        self.R_a = R_a_
        self.R_g = R_g_

    def timer_cb(self, event):
        self.publish_imu()
        return

    def publish_imu(self):
        imuMsg = Imu()
        imuMsg.angular_velocity_covariance = self.R_g
        imuMsg.linear_acceleration_covariance = self.R_a
        imuMsg.orientation_covariance = [1000000] * 9

        imuMsg.linear_acceleration.x = self.imu_data[0]
        imuMsg.linear_acceleration.y = self.imu_data[1]
        imuMsg.linear_acceleration.z = self.imu_data[2]

        imuMsg.angular_velocity.x = self.imu_data[3]
        imuMsg.angular_velocity.x = self.imu_data[4]
        imuMsg.angular_velocity.x = self.imu_data[5]

        imuMsg.orientation.x = 0.0
        imuMsg.orientation.y = 0.0
        imuMsg.orientation.z = 0.0
        imuMsg.orientation.w = 0.0

        self.imuPub.publish(imuMsg)
        print "Data Published"
        #for i in range(0,9):
        #    imuMsg.angular_velocity_covariance[i] = self
        return