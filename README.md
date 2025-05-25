# 🦾 Cyberknife-Inspired KUKA Robot Control in ROS1 & Gazebo

## 🚀 Project Overview

This project simulates a **KUKA LBR iiwa R800** robot in ROS1 and Gazebo, executing surgical-like, quasi-circular end-effector motions inspired by the Cyberknife system. It features:

- **Forward & Inverse Kinematics** (Python, DH-based, Jacobian)
- **Trajectory Planning** (parametric, surgical arcs)
- **Real-Time Joint Control** (ROS publisher/subscriber)
- **Dynamic Torque Calculation** (gravity & force compensation)
- **Gazebo Simulation** (with hardware validation on Turtlebot3)
- **PID Controller Tuning** (for smooth, stable motion)

---

# 🛠️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/roboticistjoseph/kuka_sim_for_cyber_knife.git
cd simulation_pkg/ros1_working_package/Assembly_Toby
```

## 2. Install Dependencies

- **ROS Noetic** (tested)
- **Python 3.x**
- **Gazebo**
- **Python Packages:**
  ```bash
  pip3 install numpy sympy matplotlib
  ```
- **ROS Packages:**
  ```bash
  sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-geometry-msgs ros-noetic-std-msgs
  ```

## 3. Build the ROS Workspace

```bash
catkin_make
source devel/setup.bash
```

---

# 🤖 Usage Instructions

## 1. Launch the Gazebo Simulation

```bash
roslaunch Assembly_Toby template_launch.launch
```

## 2. Make Python Scripts Executable

```bash
chmod +x publisher.py
chmod +x subscriber.py
```

## 3. Run the ROS Nodes

```bash
rosrun Assembly_Toby publisher.py
rosrun Assembly_Toby subscriber.py
```

## 4. (Optional) Hardware Implementation on Turtlebot3

- **SLAM:**
  ```bash
  roslaunch turtlebot3_slam turtlebot3_slam.launch
  ```
- **Navigation:**
  ```bash
  roslaunch turtlebot3_navigation turtlebot3_navigation.launch
  ```

---

# 🧠 Technical Highlights

## Denavit-Hartenberg (DH) Parameters

| Joint | a (mm) | α (rad) | d (mm) | θ (variable) |
|-------|--------|---------|--------|--------------|
| 1     | 0      | π/2     | 400    | θ₁           |
| 2     | 25     | 0       | 0      | θ₂           |
| 3     | 315    | 0       | 0      | θ₃           |
| 4     | 35     | π/2     | 365    | θ₄           |
| 5     | 0      | -π/2    | 0      | θ₅           |
| 6     | 0      | 0       | 161.44 | θ₆           |

- **Forward Kinematics:**  
  Each joint’s transformation matrix is built from the DH table and multiplied sequentially to get the end-effector pose.

- **Inverse Kinematics:**  
  - *Geometric method* (fast, but not suitable for redundancy/complexity)
  - *Numerical Jacobian-based method* (chosen): Iteratively solves for joint angles using the Jacobian, ideal for 6/7-DOF robots and surgical-like paths.

- **Dynamics & Torque:**  
  - Uses the equation:  
    \(\tau = M(\theta)\ddot{\theta} + C(\theta, \dot{\theta})\dot{\theta} + G(\theta)\)
  - Gravity and external force compensation ensure stable, precise motion.

## ROS Node Architecture

- **Publisher Node:**  
  - Publishes joint torques/angles as `Float64MultiArray` on `/turn` at 10Hz.
  - Handles kinematics, trajectory, and torque calculations.

- **Subscriber Node:**  
  - Subscribes to `/turn`, splits the array, and publishes to each joint’s controller topic.

---

# 📊 Example Commands

- **Check Published Messages:**
  ```bash
  rostopic echo /turn
  ```
- **Manual Joint Command:**
  ```bash
  rostopic pub /turn std_msgs/Float64MultiArray "data: [j1, j2, j4, j5, j6, j7]"
  ```

---

# 📁 Project Structure

| Folder      | Contents                                 |
|-------------|------------------------------------------|
| `src/`      | Source code (Python scripts)             |
| `launch/`   | Launch files for Gazebo/ROS              |
| `config/`   | Controller and robot config files        |
| `models/`   | Robot URDF, meshes, and CAD files        |
| `scripts/`  | Python scripts for nodes                 |

---

# 👩‍💻 Contributors

- Joseph Pranadeer Reddy Katakam
- Bhargav Kumar Soothram
- Bharadwaj Chukkala

---

# 📜 License

Apache License

---

# 🙏 Acknowledgments

- ENPM662 - Introduction to Robot Modeling  
- University of Maryland, College Park

---

# 📝 Additional Documentation

- **System Architecture**
- **Troubleshooting Guide**
- **API Documentation**
- **Testing Procedures**
- **Example Outputs/Visualizations**

---

# 💡 Summary Table: System Features

| Feature                | Implementation Detail                        | Outcome/Impact                        |
|------------------------|----------------------------------------------|---------------------------------------|
| ROS1 Pub/Sub           | Python nodes, 10Hz, Float64MultiArray        | Real-time, multi-joint control        |
| Kinematics & Dynamics  | DH, Jacobian, gravity compensation           | Accurate, force-aware motion          |
| Trajectory Planning    | Parametric, surgical-like path               | Mimics surgical arcs, smooth control  |
| Simulation & Hardware  | Gazebo, Turtlebot3                           | Robust, real-world validation         |
| Scalability            | Modular, topic-based architecture            | Extensible for future research        |
