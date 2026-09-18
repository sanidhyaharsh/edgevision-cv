import numpy as np
import pytest

from edgevision.preprocessing import (
    load_image,
    convert_to_grayscale,
    apply_gaussian_blur
)


def test_grayscale_conversion():
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    gray = convert_to_grayscale(image)

    assert gray.shape == (100, 100)
    assert gray.dtype == np.uint8


def test_gaussian_blur():
    image = np.zeros((100, 100), dtype=np.uint8)

    blurred = apply_gaussian_blur(image)

    assert blurred.shape == image.shape
    assert blurred.dtype == np.uint8


def test_invalid_kernel_size():
    image = np.zeros((100, 100), dtype=np.uint8)

    with pytest.raises(ValueError):
        apply_gaussian_blur(image, kernel_size=4)


def test_load_missing_image():
    with pytest.raises(FileNotFoundError):
        load_image("input/nonexistent_image.jpg")