import pandas as pd
import numpy as np
import random
import os

def generate_dummy_data(num_samples=1000):
    """Generates dummy satellite image data with NDVI values."""
    data = {
        "image_id": [f"img_{i}" for i in range(num_samples)],
        "latitude": np.random.uniform(-90, 90, num_samples),
        "longitude": np.random.uniform(-180, 180, num_samples),
        "ndvi": np.random.uniform(-0.2, 0.8, num_samples)
    }
    return pd.DataFrame(data)

def classify_forest(ndvi):
    """Classify land as 'Forest' or 'Non-Forest' based on NDVI value."""
    return "Forest" if ndvi > 0.3 else "Non-Forest"

def load_data(csv_file):
    """Loads data from CSV or generates dummy data if the file does not exist."""
    if os.path.exists(csv_file):
        print(f"Loading data from {csv_file}...")
        return pd.read_csv(csv_file)
    else:
        print("CSV file not found. Generating dummy data...")
        return generate_dummy_data()

def classify_and_save(df, output_file):
    """Applies classification and saves the results to a new CSV file."""
    df["classification"] = df["ndvi"].apply(classify_forest)
    df.to_csv(output_file, index=False)
    print(f"Classification complete. Results saved to {output_file}")

def main():
    input_csv = "satellite_images.csv"
    output_csv = "classified_satellite_images.csv"
    
    df = load_data(input_csv)
    classify_and_save(df, output_csv)

if __name__ == "__main__":
    main()
