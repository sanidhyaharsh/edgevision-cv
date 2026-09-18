import cv2
import numpy as np
import matplotlib.pyplot as plt


def save_image(
    image: np.ndarray,
    output_path: str
) -> None:
    """Save an image to the specified output path."""

    success = cv2.imwrite(output_path, image)

    if not success:
        raise IOError(
            f"Unable to save image: {output_path}"
        )


def create_comparison(
    original: np.ndarray,
    processed: np.ndarray,
    output_path: str,
    original_title: str = "Original Image",
    processed_title: str = "Edge Detection"
) -> None:
    """Create and save a side-by-side comparison."""

    original_rgb = cv2.cvtColor(
        original,
        cv2.COLOR_BGR2RGB
    )

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title(original_title)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap="gray")
    plt.title(processed_title)
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()