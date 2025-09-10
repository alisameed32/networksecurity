from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPiplineConfig, DataValidationConfig, DataTransformationConfig


if __name__ == "__main__":
    training_pipeline_config = TrainingPiplineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    logging.info("Initiate the data ingestion")
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    logging.info("Data Initiation Completed")
    print(data_ingestion_artifact)
    data_validation_config = DataValidationConfig(training_pipeline_config)
    data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
    logging.info("Initiate the data Validation")
    data_validation_artifact = data_validation.initiate_data_validation()
    logging.info("data Validation Completed")
    print(data_validation_artifact)
    data_transformation_config = DataTransformationConfig(training_pipeline_config)
    logging.info("data Transformation started")
    data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    print(data_transformation_artifact)
    logging.info("data Transformation completed")
    

    