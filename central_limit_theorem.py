import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Set seed to 104
np.random.seed(104)


amir_deals = pd.read_csv('./datasets/amir_deals.csv')

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()

# Fabulous job! You've just seen the central limit thorem at work. 
# Even though the distribution of num_users is not normal, the distribution of its sample means resembles the normal distribution.