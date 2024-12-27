# Testing Documentation  

## Overview  
Since the project focuses on the development of a low-fidelity prototype, no formal software testing has been conducted. However, potential test cases and validation scenarios are outlined to guide future iterations when the prototype is fully implemented.  

---

## 1. Testing Goals  
- Ensure the accuracy of machine learning predictions for energy consumption.  
- Validate the dashboard’s ability to visualize data correctly.  
- Detect and alert users about spikes in carbon intensity or unusual energy usage.  

---

## 2. Potential Test Cases  

### 1. Machine Learning Model Testing:  
- **Objective:** Evaluate model performance (Linear Regression, Random Forest).  
- **Inputs:** Historical energy data (Google CFE, Grid Carbon Intensity).  
- **Expected Output:** Predicted energy consumption and carbon intensity values.  
- **Metrics to Evaluate:**  
   - R² Score  
   - Mean Squared Error (MSE)  
   - Accuracy and F1-Score (for classification models)  

---

### 2. Data Visualization Testing:  
- **Objective:** Confirm that the dashboard displays data accurately.  
- **Test Scenarios:**  
   - Verify that boxplots reflect the correct distribution of Google CFE across regions.  
   - Ensure that histograms of carbon intensity represent the expected data trends.  
   - Check if pie and bar charts dynamically adjust based on user-selected filters.  

