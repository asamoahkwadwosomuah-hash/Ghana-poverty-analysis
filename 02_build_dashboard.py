"""
02_build_dashboard.py
------------------------
Builds a 4-panel dashboard visualizing Ghana's multidimensional poverty
trend and its underlying deprivation drivers, 2022-2025.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_csv("../data/ghana_mpi_indicators_by_quarter.csv")
indicators_only = df[df["indicator"] != "Overall MPI Incidence"]
overall = df[df["indicator"] == "Overall MPI Incidence"]

GREEN = "#046A38"
GOLD = "#FCD116"
RED = "#CE1126"

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Ghana Multidimensional Poverty (MPI) — Trends & Drivers, 2022–2025",
             fontsize=15, fontweight="bold")
fig.text(0.5, 0.955, "Source: Ghana Statistical Service, 2024 Q1–2025 Q3 Multidimensional Poverty Report",
         ha="center", fontsize=9, style="italic", color="gray")

# 1. Overall MPI incidence trend
axes[0, 0].plot(overall["quarter"], overall["deprivation_pct"], marker="o", color=RED, linewidth=2.5)
axes[0, 0].set_title("Overall Multidimensional Poverty Rate, 2022–2025")
axes[0, 0].set_ylabel("% of Population Multidimensionally Poor")
axes[0, 0].tick_params(axis="x", rotation=45, labelsize=8)
axes[0, 0].grid(alpha=0.3)
axes[0, 0].yaxis.set_major_formatter(mticker.PercentFormatter())

# 2. Current snapshot: deprivation ranking (latest quarter)
latest = indicators_only[indicators_only["quarter"] == "2025-Q3"].sort_values("deprivation_pct")
colors = [RED if v >= 15 else (GOLD if v >= 8 else GREEN) for v in latest["deprivation_pct"]]
axes[0, 1].barh(latest["indicator"], latest["deprivation_pct"], color=colors)
axes[0, 1].set_title("Deprivation by Indicator (Q3 2025 Snapshot)")
axes[0, 1].set_xlabel("% of Population Deprived")

# 3. Change over full period (2022-Q1 -> 2025-Q3) by indicator
first_q = indicators_only[indicators_only["quarter"] == "2022-Q1"].set_index("indicator")["deprivation_pct"]
last_q = indicators_only[indicators_only["quarter"] == "2025-Q3"].set_index("indicator")["deprivation_pct"]
change = (last_q - first_q).sort_values()
colors2 = [GREEN if v < 0 else RED for v in change]
axes[1, 0].barh(change.index, change.values, color=colors2)
axes[1, 0].set_title("Change in Deprivation, 2022-Q1 → 2025-Q3")
axes[1, 0].set_xlabel("Percentage-Point Change")
axes[1, 0].axvline(0, color="black", linewidth=0.8)

# 4. Trend lines for the 3 largest current deprivations
top3_indicators = latest.nlargest(3, "deprivation_pct")["indicator"].tolist()
for ind, color in zip(top3_indicators, [RED, GOLD, GREEN]):
    series = indicators_only[indicators_only["indicator"] == ind]
    axes[1, 1].plot(series["quarter"], series["deprivation_pct"], marker="o", label=ind, linewidth=2, color=color)
axes[1, 1].set_title("Trend of the 3 Largest Current Deprivations")
axes[1, 1].set_ylabel("% of Population Deprived")
axes[1, 1].tick_params(axis="x", rotation=45, labelsize=8)
axes[1, 1].legend(fontsize=9)
axes[1, 1].grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig("../outputs/dashboard.png", dpi=150, bbox_inches="tight")
print("Saved ../outputs/dashboard.png")
