from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'pyserial',
    ],
    zip_safe=True,
    maintainer='Bohdan Susulovskyi',
    maintainer_email='bsusulovskiy@gmail.com',
    description='ROS2 UART distance sensor publisher and I2C LCD subscriber',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lcd_publisher = py_pubsub.lcd_publisher:main',
            'lcd_subscriber = py_pubsub.lcd_subscriber:main',
        ],
    },
)
