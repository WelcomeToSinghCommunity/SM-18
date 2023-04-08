# Subject Statistical Method - Experiments Repository

This repository contains the code and data for the experiments conducted as part of the Subject Statistical Method course. The experiments cover a range of statistical methods and analysis.

## Experiments

The following is a brief description of each of the 10 experiments and one MANOVA Experiment ( Separate Repository )contained in this repository :

## Code
The code for the experiments is split into 6 Colab ( .pynb ) files and 4 R files:

## Python Files

Experiment 1 - This experiment analyzes the bigmlchurn-20 dataset and performs complete EDA to find useful insights.

Libraries to be imported

```sh
import pandas as pd
import numpy as np
```

Experiment 2 - This experiment computes the measures of central tendency of 4 different datasets using Python.

Experiment 3 - This experiment analyzes the NBA leaderboard data, which was taken through a real-time API. The link to the separate repository containing the code for this experiment is provided in the readme file for this experiment.

```sh
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression as slr
```

Experiment 4 - This experiment analyzes the NHANES dataset and performs EDA to find useful insights.

```sh
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
```

Experiment 5 - This experiment performs linear regression on the IRIS dataset using Python.

```sh
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
```

Experiment 6 - This experiment performs multiple regression on the Titanic and Carprice datasets, and multivariate regression on the Carprice dataset using Python.

```sh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
```


## R Files

The R experiments require the following packages to be installed:

```sh
 - tidyverse
 - dplyr
 - ggplot2
 - tidyr
```

Experiment 7 - This experiment demonstrates how to plot boxplots using R and RStudio.

Experiment 8 - This experiment demonstrates how to plot various graphs in R, such as histograms, ogive curves, and polygon curves.

Experiment 9 - This experiment performs linear regression on the IRIS dataset using R.

Experiment 10 - This experiment demonstrates how to compute skewness and kurtosis with and without using the inbuilt function in R.

## MANOVA EXPERIMENT

In this Experiment , we will demonstrate that different plant growth products lead to significantly different plant growth.

Therefore, we will have three treatments:

 - Treatment 1 (Control, No Product)
 - Treatment 2 (product 1)
 - Treatment 3 (product 2)
 
We will use three measurements for defining plant growth:

 - Height of the plant
 - Width of the plant
 - Weight of the plant

## Data

The data for the experiments is contained in the data folder. Each experiment has its own data file in CSV format.

## Running the Experiments

To run an experiment, simply run the relevant Python or R file. Before running, ensure that all necessary packages and libraries are installed.

## Contributors

This repository was created by Kishan Singh, with contributions from Chirag Devgade and Pratham Bagora.

## PLUGINS

| Plugin | README |
| ------ | ------ |
| LICENSE | [https://github.com/WelcomeToSinghCommunity/SM-18/blob/master/LICENSE] |
