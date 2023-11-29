import os
import pandas as pd
import matplotlib.pyplot as plt

def create_plot():
    # Read data from CSV
    df = pd.read_csv('input/strong.csv')

    # Example plot (modify according to your data)
    plt.figure()
    df.plot()  # Replace with your own plotting logic
    plt.title('Sample Plot')

    # Ensure the output directory exists
    os.makedirs('output/images', exist_ok=True)

    # Save plot to the images folder
    plt.savefig('output/images/sample_plot.jpg', format='jpg')

if __name__ == "__main__":
    create_plot()

