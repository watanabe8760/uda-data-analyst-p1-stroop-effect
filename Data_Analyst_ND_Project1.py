import pandas as pd
import numpy as np
from scipy import stats
from ggplot import *

stroop = pd.read_csv('stroopdata.csv')
stroop['difference'] = stroop.Incongruent - stroop.Congruent
stroop.mean()
stroop.var()
stroop.std()
stroop.describe()

# Standard error of the mean
stroop.std() / np.sqrt(stroop.count())


# Exploratory analysis
stroop.hist(sharex=True, sharey=True, figsize=(10, 3), layout=(1, 3))
qplot(stroop.difference)
ggplot(stroop, aes(x='difference')) + geom_histogram()


# Normality check
stats.anderson(stroop.Congruent, dist='norm')
stats.anderson(stroop.Incongruent, dist='norm')
stats.anderson(stroop.difference, dist='norm')


# T-test (manual)
SE = stroop.difference.std() / np.sqrt(stroop.difference.count())
stroop.difference.mean() / SE


# T-test from scipy
stats.ttest_rel(stroop.Incongruent, stroop.Congruent)

