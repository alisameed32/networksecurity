from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPiplineConfig


if __name__ == "__main__":
    training_pipeline_config = TrainingPiplineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    artifact = data_ingestion.initiate_data_ingestion()
    print(artifact)