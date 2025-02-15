import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("hotel_bookings 2.csv")  
print(df.head())
print(df.tail())

print(df.shape)

print(df.columns.tolist())


df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])
df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"], format="%d/%m/%Y")

print(df.info())

print(df.describe(include="object"))

for col in df.describe(include="object").columns:
    print(col)
    print(df[col].unique())


print(df.isnull().sum())

df.drop(["company","agent"],axis=1,inplace=True)
df.dropna(inplace=True)
print(df.isnull().sum())

print(df.describe())

df["adr"].plot(kind="box")
plt.show()

df=df[df["adr"]<5000]


#data Analysis and Visualization

cancelled_per=df["is_canceled"].value_counts(normalize=True)

print(cancelled_per)
plt.figure(figsize=(5,4))
plt.title("reservation status count")
plt.bar(["Not canceled","canceled"],df["is_canceled"].value_counts())
plt.show()






plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x="hotel", hue="is_canceled", data=df, palette="Blues")


handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, title="Cancellation Status")
plt.title("reservation status in different hotels",size=20)
plt.xlabel("hotels")
plt.ylabel("number of reservation ")
plt.show()




# Filter data for resort and city hotels
resort_hotel = df[df["hotel"] == "Resort Hotel"]
city_hotels = df[df["hotel"] == "City Hotel"]

# Compute cancellation rates
resort_cancellation_rate = resort_hotel["is_canceled"].value_counts(normalize=True)
city_cancellation_rate = city_hotels["is_canceled"].value_counts(normalize=True)

print("Resort Hotel Cancellation Rates:\n", resort_cancellation_rate)
print("City Hotel Cancellation Rates:\n", city_cancellation_rate)

# Group by reservation status date and compute average daily rate (ADR)
resort_hotel = resort_hotel.groupby("reservation_status_date")[["adr"]].mean()
city_hotels = city_hotels.groupby("reservation_status_date")[["adr"]].mean()

# Print the first few rows to check
print(resort_hotel.head())
print(city_hotels.head())

plt.figure(figsize=(20,8))
plt.title("Average Daily Rate in city and Resort Hotel",fontsize=30)
plt.plot(resort_hotel.index,resort_hotel["adr"],label="Resort Hotel")
plt.plot(city_hotels.index,city_hotels["adr"],label="city Hotel")
plt.legend(fontsize=20)
plt.show()





# Extract the month from reservation_status_date
df["month"] = df["reservation_status_date"].dt.month

# Plot reservation status per month
plt.figure(figsize=(16, 8))
ax1 = sns.countplot(x="month", hue="is_canceled", data=df, palette="Blues")

# Titles and labels
plt.title("Reservation Status Per Month", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Reservations", fontsize=14)


plt.legend(title="Cancellation Status", labels=["Not Canceled", "Canceled"])

plt.show()





plt.figure(figsize=(15, 8))
plt.title("ADR per month", fontsize=30)

# Corrected argument format for barplot
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())

plt.show()  # Removed legend since it's unnecessary

cancelled_data = df[df["is_canceled"] == 1]
top_10_country = cancelled_data["country"].value_counts()[:10]

plt.figure(figsize=(8, 8))
plt.title("Top 10 countries with reservation canceled")

plt.pie(top_10_country, autopct="%.2f", labels=top_10_country.index)

plt.show()


print(df["market_segment"].value_counts())



canceled_data=df[df["is_canceled"]==1]
top_10_country=canceled_data["country"].value_counts()[:10]

plt.figure(figsize=(10,9))
plt.title("top 10 country with reservation canceled")
plt.pie(top_10_country,autopct="%.2f",labels=top_10_country.index)
plt.show()


print(df["market_segment"].value_counts(normalize=True))



