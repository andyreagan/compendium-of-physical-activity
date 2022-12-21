import pandas as pd
from sqlalchemy import create_engine

all_pages = {
    "bicycling": pd.read_html("data/bicycling.html"),
    "conditioning_exercise": pd.read_html("data/conditioning_exercise.html"),
    "dancing": pd.read_html("data/dancing.html"),
    "fishing_hunting": pd.read_html("data/fishing_hunting.html"),
    "home_activity": pd.read_html("data/home_activity.html"),
    "home_repair": pd.read_html("data/home_repair.html"),
    "inactivity": pd.read_html("data/inactivity.html"),
    "lawn_garden": pd.read_html("data/lawn_garden.html"),
    "miscellaneous": pd.read_html("data/miscellaneous.html"),
    "music_playing": pd.read_html("data/music_playing.html"),
    "occupation": pd.read_html("data/occupation.html"),
    "running": pd.read_html("data/running.html"),
    "self_care": pd.read_html("data/self_care.html"),
    "sexual_activity": pd.read_html("data/sexual_activity.html"),
    "sports": pd.read_html("data/sports.html"),
    "transportation": pd.read_html("data/transportation.html"),
    "walking": pd.read_html("data/walking.html"),
    "water_activities": pd.read_html("data/water_activities.html"),
    "winter_activities": pd.read_html("data/winter_activities.html"),
    "religious_activities": pd.read_html("data/religious_activities.html"),
    "volunteer_activities": pd.read_html("data/volunteer_activities.html"),
}

for k in all_pages.keys():
    d = all_pages[k][0].copy()
    clean_colnames = [x.replace(".1", "") for x in d.columns]
    clean_colnames[-1] = "Description"
    clean_colnames_2 = d.iloc[0, :]
    clean_colnames_2[-1] = ""
    d.columns = pd.MultiIndex.from_arrays([clean_colnames, clean_colnames_2])
    d = d.iloc[1:, :]
    d["Category"] = k
    all_pages[k] = d

all_activities = pd.concat(all_pages.values())

all_activities.to_json("compendiumofphysicalactivities.json", orient="records")
all_activities.to_parquet("compendiumofphysicalactivities.parquet", index=False)
all_activities.to_csv("compendiumofphysicalactivities.csv", sep="|", index=False)
all_activities.to_excel("compendiumofphysicalactivities.xlsx")
all_activities.to_html("compendiumofphysicalactivities.html", index=False)

engine = create_engine("sqlite:///compendiumofphysicalactivities.db", echo=False)
all_activities.to_sql("all_activities", con=engine)
