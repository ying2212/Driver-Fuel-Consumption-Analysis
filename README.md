# Driver-Fuel-Consumption-Analysis
# Z-Score Analysis for Fuel Cost Data

This project analyzes fuel consumption patterns among drivers to identify potential anomalies in their fuel receipt claims. Using Z-scores, the analysis highlights data points where fuel consumption deviates significantly from expected patterns.

## Objective
The goal of this project is to ensure accountability and detect potential issues such as fraudulent fuel claims, inefficient driving habits, or inaccurate mileage reporting.

## When Do Anomalies Occur?
*Anomalies may occur under the following conditions:*

Excessive Fuel Purchases: When the amount of fuel purchased is disproportionately high compared to the distance traveled.
Underreported Mileage: When the kilometers reported are too low relative to the fuel purchased.
Fuel Price Variations: When there are significant deviations in fuel cost that do not align with the base price per liter.


## Features
*Data Input:* Reads fuel consumption data from a .csv file.
*Z-Score Calculation:* Leverages pre-calculated Z-scores from the dataset to identify outliers.
*Data Analysis:*
- Metric Used: (Fuel (Liters) * Base Price) / KM
- Anomalies are flagged using Z-scores, with thresholds set at Z > 1.5 or Z < -1.5.
*Visualizations:*
- Scatter plots showing Z-scores over time.
- Anomalies highlighted based on Z-score thresholds.
- Threshold Customization: Users can adjust Z-score thresholds to redefine anomaly detection

## Dataset
- `KH Driver.csv`: Contains the fuel cost data, including the calculated Z-scores.
<img width="960" alt="Screenshot 2025-01-11 at 8 43 31 PM" src="https://github.com/user-attachments/assets/43476062-5e3d-416e-b060-a6b3fa5225c2" />
