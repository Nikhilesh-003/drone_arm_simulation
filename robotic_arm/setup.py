from setuptools import setup
import os
from glob import glob


package_name = 'robotic_arm'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share','robotic_arm'),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nikhil',
    maintainer_email='nikhil@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "sim_launch = robotic_arm.sim_launch.launch:generate_launch_description",
            "joint_state_publisher = robotic_arm.joint_state_publisher:main",
            "joint_state_publisher_gui = robotic_arm.joint_state_publisher_gui:main"
        ],
    },
)
