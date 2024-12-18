# Jupyter Notebooks

This folder contains Jupyter Notebooks used for data collection, cleaning, analysis, visualization, and machine learning modeling for the **GreenCloud Sustainability Dashboard** project.

---

## **Notebooks Overview**

### **1. Regional Carbon Analysis (2019-2023)**  
- **Files**:  
  - `region_carbon_2019.ipynb`  
  - `region_carbon_2020.ipynb`  
  - `region_carbon_2021.ipynb`  
  - `region_carbon_2022.ipynb`  
  - `region_carbon_2023.ipynb`  
- **Purpose**:  
  - Perform yearly data collection and exploration for each region.  
  - Visualize distributions (e.g., histograms, boxplots) and analyze `Google CFE` and `Grid Carbon Intensity`.  
  - Examples of functions included:  
    - `print_histograms(df)`  
    - `bar_chart(df)`  
    - `geographic_heat_map(df)`.  

---

### **2. Google Cloud CFE Trends Analysis**  
- **File**: `Google_Cloud_CFE_trends_2019_2023.ipynb`  
- **Purpose**:  
  - Combine and clean datasets from 2019-2023, including manual data from reports.  
  - Analyze year-over-year trends in `Google CFE` and `Grid Carbon Intensity`.  
  - Create comparative visualizations such as:  
    - Line charts for `Google CFE` and `Grid Carbon Intensity` trends.  
    - Correlation matrix heatmaps.  
    - Regional boxplots for key metrics.  

---

### **3. Region Carbon Info (Merged Dataset)**  
- **File**: `region_carbon_merged.ipynb`  
- **Purpose**:  
  - Merge and consolidate yearly datasets into a unified dataset.  
  - Perform advanced feature engineering, including:  
    - Consolidation of carbon intensity columns.  
    - Calculation of year-over-year changes.  
    - Standard deviation analysis for regional metrics.  
  - Functions include:  
    - `load_and_merge_dataset()`  
    - `consolidate_carbon_intensity()`.  

---

### **4. Machine Learning and Visualization**  
- **File**: `model_exploration.ipynb`  
- **Purpose**:  
  - Explore regression and classification models:  
    - Predict `Grid Carbon Intensity`.  
    - Categorize regions based on `Google CFE`.  
  - Evaluate models like:  
    - **Linear Regression**: R² and MSE.  
    - **Logistic Regression**: Accuracy and classification report.  
    - **Random Forest** (regressor and classifier).  
  - Includes data preparation steps:  
    - Feature engineering.  
    - Min-Max scaling for normalization.  

---

## **Usage Notes**  
- Notebooks are organized to follow the analysis workflow:  
  1. Yearly data exploration.  
  2. Consolidation and trends analysis.  
  3. Machine learning exploration and visualization.  

- Visual outputs and descriptive titles are included in each notebook for clarity.  

- For more details on the dataset and preprocessing steps, refer to the `data/` folder.

---

## **Future Improvements**  
- Automate manual data collection processes.  
- Incorporate additional features for model predictions, such as real-time data streams.  
- Integrate more robust visualizations directly into the dashboard prototype.  
