

from src.finetune_mask_language_model.config.configuration import ConfigManager
from src.finetune_mask_language_model.components.data_validation import DataValidation


class DataValidationPipeline:

    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validation_files()


