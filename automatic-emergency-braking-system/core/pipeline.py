import depthai as dai
from constants.config import LABELS, get_model_path

def create_pipeline():
    pipeline = dai.Pipeline()

    cam_rgb = pipeline.create(dai.node.ColorCamera)
    cam_rgb.setPreviewSize(300, 300)
    cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    cam_rgb.setInterleaved(False)
    cam_rgb.setFps(15)
    cam_rgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)

    mono_left = pipeline.create(dai.node.MonoCamera)
    mono_right = pipeline.create(dai.node.MonoCamera)
    mono_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
    mono_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
    mono_left.setBoardSocket(dai.CameraBoardSocket.CAM_B)
    mono_right.setBoardSocket(dai.CameraBoardSocket.CAM_C)

    stereo = pipeline.create(dai.node.StereoDepth)
    stereo.setDepthAlign(dai.CameraBoardSocket.CAM_A)
    mono_left.out.link(stereo.left)
    mono_right.out.link(stereo.right)

    detection_nn = pipeline.create(dai.node.MobileNetSpatialDetectionNetwork)
    detection_nn.setBlobPath(get_model_path())
    detection_nn.setConfidenceThreshold(0.5)
    cam_rgb.preview.link(detection_nn.input)
    stereo.depth.link(detection_nn.inputDepth)

    xout_rgb = pipeline.create(dai.node.XLinkOut)
    xout_rgb.setStreamName("rgb")
    cam_rgb.preview.link(xout_rgb.input)

    xout_nn = pipeline.create(dai.node.XLinkOut)
    xout_nn.setStreamName("detections")
    detection_nn.out.link(xout_nn.input)

    return pipeline
