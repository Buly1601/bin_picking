import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped
from open_manipulator_msgs.msg import KinematicsPose
from open_manipulator_msgs.srv import SetKinematicsPose, SetJointPosition
from open_manipulator_libs.robotis_manipulator import RobotisManipulator

rospy.init_node("move_to_xyz_position_node")

robot = RobotisManipulator()

target_pose = PoseStamped()
target_pose.header.frame_id = "world"
target_pose.pose.position.x = 0.5 # Establecer la posición deseada en x
target_pose.pose.position.y = 0.0 # Establecer la posición deseada en y
target_pose.pose.position.z = 0.2 # Establecer la posición deseada en z

joint_positions = robot.get_inverse_kinematics(target_pose)

goal_joint_states_publisher = rospy.Publisher("/goal_joint_states", JointState, queue_size=10)
joint_states = JointState()
joint_states.name = robot.get_joint_name()
joint_states.position = joint_positions
goal_joint_states_publisher.publish(joint_states)

