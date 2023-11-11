import numpy as np
import pandas as pd

file_path = ""

def score_fitness (data: np.array) -> tuple:
    data = pd.read_csv(file_path)
