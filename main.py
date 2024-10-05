

from src.finetune_mask_language_model.logging import logger 
from src.finetune_mask_language_model.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetune_mask_language_model.pipeline.data_validation_pipeline import DataValidationPipeline
from src.finetune_mask_language_model.pipeline.data_transformation_pipeline import DataTransformationPipeline



STAGE_STATE = "data ingestion"

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f"Data ingestion stage completed successfully. Stage state: {STAGE_STATE}")
except Exception as e:
    logger.error(f"Error in {STAGE_STATE}: {str(e)}")


STAGE_STATE = "data validation"

try:
    data_validation = DataValidationPipeline()
    data_validation.run()
    logger.info(f"Data ingestion stage completed successfully. Stage state: {STAGE_STATE}")
except Exception as e:
    logger.error(f"Error in {STAGE_STATE}: {str(e)}")



STAGE_STATE = "data transformation"


try:
    data_transformation = DataTransformationPipeline()
    data_transformation.run()
    logger.info(f"Data ingestion stage completed successfully. Stage state: {STAGE_STATE}")
except Exception as e:
    logger.error(f"Error in {STAGE_STATE}: {str(e)}")
