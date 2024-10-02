import os

from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import yaml
import json

from src.finetune_mask_language_model.logging import logger



@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")



@ensure_annotations
def create_directories(path_of_directories: list, verbose = True):
    try:
        for path in path_of_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created: {path}")
    except Exception as e:
        logger.error(f"Error creating directories: {e}")


