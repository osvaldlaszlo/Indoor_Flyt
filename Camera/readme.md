Follow the ROS guide : http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

apt-get install ros-indigo-camera-calibration

rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.01345 image:=/Miniwonga/Odroid720p/image_raw camera:=/Miniwonga/Odroid720p
