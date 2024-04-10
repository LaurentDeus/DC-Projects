import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

world_happiness = pd.read_csv('./datasets/world_happiness.csv')


# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)

# Show plot
plt.show()


# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x="life_exp", y="happiness_score", data=world_happiness, ci=None)

plt.show()


# Correlation between life_exp and happiness_score
cor = world_happiness.life_exp.corr(world_happiness.happiness_score)
print(cor)

# Vibrant visualizations! Scatterplots with trendlines are a great way to verify that a relationship 
# between two variables is indeed linear.




# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap',y='life_exp',data=world_happiness)

# Show plot
plt.show()


# Correlation between gdp_per_cap and life_exp
cor = world_happiness.gdp_per_cap.corr(world_happiness.life_exp)

# Correct! The correlation coefficient can't account for any relationships that aren't linear, 
# regardless of strength.