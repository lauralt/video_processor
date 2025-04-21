from video.camera import Camera

video_camera = Camera()
video_camera.set_scaling(640, 360)
video_camera.set_format("output.mp4")
video_camera.run()
video_camera.display_output()
