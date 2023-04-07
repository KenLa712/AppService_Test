import pandas as pd
from random import randrange
import numpy as np
class DataCreator():
    def __init__(self, number : int):
        self.number = number,
        self.df = None

    def create_random_df(self):

        # Set the random seed for reproducibility
        np.random.seed(self.number)

        # Generate the random dataframe
        data = np.random.randint(0, 101, size=(1000, 5))
        self.df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])

        # Return DF
        print(self.df)
