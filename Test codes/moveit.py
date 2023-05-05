#!/usr/bin/env python3.8

import moveit_commander 
import sys
import rospy
import geometry_msgs.msg


# Inicializar MoveIt!
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_example', anonymous=True)

# Crear objeto de la clase MoveGroupCommander para el grupo de articulaciones del robot
group_name = "arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

# Obtener información del estado actual del robot
current_state = move_group.get_current_state()

# Obtener la cinemática inversa para un objetivo específico
target_pose = geometry_msgs.msg.PoseStamped()
target_pose.header.frame_id = "base_link"
target_pose.pose.position.x = 0.5
target_pose.pose.position.y = 0.0
target_pose.pose.position.z = 0.5
target_pose.pose.orientation.w = 1.0
ik_solution = move_group.get_ik(target_pose)

# Establecer la posición y orientación deseada del efector final del robot utilizando la cinemática inversa
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = ik_solution[0]
joint_goal[1] = ik_solution[1]
joint_goal[2] = ik_solution[2]
joint_goal[3] = ik_solution[3]
joint_goal[4] = ik_solution[4]
joint_goal[5] = ik_solution[5]

# Planificar la trayectoria para alcanzar el objetivo utilizando la cinemática inversa
move_group.set_joint_value_target(joint_goal)
plan = move_group.plan()

# Ejecutar la trayectoria planificada
move_group.execute(plan, wait=True)

# Limpiar todo antes de salir
moveit_commander.roscpp_shutdown()