markdown

# 🐢 ROS1 Turtle Simulator Guide
### *Running inside Docker Container*

---

<div align="center">
  
[![ROS](https://img.shields.io/badge/ros-noetic-blue)](https://wiki.ros.org/noetic)
[![Docker](https://img.shields.io/badge/docker-required-blue)](https://www.docker.com/)
[![Turtlesim](https://img.shields.io/badge/turtlesim-simulator-green)]()

</div>

## 📋 Prerequisites

✅ Docker installed on your system  
✅ ROS1 Noetic container running  
✅ Basic terminal knowledge  
✅ X11 server (for GUI display)

---

## 🚀 Quick Start Guide

### **TERMINAL 1 - Start ROS Master**
```bash
# First, allow Docker to show graphics (run on HOST machine)
xhost +

# Enter the container
sudo docker exec -it robot bash

# Source ROS (always do this first!)
source /opt/ros/noetic/setup.bash

# Start the ROS master
roscore

    ⚠️ IMPORTANT: Keep this terminal open - roscore must keep running!

TERMINAL 2 - Start Turtle Simulator
bash

# Enter the container (new terminal)
sudo docker exec -it robot bash

# Source ROS
source /opt/ros/noetic/setup.bash

# Launch the turtle simulator
rosrun turtlesim turtlesim_node

    🐢 A blue window will appear with a turtle in the center

TERMINAL 3 - Control the Turtle
bash

# Enter the container (another new terminal)
sudo docker exec -it robot bash

# Source ROS
source /opt/ros/noetic/setup.bash

# Start keyboard control
rosrun turtlesim turtle_teleop_key

    ⌨️ Use arrow keys to move the turtle around

TERMINAL 4 - Inspection & Monitoring
bash

# Enter the container (4th terminal)
sudo docker exec -it robot bash

# Source ROS
source /opt/ros/noetic/setup.bash

🔍 Inspection Commands
<details> <summary><b>📋 List all running nodes</b> (click to expand)</summary>
bash

rosnode list

Expected output:
text

/rosout
/teleop_turtle
/turtlesim

</details><details> <summary><b>📋 List all active topics</b> (click to expand)</summary>
bash

rostopic list

Expected output:
text

/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

</details><details> <summary><b>🔌 Check who publishes to cmd_vel</b> (click to expand)</summary>
bash

rostopic info /turtle1/cmd_vel

Expected output:
text

Type: geometry_msgs/Twist

Publishers: 
 * /teleop_turtle (http://localhost:34567/)

Subscribers: 
 * /turtlesim (http://localhost:34568/)

</details><details> <summary><b>📊 See turtle position in real-time</b> (click to expand)</summary>
bash

rostopic echo /turtle1/pose

Live data output:
text

x: 5.5
y: 5.5
theta: 0.0
linear_velocity: 2.0
angular_velocity: 0.0
---
x: 6.2
y: 5.5
theta: 0.0
linear_velocity: 2.0
angular_velocity: 0.0
---

    ⏹️ Press Ctrl+C to stop viewing

</details>
📊 Node & Topic Diagram
<div align="center">
text

┌────────────────┐      /turtle1/cmd_vel      ┌────────────────┐
│                │  ────────────────────────►  │                │
│  teleop_turtle │                             │   turtlesim    │
│   (Publisher)  │                             │  (Subscriber)  │
│                │  ◄────────────────────────  │                │
└────────────────┘      /turtle1/pose          └────────────────┘
                         (feedback)

</div>
🎮 Control Reference
Key	Action	Description
↑	Move forward	Increases linear velocity
↓	Move backward	Decreases linear velocity
←	Turn left	Increases angular velocity (counter-clockwise)
→	Turn right	Increases angular velocity (clockwise)
Ctrl+C	Stop node	Terminates the running process
📚 Useful Commands Reference
Command	Description
rosnode list	Show all active nodes
rosnode info /node_name	Show details about a specific node
rostopic list	Show all active topics
rostopic echo /topic_name	Display real-time messages on a topic
rostopic info /topic_name	Show publishers and subscribers of a topic
rqt_graph	Show graphical node diagram
rosservice list	Show available services
⚠️ Important Notes

✅ Always source ROS in every new terminal: source /opt/ros/noetic/setup.bash
✅ roscore must be running before starting any other nodes
✅ Each terminal runs independently - don't close them while the system is running
✅ Use Ctrl+C to gracefully stop any running node
✅ The turtle window shows the simulation visually
🐛 Troubleshooting
Problem	Solution
No turtle window	Make sure roscore is running in Terminal 1 and xhost + was executed
Can't move turtle	Click on the teleop terminal window first, then use arrow keys
"Connection refused"	Verify you sourced ROS in every terminal: source /opt/ros/noetic/setup.bash
Docker display issues	On host machine, run: xhost +local:docker for better security
📝 Quick Start Summary
<details open> <summary><b>Click to expand terminal commands summary</b></summary>
Terminal 1 (keep open)
bash

sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
roscore

Terminal 2 (keep open)
bash

sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosrun turtlesim turtlesim_node

Terminal 3 (keep open)
bash

sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosrun turtlesim turtle_teleop_key

Terminal 4 (for inspection)
bash

sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosnode list
rostopic list

</details><div align="center">
🎉 You're now ready to explore ROS1 with turtlesim! 🎉
