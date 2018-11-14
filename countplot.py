import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)
plt.show()
