from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ourpkg'


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'lauch'),glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='agonb',
    maintainer_email='alan.gonzales@ucb.edu.bo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_node = ourpkg.my_node:main',
            'sensors_pub = ourpkg.two_sensors:main',
            'sensors_monitor = ourpkg.sensor_monitor:main',
            'robot_state = ourpkg.robot_state_monitor:main',
        ],
    },
)
