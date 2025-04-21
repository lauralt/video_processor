import cv2

from utils.file import open_file
from video.frame import FlipMode, Frame


class Camera:
    def __init__(self, device_index=0):
        """Initialise a camera object."""
        # the filename of the processed video output.
        self.output_filename = None
        # the VideoWriter object associated with the output file.
        self.out = None

        # Use default video format.
        cap = cv2.VideoCapture(device_index)
        if not cap.isOpened():
            raise RuntimeError("Could not open camera.")
            # Mac camera is not available in Linux VM (VirtualBox).
            # To test the app, one already existing video can be used as input:
            # cap = cv2.VideoCapture("movie.mov")
        self.fps = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # Force width and height to int as this is the expected type of `cv2.VideoWriter`.
        # This will be the default values used when no manual (user) scaling is done.
        self.scale_to = (int(width), int(height))
        self.cap = cap

    def set_scaling(self, target_width: int, target_height: int):
        """Set the scaling of each frame."""
        self.scale_to = (target_width, target_height)

    def set_format(self, filename: str, codec: str = "avc1"):
        """Set the format (codec) of the video output file.

        The default format is `avc1` which is the identifier of `h264`.
        `filename` is the name of the file for the processed video output.
        """
        if self.scale_to is None:
            raise ValueError("Scaling was not set.")
        fourcc = cv2.VideoWriter.fourcc(*codec)
        self.output_filename = filename

        self.out = cv2.VideoWriter(
            self.output_filename, fourcc, self.fps, self.scale_to
        )

    def display_output(self):
        """Display the processed video output."""
        open_file(self.output_filename)

    def run(self, quit_key="q"):
        """Records video from the camera and processes it."""
        # Start the livestreaming.
        print(f"Streaming live... (Press '{quit_key}' to stop the streaming.)")

        while True:
            ret, raw_frame = self.cap.read()
            if not ret:
                print("Could not capture frame.")
                break

            cv2.imshow("Processing...", raw_frame)

            # Do the required processing.
            video_frame = Frame(raw_frame)
            video_frame.resize(*self.scale_to).invert_colors().flip(FlipMode.HORIZONTAL)

            processed = video_frame.get()

            cv2.imshow("Processed video", processed)
            if self.out:
                self.out.write(processed)

            if cv2.waitKey(1) & 0xFF == ord(quit_key):
                break

        self.cleanup()

    def cleanup(self):
        """Free the resources."""
        self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()
