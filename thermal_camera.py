import cv2
from lepton3 import Lepton

def capture_thermal_image():
    with Lepton() as l:
        frame, _ = l.capture()
        image = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
        cv2.imwrite("thermal.jpg", image)
        return "thermal.jpg"

capture_thermal_image()
