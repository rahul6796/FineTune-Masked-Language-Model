

from src.finetune_mask_language_model.constant import CONFIG_FILE, PARAMS_FILE
from src.finetune_mask_language_model.utils.common import read_yaml, create_directories
from src.finetune_mask_language_model.entity import DataIngestionConfig, DataValidationConfig
from src.finetune_mask_language_model.entity import DataTransformationConfig



class ConfigManager:

    def __init__(self, config_file = CONFIG_FILE, params_file = PARAMS_FILE):

        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)

        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_file_dir=config.local_file_dir,
            unzip_dir = config.unzip_dir,
        )
        return data_ingestion_config

    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            ALL_FILES = config.ALL_FILES,
            STATUS = config.STATUS)


        return data_validation_config


    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer = config.tokenizer
        )
    
        return data_transformation_config







        


