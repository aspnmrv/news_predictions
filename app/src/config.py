import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"


# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
classificator_model_ru = config_yaml["CLASSIFICATOR_MODEL_RU"]
summarize_model_ru = config_yaml["SUMMARIZE_MODEL_RU"]
