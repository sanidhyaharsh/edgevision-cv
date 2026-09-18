# EdgeVision

## Command-Line Computer Vision Toolkit for Edge Detection and Image Analysis

EdgeVision is a Python-based computer vision toolkit that performs image preprocessing, edge detection, edge analysis, visualization, and result comparison through a command-line interface.

The project implements two classical edge detection techniques:

- Canny Edge Detection
- Sobel Edge Detection

It also provides a comparison mode to analyze the results produced by both methods.

---

## Features

- Load images from the command line
- Convert images to grayscale
- Apply Gaussian filtering for noise reduction
- Perform Canny edge detection
- Perform Sobel gradient-based edge detection
- Compare Canny and Sobel results
- Calculate edge pixel count
- Calculate edge density
- Detect contours
- Generate edge visualization images
- Generate JSON analysis reports
- Run automated unit tests using pytest
- Fully executable through the command line

---

## Project Structure

```text
EdgeVision/
│
├── edgevision/
│   ├── __init__.py
│   ├── analysis.py
│   ├── edge_detection.py
│   ├── preprocessing.py
│   ├── utils.py
│   └── visualization.py
│
├── input/
│   └── images.jpg
│
├── output/
│   └── .gitkeep
│
├── tests/
│   ├── test_analysis.py
│   ├── test_edge_detection.py
│   └── test_preprocessing.py
│
├── docs/
│   └── diagrams/
│       └── project_diagrams.md
│
├── main.py
├── pytest.ini
├── requirements.txt
├── statement.md
├── README.md
└── .gitignore

Technologies Used
Python 3.12+
OpenCV
NumPy
Matplotlib
Pytest
Requirements

The project requires Python 3.12 or later and the packages listed in requirements.txt.

The recommended setup uses a Python virtual environment.

Installation
1. Clone the repository
git clone https://github.com/sanidhyaharsh/edgevision-cv.git
2. Enter the project directory
cd edgevision-cv
3. Create a virtual environment

On Windows:

python -m venv venv
4. Activate the virtual environment

PowerShell:

.\venv\Scripts\Activate.ps1

Command Prompt:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
Running the Project

EdgeVision is executed through main.py.

The general command format is:

python main.py --input <image-path> --method <method>
Canny Edge Detection

To perform Canny edge detection:

python main.py --input input/images.jpg --method canny

The program:

Loads the input image.
Converts it to grayscale.
Applies Gaussian filtering.
Performs Canny edge detection.
Calculates edge statistics.
Detects contours.
Generates visualization and analysis results.
Sobel Edge Detection

To perform Sobel edge detection:

python main.py --input input/images.jpg --method sobel

The program calculates the horizontal and vertical image gradients and combines them to obtain the Sobel edge magnitude.

Comparison Mode

To run both Canny and Sobel edge detection:

python main.py --input input/images.jpg --method compare

The comparison mode processes the image using both methods and reports their edge densities.

Example output from the tested sample image:

Canny edge density: 2.09%
Sobel edge density: 89.08%

[✓] Results saved successfully
Output

Generated results are stored in the output/ directory during execution.

Depending on the selected method, the program generates:

Edge detection PNG images
Comparison visualizations
JSON analysis reports

Example generated files include:

output/
├── images_canny.png
├── images_canny_comparison.png
├── images_canny_report.json
├── images_sobel.png
├── images_sobel_comparison.png
└── images_sobel_report.json

These files are generated during execution and are not tracked in Git because they are excluded through .gitignore.

Image Analysis

EdgeVision calculates the following analysis values:

Edge Pixel Count

The number of pixels identified as edge pixels in the generated edge map.

Edge Density

The percentage of pixels classified as edges relative to the total number of image pixels.

Contour Detection

Contours are detected from the generated edge map to provide additional structural information about the image.

Automated Testing

The project includes automated tests using pytest.

Run all tests with:

pytest -v

The current implementation contains tests covering:

Image loading
Grayscale conversion
Gaussian filtering
Invalid Gaussian kernel sizes
Canny output shape
Invalid Canny thresholds
Sobel output shape
Sobel edge detection
Edge pixel counting
Edge density calculation
Contour detection
Complete analysis generation
Test Result

The complete test suite was successfully executed with:

12 passed in 0.12s
Computer Vision Pipeline

The main processing pipeline is:
Input Image
     |
     v
Image Loading
     |
     v
Grayscale Conversion
     |
     v
Gaussian Filtering
     |
     v
Edge Detection
   /     \
  /       \
Canny    Sobel
  \       /
   \     /
    v   v
Image Analysis
     |
     +--> Edge Pixel Count
     |
     +--> Edge Density
     |
     +--> Contour Detection
     |
     v
Visualization
     |
     v
JSON Report

Detailed system architecture, workflow, use case, component, sequence, and data flow diagrams are available in:

docs/diagrams/project_diagrams.md
Error Handling

The application validates input files and processing parameters.

Examples of handled conditions include:

Missing input image
Invalid Gaussian kernel size
Invalid Canny threshold configuration
Invalid or unsupported input conditions

Errors are reported through the command-line interface.

Design Approach

EdgeVision follows a modular architecture.

The major responsibilities are separated into independent modules:
| Module              | Responsibility                                              |
| ------------------- | ----------------------------------------------------------- |
| `main.py`           | Command-line interface and pipeline orchestration           |
| `preprocessing.py`  | Image loading, grayscale conversion, and Gaussian filtering |
| `edge_detection.py` | Canny and Sobel edge detection                              |
| `analysis.py`       | Edge statistics and contour detection                       |
| `visualization.py`  | Visualization and comparison output generation              |
| `utils.py`          | File and JSON report utilities                              |
| `tests/`            | Automated testing of core functionality                     |

Limitations
The application currently operates through a command-line interface.
Results depend on the quality and characteristics of the input image.
Sobel edge detection can produce a denser edge map than Canny because it produces gradient magnitude rather than applying Canny's full edge-thinning and thresholding pipeline.
The current implementation does not use a database or cloud storage.
Future Improvements

Possible future improvements include:

Support for additional edge detection techniques
Interactive threshold configuration
Batch processing of multiple images
Additional image quality metrics
Improved visualization options
Support for additional image formats
Performance optimization for large images
Academic Project

Project: EdgeVision - Image Edge Detection & Analysis Toolkit

Course: Computer Vision

Type: Evaluated Course Project

Methods: Canny and Sobel Edge Detection

Interface: Command Line

Repository:
https://github.com/sanidhyaharsh/edgevision-cv

