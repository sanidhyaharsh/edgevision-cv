import numpy as np

from edgevision.analysis import (
    calculate_edge_pixel_count,
    calculate_edge_density,
    detect_contours,
    generate_analysis
)


def test_edge_pixel_count():
    image = np.zeros((10, 10), dtype=np.uint8)

    image[5, :] = 255

    assert calculate_edge_pixel_count(image) == 10


def test_edge_density():
    image = np.zeros((10, 10), dtype=np.uint8)

    image[5, :] = 255

    assert calculate_edge_density(image) == 10.0


def test_detect_contours():
    image = np.zeros((100, 100), dtype=np.uint8)

    image[25:75, 25:75] = 255

    contours = detect_contours(image)

    assert len(contours) >= 1


def test_generate_analysis():
    image = np.zeros((100, 100), dtype=np.uint8)

    image[50, :] = 255

    result = generate_analysis(image)

    assert result["image_width"] == 100
    assert result["image_height"] == 100
    assert result["edge_pixels"] == 100
    assert result["edge_density_percent"] == 1.0