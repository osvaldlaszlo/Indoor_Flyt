Camera calibration
===================

Follow the ROS guide : http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

Edit camera acquisition via the launch file : `/flyt/flytos/flytcore/share/vision_apps/cam_api.launch`

NOTE : For an A3, the square size is 0.01345 meter

```bash
apt-get install ros-indigo-camera-calibration

rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.01345 image:=/Miniwonga/Odroid720p/image_raw camera:=/Miniwonga/Odroid720p

# Verify if /flyt/flytos/flytcore/share/vision_apps/calibrationdata is created, else save calibration and manually copy calibrationdata
```
