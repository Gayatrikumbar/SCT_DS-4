import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/sobhan-moosavi/U.S.-Accidents/main/US_Accidents_Dec21_updated.csv"
data = pd.read_csv(url)

print(data.head())

data = data.dropna(subset=['Start_Time', 'Weather_Condition', 'Road_Condition', 'Severity', 'City', 'State'])


data['Start_Time'] = pd.to_datetime(data['Start_Time'])
data['Hour'] = data['Start_Time'].dt.hour
data['Day_of_Week'] = data['Start_Time'].dt.dayofweek


plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=data)
plt.title("Accidents by Hour of the Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Accidents")
plt.show()


plt.figure(figsize=(10, 5))
sns.countplot(x='Day_of_Week', data=data)
plt.title("Accidents by Day of the Week")
plt.xlabel("Day of the Week (0=Monday, 6=Sunday)")
plt.ylabel("Number of Accidents")
plt.show()


top_cities = data['City'].value_counts().head(10).index
city_data = data[data['City'].isin(top_cities)]
plt.figure(figsize=(12, 6))
sns.countplot(x='City', data=city_data, order=top_cities)
plt.title("Top 10 Cities with the Most Accidents")
plt.xlabel("City")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Condition', data=data, order=data['Weather_Condition'].value_counts().head(10).index)
plt.title("Top 10 Weather Conditions During Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='Road_Condition', data=data, order=data['Road_Condition'].value_counts().head(10).index)
plt.title("Top 10 Road Conditions During Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Road Condition")
plt.show()
