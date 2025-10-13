import os
import pandas as pd
from scripts.data_processing import generate_data

def test_generate_data_creates_file():
    output_file = 'output/data.csv'
    
    # Remove file if exists before test
    if os.path.exists(output_file):
        os.remove(output_file)
    
    generate_data()
    
    # Check file exists
    assert os.path.isfile(output_file), "Output CSV file was not created"
    
    # Read the file and check data shape and columns
    data = pd.read_csv(output_file)
    assert data.shape[0] == 10, "Data does not have 10 rows"
    assert 'ID' in data.columns and 'Value' in data.columns, "Expected columns missing"

