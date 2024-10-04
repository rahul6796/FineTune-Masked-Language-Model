

import os
import urllib.request as request
import zipfile
from pathlib import Path

from src.finetune_mask_language_model.entity import DataIngestionConfig
from src.finetune_mask_language_model.logging import logger



class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        try:
            
            if not os.path.exists(self.config.local_file_dir):
                filename, headers = request.urlretrieve(
                    url = self.config.source_url,
                    filename = self.config.local_file_dir
                )
                logger.info(f'{filename} download with following info : \{headers}')
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_file_dir))}")  

        except Exception as e:
            logger.error(f'error is raised from download file :: {e}')


    def extract_zip_file(self):
    
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_file_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    