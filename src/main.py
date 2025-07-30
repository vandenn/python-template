import numpy as np
import pandas as pd

from src.settings import settings

if __name__ == "__main__":
    print("Hello world!")

    x = pd.Series([1, 2, 3, np.nan])
    print(x)

    print(f"Dummy Env Var: {settings.dummy_env_var}")
