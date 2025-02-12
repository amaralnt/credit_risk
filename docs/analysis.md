# Analysis Results

## 1. Portfolio Analysis

### 1.1 Portfolio Overview
- Total portfolio: $30.1B across 2M loans
- Average loan size: $15,048
- Overall default rate: 13.05%
- Interest rate range: 5.31% to 30.99% (mean: 13.09%)
- Portfolio concentration in grades B-C (1.16M loans)

### 1.2 Key Metrics Summary
```
Metric          Mean     Median    Std Dev
loan_amnt     15048.02  12925.00   9189.92
int_rate         13.09     12.62      4.83
dti              18.48     17.84      8.83
credit_history   16.40     14.83      7.68
revol_util       50.31     50.30     24.65
```

## 2. Risk Factor Analysis

### 2.1 Grade-Based Risk
- Default rates by grade:
  * Grade A: 3.66%
  * Grade B: 8.81%
  * Grade C: 14.59%
  * Grade D: 20.63%
  * Grade E: 28.51%
  * Grade F: 36.70%
  * Grade G: 40.43%

### 2.2 Term Length Impact
- 36-month terms: 11.12% default rate
- 60-month terms: 17.82% default rate
- 60% higher defaults in longer terms

### 2.3 Borrower Characteristics
- Home ownership influence:
  * Mortgage: 11.35% default rate
  * Rent: 15.15% default rate
  * Own: 13.09% default rate

- Income levels:
  * Very High: 9.96% default rate
  * High: 11.99% default rate
  * Medium: 13.39% default rate
  * Low: 14.37% default rate
  * Very Low: 15.35% default rate

### 2.4 Risk Indicators
- High DTI (>30%):
  * Prevalence: 10.9%
  * Default Rate: 16.7%

- High Utilization (>60%):
  * Prevalence: 36.6%
  * Default Rate: 15.1%

- High Risk Grade:
  * Prevalence: 8.4%
  * Default Rate: 31.1%

## 3. Business Impact Analysis

### 3.1 Risk Concentration
- High-risk grades (8.4% of portfolio) drive 31.1% of defaults
- Geographic variations exceed 15% default rates in some states
- Term length significantly impacts portfolio performance

### 3.2 Opportunity Areas
1. Income Verification Process
   - Unverified loans show surprisingly lower defaults
   - Potential for process optimization

2. Geographic Risk Adjustment
   - Significant state-level variations
   - Opportunity for regional pricing optimization

3. Term Length Strategy
   - Clear risk differential between terms
   - Potential for term-based pricing refinement

## 4. Statistical Validation

### 4.1 Risk Factor Significance
All analyzed factors show statistical significance (p < 0.0001):
- Grade-based default rates
- Term length impact
- Income level correlation
- Geographic variations

### 4.2 Predictive Power
Information Values (IV):
- DTI: 0.0389
- Revolving utilization: 0.0360
- Credit history: 0.0117

### 4.3 Model Performance
Logistic Regression Odds Ratios:
- Account-to-history ratio: 1.138
- DTI: 1.021
- Credit history: 0.987