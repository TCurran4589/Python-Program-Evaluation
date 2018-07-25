import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import manksi

np.random.normal(0, 100, 10000)

dataFrame = pd.DataFrame({"treatment_status" : np.random.randint(0,2,100000),
                          "before" : np.random.normal(50,25,100000),
                          "after": np.random.normal(50,25,100000)
                          })


manski = manski.manski_bounds(treatment_status = dataFrame.treatment_status,
                              before = dataFrame.before,
                              after = dataFrame.after,
                              graph = True)
