import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """Load an image from the given file path."""

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            f"Unable to load image: {image_path}"
        )

    return image


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert a BGR image to grayscale."""

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(
    grayscale_image: np.ndarray,
    kernel_size: int = 5
) -> np.ndarray:
    """Reduce image noise using Gaussian filtering."""

    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError(
            "Kernel size must be a positive odd number."
        )

    return cv2.GaussianBlur(
        grayscale_image,
        (kernel_size, kernel_size),
        0
    )