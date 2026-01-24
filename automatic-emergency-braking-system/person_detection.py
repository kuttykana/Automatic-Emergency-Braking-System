#!/usr/bin/env python3
"""
Entry point for the Automatic Emergency Braking System
"""

import cv2
import depthai as dai
import time
from datetime import datetime

from core.motor_control import extend_actuator, retract_actuator
from core.firebase import send_to_firebase
from core.pipeline import create_pipeline
from constants.config import DISTANCE_THRESHOLD, FIREBASE_INTERVAL, LABELS

def main():
    pipeline = create_pipeline()
    last_firebase_time = 0

    with dai.Device(pipeline) as device:
        q_rgb = device.getOutputQueue("rgb", 4, False)
        q_det = device.getOutputQueue("detections", 4, False)

        frame = None
        detections = []

        while True:
            in_rgb = q_rgb.tryGet()
            if in_rgb is not None:
                frame = in_rgb.getCvFrame()

            in_det = q_det.tryGet()
            if in_det is not None:
                detections = in_det.detections

            if frame is not None:
                persons = [d for d in detections if LABELS[d.label] == "person"]

                if persons:
                    nearest = min(persons, key=lambda d: d.spatialCoordinates.z)
                    dist_m = nearest.spatialCoordinates.z / 1000.0

                    print(f"Nearest person: {dist_m:.2f} m")

                    firebase_data = {
                        "timestamp": datetime.now().isoformat(),
                        "distance_meters": round(dist_m, 2),
                        "distance_cm": round(dist_m * 100, 1)
                    }

                    if time.time() - last_firebase_time > FIREBASE_INTERVAL:
                        send_to_firebase(firebase_data)
                        last_firebase_time = time.time()

                    if dist_m < DISTANCE_THRESHOLD:
                        extend_actuator()
                    else:
                        retract_actuator()
                else:
                    retract_actuator()

                for d in persons:
                    z = d.spatialCoordinates.z / 1000
                    x1 = int(d.xmin * frame.shape[1])
                    y1 = int(d.ymin * frame.shape[0])
                    x2 = int(d.xmax * frame.shape[1])
                    y2 = int(d.ymax * frame.shape[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{z:.2f}m", (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

                cv2.imshow("Person Detection + Actuator", frame)

            if cv2.waitKey(1) == ord('q'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
