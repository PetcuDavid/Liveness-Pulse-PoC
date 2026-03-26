import cv2
import numpy as np

# Initialize capture (Use 0 for webcam or OBS Virtual Cam index)
cap = cv2.VideoCapture(0)

def get_pulse_signature(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    rows, cols = gray.shape
    crow, ccol = rows//2, cols//2
    # Check specific frequency energy
    energy = np.abs(fshift[crow+50, ccol+50])
    return energy

attack_mode = False
integrity_history = []
BUFFER_SIZE = 10 # For Temporal Smoothing

while True:
    ret, frame = cap.read()
    if not ret: break
    display_frame = frame.copy()

    if attack_mode:
        display_frame = cv2.GaussianBlur(display_frame, (25, 25), 0)
    
    sig = get_pulse_signature(display_frame)
    integrity_history.append(sig)
    if len(integrity_history) > BUFFER_SIZE:
        integrity_history.pop(0) 
    
    avg_sig = sum(integrity_history) / len(integrity_history)
    
    # Decision Logic
    if avg_sig < 1200: 
        status, color = "!!! TAMPERED / DEEPFAKE !!!", (0, 0, 255)
    else:
        status, color = "INTEGRITY: SECURE", (0, 255, 0)

    # UI Overlay
    cv2.putText(display_frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow('Liveness-Pulse Guard', display_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('a'): attack_mode = not attack_mode 
    if key == ord('q'): break

cap.release()
cv2.destroyAllWindows()
