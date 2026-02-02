#!/usr/bin/env python3
"""
Process results from previous step.
This script reads the results.json artifact and generates a summary report.
"""

import os
import sys
import json
import logging
from pathlib import Path

# Configure logging to output to stdout/stderr (visible in docker logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("Cinderflow Results Processor")
    logger.info("=" * 60)
    
    # Read parameters from environment variables
    report_type = os.environ.get("ALTAI_PARAM_REPORT_TYPE", "summary")
    output_format = os.environ.get("ALTAI_PARAM_OUTPUT_FORMAT", "json")
    
    logger.info("\nParameters:")
    logger.info(f"  Report Type: {report_type}")
    logger.info(f"  Output Format: {output_format}")
    
    # Read input artifact from step1
    # Input artifacts are mounted at /inputs/{producer}/{artifact_name}
    input_results_path = Path("/inputs/process/results.json")
    
    if not input_results_path.exists():
        logger.error(f"Input artifact not found at {input_results_path}")
        logger.info("Available inputs:")
        inputs_dir = Path("/inputs")
        if inputs_dir.exists():
            for item in inputs_dir.rglob("*"):
                if item.is_file():
                    logger.info(f"  {item}")
        sys.exit(1)
    
    logger.info(f"\nReading input artifact from: {input_results_path}")
    with open(input_results_path, "r") as f:
        results_data = json.load(f)
    
    logger.info(f"Loaded {len(results_data)} results from previous step")
    
    # Process the results
    total_value = sum(item.get("value", 0) for item in results_data)
    avg_value = total_value / len(results_data) if results_data else 0
    messages = [item.get("message", "") for item in results_data]
    
    logger.info(f"\nProcessing results...")
    logger.info(f"  Total value: {total_value}")
    logger.info(f"  Average value: {avg_value:.2f}")
    logger.info(f"  Number of iterations: {len(results_data)}")
    
    # Generate report based on report_type
    report = {
        "report_type": report_type,
        "summary": {
            "total_iterations": len(results_data),
            "total_value": total_value,
            "average_value": avg_value,
            "first_message": messages[0] if messages else "",
            "last_message": messages[-1] if messages else "",
        },
        "processed_at": str(Path(input_results_path).stat().st_mtime),
    }
    
    # Ensure output directory exists
    output_dir = Path("/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write output based on format
    if output_format == "json":
        output_file = output_dir / "report.json"
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)
        logger.info(f"\nReport written to: {output_file}")
    elif output_format == "text":
        output_file = output_dir / "report.txt"
        with open(output_file, "w") as f:
            f.write(f"Results Processing Report\n")
            f.write(f"{'=' * 60}\n")
            f.write(f"Report Type: {report_type}\n")
            f.write(f"Total Iterations: {report['summary']['total_iterations']}\n")
            f.write(f"Total Value: {report['summary']['total_value']}\n")
            f.write(f"Average Value: {report['summary']['average_value']:.2f}\n")
            f.write(f"First Message: {report['summary']['first_message']}\n")
            f.write(f"Last Message: {report['summary']['last_message']}\n")
        logger.info(f"\nReport written to: {output_file}")
    else:
        logger.error(f"Unknown output format: {output_format}")
        sys.exit(1)
    
    # Also create a statistics file
    stats_file = output_dir / "statistics.json"
    stats = {
        "total_items": len(results_data),
        "total_value": total_value,
        "average_value": avg_value,
        "min_value": min(item.get("value", 0) for item in results_data) if results_data else 0,
        "max_value": max(item.get("value", 0) for item in results_data) if results_data else 0,
    }
    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=2)
    
    logger.info(f"Statistics written to: {stats_file}")
    logger.info("\n" + "=" * 60)
    logger.info("Results processing completed successfully!")
    logger.info("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
