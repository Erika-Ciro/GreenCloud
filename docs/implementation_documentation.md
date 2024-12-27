# Implementation Documentation  

## Overview  
This document outlines the key steps taken to develop the low-fidelity prototype for the Sustainability Dashboard. It also provides an overview of the system architecture, ethical considerations, and potential future improvements.  

---  

## 1. System Architecture  
The architecture of the project is designed to analyze energy consumption and carbon emissions from Google Cloud data (2019-2023). The system integrates data processing, machine learning modeling, and dashboard visualization.  

### Architecture Diagram  
The architecture consists of the following stages:  
1. **Data Ingestion:**  
   - CSV files from Google Cloud Reports (2019-2023).  
   - Preprocessing scripts for data cleaning and merging.  
2. **Data Processing:**  
   - Feature engineering (Google CFE, Grid Carbon Intensity).  
   - Handling missing values and normalization.  
3. **Machine Learning Models:**  
   - Linear Regression, Random Forest Regressor, and Logistic Regression.  
   - Models trained to predict energy consumption and carbon intensity.  
4. **Visualization (Prototype):**  
   - A low-fidelity dashboard designed in Canva.  
   - Displays energy metrics, predictions, and recommendations.  

---

## 2. Prototype Development  
The low-fidelity prototype was created to represent the conceptual design of the Sustainability Dashboard. It aims to provide insights into energy consumption patterns and suggest solutions for reducing carbon emissions.  

### Key Prototype Features:  
- **Real-time Monitoring:**  
   - Visualize energy consumption across regions.  
- **Prediction Section:**  
   - Forecast energy usage for the next 24 hours.  
- **Problem Detection and Alerts:**  
   - Notify users about spikes in energy consumption or high carbon intensity.  
- **User Interaction:**  
   - Filters to adjust views and focus on specific regions or time frames.  

---

## 3. Ethical Considerations  
The project emphasizes ethical considerations, including:  
- **Data Privacy:**  
   - No personal or sensitive data is used. The data is sourced from public Google Cloud reports.  
- **Transparency:**  
   - Clear communication of predictions and recommendations.  
- **Compliance with GDPR:**  
   - Although no user data is collected, the design ensures transparency and accountability in line with GDPR principles.  

---

## 4. Future Improvements  
- Develop a high-fidelity prototype with real-time data integration.  
- Implement interactive elements for deeper user engagement.  
- Expand the machine learning models to incorporate more variables and improve accuracy.  
