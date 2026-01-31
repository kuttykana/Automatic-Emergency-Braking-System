# Automatic Emergency Braking System

The **Automatic Emergency Braking (AEB) System** is a safety project designed to prevent collisions by detecting obstacles and automatically applying the brakes. It utilizes AI-based person detection along with a 3D depth camera and a motorized actuator for real-time vehicle safety enhancement.

---

## 🚀 Features

- **Real-time object detection:** Identifies obstacles, including humans, with high accuracy using an OAK-D Lite AI camera.
- **Emergency braking system:** Deploys a motorized actuator in response to nearby obstacles.
- **Firebase integration:** Captures and shares detection data through a cloud-based Firebase database.
- **Customizable configurations:** Easily adjust distance thresholds and GPIO pin configurations.

---

## 🧰 Installation Guide

### **Prerequisites**
Before you begin:
- Make sure you have a **Raspberry Pi 5** set up with sufficient power.
- **Hardware components required:**
  - **OAK-D Lite camera**
  - **Linear Actuator for braking**
  - **Bidirectional Motor Driver**
  - **USB 3.0 Cable**
  - **Jumper Cables**
  - **Power Supply**
- Install **Python 3.x** on your Raspberry Pi.

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/kuttykana/Automatic-Emergency-Braking-System.git
   cd Automatic-Emergency-Braking-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure project settings:
   - Update the `constants/config.py` file to set the correct GPIO pins, thresholds, and other settings. 

4. Run the main script:
   ```bash
   python3 automatic-emergency-braking-system/person_detection_rpi_5.py
   ```

---

## 🛠️ Repository Structure

The repository is organized into the following structure:

```
Automatic-Emergency-Braking-System/
│
├── automatic-emergency-braking-system/
│   ├── constants/               # Configuration and constants
│   │   └── config.py
│   ├── core/                    # Core functionality
│   │   ├── firebase.py          # Firebase communication logic
│   │   ├── motor_control.py     # Actuator and motor control logic
│   │   └── pipeline.py          # Pipeline creation logic for OAK-D
│   ├── docs/                    # Documentation
│   │   ├── user_manual.md       # Detailed user instructions
│   │   └── getting_started.md   # Setup and installation guide
│   ├── images/                  # Stored project images or diagrams (currently empty)
│   ├── models/                  # Place pre-trained models like mobilenet-ssd.blob here (currently empty)
│   ├── tests/                   # Unit and integration tests (currently empty)
│   └── person_detection_rpi_5.py # Main script
│
├── requirements.txt             # Python dependencies
└── README.md                    # Project introduction and overall guide
```

---

## 📷 Videos
Video of my setup and hardware components are in the `Video` directory to provide better visualization for users.

---

## Contributing
Contributions are welcome! Please follow the guidelines mentioned in `CONTRIBUTING.md` (if applicable) or create a pull request with your improvements.

---

## License
This project is released under the [Apache License](LICENSE).

Feel free to contribute, modify, and use it for non-commercial purposes.

---

## Acknowledgments
This project is made possible by the support of the AI and open-source communities. Special thanks to DepthAI for their incredible tools!
