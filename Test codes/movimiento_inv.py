#!/usr/bin/env python3.8

import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from std_msgs.msg import Header
import sys

# Función para mover el efector final a la posición deseada
def move_to_position(x=0.2, y=0, z=0.2):
    # Crear un objeto Pose con la posición deseada
    pose = Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z

    # Crear un objeto PoseStamped con la posición y un header vacío
    pose_stamped = PoseStamped()
    pose_stamped.header = Header()
    pose_stamped.pose = pose

    # Crear un objeto moveit_commander y establecer el grupo de control del efector final
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    group = moveit_commander.MoveGroupCommander('arm')

    # Establecer la posición deseada como objetivo del grupo
    group.set_pose_target(pose_stamped)

    # Planificar y ejecutar el movimiento
    plan = group.plan()
    print(plan[1])
    group.execute(plan[1])

    # Cerrar el objeto moveit_commander
    moveit_commander.roscpp_shutdown()


if __name__ == '__main__':
    move_to_position()