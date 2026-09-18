import cv2
import numpy as np


def detect_canny_edges(
    image: np.ndarray,
    lower_threshold: int = 100,
    upper_threshold: int = 200
) -> np.ndarray:
    """Detect edges using the Canny edge detector."""

    if lower_threshold < 0 or upper_threshold < 0:
        raise ValueError("Thresholds cannot be negative.")

    if lower_threshold >= upper_threshold:
        raise ValueError(
            "Lower threshold must be smaller than upper threshold."
        )

    return cv2.Canny(
        image,
        lower_threshold,
        upper_threshold
    )


def detect_sobel_edges(image: np.ndarray) -> np.ndarray:
    """Detect edges using the Sobel gradient operator."""

    sobel_x = cv2.Sobel(
        image,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    sobel_y = cv2.Sobel(
        image,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    magnitude = cv2.magnitude(
        sobel_x,
        sobel_y
    )

    magnitude = cv2.convertScaleAbs(magnitude)

    return magnitude