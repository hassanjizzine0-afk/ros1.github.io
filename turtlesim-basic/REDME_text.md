


### **TERMINAL 1** - Start ROS Master

```bash
# First, allow Docker to show graphics (run on HOST machine)
xhost +

# Enter the container
sudo docker exec -it robot bash

# Source ROS (always do this first!)
source /opt/ros/noetic/setup.bash

# Start the ROS master
roscore

    ⚠️ Keep this terminal open - roscore must keep running!

TERMINAL 2 - Start Turtle Simulator
bash
Copy

# Enter the container (new terminal)
sudo docker exec -it robot bash

# Source ROS
source /opt/ros/noetic/setup.bash

# Launch the turtle simulator
rosrun turtlesim turtlesim_node

    🐢 A blue window will appear with a turtle in the center

TERMINAL 3 - Control the Turtle
bash
Copy

# Enter the container (another new terminal)
sudo docker exec -it robot bash

# Source ROS
source /opt/ros/noetic/setup.bash

# Start keyboard control
rosrun turtlesim turtle_teleop_key

    ⌨️ Use arrow keys to move the turtle around

🔍 Inspection Commands (Terminal 4)
Open a 4th terminal and try these commands:
📋 List all running nodes
bash
Copy

rosnode list

Expected output:
plain
Copy

/rosout
/teleop_turtle
/turtlesim

📋 List all active topics
bash
Copy

rostopic list

Expected output:
plain
Copy

/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

🔌 Check who publishes to cmd_vel
bash
Copy

rostopic info /turtle1/cmd_vel

Expected output:
plain
Copy

Type: geometry_msgs/Twist

Publishers: 
 * /teleop_turtle (http://localhost:34567/)

Subscribers: 
 * /turtlesim (http://localhost:34568/)

📊 See turtle position in real-time
bash
Copy

rostopic echo /turtle1/pose

This shows live data:
plain
Copy

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

    Press Ctrl+C to stop viewing

📊 Node & Topic Diagram
plain
Copy

┌────────────────┐      /turtle1/cmd_vel      ┌────────────────┐
│                │  ────────────────────────►  │                │
│  teleop_turtle │                             │   turtlesim    │
│   (Publisher)  │                             │  (Subscriber)  │
│                │  ◄────────────────────────  │                │
└────────────────┘      /turtle1/pose          └────────────────┘
                         (feedback)

🎮 How to Control
Table
Copy
Key	Action
↑	Move forward
↓	Move backward
←	Turn left
→	Turn right
Ctrl+C	Stop the node
📚 Useful Commands Reference
Table
Copy
Command	Description
rosnode list	Show all active nodes
rosnode info /node_name	Show details about a node
rostopic list	Show all active topics
rostopic echo /topic_name	Display messages on a topic
rostopic info /topic_name	Show publishers/subscribers
rqt_graph	Show graphical node diagram
rosservice list	Show available services
⚠️ Important Notes

    ✅ Always source ROS in every new terminal: source /opt/ros/noetic/setup.bash
    ✅ roscore must be running before starting any other nodes
    ✅ Each terminal runs independently - don't close them
    ✅ Use Ctrl+C to stop any running node
    ✅ The turtle window shows the simulation visually

🐛 Troubleshooting
Q: The turtle window doesn't appear?

    A: Make sure roscore is running in Terminal 1

Q: Can't move the turtle with arrow keys?

    A: Click on the teleop terminal window first, then use arrows

Q: Getting "connection refused" errors?

    A: Make sure you sourced ROS in every terminal

📝 Quick Start Summary
bash
Copy

# Terminal 1 (keep open)
sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
roscore

# Terminal 2 (keep open)
sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosrun turtlesim turtlesim_node

# Terminal 3 (keep open)
sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosrun turtlesim turtle_teleop_key

# Terminal 4 (for inspection)
sudo docker exec -it robot bash
source /opt/ros/noetic/setup.bash
rosnode list
rostopic list
