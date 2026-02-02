#!/usr/bin/env python3
"""
Sample workflow script for Cinderflow.
This script demonstrates a simple workflow that processes data and produces outputs.
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
    logger.info("Cinderflow Sample Workflow")
    logger.info("=" * 60)
    
    # Read parameters from environment variables
    # Parameters are passed as ALTAI_PARAM_<KEY> (uppercase)
    message = os.environ.get("ALTAI_PARAM_MESSAGE", "Hello from Cinderflow")
    iterations = int(os.environ.get("ALTAI_PARAM_ITERATIONS", "5"))
    
    logger.info("\nParameters:")
    logger.info(f"  Message: {message}")
    logger.info(f"  Iterations: {iterations}")
    
    # Ensure output directory exists
    output_dir = Path("/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process data
    logger.info("\nProcessing data...")
    results = []
    for i in range(iterations):
        result = {
            "iteration": i + 1,
            "message": f"{message} - Iteration {i + 1}",
            "value": (i + 1) * 10
        }
        results.append(result)
        logger.info(f"  Iteration {i + 1}: {result['message']}")
    
    # Write output artifact
    output_file = output_dir / "results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"\nOutput written to: {output_file}")
    logger.info(f"Total results: {len(results)}")
    
    # Create a summary file
    summary_file = output_dir / "summary.txt"
    with open(summary_file, "w") as f:
        f.write("Workflow completed successfully\n")
        f.write(f"Message: {message}\n")
        f.write(f"Iterations: {iterations}\n")
        f.write(f"Results: {len(results)}\n")
    
    logger.info("Summary written to: %s", summary_file)
    logger.info("\n" + "=" * 60)
    logger.info("Workflow completed successfully!")
    logger.info("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
