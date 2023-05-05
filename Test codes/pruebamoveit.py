#!/usr/bin/env python3.8

import rospy
from geometry_msgs.msg import Pose
from open_manipulator_msgs.srv import SetKinematicsPose, SetKinematicsPoseRequest

def main():
    rospy.init_node('open_manipulator_movement')
    rospy.wait_for_service('/goal_task_space_path')
    set_kinematics_pose = rospy.ServiceProxy('/goal_task_space_path', SetKinematicsPose)

    # Define la posición deseada del efector final
    target_position = Pose()
    target_position.orientation.w=1.0
    target_position.position.x = 0.27
    target_position.position.y = 0.0
    target_position.position.z = 0.205

    # Crear un objeto SetKinematicsPoseRequest y establecer la posición deseada
    request = SetKinematicsPoseRequest()
    request.end_effector_name = 'gripper'
    request.kinematics_pose.pose = target_position

    # Enviar la solicitud de movimiento al robot
    result = set_kinematics_pose(request)


    if result.is_planned:
        rospy.loginfo('Movimiento planificado y ejecutado correctamente')
    else:
        rospy.logerr('No se pudo planificar o ejecutar el movimiento')

if __name__ == '__main__':
    main()