import numpy as np
import pytest

from edgevision.edge_detection import (
    detect_canny_edges,
    detect_sobel_edges
)


def test_canny_output_shape():
    image = np.zeros((100, 100), dtype=np.uint8)

    edges = detect_canny_edges(image)

    assert edges.shape == image.shape
    assert edges.dtype == np.uint8


def test_canny_invalid_thresholds():
    image = np.zeros((100, 100), dtype=np.uint8)

    with pytest.raises(ValueError):
        detect_canny_edges(
            image,
            lower_threshold=200,
            upper_threshold=100
        )


def test_sobel_output_shape():
    image = np.zeros((100, 100), dtype=np.uint8)

    edges = detect_sobel_edges(image)

    assert edges.shape == image.shape
    assert edges.dtype == np.uint8


def test_sobel_detects_edge():
    image = np.zeros((100, 100), dtype=np.uint8)

    image[:, 50:] = 255

    edges = detect_sobel_edges(image)

    assert np.count_nonzero(edges) > 0