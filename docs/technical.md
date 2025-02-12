# Technical Documentation

## 1. Data Overview
Analysis of a 2M loan portfolio ($30.1B) from a major peer-to-peer lending platform. The project encompasses data cleaning, feature engineering, exploratory analysis, and statistical validation of risk factors.

### 1.1 Data Dictionary
| Feature | Description | Type | Example |
|---------|-------------|------|---------|
| loan_amnt | Listed loan amount applied for by borrower | Float | 32000.0 |
| term | Number of monthly payments (36 or 60) | Integer | 36 |
| int_rate | Interest rate on the loan | Float | 10.49 |
| installment | Monthly payment amount | Float | 687.65 |
| grade | Assigned loan grade | String | 'B' |
| sub_grade | Assigned loan subgrade | String | 'B3' |
| emp_title | Borrower's job title | String | 'Teacher' |
| emp_length | Employment length in years (0-10) | Integer | 10 |
| home_ownership | Home ownership status | String | 'MORTGAGE' |
| annual_inc | Self-reported annual income | Float | 120000.0 |
| verification_status | Income verification status | String | 'Verified' |
| issue_d | Loan funding date | Date | '2023-01-01' |
| loan_status | Current loan status | String | 'Current' |
| zip_code | First 3 digits of ZIP code | String | '900' |
| addr_state | State of residence | String | 'CA' |
| dti | Debt-to-Income ratio | Float | 18.48 |
| earliest_cr_line | Earliest credit line date | Date | '2001-04-01' |
| open_acc | Number of open credit lines | Integer | 16 |
| pub_rec | Number of derogatory public records | Integer | 0 |
| revol_bal | Total revolving balance | Float | 39687.0 |
| revol_util | Revolving utilization rate (%) | Float | 57.8 |
| total_acc | Total number of credit lines | Integer | 42 |
| initial_list_status | Initial listing status (W/F) | String | 'W' |
| application_type | Individual/Joint application | String | 'Individual' |
| mort_acc | Number of mortgage accounts | Integer | 2 |
| pub_rec_bankruptcies | Number of bankruptcies | Integer | 0 |

## 2. Technical Implementation

### 2.1 Data Pipeline
The data pipeline processes raw loan data through several stages:

**Raw Data Processing**
- Loads CSV data from raw directory
- Selects 27 essential features for analysis
- Converts to efficient parquet format

**Sampling Strategy**
- Extracts 2M random loans using stratified sampling
- Maintains original data distribution
- Ensures statistical significance

**Quality Checks**
- Verifies data completeness
- Validates file paths and directories
- Confirms data type consistency
- Monitors sample representation

### 2.2 Data Cleaning
The data cleaning process ensures data quality through systematic steps:

**Data Validation**
- Standardized date formats to YYYY-MM-DD
- Verified data type consistency
- Ensured logical value ranges

**Missing Value Treatment**
- Numeric columns filled with median values
- Categorical columns filled with mode values
- Preserves data distribution while handling gaps

**Outlier Handling**
- Capped Debt-to-Income ratio (DTI) at 99th percentile
- Capped revolving utilization at 99th percentile
- Removes extreme values while maintaining distribution integrity

### 2.3 Feature Engineering
The feature engineering process created derived variables and risk indicators:

**Credit History Metrics**
- Credit history duration (years since earliest credit line)
- Account velocity (accounts opened per year)
- Monthly debt burden (installment to income ratio)

**Binary Risk Flags**
- Default status (based on loan outcome)
- High DTI (>30%)
- High revolving utilization (>60%)
- High-risk grade (grades E, F, G)
- Unverified income status

### 2.4 Analysis Methods
The analysis methodology included:

**Exploratory Analysis**
- Portfolio composition analysis
- Risk factor identification
- Geographic distribution mapping
- Term length impact assessment

**Statistical Validation**
- Significance testing of risk factors
- Logistic regression modeling
- Information Value calculations
- Cross-validation procedures