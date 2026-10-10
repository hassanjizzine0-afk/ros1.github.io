# RPLIDAR A1 on Raspberry Pi — Publishing `/scan`, Running Hector SLAM, and Visualizing in RViz

This guide covers how to connect an **RPLIDAR A1** to a **Raspberry Pi** running ROS 1 Noetic, publish `/scan` to a remote `roscore` on a laptop, run **Hector SLAM** for mapping, and visualize everything in **RViz**.

> For general ROS 1 networking concepts, see the companion guide.

---

## 🔌 Hardware

| Component | Notes |
|---|---|
| Raspberry Pi (3/4/5) | Running Ubuntu 20.04 + ROS Noetic |
| Laptop | Running ROS Noetic (native or Docker) — where `roscore` runs |
| RPLIDAR A1 | Connected to the Pi via USB |
| USB cable | Data + power |

---

## 🔋 Important: Power the Lidar from the Pi

The RPLIDAR A1 requires **stable 5V at ~1.5A**. USB ports on laptops often cannot supply this, causing the lidar to **spin for 1–2 seconds and then stop**.

**Always connect the lidar to the Raspberry Pi**, not directly to the laptop.

---

## 📦 Step 1: Install the RPLIDAR Driver (on the Pi)

### Option A — from apt (recommended)

```bash
sudo apt update
sudo apt install -y ros-noetic-rplidar-ros
```

### Option B — from source

```bash
cd ~/catkin_ws/src
git clone https://github.com/Slamtec/rplidar_ros.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

---

## 📦 Step 2: Install Hector SLAM (on the laptop)

On the **laptop** (where `roscore` runs):

```bash
sudo apt update
sudo apt install -y ros-noetic-hector-slam
```

---

## 🔐 Step 3: Grant Permissions to the USB Port (on the Pi)

```bash
ls /dev/ttyUSB*
```

Usually `/dev/ttyUSB0`. Grant access:

```bash
sudo chmod 666 /dev/ttyUSB0
```

To make it permanent:

```bash
sudo usermod -a -G dialout $USER
```

Then log out and back in.

---

## 🌐 Step 4: Set the ROS Environment

### 4.1. On the Laptop (where `roscore` runs)

Edit `~/.bashrc`:

```bash
nano ~/.bashrc
```

Add at the end:

```bash
export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=10.42.0.1
```

Apply:

```bash
source ~/.bashrc
```

**Verify:**

```bash
echo $ROS_MASTER_URI
echo $ROS_IP
```

Should print:

```
http://10.42.0.1:11311
10.42.0.1
```

Start `roscore`:

```bash
roscore
```

### 4.2. On the Raspberry Pi

Edit `~/.bashrc`:

```bash
nano ~/.bashrc
```

Add at the end:

```bash
export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=10.42.0.137
```

Apply:

```bash
source ~/.bashrc
```

**Verify:**

```bash
echo $ROS_MASTER_URI
echo $ROS_IP
```

Should print:

```
http://10.42.0.1:11311
10.42.0.137
```

---

## 🚀 Step 5: Run the Lidar Driver on the Pi

Make sure `roscore` is already running on the laptop. Then on the Pi:

```bash
roslaunch rplidar_ros rplidar_a1.launch \
    _serial_port:=/dev/ttyUSB0 \
    _serial_baudrate:=115200 \
    _frame_id:=laser \
    _inverted:=false \
    _angle_compensate:=true
```

You should see:

```
[ INFO] [rplidarNode]: RPLIDAR running on serial port /dev/ttyUSB0
[ INFO] [rplidarNode]: RPLIDAR health status : 0
```

---

## 🔗 Step 6: Publish a Static Transform (`map` → `laser`)

Hector SLAM and RViz need to know where the lidar is relative to a global frame. Without this, you will get:

```
No TF data
tf2 frame_ids cannot be empty
```

### Option A — Run it manually on the laptop

```bash
rosrun tf static_transform_publisher 0 0 0 0 0 0 map laser 100
```

**Explanation:**

| Argument | Meaning |
|---|---|
| `0 0 0` | X, Y, Z offset |
| `0 0 0` | Roll, Pitch, Yaw |
| `map` | Parent frame |
| `laser` | Child frame |
| `100` | Publish period (100 ms = 10 Hz) |

Keep this terminal open.

### Option B — Add it to a launch file

Create `slam.launch`:

```xml
<launch>
    <!-- Static transform: map -> laser -->
    <node pkg="tf" type="static_transform_publisher" name="map_to_laser"
          args="0 0 0 0 0 0 map laser 100"/>

    <!-- Hector SLAM -->
    <node pkg="hector_mapping" type="hector_mapping" name="hector_mapping" output="screen">
        <param name="map_frame" value="map"/>
        <param name="base_frame" value="laser"/>
        <param name="odom_frame" value="laser"/>
        <param name="scan_topic" value="/scan"/>
        <param name="map_resolution" value="0.05"/>
        <param name="map_size" value="2048"/>
        <param name="map_update_distance_thresh" value="0.05"/>
        <param name="map_update_angle_thresh" value="0.05"/>
        <param name="laser_max_dist" value="5.0"/>
    </node>
</launch>
```

---

## 🗺️ Step 7: Run Hector SLAM (on the laptop)

If not using a launch file, run it manually on the **laptop**:

```bash
rosrun hector_mapping hector_mapping \
    _map_frame:=map \
    _base_frame:=laser \
    _odom_frame:=laser \
    _scan_topic:=/scan \
    _map_resolution:=0.05 \
    _map_size:=2048 \
    _map_update_distance_thresh:=0.05 \
    _map_update_angle_thresh:=0.05 \
    _laser_max_dist:=5.0
```

Keep this terminal open.

---

## ✅ Step 8: Verify Topics

On the **laptop**:

```bash
rostopic list
```

You should see:

```
/scan
/map
/tf
/tf_static
```

Check the scan:

```bash
rostopic hz /scan
```

Should be around **5–10 Hz** for RPLIDAR A1.

Check the map:

```bash
rostopic echo /map
```

---

## 🖼️ Step 9: Visualize in RViz (on the laptop)

On the laptop:

```bash
rviz
```

In RViz:

1. **Global Options** → **Fixed Frame** → type **`map`** manually.
   - ⚠️ Do **not** leave it empty — this causes the `frame_ids cannot be empty` warning.
2. **Add** → **By Topic** → **LaserScan** → **`/scan`**.
3. **Add** → **By Topic** → **Map** → **`/map`**.
4. The lidar points and the map should appear.

---

## ⚠️ Common Issues

| Problem | Solution |
|---|---|
| Lidar spins 1–2 seconds and stops | Not enough power — connect it to the Pi |
| `/dev/ttyUSB0` permission denied | `sudo chmod 666 /dev/ttyUSB0` |
| `No TF data` in RViz | Run `static_transform_publisher` (Step 6) |
| `tf2 frame_ids cannot be empty` | Set **Fixed Frame** in RViz to `map` |
| `/scan` not visible on laptop | Check `ROS_MASTER_URI` and `ROS_IP` on both devices |
| `package not found` | `sudo apt install ros-noetic-rplidar-ros` or `ros-noetic-hector-slam` |

---

## 📌 Useful Commands

```bash
# Check lidar port
ls /dev/ttyUSB*

# Run lidar driver on Pi
roslaunch rplidar_ros rplidar_a1.launch

# Publish static transform on laptop
rosrun tf static_transform_publisher 0 0 0 0 0 0 map laser 100

# Run Hector SLAM on laptop
rosrun hector_mapping hector_mapping \
    _map_frame:=map _base_frame:=laser _odom_frame:=laser \
    _scan_topic:=/scan _map_resolution:=0.05 _map_size:=2048 \
    _map_update_distance_thresh:=0.05 _map_update_angle_thresh:=0.05 \
    _laser_max_dist:=5.0

# List topics
rostopic list

# Check scan frequency
rostopic hz /scan

# Check static transforms
rostopic echo /tf_static
```

---
