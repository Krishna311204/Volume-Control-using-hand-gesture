# Hand Tracking for Volume Control

This project demonstrates real-time hand tracking using MediaPipe and allows controlling the system volume by measuring the distance between the thumb and index finger.

## Features
- Real-time hand tracking using the webcam.
- Detects the thumb and index finger to calculate the distance between them.
- Maps the distance to the system volume level using Pycaw.
- Displays the distance and current volume percentage on the video feed.

## Requirements
To run this project, you need the following:

### Software:
- Python 3.7 or later

### Python Libraries:
Install the required libraries using pip:
```bash
pip install opencv-python mediapipe pycaw comtypes numpy
```

## How It Works
1. **Hand Tracking**: The project uses MediaPipe to detect and track hand landmarks in real time.
2. **Landmark Detection**: Tracks the tip of the thumb and index finger to calculate their distance.
3. **Volume Mapping**: Uses the distance between the two landmarks to set the system volume via Pycaw.
4. **Visualization**: Overlays the distance and volume percentage on the video feed.

## Usage
1. Clone or download the script.
2. Ensure your webcam is functional.
3. Run the Python script:
   ```bash
   python hand_tracking_volume_control.py
   ```
4. Move your thumb and index finger closer or farther apart to increase or decrease the volume, respectively.
5. Press `q` to exit the application.

## Customization
- **Distance Range**: Adjust the distance range `[20, 150]` in the code to better suit your hand movements.
- **Volume Range**: The volume range is automatically mapped based on the system's audio settings.

## Example Output
The application shows:
- A live video feed with hand landmarks drawn.
- Real-time distance between the thumb and index finger.
- Current system volume percentage.

## Troubleshooting
- Ensure your webcam is properly connected and accessible.
- Check if the required libraries are installed.
- If the volume control isn't responsive, adjust the distance range in the code.

## Acknowledgements
This project uses:
- [MediaPipe](https://mediapipe.dev/) for real-time hand tracking.
- [PyCaw](https://github.com/AndreMiras/pycaw) for system audio control.

## License
This project is for educational purposes. Feel free to modify and use it as needed.

---

Enjoy controlling your volume with simple hand gestures!
