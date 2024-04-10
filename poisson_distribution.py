# Amir responds to 4 leads each day. In this exercise, 
# you'll calculate probabilities of Amir responding to different numbers of leads.

# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5,4) #lambda = 4 , P(x=5)=pmf(x,lambda)

print(prob_5)

# Amir's coworker responds to an average of 5.5 leads per day. 
# What is the probability that she answers 5 leads in a day?


# Probability of 5 responses
prob_coworker = poisson.pmf(5,5.5)

print(prob_coworker)

# What's the probability that Amir responds to 2 or fewer leads in a day?
prob_coworker = poisson.pmf(5,5.5)


# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2,4) #Here We use cumulative distr Function passing X and Lambda P(X<2), Lambda = 4
print(prob_2_or_less)

# What's the probability that Amir responds to more than 10 leads in a day?
# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10,4)
print(prob_over_10)

# Perfect Poisson probabilities! Note that if you provide poisson.pmf() or poisson.cdf() with a non-integer, 
# it throws an error since the Poisson distribution only applies to integers.
