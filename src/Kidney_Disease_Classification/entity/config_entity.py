# entity = return type of data ingestion function
from dataclasses import dataclass
from pathlib import Path 

# everything from config.yml return heare as a variable
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str 
    local_data_file: Path 
    unzip_dir: Path 