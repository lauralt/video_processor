import cv2
from enum import Enum


class FlipMode(Enum):
    """Flip modes for image transformation using OpenCV.

    These values correspond to the flip codes expected by `cv2.flip()`:

    - 1: Flip horizontally (left ↔ right),
    - 0: Flip vertically (top ↔ bottom),
    - -1: Flip both vertically and horizontally (diagonal mirror).
    """

    HORIZONTAL = 1
    VERTICAL = 0
    COMPLETE = -1


class Frame:
    def __init__(self, frame):
        """Initializes a wrapper object over a video frame."""
        self.frame = frame

    def resize(self, width, height):
        """Resize the frame to `width` width and `height` height."""
        self.frame = cv2.resize(self.frame, (width, height))
        return self

    def invert_colors(self):
        """Invert every pixel of the frame (change to its opposite value)."""
        self.frame = cv2.bitwise_not(self.frame)
        return self

    def flip(self, mode: FlipMode):
        """Rotate the frame in the selected `mode`."""
        # Extend `FlipMode` if you want to add more options.
        self.frame = cv2.flip(self.frame, mode.value)

    def get(self):
        """Return the wrapped frame."""
        return self.frame
