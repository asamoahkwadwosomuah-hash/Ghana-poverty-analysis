"""
01_analysis.py
----------------
Analyzes which deprivation indicators drive Ghana's multidimensional
poverty most, and how each has trended from 2022 to 2025.
"""

import pandas as pd

df = pd.read_csv("../data/ghana_mpi_indicators_by_quarter.csv")
indicators_only = df[df["indicator"] != "Overall MPI Incidence"]

print("=" * 65)
print("Q1. Which deprivation is currently (2025 Q3) the single largest problem?")
latest = indicators_only[indicators_only["quarter"] == "2025-Q3"].sort_values("deprivation_pct", ascending=False)
print(latest[["indicator", "deprivation_pct"]].to_string(index=False))

print("\n" + "=" * 65)
print("Q2. How has overall multidimensional poverty trended, 2022 Q1 -> 2025 Q3?")
overall = df[df["indicator"] == "Overall MPI Incidence"]
print(overall[["quarter", "deprivation_pct"]].to_string(index=False))
first, last = overall.iloc[0]["deprivation_pct"], overall.iloc[-1]["deprivation_pct"]
print(f"\nNet change 2022-Q1 -> 2025-Q3: {last - first:+.1f} percentage points")

print("\n" + "=" * 65)
print("Q3. Which indicators improved the most, and which got worse, over the full period?")
first_q = indicators_only[indicators_only["quarter"] == "2022-Q1"].set_index("indicator")["deprivation_pct"]
last_q = indicators_only[indicators_only["quarter"] == "2025-Q3"].set_index("indicator")["deprivation_pct"]
change = (last_q - first_q).sort_values()
print(change)

print("\n" + "=" * 65)
print("Q4. Which indicator moved the most in the most recent quarter (Q2 2025 -> Q3 2025)?")
q2 = indicators_only[indicators_only["quarter"] == "2025-Q2"].set_index("indicator")["deprivation_pct"]
q3 = indicators_only[indicators_only["quarter"] == "2025-Q3"].set_index("indicator")["deprivation_pct"]
recent_change = (q3 - q2).sort_values()
print(recent_change)

print("\n" + "=" * 65)
print("Q5. Health insurance and toilet facility are consistently the top-2 deprivations —")
print("    what share of the 'deprivation gap' do they represent in the latest quarter?")
top2 = latest.head(2)["deprivation_pct"].sum()
total = latest["deprivation_pct"].sum()
print(f"Health insurance + Toilet facility = {top2:.1f} points out of {total:.1f} total indicator points ({top2/total*100:.1f}%)")
