import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=1, 
                       min_detection_confidence=0.5, 
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Pycaw setup for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get the volume range and initialize variables
volume_range = volume.GetVolumeRange()  # Min, Max, and Step
min_volume, max_volume = volume_range[0], volume_range[1]

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get landmarks for thumb and index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Convert normalized coordinates to pixel values
            h, w, _ = frame.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            
            # Calculate the distance between the thumb and index finger
            distance = np.linalg.norm([thumb_x - index_x, thumb_y - index_y])
            
            # Map the distance to the system's volume range
            mapped_volume = np.interp(distance, [20, 150], [min_volume, max_volume])
            volume.SetMasterVolumeLevel(mapped_volume, None)
            
            # Display the distance and volume on the frame
            cv2.putText(frame, f'Distance: {int(distance)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (255, 0, 0), 2)
            cv2.putText(frame, f'Volume: {int(np.interp(mapped_volume, [min_volume, max_volume], [0, 100]))}%', 
                        (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Hand Tracking - Volume Control", frame)
    
    # Exit with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
