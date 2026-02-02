# Cinderflow Sample Workflow

This is a sample repository for testing Cinderflow workflows with GitHub-hosted repositories.

## Structure

- `main.py`: Main workflow script that processes data and produces outputs
- `Dockerfile`: Docker image definition for the workflow

## Usage

This repository is designed to be used with Cinderflow workflows. The workflow will:

1. Clone this repository
2. Build a Docker image from the Dockerfile
3. Run the container with the specified parameters
4. Collect outputs from `/outputs` directory

## Parameters

The workflow accepts the following parameters (via environment variables):

- `ALTAI_PARAM_MESSAGE`: Custom message to process (default: "Hello from Cinderflow")
- `ALTAI_PARAM_ITERATIONS`: Number of iterations to run (default: 5)

## Outputs

The workflow produces:

- `results.json`: JSON file containing iteration results
- `summary.txt`: Text summary of the workflow execution
