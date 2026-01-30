#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("country_wise_latest.csv")
print(df.head())


# In[2]:


import pandas as pd
df = pd.read_csv("country_wise_latest.csv")
print(df.tail())


# In[3]:


import pandas as pd
df = pd.read_csv("country_wise_latest.csv")
print(df.info)


# In[8]:


import pandas as pd
df = pd.read_csv("country_wise_latest.csv")
print(df.shape)


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("country_wise_latest.csv")

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
most_deaths_country = (
        dataset[dataset['Country/Region'] == '']
    .count()
    .sort_values(ascending=False)
    .head(10)
)
axs[0, 0].bar(most_deaths_country.index, most_deaths_country)
axs[0, 0].set_title("Most deaths in the country/Region")
axs[0, 0].tick_params(axis='x', rotation=45)
                       


# In[14]:


plt.tight_layout()
plt.show()


# In[4]:


import pandas as pd
df = pd.read_csv("country_wise_latest.csv")
print(df.describe)


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataset = pd.read_csv("country_wise_latest.csv")
sns.countplot(x='Deaths', data=dataset)
plt.show


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("country_wise_latest.csv")
dataset.groupby('Country/Region')['Deaths'].sum().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 Countries most deaths')

plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("country_wise_latest.csv")

Active_cases = dataset ['Country/Region'].value_counts()
Active_cases.plot(kind='line') 
Active_cases.plot.line()
autopct='%1.1f%%', 
startangle=90,
# colors =['skyblue','green'])
plt.title =("Active_cases In Countries")
plt.show()


# In[35]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("country_wise_latest.csv")
top10 = df.sort_values(by="Confirmed", ascending=False).head(10)

plt.bar(top10["Country/Region"], top10["Confirmed"])
plt.xticks(rotation=45)
# plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.show()


# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("country_wise_latest.csv")

# Keep only needed columns and drop missing rows
plot_df = df[["Confirmed", "Deaths"]].dropna()

x = plot_df["Confirmed"]
y = plot_df["Deaths"]

plt.scatter(x, y)
plt.xlabel("Confirmed")
plt.ylabel("Deaths")
# plt.title("Confirmed vs Deaths")
plt.show()

plt.show()


# In[39]:


import seaborn as sns
import pandas as pd
corr = df[["Confirmed","Deaths","Recovered","Active"]].corr()
sns.heatmap(corr , annot =True)
# plt.title(("Correlation Heatmap"))
plt.show()


# In[41]:


import pandas as pd
import seaborn as sns

india = df[df["Country/Region"] == "India"]

values = [india["Confirmed"].values[0],
          india["Deaths"].values[0],
          india["Recovered"].values[0]]

labels = ["Confirmed", "Deaths", "Recovered"]

plt.bar(labels, values)
# plt.title("India COVID Summary")
plt.show()


# In[ ]:




