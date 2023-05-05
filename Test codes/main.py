#! /usr/bin/env python3

import ik
import rospy
import sys
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
import math
import numpy as np


rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_joint_space_path')
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
goal_joint_space_path_request_object = SetJointPositionRequest()
rospy.wait_for_service('/goal_tool_control')


def prof():

    goal_joint_space_path_request_object.planning_group = 'arm'
    goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    goal_joint_space_path_request_object.joint_position.position = [0,0,0,0.2]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)
    
def dis_object():

    goal_joint_space_path_request_object.planning_group = 'arm'
    goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    goal_joint_space_path_request_object.joint_position.position = [2.6,-1,0.3,0.7]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)

def goto_object():

    #grados obtenidos por ik

    #grados=IKPY.inversa()
    
    goal_joint_space_path_request_object.planning_group = 'arm'
    goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    goal_joint_space_path_request_object.joint_position.position =[0.0, 0.6254807785715765, 0.17918637510279709, -0.1938897081106612, 0.0]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)


def home():
    
    goal_joint_space_path_request_object.planning_group = 'arm'
    goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    goal_joint_space_path_request_object.joint_position.position = [0,-1,0.3,0.7]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)



def open_grip():

    goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
    goal_joint_space_path_request_object = SetJointPositionRequest()

    
    goal_joint_space_path_request_object.planning_group = 'gripper'
    goal_joint_space_path_request_object.joint_position.joint_name = ['gripper']
    goal_joint_space_path_request_object.joint_position.position = [0.01]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0



    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)

def close_grip():

    goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
    goal_joint_space_path_request_object = SetJointPositionRequest()
    goal_joint_space_path_request_object.planning_group = 'gripper'
    goal_joint_space_path_request_object.joint_position.joint_name = ['gripper']
    goal_joint_space_path_request_object.joint_position.position = [0.0]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)


def cero():

    
    goal_joint_space_path_request_object.planning_group = 'arm'
    goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    goal_joint_space_path_request_object.joint_position.position = [0,0,0,0]
    goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
    goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
    goal_joint_space_path_request_object.path_time = 2.0

    rospy.loginfo("Doing Service Call ...")
    result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
    print (result)
    rospy.sleep(2.5)


if __name__ == "__main__":
    cero()
    goto_object()
    

    