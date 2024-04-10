import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Set seed to 104
np.random.seed(104)


amir_deals = pd.read_csv('./datasets/amir_deals.csv')
all_deals = pd.read_csv('./datasets/amir_deals.csv')


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


# The mean of means
# You want to know what the average number of users (num_users) is per deal,
# but you want to know this number for the entire company so that 
# you can see if Amir's deals have more or fewer users than the company's average deal. 
# The problem is that over the past year, the company has worked on more than ten thousand deals,
# so it's not realistic to compile all the data. 
# Instead, you'll estimate the mean by taking several random samples of deals, 
# since this is much easier than collecting data from everyone in the company.

# amir_deals is available and the user data for all the company's deals is available in all_deals. 
# Both pandas as pd and numpy as np are loaded.

# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20,replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))


# Magnificent mean calculation! 
# Amir's average number of users is very close to the overall average, 
# so it looks like he's meeting expectations. Make sure to note this in his performance review!
