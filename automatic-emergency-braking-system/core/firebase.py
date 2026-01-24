import requests
import threading
from constants.config import FIREBASE_URL

def send_to_firebase(detection_data):
    def _send():
        try:
            url = f"{FIREBASE_URL}/current_detection.json"
            response = requests.put(url, json=detection_data, timeout=2)

            if response.status_code == 200:
                print("  ✓ Data sent to Firebase successfully")
            else:
                print(f"  ✗ Failed to send to Firebase: {response.status_code}")
        except Exception as e:
            print(f"  ✗ Firebase error: {e}")

    threading.Thread(target=_send, daemon=True).start()
