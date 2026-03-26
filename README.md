# Liveness Pulse - Real-Time Video Integrity Verification

**Liveness Pulse** is a Proof of Concept (PoC) designed to ensure video stream integrity against live deepfake impersonation. Unlike traditional passive detection, this system uses **Frequency Domain Steganography** to validate the source.

## Core Concept
- **Integrity over Detection:** We don't guess if a face is real; we verify if the pixel data was regenerated.
- **FFT Analysis:** Uses Fast Fourier Transform to monitor signal energy stability.
- **Temporal Smoothing:** A 10-frame circular buffer filters natural motion blur to reduce false positives.

## Performance
- **Latency:** < 5ms (Optimized for 4K streams).
- **Stack:** Python, OpenCV, NumPy.

## Installation & Usage
1. Clone the repo: `git clone https://github.com/PetcuDavid/LivenessPulse-PoC`
2. Install dependencies: `pip install opencv-python numpy`
3. Run the demo: `python main.py`
4. Press **'a'** to simulate a deepfake/blur attack.
