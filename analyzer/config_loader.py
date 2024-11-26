"""
Configuration Loader Module

This module handles loading and validating the configuration file for the Number Analyzer.
The configuration file (analyzer-config.json) defines the categories and rules for
analyzing numbers.

Example Configuration:
{
    "categories": [
        {
            "label": "Even",
            "rule": "even"
        },
        {
            "label": "DivBy3",
            "rule": "lambda x: x % 3 == 0"
        }
    ]
}
"""

import json
import os
from pathlib import Path


def load_config(config_file='analyzer-config.json'):
    """
    Load and validate the configuration from a JSON file.
    
    The configuration file should contain a list of categories, where each category
    has a label and a rule. Rules can be predefined ('even', 'odd', 'prime') or
    custom lambda expressions.
    
    Args:
        config_file (str): Path to the configuration file, relative to the project root
            Defaults to 'analyzer-config.json'
            
    Returns:
        dict: The validated configuration dictionary
        
    Raises:
        FileNotFoundError: If the configuration file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        ValueError: If the configuration format is invalid
        
    Example:
        >>> config = load_config()
        >>> print(config['categories'][0]['label'])
        'Even'
    """
    # Find the project root directory (where analyzer-config.json should be)
    project_root = Path(__file__).parent.parent
    config_path = project_root / config_file
    
    # Load and parse the JSON file
    try:
        with open(config_path) as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in configuration file: {e}")
        
    # Validate the configuration structure
    if not isinstance(config, dict) or 'categories' not in config:
        raise ValueError("Configuration must contain a 'categories' key")
        
    if not isinstance(config['categories'], list):
        raise ValueError("'categories' must be a list")
        
    # Validate each category
    for category in config['categories']:
        if not isinstance(category, dict):
            raise ValueError("Each category must be a dictionary")
            
        if 'label' not in category or 'rule' not in category:
            raise ValueError("Each category must have 'label' and 'rule' keys")
            
        if not isinstance(category['label'], str) or not isinstance(category['rule'], str):
            raise ValueError("Category 'label' and 'rule' must be strings")
    
    return config
