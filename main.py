from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'DATA_INGESTION_STAGE'


try:
    logger.info(f"**********************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


try:
        logger.info(f"**********************")
        logger.info(f">>>>>>  stage {STAGE_NAME} stared <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  stage {STAGE_NAME} completed <<<<<<\n\nx=======x")
except Exception as e:
    
    logger.exception(e)
    raise e
