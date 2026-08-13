# Ghana Multidimensional Poverty: Trends & Drivers (2022–2025)

**A national-development time-series analysis — Python, pandas, matplotlib — using official Ghana Statistical Service data to identify what's actually driving poverty in Ghana, and whether it's improving.**

## Business/policy context

Ghana measures poverty two ways: monetary poverty (income-based) and **multidimensional poverty (MPI)** — a broader measure capturing whether households are deprived across 13 indicators spanning living conditions, health, education, and employment. A person is classified as multidimensionally poor if they're deprived in at least a third of the weighted indicators. This is the more policy-actionable of the two measures, because it points directly at *which* deprivation to fix, not just *how many* people are poor.

This project analyzes the **quarterly indicator-level breakdown** GSS publishes — specific deprivation rates across 13 indicators (health insurance, sanitation, nutrition, housing, etc.) tracked every quarter from **2022 Q1 to 2025 Q3** — to answer: *is poverty improving, and if so, which specific deprivations are driving the change?*

**Dataset:** Figure 4.2 from the GSS's [2024 Q1–2025 Q3 Multidimensional Poverty Report](https://sdgsghana.gov.gh/wp-content/uploads/2026/01/06-2024-2025Q3-MPI-Report_21012026-signed-final.pdf) — 14 quarters × 13 individual deprivation indicators, published January 2026.

## A note on data provenance

Like the companion NEET project in this portfolio, this data was **manually transcribed** from an official GSS PDF table (not scraped or downloaded as CSV, since GSS does not publish one for this figure) and validated: the transcribed Q3 2025 overall MPI incidence (21.9%) was checked against the report's own stated headline figure (21.9%) and matches exactly.

## Business/research questions answered

1. Has Ghana's multidimensional poverty rate improved or worsened since 2022?
2. Which specific deprivation is currently the single biggest driver of poverty?
3. Which deprivations have improved the most (and least) since 2022?
4. Are there any recent, sudden shifts that don't show up in the slow-moving headline number?

## Process

1. **Transcribe & validate** (`notebooks/00_build_raw_data.py`) — transcribed the official 13-indicator × 14-quarter table into long-format CSV, validated against the report's own stated headline figure.
2. **Analyze** (`notebooks/01_analysis.py`) — ranked current deprivations, computed long-run and most-recent-quarter change per indicator, and quantified how concentrated poverty is in the top deprivations.
3. **Visualize** (`notebooks/02_build_dashboard.py`) — built a 4-panel dashboard covering the headline trend, a current snapshot ranking, long-run change by indicator, and a close-up trend of the three worst current deprivations.

## Key findings

- **Multidimensional poverty fell substantially**: from 28.3% in Q1 2022 to 21.9% in Q3 2025 — a 6.4 percentage-point improvement, though the path wasn't linear (it briefly spiked to 32.4% in mid-2022 and again to 28.5% in Q2 2024 before resuming its decline).
- **Health insurance coverage and toilet/sanitation access remain, by far, the two largest deprivations**, together accounting for roughly 31% of all deprivation points measured in the latest quarter — squarely matching the report's own policy recommendation to prioritize NHIS expansion and sanitation investment.
- **School lag improved the most of any indicator** (−11.8 points since 2022), suggesting education-retention interventions over this period had a real, measurable effect.
- **A striking anomaly: household overcrowding surged from 11.4% to 21.6% in a single quarter** (Q2 2025 → Q3 2025) — a 10.2 percentage-point jump that took it from the *least* concerning indicator to the *most* concerning one almost overnight. This is large enough that it looks more like a data or definitional shift than a genuine one-quarter social change, and would be the first thing I'd flag to GSS or investigate further before acting on it — a good example of why raw trend data needs a sanity check before it drives policy.
- **Employment deprivation is comparatively small and improving** (7.8% → 4.5%), which — read alongside the youth NEET findings in the companion project in this portfolio — suggests Ghana's poverty problem is now more about *access to services* (health insurance, sanitation) than about *access to work* for the population as a whole, even though youth-specific labour exclusion remains a distinct, serious problem.

## Recommendations

- Prioritize NHIS (health insurance) enrollment and renewal simplification, and sanitation/toilet infrastructure — these two alone represent the largest, most persistent share of measured deprivation.
- Investigate the Q3 2025 overcrowding spike before treating it as a genuine trend — check whether survey methodology, question wording, or sampling changed between quarters, since a jump this large in one quarter is unusual relative to every other indicator's smoother trajectory.
- Study what drove the sharp school lag improvement (−11.8 points) as a potential template for interventions in slower-moving indicators like nutrition and housing.

## Repo structure

```
data/           transcribed and validated GSS MPI indicator dataset (CSV)
notebooks/      data transcription/validation, analysis, and dashboard scripts
outputs/        dashboard.png
```

## Tools used

Python (pandas, matplotlib), data transcription and validation, time-series analysis.

---
*Data source: Ghana Statistical Service, 2024 Q1–2025 Q3 Multidimensional Poverty Report (published January 2026). This project uses official published statistics for analytical and portfolio purposes; it is not affiliated with or endorsed by the Ghana Statistical Service.*
