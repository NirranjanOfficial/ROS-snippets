from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nirranjan',
    maintainer_email='nirranjan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main","robot_news_station = my_py_pkg.robot_news_station:main" 
            ,"Smartphone = my_py_pkg.smartphone:main"#py_nose specifies its an py node,#my_py_pkg is the file name,main specifies the starting place of the execution
        ],
    },
)
