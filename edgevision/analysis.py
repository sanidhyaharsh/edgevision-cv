import cv2
import numpy as np


def calculate_edge_pixel_count(
    edge_image: np.ndarray
) -> int:
    """Count the number of detected edge pixels."""

    return int(np.count_nonzero(edge_image))


def calculate_edge_density(
    edge_image: np.ndarray
) -> float:
    """Calculate the percentage of pixels classified as edges."""

    total_pixels = edge_image.size

    if total_pixels == 0:
        return 0.0

    edge_pixels = calculate_edge_pixel_count(edge_image)

    return (edge_pixels / total_pixels) * 100


def detect_contours(
    edge_image: np.ndarray
) -> list:
    """Detect contours from an edge image."""

    contours, _ = cv2.findContours(
        edge_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours


def generate_analysis(
    edge_image: np.ndarray
) -> dict:
    """Generate numerical statistics for an edge image."""

    height, width = edge_image.shape[:2]

    edge_pixels = calculate_edge_pixel_count(edge_image)
    density = calculate_edge_density(edge_image)
    contours = detect_contours(edge_image)

    return {
        "image_width": width,
        "image_height": height,
        "edge_pixels": edge_pixels,
        "edge_density_percent": round(density, 2),
        "contours_detected": len(contours)
    }