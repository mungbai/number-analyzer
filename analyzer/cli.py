import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Number Analyzer")
    parser.add_argument('min', type=int, help='Minimum number (inclusive)')
    parser.add_argument('max', type=int, help='Maximum number (inclusive)')
    return parser.parse_args()
