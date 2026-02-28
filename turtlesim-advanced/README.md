 Advanced ROS project with Turtlesim featuring 3 Python nodes: ANBAR writer, Circle mover, and Keyboard controller.


## 🚀 Quick Start

### Step 1: Create Workspace
```bash
# Create the workspace folder
mkdir -p ~/catkin_ws/src
```

### Step 2: Navigate to Workspace
```bash
# Go to the workspace root
cd ~/catkin_ws
```

### Step 3: Build the Workspace
```bash
# Build for the first time
catkin_make
```

### Step 4: Source the Workspace
```bash
# Add to current terminal session
source devel/setup.bash
```

> 💡 **Tip:** Add this line to your `~/.bashrc` to auto-source:
> ```bash
> echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
> ```

---

### Step 5: Create Package with Dependencies
```bash
# Navigate to source folder
cd ~/catkin_ws/src
```

```bash
# Create package with all required dependencies
catkin_create_pkg my_first_pkg std_msgs geometry_msgs roscpp rospy
```

```bash
# Go to your new package
cd my_first_pkg
```

> 📌 **Note:** Don't forget to add turtlesim dependency to `package.xml`
> [🔍 Click to view my package.xml](src/my_first_pkg/package.xml)

---

## 🐍 Python Nodes Setup

### Step 6: Create Scripts Folder
```bash
# Create scripts directory inside your package
mkdir scripts
```

### Step 7: Go to Scripts Folder
```bash
# Navigate to scripts folder
cd scripts
```

### Step 8: Create Python Files
```bash
# Create all three Python files
touch anbar_writer.py circle_mover.py keyboard_control.py
```

### Step 9: Make Files Executable
```bash
# Give execute permission to all Python files
chmod +x *.py
```

### Step 10: View/Copy Code
- 📝 [anbar_writer.py](src/my_first_pkg/scripts/anbar_writer.py) - Copy the code from this link
- ⭕ [circle_mover.py](src/my_first_pkg/scripts/circle_mover.py) - Copy the code from this link
- ⌨️ [keyboard_control.py](src/my_first_pkg/scripts/keyboard_control.py) - Copy the code from this link

---

## 🔧 CMakeLists.txt Configuration

### Step 11: Edit CMakeLists.txt
```bash
# Go back to package root
cd ~/catkin_ws/src/my_first_pkg
```

```bash
# Open CMakeLists.txt with your favorite editor
nano CMakeLists.txt
# or
code CMakeLists.txt
# or
gedit CMakeLists.txt
```

### Step 12: Add This Section to CMakeLists.txt
Find and uncomment/add these lines:

```cmake
## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/anbar_writer.py
  scripts/circle_mover.py
  scripts/keyboard_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

> 📌 **[🔍 View my complete CMakeLists.txt](src/my_first_pkg/CMakeLists.txt)**

---

## 🏗️ Build Everything

### Step 13: Go to Workspace Root
```bash
# Navigate back to workspace
cd ~/catkin_ws
```

### Step 14: Build the Package
```bash
# Build everything
catkin_make
```

### Step 15: Source the Workspace Again
```bash
# Source to update environment
source devel/setup.bash
```

---

## ▶️ How to Run (Choose One)

### Option 1: Run ANBAR Writer
```bash
# First, make sure turtlesim is running
rosrun turtlesim turtlesim_node
```

```bash
# In a new terminal, run the ANBAR writer
rosrun my_first_pkg anbar_writer.py
```
> ✍️ *This will make the turtle draw "ANBAR" text*

### Option 2: Run Circle Mover
```bash
# First, make sure turtlesim is running
rosrun turtlesim turtlesim_node
```

```bash
# In a new terminal, run the circle mover
rosrun my_first_pkg circle_mover.py
```
> ⭕ *The turtle will move in a perfect circle*

### Option 3: Run Keyboard Control
```bash
# First, make sure turtlesim is running
rosrun turtlesim turtlesim_node
```

```bash
# In a new terminal, run keyboard control
rosrun my_first_pkg keyboard_control.py
```
> ⌨️ *Use WASD keys to control the turtle manually*

---

## 🚀 Run Everything with Launch File

```bash
# Run all nodes at once
roslaunch my_first_pkg advanced.launch
```

<details>
<summary><b>📋 View launch file contents</b> (click to expand)</summary>

```xml
<!-- advanced.launch -->
<launch>
    <!-- Start turtlesim node -->
    <node pkg="turtlesim" type="turtlesim_node" name="turtlesim"/>
    
    <!-- Run all three Python nodes -->
    <node pkg="my_first_pkg" type="anbar_writer.py" name="anbar_writer"/>
    <node pkg="my_first_pkg" type="circle_mover.py" name="circle_mover"/>
    <node pkg="my_first_pkg" type="keyboard_control.py" name="keyboard_control"/>
</launch>
```

[🔍 View full launch file](launch/advanced.launch)
</details>

---

## ⌨️ Keyboard Controls

| Key | Action | Node |
|:---:|:------:|:----:|
| **W** | Move forward | `keyboard_control.py` |
| **A** | Turn left | `keyboard_control.py` |
| **S** | Move backward | `keyboard_control.py` |
| **D** | Turn right | `keyboard_control.py` |
| **Ctrl+C** | Stop any node | All nodes |

---

## 📝 Quick Reference - All Commands

### Workspace Setup:
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### Package Creation:
```bash
cd ~/catkin_ws/src
catkin_create_pkg my_first_pkg std_msgs geometry_msgs roscpp rospy
```

### Scripts Setup:
```bash
cd ~/catkin_ws/src/my_first_pkg
mkdir scripts
cd scripts
touch anbar_writer.py circle_mover.py keyboard_control.py
chmod +x *.py
```

### Build:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### Run:
```bash
# Individual nodes
rosrun my_first_pkg anbar_writer.py
rosrun my_first_pkg circle_mover.py
rosrun my_first_pkg keyboard_control.py

# OR all together
roslaunch my_first_pkg advanced.launch
```

---

## 👤 Author

<div align="center">

**GitHub:** [@hassanjizzine0-afk](https://github.com/hassanjizzine0-afk)

---

### ⭐ If you found this project helpful, consider giving it a star!

</div>
```
