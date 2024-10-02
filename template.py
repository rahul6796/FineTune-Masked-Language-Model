

import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

project_name = 'finetune_mask_language_model'


list_of_files = [
    '.github/wrokflow/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/contant/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/logging/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'requirements.txt',
    'app.py',
    'main.py',
    'Dockerfile'
]


for filepath in list_of_files:
    # convert the all filename to filepath
    filepath = Path(filepath)

    # split the filepath into the filename, filedir

    filedir, filename = os.path.split(filepath)
    # print(filedir, '-----', filename)

    if filedir != "":

        os.makedirs(filedir, exist_ok = True)
        logging.info(f'creating directory: {filedir} for the file name : {filename}')

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass

        logging.info(f'created empty file : {filepath}')

    else:
        logging.info(f'file already exist of filename :: {filename}')















