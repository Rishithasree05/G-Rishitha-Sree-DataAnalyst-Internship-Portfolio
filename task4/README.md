# ApexPlanet Task 4 – Data Storytelling & Statistical Validation

## 📊 Project Overview

This repository contains the final deliverables for **Task 4 of the ApexPlanet Data Analytics Internship**.

The task focuses on transforming the analysis from previous tasks into a clear business story and validating an important business finding using statistical hypothesis testing.

## 🎯 Objectives

* Synthesize the findings from previous data analysis tasks.
* Present key business insights through a professional PowerPoint presentation.
* Formulate and test a business hypothesis.
* Use statistical testing to validate differences in customer sales.
* Translate statistical findings into actionable business recommendations.

## 🧪 Hypothesis Testing

### Business Question

Is there a statistically significant difference in average `Total_Sales` between male and female customers?

### Hypotheses

**Null Hypothesis (H₀):**
There is no statistically significant difference in average Total_Sales between male and female customers.

**Alternative Hypothesis (H₁):**
There is a statistically significant difference in average Total_Sales between male and female customers.

### Statistical Test

**Welch's Independent Two-Sample t-test**

* Significance level: 0.05
* Test type: Two-tailed

### Results

| Metric           |       Male |     Female |
| ---------------- | ---------: | ---------: |
| Sample Size      |        511 |        489 |
| Mean Total Sales | 141,807.34 | 136,883.21 |

* Difference in mean sales: **4,924.13**
* t-statistic: **0.6826**
* p-value: **0.495011**

### Conclusion

Since the p-value (**0.495011**) is greater than the significance level (**0.05**), the null hypothesis is **not rejected**.

There is insufficient statistical evidence to conclude that average Total_Sales differs significantly between male and female customers.

### Business Interpretation

Although male customers have a higher observed average Total_Sales, the difference is not statistically significant. Therefore, gender alone should not be used as a strong basis for major sales or marketing decisions.

## 📁 Deliverables

* `Final_Presentation.pptx` — Final business presentation and data story.
* `Hypothesis_Testing_Summary.pdf` — Detailed statistical testing summary.
* `hypothesis_testing.py` — Python script used to perform the Welch's t-test.

## 🛠️ Tools Used

* Python
* Pandas
* SciPy
* Microsoft Excel
* Power BI
* MySQL

## 👩‍💻 Author

**G Rishitha Sree**

Data Analytics Intern
