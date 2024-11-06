import os
import kagglehub

# Get the Kaggle API credentials path from the environment variable
kaggle_config_dir = os.getenv("KAGGLE_CONFIG_DIR")
if kaggle_config_dir:
    os.environ["KAGGLE_CONFIG_DIR"] = kaggle_config_dir
else:
    raise ValueError("KAGGLE_CONFIG_DIR environment variable is not set.")

# Download latest version
dataset_path = kagglehub.dataset_download("arhamrumi/amazon-product-reviews", "data")
print("Path to dataset files:", dataset_path)