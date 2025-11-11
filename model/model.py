import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

os.makedirs("res", exist_ok=True)

df = pd.read_excel("WW Marine Datashare.xlsx")
df = df[["Sample Longitude", "Sample Latitude", "Sample Date"]].dropna()
df["Sample Date"] = pd.to_datetime(df["Sample Date"], errors="coerce")
df = df[df["Sample Date"].dt.year == 2015].reset_index(drop=True)

lat_rad = np.radians(df["Sample Latitude"].to_numpy())
lon_rad = np.radians(df["Sample Longitude"].to_numpy())
X = np.c_[np.cos(lat_rad) * np.cos(lon_rad),
          np.cos(lat_rad) * np.sin(lon_rad),
          np.sin(lat_rad)]

kmeans = KMeans(n_clusters=6, n_init=20, random_state=0).fit(X)
df["cluster"] = kmeans.labels_

plt.figure(figsize=(10, 5))
plt.scatter(df["Sample Longitude"], df["Sample Latitude"],
            c=df["cluster"], s=10, alpha=0.7, edgecolor="none")
plt.title("K-Means Clustering on Unit Sphere (2015 Samples)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.tight_layout()
plt.savefig("res/kmeans_sphere_clusters_2015.png", dpi=300)
plt.show()
