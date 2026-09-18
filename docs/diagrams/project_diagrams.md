# EdgeVision - Design Diagrams

## 1. System Architecture Diagram

```mermaid
flowchart TD
    A[User / Command Line] --> B[main.py]
    B --> C[Input Validation]
    C --> D[Preprocessing Module]

    D --> D1[Load Image]
    D --> D2[Grayscale Conversion]
    D --> D3[Gaussian Filtering]

    D --> E[Edge Detection Module]

    E --> E1[Canny Edge Detection]
    E --> E2[Sobel Edge Detection]

    E1 --> F[Analysis Module]
    E2 --> F

    F --> F1[Edge Pixel Count]
    F --> F2[Edge Density]
    F --> F3[Contour Detection]

    F --> G[Visualization Module]
    F --> H[JSON Report]

    G --> I[PNG Output]
    H --> J[JSON Output]
```

## 2. Process Workflow Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Receive Input Image and CLI Parameters]
    B --> C{Is Input Valid?}

    C -- No --> D[Display Error Message]
    D --> Z([End])

    C -- Yes --> E[Load Image]
    E --> F[Convert to Grayscale]
    F --> G[Apply Gaussian Blur]

    G --> H{Selected Method}

    H -- Canny --> I[Apply Canny Edge Detection]
    H -- Sobel --> J[Apply Sobel Gradient Detection]

    H -- Compare --> K[Apply Canny]
    K --> L[Apply Sobel]

    I --> M[Analyze Edge Map]
    J --> M

    L --> N[Analyze Canny and Sobel Results]

    M --> O[Generate Visualization]
    M --> P[Generate JSON Report]

    N --> Q[Generate Comparison Results]
    Q --> O
    Q --> P

    O --> R[Save PNG Results]
    P --> S[Save JSON Results]

    R --> T([End])
    S --> T
```

## 3. Use Case Diagram

```mermaid
flowchart LR
    User((User))

    UC1[Provide Input Image]
    UC2[Select Detection Method]
    UC3[Configure Canny Thresholds]
    UC4[Process Image]
    UC5[View Edge Statistics]
    UC6[Generate Visual Results]
    UC7[Generate JSON Report]
    UC8[Compare Canny and Sobel]
    UC9[Run Automated Tests]

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
    User --> UC8
    User --> UC9
```

## 4. Component Diagram

```mermaid
flowchart TD
    CLI[main.py<br/>Command Line Interface]

    PRE[preprocessing.py<br/>Image Preprocessing]
    EDGE[edge_detection.py<br/>Canny + Sobel]
    ANALYSIS[analysis.py<br/>Edge Analysis]
    VIS[visualization.py<br/>Visualization]
    UTIL[utils.py<br/>File Utilities]

    CLI --> PRE
    CLI --> EDGE
    CLI --> ANALYSIS
    CLI --> VIS
    CLI --> UTIL

    PRE --> EDGE
    EDGE --> ANALYSIS
    ANALYSIS --> VIS
    ANALYSIS --> UTIL

    VIS --> OUT1[PNG Results]
    UTIL --> OUT2[JSON Reports]
```

## 5. Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant CLI as main.py
    participant Pre as Preprocessing
    participant Edge as Edge Detection
    participant Analysis as Analysis
    participant Visual as Visualization
    participant Utils as Utilities

    User->>CLI: Provide image and method
    CLI->>Pre: Load image
    Pre-->>CLI: Loaded image

    CLI->>Pre: Convert to grayscale
    Pre-->>CLI: Grayscale image

    CLI->>Pre: Apply Gaussian filtering
    Pre-->>CLI: Blurred image

    CLI->>Edge: Apply selected edge detector
    Edge-->>CLI: Edge map

    CLI->>Analysis: Analyze edge map
    Analysis-->>CLI: Statistics and contours

    CLI->>Visual: Create visualization
    Visual-->>CLI: Visualization saved

    CLI->>Utils: Save analysis report
    Utils-->>CLI: JSON report saved

    CLI-->>User: Display processing results
```

## 6. Data Flow Diagram

```mermaid
flowchart LR
    A[Input JPG / PNG] --> B[OpenCV Image]
    B --> C[Grayscale Image]
    C --> D[Gaussian Filtered Image]
    D --> E[Edge Map]

    E --> F[Edge Pixel Count]
    E --> G[Edge Density]
    E --> H[Contour Detection]

    F --> I[Analysis Report]
    G --> I
    H --> I

    E --> J[PNG Visualization]
    I --> K[JSON File]
```

7. Storage Design

EdgeVision does not use a relational database.

The application uses:

Input image files stored in the input/ directory.
Generated visual outputs stored in the output/ directory.
Analysis results stored as JSON files.
No user accounts or persistent database records are required.

Therefore, an ER diagram is not applicable to the current implementation.

8. Module Responsibilities

| Module              | Responsibility                                          |
| ------------------- | ------------------------------------------------------- |
| `main.py`           | Command-line interface and pipeline orchestration       |
| `preprocessing.py`  | Image loading, grayscale conversion, Gaussian filtering |
| `edge_detection.py` | Canny and Sobel edge detection                          |
| `analysis.py`       | Edge statistics and contour detection                   |
| `visualization.py`  | Result and comparison image generation                  |
| `utils.py`          | Directory creation and JSON report generation           |
| `tests/`            | Automated validation of core functionality              |
