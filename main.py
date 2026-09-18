import argparse
import os

from edgevision.preprocessing import (
    load_image,
    convert_to_grayscale,
    apply_gaussian_blur
)

from edgevision.edge_detection import (
    detect_canny_edges,
    detect_sobel_edges
)

from edgevision.analysis import generate_analysis

from edgevision.visualization import (
    save_image,
    create_comparison
)

from edgevision.utils import (
    ensure_directory,
    save_json
)


def parse_arguments():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="EdgeVision - Image Edge Detection and Analysis Toolkit"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--method",
        choices=["canny", "sobel", "compare"],
        default="canny",
        help="Edge detection method"
    )

    parser.add_argument(
        "--lower",
        type=int,
        default=100,
        help="Lower threshold for Canny detection"
    )

    parser.add_argument(
        "--upper",
        type=int,
        default=200,
        help="Upper threshold for Canny detection"
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Output directory"
    )

    return parser.parse_args()


def main():
    """Run the EdgeVision pipeline."""

    args = parse_arguments()

    ensure_directory(args.output)

    print("\n" + "=" * 45)
    print("           EDGEVISION")
    print(" Image Edge Detection & Analysis Toolkit")
    print("=" * 45)

    print(f"\nInput image: {args.input}")
    print(f"Method: {args.method}")

    # Step 1: Load image
    image = load_image(args.input)
    print("[✓] Image loaded")

    # Step 2: Preprocessing
    grayscale = convert_to_grayscale(image)
    print("[✓] Converted to grayscale")

    blurred = apply_gaussian_blur(grayscale)
    print("[✓] Gaussian filtering applied")

    base_name = os.path.splitext(
        os.path.basename(args.input)
    )[0]

    # Step 3: Edge detection
    if args.method == "canny":

        edges = detect_canny_edges(
            blurred,
            args.lower,
            args.upper
        )

        method_name = "Canny"

    elif args.method == "sobel":

        edges = detect_sobel_edges(blurred)

        method_name = "Sobel"

    else:

        canny_edges = detect_canny_edges(
            blurred,
            args.lower,
            args.upper
        )

        sobel_edges = detect_sobel_edges(blurred)

        method_name = "Comparison"

        save_image(
            canny_edges,
            os.path.join(
                args.output,
                f"{base_name}_canny.png"
            )
        )

        save_image(
            sobel_edges,
            os.path.join(
                args.output,
                f"{base_name}_sobel.png"
            )
        )

        create_comparison(
            image,
            canny_edges,
            os.path.join(
                args.output,
                f"{base_name}_canny_comparison.png"
            ),
            "Original Image",
            "Canny Edges"
        )

        create_comparison(
            image,
            sobel_edges,
            os.path.join(
                args.output,
                f"{base_name}_sobel_comparison.png"
            ),
            "Original Image",
            "Sobel Edges"
        )

        # Analyze both methods
        canny_analysis = generate_analysis(canny_edges)
        sobel_analysis = generate_analysis(sobel_edges)

        report = {
            "input_image": args.input,
            "method": method_name,
            "canny": canny_analysis,
            "sobel": sobel_analysis
        }

        save_json(
            report,
            os.path.join(
                args.output,
                f"{base_name}_comparison_report.json"
            )
        )

        print("[✓] Canny and Sobel processing completed")

        print("\nResults:")
        print(
            f"Canny edge density: "
            f"{canny_analysis['edge_density_percent']}%"
        )
        print(
            f"Sobel edge density: "
            f"{sobel_analysis['edge_density_percent']}%"
        )

        print("\n[✓] Results saved successfully")
        return

    print(f"[✓] {method_name} edge detection completed")

    # Step 4: Analysis
    analysis = generate_analysis(edges)
    print("[✓] Edge analysis completed")

    # Step 5: Save results
    edge_output = os.path.join(
        args.output,
        f"{base_name}_{args.method}.png"
    )

    comparison_output = os.path.join(
        args.output,
        f"{base_name}_{args.method}_comparison.png"
    )

    report_output = os.path.join(
        args.output,
        f"{base_name}_{args.method}_report.json"
    )

    save_image(edges, edge_output)

    create_comparison(
        image,
        edges,
        comparison_output,
        "Original Image",
        f"{method_name} Edges"
    )

    report = {
        "input_image": args.input,
        "method": method_name,
        "analysis": analysis
    }

    save_json(report, report_output)

    # Step 6: Display summary
    print("\n" + "-" * 45)
    print("              RESULTS")
    print("-" * 45)

    print(
        f"Image size       : "
        f"{analysis['image_width']} x "
        f"{analysis['image_height']}"
    )

    print(
        f"Edge pixels      : "
        f"{analysis['edge_pixels']}"
    )

    print(
        f"Edge density     : "
        f"{analysis['edge_density_percent']}%"
    )

    print(
        f"Contours detected: "
        f"{analysis['contours_detected']}"
    )

    print("-" * 45)
    print(f"Edge image       : {edge_output}")
    print(f"Comparison       : {comparison_output}")
    print(f"Report           : {report_output}")
    print("\n[✓] Processing completed successfully!")


if __name__ == "__main__":
    main()