import plotly.express as px

import pandas as pd
import numpy as np

df = pd.DataFrame(dict(
    x_axis = [i for i in range(50)],
    y_axis = np.random.randint(15, 20, 50)
))

fig = px.line(        
        df, #Data Frame
        x = "x_axis", #Columns from the data frame
        y = "y_axis",
        title = "Line Plot"
)

fig.show()
