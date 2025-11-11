import pandas as pd
import matplotlib.pyplot as plt

# read in 'WW Marine Datashare.xlsx' as a xlsx to a pandas dataframe

marine_df = pd.read_excel("WW Marine Datashare.xlsx")
# drop unimportant features
marine_df = marine_df.filter(['record','Date Filtered', 'Date Counted','Sample Longitude','Sample Latitude','Sample Location','Sample Time (local)','Sample Date','Record','Depth of Sample (M)','Sample Volume (L)','Total Pieces','Total Pieces/L','notes','Sampling Site Info','Lab Notes'])
# first five or so samples don't
print(marine_df['Date Filtered'].isna().sum())
# we need to plot amount found agaisnt sample date
df = pd.read_excel("WW Marine Datashare.xlsx")
df.columns = df.columns.str.strip()

# pick a date column, parse to datetime
date = pd.to_datetime(df.get("Sample Date"), errors="coerce").fillna(
        pd.to_datetime(df.get("Date Filtered"), errors="coerce")
)
date = date.dropna()

plt.figure(figsize=(10,4))
plt.hist(date, bins=100)  # change 30 to fewer/more bins
plt.title("Histogram of Sample Dates")
plt.xlabel("Date")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Setup ---
os.makedirs("res", exist_ok=True)

# --- Load the dataset ---
marine_df = pd.read_excel("WW Marine Datashare.xlsx")

# Extract just lat/lon columns, dropping invalid rows
marine_df = marine_df[["Sample Longitude", "Sample Latitude"]].dropna()

# --- Plot sample locations ---
plt.figure(figsize=(10, 5))
plt.scatter(
    marine_df["Sample Longitude"],
    marine_df["Sample Latitude"],
    s=10, color="dodgerblue", alpha=0.6, edgecolor="none"
)
plt.title("Global Microplastic Sampling Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.grid(alpha=0.3)
plt.tight_layout()

# Save to file
output_path = os.path.join("res", "sample_map.png")
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Saved sample location map to {output_path}")
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Setup ---
os.makedirs("res", exist_ok=True)

# --- Load the dataset ---
marine_df = pd.read_excel("WW Marine Datashare.xlsx")

# Parse date column into datetime and drop rows with invalid coordinates or missing dates
marine_df["Sample Date"] = pd.to_datetime(marine_df["Sample Date"], errors="coerce")
marine_df = marine_df.dropna(subset=["Sample Longitude", "Sample Latitude", "Sample Date"])

# --- Filter for 2015 only ---
marine_2015 = marine_df[marine_df["Sample Date"].dt.year == 2015]

print(f"Total 2015 samples: {len(marine_2015)}")

# --- Plot 2015 sample locations ---
plt.figure(figsize=(10, 5))
plt.scatter(
    marine_2015["Sample Longitude"],
    marine_2015["Sample Latitude"],
    s=10, color="dodgerblue", alpha=0.6, edgecolor="none"
)
plt.title("Global Microplastic Sampling Locations (2015)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.grid(alpha=0.3)
plt.tight_layout()

# Save to file
output_path = os.path.join("res", "sample_map_2015.png")
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Saved 2015 sample location map to {output_path}")
