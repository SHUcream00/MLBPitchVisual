import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize(dataframe, balltype):
    df = dataframe

    #Filter by balltype
    res = df[df["pitch_type"] == balltype]

    #Group by results
    groups = res.groupby("description")
    for name, group in groups:
        if name == "miss":
            plt.plot(group["plate_x"], group["plate_z"], marker="o", linestyle="", color="none", ms = 3, mec="#9A9A9A", label=name)
        else:
            plt.plot(group["plate_x"], group["plate_z"], marker="o", linestyle="", color="none", ms = 3, mec="#03A77F", label=name)


    #Fixing the viewpoint of the plot
    axes = plt.gca()
    axes.set_xlim([-2.50,2.50])
    axes.set_ylim([0.00,5.00])

    #Setting strike zone
    sz_top_avg = res["sz_top"].mean()
    sz_bottom_avg = res["sz_bot"].mean()
    sz_left = -0.85
    sz_right = 0.85

    #Drawing strike zone
    plt.plot((sz_left, sz_right), (sz_top_avg, sz_top_avg), 'k-')
    plt.plot((sz_left, sz_right), (sz_bottom_avg, sz_bottom_avg), 'k-')
    plt.plot((sz_left, sz_left), (sz_top_avg, sz_bottom_avg), 'k-')
    plt.plot((sz_right, sz_right), (sz_top_avg, sz_bottom_avg), 'k-')

    #Setting labels
    plt.xlabel("Horizontal Location")
    plt.ylabel("Vertical Location")
    plt.title(f"{player_name} 2018\n {ballname_dict.get(balltype, balltype)}")

    plt.legend()
    plt.show()


#Setting up Name and CSV location
player_name = "Put player name"
file_src = "Put target csv"

raw = pd.read_csv(file_src)
df = pd.DataFrame(raw)

#For filtering cases
replace_dict = {"description": {"hit_into_play_no_out": "contact", "hit_into_play": "contact", "hit_into_play_score": "contact", "swinging_strike": "miss", "swinging_strike_blocked": "miss"}}
ballname_dict = {"FF": "4-Seam Fastball", "CH": "Changeup", "CU": "Curveball", "SL": "Slider", "FT": "2-Seam Fastball", "AB": "Automatic Ball",
                "AS": "Automatic Strike", "EP": "Eephus", "FC": "Cutter", "FO": "Forkball", "FS": "Splitter", "GY": "Gyroball", "IN": "Intentional Ball",
                "KC": "Knuckle Curve", "NP": "No Pitch", "PO": "Pitchout", "SC": "Screwball", "SI": "Sinker", "UN": "Unknown"}

df = df.replace(replace_dict)
df = df[df["description"].isin(["contact", "miss"])]
for i in df["pitch_type"].unique():
    visualize(df, i)
