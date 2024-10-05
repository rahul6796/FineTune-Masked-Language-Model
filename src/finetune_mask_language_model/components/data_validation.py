

from src.finetune_mask_language_model.entity import DataValidationConfig
from src.finetune_mask_language_model.logging import logger
import os


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validation_files(self) -> bool:

        all_required_files  = os.listdir(os.path.join('artifacts', 'data_ingestion', 'imbd'))

        validation_status = None

        for files in all_required_files:

            if files not in self.config.ALL_FILES:

                validation_status = False
                
                with open(self.config.STATUS, 'w') as f:

                    f.write(f'Validation Status : {validation_status}')
            else:
                validation_status = True

                with open(self.config.STATUS, 'w') as f:
                
                    f.write(f'Validation Status : {validation_status}')
        
        return validation_status





