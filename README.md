 NIFTY 50 Market Regime Classification

Objective

Build a time-series classification system that identifies daily market regimes for NIFTY 50:
	•	Uptrend
	•	Downtrend
	•	Sideways

The goal is structural regime detection, not price prediction.

⸻

Why This Problem?

Market regimes influence:
	•	Risk allocation
	•	Strategy switching
	•	Volatility targeting
	•	Portfolio management

Instead of predicting price (noisy and unstable), this project focuses on detecting structural behavior.

⸻

Data
	•	Source: Yahoo Finance (^NSEI)
	•	Time range: 2012–2026
	•	Frequency: Daily
	•	Features used:
	•	Close
	•	Volume

⸻

Regime Definition

Regimes were labeled using deterministic rules:

Uptrend:
	•	MA_20 > MA_50
	•	Close > MA_20

Downtrend:
	•	MA_20 < MA_50
	•	Close < MA_20

Sideways:
	•	Otherwise

Labels were created before ML training.

Train/Test Strategy

Time-aware split:
	•	Train: 2012–2020
	•	Test: 2021–2026

No random shuffling used.

This prevents future data leakage.

⸻

Models Compared
	1.	Logistic Regression (baseline)
	2.	Random Forest

Features were scaled for linear models.

⸻

Results

Final Random Forest performance:

Accuracy: 0.79

Strongest regime detection:
	•	Uptrend and Downtrend

Most challenging:
	•	Sideways regime (structurally ambiguous)

⸻

Feature Importance

Top features:
	1.	dist_ma20
	2.	ma20_slope
	3.	return_5
	4.	vol_20
	5.	volume_ratio

Major improvement came from adding MA slope, which introduced directional persistence.

⸻

Key Learnings
	•	Feature engineering had greater impact than model complexity.
	•	Time-aware split is critical in financial ML.
	•	Regime definition strongly influences classification performance.
	•	Simpler models can perform competitively with well-designed features.

⸻

Limitations
	•	Regimes defined using moving average rules (rule bias).
	•	Index volume may not fully represent true market participation.
	•	No walk-forward validation yet.