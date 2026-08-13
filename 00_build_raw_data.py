"""
00_build_raw_data.py
----------------------
Transcribes Figure 4.2 ("Deprivation in each Indicator by Quarter") from the
Ghana Statistical Service's 2024 Q1-2025 Q3 Multidimensional Poverty Report
into a structured, long-format CSV for time-series analysis.

Source (official GSS publication, via the SDGs Ghana portal):
https://sdgsghana.gov.gh/wp-content/uploads/2026/01/06-2024-2025Q3-MPI-Report_
21012026-signed-final.pdf (Figure 4.2, p.22)

Each of Ghana's 13 MPI indicators represents the % of the population deprived
in that specific area (e.g., no health insurance, malnourished, no toilet
facility) for every quarter from 2022 Q1 to 2025 Q3 (2025 Q1 not published
in this indicator series in the source report).
"""

import pandas as pd

quarters = ["2022-Q1","2022-Q2","2022-Q3","2022-Q4",
            "2023-Q1","2023-Q2","2023-Q3","2023-Q4",
            "2024-Q1","2024-Q2","2024-Q3","2024-Q4",
            "2025-Q2","2025-Q3"]

indicators = {
    "Overall MPI Incidence": [28.3,32.4,32.3,31.7, 28.3,27.7,28.6,27.4, 24.0,28.5,24.9,24.9, 23.1,21.9],
    "School attainment":     [0.8,0.8,0.6,0.9, 0.8,0.9,0.8,0.6, 0.7,0.7,0.6,0.6, 0.8,1.0],
    "Electricity":           [6.9,7.5,9.1,8.6, 8.7,8.8,9.0,8.1, 8.0,8.7,8.6,8.4, 5.7,6.1],
    "Employed":              [7.8,10.2,7.9,8.5, 5.8,5.4,5.0,5.0, 5.2,5.6,5.3,4.1, 3.8,4.5],
    "Cooking fuel":          [9.3,10.1,11.6,9.8, 9.1,9.0,10.0,10.3, 7.4,9.0,8.0,8.6, 9.4,8.4],
    "School attendance":     [9.3,10.3,10.4,9.7, 8.5,7.0,8.2,8.9, 8.0,8.5,8.7,9.1, 7.0,9.4],
    "Drinking water":        [9.9,9.9,10.2,9.6, 9.5,9.2,9.1,8.7, 8.4,8.6,8.0,7.8, 6.8,6.3],
    "Assets":                [11.8,15.1,13.1,13.2, 15.0,14.6,10.4,10.2, 9.2,10.5,5.5,7.8, 9.8,9.5],
    "Nutrition":             [12.9,14.4,16.1,15.5, 13.9,13.2,15.4,14.1, 10.6,15.1,13.3,13.4, 15.8,10.6],
    "Overcrowding":          [14.1,15.8,17.4,16.3, 14.6,13.3,14.4,14.8, 12.4,14.1,12.2,12.5, 11.4,21.6],
    "School lag":            [15.7,18.5,20.2,19.5, 17.2,17.8,19.2,16.4, 14.1,19.4,15.3,15.5, 7.9,3.9],
    "Housing":               [18.2,17.8,17.9,18.3, 18.8,18.5,19.1,17.8, 15.4,17.8,16.1,16.6, 14.8,14.5],
    "Toilet facility":       [26.4,27.0,29.6,28.4, 26.3,25.6,26.6,25.0, 22.5,26.0,23.0,23.1, 21.6,20.7],
    "Health insurance":      [26.5,30.7,30.5,29.6, 26.7,26.0,26.7,26.1, 22.2,26.0,23.0,23.3, 21.3,19.5],
}

rows = []
for indicator, values in indicators.items():
    assert len(values) == len(quarters), f"{indicator} has {len(values)} values, expected {len(quarters)}"
    for q, v in zip(quarters, values):
        rows.append({"quarter": q, "indicator": indicator, "deprivation_pct": v})

df = pd.DataFrame(rows)
df.to_csv("../data/ghana_mpi_indicators_by_quarter.csv", index=False)
print(f"Saved {len(df)} rows ({len(indicators)} indicators x {len(quarters)} quarters)")
print(f"to ../data/ghana_mpi_indicators_by_quarter.csv")

# Sanity check: overall incidence should match report's stated Q3 2025 figure (21.9%)
latest = df[(df["indicator"] == "Overall MPI Incidence") & (df["quarter"] == "2025-Q3")]
print("\nSanity check — Q3 2025 overall incidence:", latest["deprivation_pct"].values[0], "% (report states 21.9%)")
