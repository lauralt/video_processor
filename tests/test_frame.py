import numpy as np
from video.frame import Frame, FlipMode


def test_invert():
    frame = np.zeros((2, 2, 3), dtype=np.uint8)
    vf = Frame(frame)
    inverted = vf.invert_colors().get()

    expected = 255 * np.ones((2, 2, 3), dtype=np.uint8)
    assert np.array_equal(inverted, expected)

    frame = np.array(
        [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8
    )
    vf = Frame(frame)
    inverted = vf.invert_colors().get()

    expected = np.array(
        [[[0, 255, 255], [255, 0, 255]], [[255, 255, 0], [0, 0, 255]]], dtype=np.uint8
    )
    assert np.array_equal(inverted, expected)


def test_resize():
    frame = np.zeros((10, 10, 3), dtype=np.uint8)
    vf = Frame(frame)
    resized = vf.resize(5, 4).get()
    assert resized.shape == (4, 5, 3)

    frame = np.zeros((12, 6, 14), dtype=np.uint8)
    vf = Frame(frame)
    resized = vf.resize(5, 7).get()
    assert resized.shape == (7, 5, 14)


def test_flip():
    frame = np.array(
        [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8
    )

    frame = Frame(frame)
    # test the horizontal flip.
    frame.flip(FlipMode.HORIZONTAL)
    flipped = frame.get()

    expected = np.array(
        [[[0, 255, 0], [255, 0, 0]], [[255, 255, 0], [0, 0, 255]]], dtype=np.uint8
    )
    assert np.array_equal(flipped, expected)

    # test the vertical flip.
    frame.flip(FlipMode.VERTICAL)
    flipped = frame.get()

    expected = np.array(
        [[[255, 255, 0], [0, 0, 255]], [[0, 255, 0], [255, 0, 0]]], dtype=np.uint8
    )
    assert np.array_equal(flipped, expected)

    # test the complete flip.
    frame.flip(FlipMode.COMPLETE)
    flipped = frame.get()

    expected = np.array(
        [
            [[255, 0, 0], [0, 255, 0]],
            [
                [0, 0, 255],
                [255, 255, 0],
            ],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(flipped, expected)
