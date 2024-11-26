"""
Number Analyzer Main Module

This is the main entry point for the Number Analyzer application.
It handles command-line arguments and orchestrates the analysis process.

Usage:
    python -m analyzer.main [min_value] [max_value] [-o output_file]
    
Example:
    python -m analyzer.main 1 20
    This will analyze numbers from 1 to 20 and print results to console
    
    python -m analyzer.main 1 1000 -o results.rtf
    This will analyze numbers from 1 to 1000 and save results to results.rtf
"""

import sys
import json
from pathlib import Path
from .cli import parse_arguments
from .config_loader import load_config
from .number_analyzer import NumberAnalyzer


def load_config():
    """
    Load the configuration from analyzer-config.json file.
    
    The configuration file should be in the root directory of the project
    and contain category definitions.
    
    Returns:
        dict: The configuration dictionary containing category definitions
        
    Raises:
        FileNotFoundError: If analyzer-config.json doesn't exist
        json.JSONDecodeError: If the config file contains invalid JSON
    """
    config_path = Path(__file__).parent.parent / 'analyzer-config.json'
    try:
        with open(config_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {e}")
        sys.exit(1)


def main():
    """
    Main entry point for the Number Analyzer application.
    
    This function:
    1. Loads the configuration
    2. Parses command-line arguments
    3. Creates a NumberAnalyzer instance
    4. Runs the analysis on the specified range
    5. Handles output (console or file)
    
    Any errors during execution will result in an appropriate error message
    and a non-zero exit code.
    """
    try:
        # Parse arguments and load config
        args = parse_arguments()
        config = load_config()
        
        # Create and run analyzer
        analyzer = NumberAnalyzer(config)
        
        # If output file is specified, save directly to file
        if args.output:
            filepath = analyzer.save_to_rtf(args.min, args.max, args.output)
            print(f"Results saved to: {filepath}")
        else:
            # Otherwise, let the run method handle console output
            # and potential file output for large ranges
            analyzer.run(args.min, args.max)
            
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
