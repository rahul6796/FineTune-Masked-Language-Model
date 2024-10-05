

from src.finetune_mask_language_model.config.configuration import ConfigManager
from src.finetune_mask_language_model.components.data_transformation import DataTransformation


class DataTransformationPipeline:


    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        

