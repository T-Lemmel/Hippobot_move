from simple_launch import SimpleLauncher
import os

sl = SimpleLauncher(use_sim_time=True)
sl.declare_arg('rviz', True)
base_path = os.path.abspath(os.path.dirname(__file__))

def launch_setup():

    sl.node('move', 'waypoint_publisher')
    sl.node('move', 'place_frame.py')
    sl.node('move', 'tracker.py')

    if sl.arg('rviz'):
        sl.rviz(base_path + '/config.rviz')

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
