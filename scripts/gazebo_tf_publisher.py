#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import tf

from gazebo_msgs.msg import ModelStates

class Tf_publisher():
    def __init__(self):
        self.model_name_ = rospy.get_param("~model_name")
        self.base_frame_id_ = rospy.get_param("~base_frame_id")
        self.global_frame_id_ = rospy.get_param("~global_frame_id")
        self.tf_time_delay_ = rospy,get_param("~tf_time_delay")
        self.model_index_ = None
        self.first_sub_ = True

        # topic name
        gazebo_model_topic_name = "/gazebo/model_states"

        # subscriber
        self.gazebo_model_sub = rospy.Subscriber(gazebo_model_topic_name, ModelStates, self.cb_gazebo_model, queue_size=1)

        # tf broadcaster
        self.tf_broadcaster = tf.TransformBroadcaster()

    def cb_gazebo_model(self, _gazebo_model):
        cb_time = rospy.Time.now()
        tf_time = cb_time - rospy.Duration.from_sec(tf_time_delay_)
        if self.first_sub_:
            self.model_index_ = _gazebo_model.name.index(self.model_name_)
            self.first_sub_ = False
        else:
            model_pose_ = _gazebo_model.pose[self.model_index_]
            self.boroadcast_tf(model_pose_, tf_time)

    def boroadcast_tf(self, _model_pose, _time):
        x = _model_pose.position.x
        y = _model_pose.position.y
        z = _model_pose.position.z
        qx = _model_pose.orientation.x
        qy = _model_pose.orientation.y
        qz = _model_pose.orientation.z
        qw = _model_pose.orientation.w
        # rospy.loginfo("{} : ({}, {})".format(self.model_name_, x, y))
        self.tf_broadcaster.sendTransform((x, y, z), (qx, qy, qz, qw), _time, self.base_frame_id_, self.global_frame_id_)
        # rospy.loginfo("{} tf publish".format(self.model_name_))

def main():
    rospy.init_node("gazebo_tf_publisher")

    tf_pub = Tf_publisher()

    rospy.spin()

if __name__ == '__main__':
    main()
