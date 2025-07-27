# ROS-snippets
It contains basic Python code for ROS functions using both OOPs and no OOPS.
In order to make it run properly, install ROS2 Humble, source your bash then run!

To access this codes in local git clone this repo by,
```bash
git clone https://github.com/NirranjanOfficial/ROS-snippets.git
cd ROS-snippets
```

Method to install ROS2 Humble is mentioned below!

## Step 1: Set Locale

Make sure you have a UTF-8 locale configured:

```bash
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

## Step 2: Add ROS 2 GPG Key

```bash
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

## Step 3: Add the ROS 2 Repository

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## Step 4: Install ROS 2 Humble Desktop

```bash
sudo apt update
sudo apt install ros-humble-desktop
```

## Step 5: Source the ROS 2 Environment

```bash
source /opt/ros/humble/setup.bash
```
