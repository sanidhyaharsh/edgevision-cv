# Project Statement

## Project Title

EdgeVision – Image Edge Detection and Analysis Toolkit

## Problem Statement

Edges are important features in digital images because they represent significant changes in intensity and often correspond to object boundaries, shapes, and structural details. Different edge detection techniques can produce different results depending on the characteristics of an image.

The objective of EdgeVision is to develop a command-line Computer Vision toolkit that preprocesses an input image, detects edges using Canny and Sobel methods, analyzes the resulting edge maps, and generates visual and numerical outputs.

The system provides a simple way to perform edge detection and compare the results of two commonly used Computer Vision techniques.

## Scope of the Project

The project focuses on image-based edge detection and analysis.

The system includes:

- Image loading and validation
- Grayscale conversion
- Gaussian filtering for noise reduction
- Canny edge detection
- Sobel gradient-based edge detection
- Edge pixel counting
- Edge density calculation
- Contour detection
- Canny and Sobel comparison
- Visual result generation
- JSON-based analysis reports
- Automated testing

The project is designed to process static image files through a command-line interface.

## Target Users

The intended users include:

- Computer Vision students
- Beginners learning image processing
- Students experimenting with edge detection algorithms
- Developers building basic image-processing pipelines
- Researchers performing preliminary image analysis

## High-Level Features

1. **Image Preprocessing**
   - Loads and validates the input image.
   - Converts images to grayscale.
   - Applies Gaussian filtering.

2. **Canny Edge Detection**
   - Detects significant image boundaries using the Canny algorithm.
   - Supports configurable lower and upper thresholds.

3. **Sobel Edge Detection**
   - Calculates image gradients in horizontal and vertical directions.
   - Produces a gradient magnitude edge representation.

4. **Edge Analysis**
   - Calculates the number of edge pixels.
   - Calculates edge density.
   - Detects contours.

5. **Comparison Mode**
   - Processes the same image using Canny and Sobel.
   - Generates comparative statistics and visual outputs.

6. **Result Generation**
   - Saves processed edge images.
   - Generates side-by-side comparison images.
   - Stores analysis results in JSON format.

7. **Validation and Testing**
   - Validates user input and processing parameters.
   - Includes automated tests using pytest.