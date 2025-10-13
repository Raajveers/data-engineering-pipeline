import pandas as pd
import numpy as np

def generate_data():
    data = pd.DataFrame({
        'ID': np.arange(1, 11),
        'Value': np.random.randint(1, 100, 10)
    })
    print("Generated Data:")
    print(data)

if __name__ == "__main__":
    generate_data()
