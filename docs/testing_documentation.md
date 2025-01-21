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

### 2.1. Machine Learning Model Testing:  
- **Objective:** Evaluate model performance (Linear Regression, Random Forest).  
- **Inputs:** Historical energy data (Google CFE, Grid Carbon Intensity).  
- **Expected Output:** Predicted energy consumption and carbon intensity values.  
- **Metrics to Evaluate:**  
   - R² Score  
   - Mean Squared Error (MSE)  
   - Accuracy and F1-Score (for classification models)
     
### 2.2. Data Visualization Testing:  
- **Objective:** Confirm that the dashboard visualizes data accurately and dynamically.
- **Test Scenarios:**
    - Verify that boxplots reflect the correct distribution of Google CFE across regions.
    - Ensure that histograms of carbon intensity align with expected trends.
    - Test pie and bar charts to confirm they adjust dynamically based on user-selected filters.

### 2.3 Usability Testing
- **Objective:** Validate the ease of use and intuitiveness of the dashboard prototype.
- **Test Scenarios:**
    - Evaluate the clarity of visualizations for stakeholders.
    - Check navigation flow and the responsiveness of filters.
    - Collect qualitative feedback from users about the interface design

---

## 3. Risk Assessment

### 3.1 Identified Risks
- **Data Visualization Accuracy:**
   - Risk: Incorrect representation of data trends.
   - Mitigation: Cross-check visualizations with raw data during testing.

- **Model Accuracy:**
   - Risk: Predictions may not align with real-world data due to limited datasets.
   - Mitigation: Expand datasets and fine-tune models in future iterations.

- **User Interaction:**
   - Risk: Filters or visualizations may not respond intuitively.
   - Mitigation: Conduct usability tests with diverse user groups.

---

## 4. Future Testing Plans

###  4.1 Integration Testing
- **Objective:** Ensure seamless interaction between the data preprocessing pipeline, machine learning models, and the dashboard prototype.
- **Scenarios:**
   - Validate that data flows correctly from preprocessing to visualization.
   - Ensure that predictions are accurately displayed on the dashboard.

###  4.2 Real-Time Data Validation
- **Objective:** Test the dashboard’s performance with real-time data inputs.
- **Scenarios:**
   - Simulate real-time energy consumption data and validate visualizations.
   - Test alert notifications for energy spikes.

### 4.3 User Feedback Testing
- **Objective:** Collect user feedback to refine the prototype.
- **Scenarios:**
   - Conduct surveys or interviews to evaluate satisfaction with the dashboard.
   - Use stakeholder feedback to prioritize future feature development.

