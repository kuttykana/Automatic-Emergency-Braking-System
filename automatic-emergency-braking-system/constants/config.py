# GPIO Pins
DIR_PIN = 17
PWM_PIN = 18

# Distance threshold in meters
DISTANCE_THRESHOLD = 5.0

# Actuator Settings
ACTUATOR_FULL_TRAVEL_TIME = 12.47
PWM_FREQUENCY = 20000
PWM_PERIOD = 1.0 / PWM_FREQUENCY

# Firebase
FIREBASE_URL = "https://haficollab-default-rtdb.asia-southeast1.firebasedatabase.app"
FIREBASE_INTERVAL = 1.0  # seconds

# Labels
LABELS = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat",
    "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

def get_model_path():
    import blobconverter
    return blobconverter.from_zoo(
        name="mobilenet-ssd",
        shaves=6,
        version="2021.4"
    )
