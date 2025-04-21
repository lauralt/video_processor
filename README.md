# Video processing application

The `video_processor` application provides a minimal interface for basic video
frame and camera setup. It also runs a demo application that does livestreaming
from the first camera, processes the stream, and then generates an output video
in H.264 format.

## Platform support

This application was tested on macOS (Arm-based), and partially on Linux
(Ubuntu).

## Requirements

- Python 3
- pip3
- make
- opencv-python

Optional (for testing, formatting etc.):
- pytest
- black
- ruff linter

Also make sure you have a video player installed. On Mac the application was
tested with QuickTime Player, and in an Ubuntu VM with VLC.

*Note* more instructions can be added here, e.g. how to install each package
depending on your platform/distribution, useful links etc.

## Building and Running

To build and start the application run the following:

```bash
make run
```

You should see two video streams on the screen:

- one with the raw output
- one that is processed with the following:
    - scaled to (640, 360),
    - flipped horizontally,
    - inverted colors.

To stop the streaming, press `q`. An output video will be displayed in a new
window. This video is the streamed, processed one before, but with H.264 codec
applied.

## Testing

*Note* Currently, there are only tests for the Frame object. The Camera one and
the utilities from `utils` require some level of mocking. This is future work.

```bash
make test
```
