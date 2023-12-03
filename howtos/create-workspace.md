# Create workspace
ros_workspaces is a base folder for all workspaces. It is a monorepository for all the stuff that is and will be build unless decided otherwise in future

First, create a directory (ros2_ws) to contain new workspace:

```bash
mkdir -p ~/repos/ros_workspaces/new_wspace/src
cd ~/repos/ros_workspaces/new_wspace
``` 

At this point the workspace contains a single empty directory src:

```
.
└── src

1 directory, 0 files
```

# Add some sources

```
.
└── src
    └── examples
        ├── CONTRIBUTING.md
        ├── LICENSE
        ├── rclcpp
        ├── rclpy
        └── README.md

4 directories, 3 files
```

# Source an underlay

It is important that we have sourced the environment for an existing ROS 2 installation that will provide our workspace with the necessary build dependencies for the example packages. This is achieved by sourcing the setup script provided by a binary installation or a source installation, ie. another colcon workspace (see Installation). We call this environment an underlay.

Our workspace, ros2_ws, will be an overlay on top of the existing ROS 2 installation. In general, it is recommended to use an overlay when you plan to iterate on a small number of packages, rather than putting all of your packages into the same workspace.

# Build the workspace

In the root of the workspace, run colcon build. Since build types such as ament_cmake do not support the concept of the devel space and require the package to be installed, colcon supports the option --symlink-install. This allows the installed files to be changed by changing the files in the source space (e.g. Python files or other non-compiled resources) for faster iteration.

``` bash
colcon build --symlink-install
```

```
.
├── build
├── install
├── log
└── src

4 directories, 0 files
```

# Run tests

To run tests for the packages we just built, run the following:

``` bash
colcon test
```