# Cinderflow Sample Workflow

This is a sample repository for testing Cinderflow workflows with GitHub-hosted repositories.

## Structure

- `main.py`: Main workflow script that processes data and produces outputs
- `process_results.py`: Script to process and analyze results from previous steps
- `Dockerfile`: Docker image definition for the workflow

## Usage

This repository is designed to be used with Cinderflow workflows. The workflow will:

1. Clone this repository
2. Build a Docker image from the Dockerfile
3. Run the container with the specified parameters
4. Collect outputs from `/outputs` directory

## Scripts

### main.py

Main workflow script that processes data and produces outputs.

**Parameters:**
- `ALTAI_PARAM_MESSAGE`: Custom message to process (default: "Hello from Cinderflow")
- `ALTAI_PARAM_ITERATIONS`: Number of iterations to run (default: 5)

**Outputs:**
- `results.json`: JSON file containing iteration results
- `summary.txt`: Text summary of the workflow execution

### process_results.py

Processes results from previous workflow steps.

**Parameters:**
- `ALTAI_PARAM_REPORT_TYPE`: Type of report to generate (default: "summary")
- `ALTAI_PARAM_OUTPUT_FORMAT`: Output format - "json" or "text" (default: "json")

**Inputs:**
- Reads from `/inputs/process/results.json` (artifact from previous step)

**Outputs:**
- `report.json` or `report.txt`: Processed report based on output format
- `statistics.json`: Statistical analysis of the results
