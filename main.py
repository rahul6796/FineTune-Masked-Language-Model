

from src.finetune_mask_language_model.logging import logger 
from src.finetune_mask_language_model.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_STATE = "data ingestion"

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f"Data ingestion stage completed successfully. Stage state: {STAGE_STATE}")
except Exception as e:
    logger.error(f"Error in {STAGE_STATE}: {str(e)}")
