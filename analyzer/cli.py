"""
Command Line Interface Module

This module handles the command-line interface for the Number Analyzer application.
It provides argument parsing and validation for the min and max values that define
the range of numbers to analyze.

Example:
    python -m analyzer.main 1 100
    This command will analyze numbers from 1 to 100.
"""

import argparse
from .number_analyzer import NumberAnalyzer


def parse_arguments():
    """
    Parse and validate command-line arguments using argparse.
    
    This function sets up the argument parser with the following arguments:
    - min: The minimum value of the range to analyze
    - max: The maximum value of the range to analyze
    - output: Optional output file path for saving results
    
    Returns:
        argparse.Namespace: An object containing the parsed arguments
            - min (int): The minimum value to analyze
            - max (int): The maximum value to analyze
            - output (str, optional): Path to save results
            
    Example:
        >>> args = parse_arguments()
        >>> print(args.min, args.max)
        1 100
    """
    parser = argparse.ArgumentParser(
        description=(
            "Analyze numbers within a range based on configurable categories.\n"
            f"Valid range: {NumberAnalyzer.MIN_VALUE} to {NumberAnalyzer.MAX_VALUE}"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Add arguments for the minimum and maximum values
    parser.add_argument(
        "min",
        type=int,
        help=f"The minimum value of the range to analyze (>= {NumberAnalyzer.MIN_VALUE})"
    )
    
    parser.add_argument(
        "max",
        type=int,
        help=f"The maximum value of the range to analyze (<= {NumberAnalyzer.MAX_VALUE})"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Save results to this RTF file instead of printing to console"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Basic validation of the range
    if args.min < NumberAnalyzer.MIN_VALUE or args.max > NumberAnalyzer.MAX_VALUE:
        parser.error(
            f"Values must be between {NumberAnalyzer.MIN_VALUE} "
            f"and {NumberAnalyzer.MAX_VALUE}"
        )
    
    if args.min >= args.max:
        parser.error("Minimum value must be less than maximum value")
    
    return args
