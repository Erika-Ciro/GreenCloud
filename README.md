# GreenCloud Sustainability Dashboard for Cloud Providers

## Project Overview
A Sustainability Dashboard prototype designed to monitor cloud energy consumption, predict usage trends, and track carbon emissions.

 **GreenCloud** is a prototype developed as part of my Bachelor's thesis project titled:
**"Analysis and Reduction of the Carbon Footprint in the Cloud"**

This project aims to help cloud providers monitor energy consumption, track carbon emissions, and predict energy usage trends. By offering actionable insights, the dashboard supports efforts to optimize energy usage and reduce carbon footprints in cloud data centers.


## Features
The GreenCloud Sustainability Dashboard includes the following key functionalities:

**1. Energy Consumption Monitoring**

- Visualizes hourly and regional energy consumption using interactive charts.

**2. Carbon Emissions Tracking**

- Tracks emissions data by region and identifies high-emission areas through pie charts and benchmarks.

**3. Predictive Analytics**

- Uses historical data to forecast future energy consumption trends, supporting proactive energy management.

**4. Problem Detection and Recommendations**

- Detects unusual energy usage or emission spikes and suggests optimization strategies to improve efficiency.

**5. User-Friendly Visualizations**

- Provides clear, actionable insights through interactive dashboards and data visualizations.


## Technologies Used

The project incorporates the following technologies and tools:

- **Programming Languages & Libraries:**
- Python 3.8
- TensorFlow/ Scikit-learn for machine learning models
- Matplotlib, Ploty for data visualization

- **Prototyping Tool:**
- Canva (for the low-fidelity prototype design)


## Data 
The datasets used in this project were sourced from the **Google Cloud Sustainability Reports (2019-2023)**. The processed data includes key metrics such as:

-**Google Cloud Region**

-**Location**

-**Grid Carbon Intensity (gCO2eq/kWh)**

-**Google CFE(%)**

For details on raw and processed data, see the ```data/``` folder.

## Directory Structure
The repository is organized as follows:

```plaintext
GreenCloud/
│
├── data/                     # Dataset files used for analysis and predictions
│   ├── raw/                  # Original datasets (2019-2023)
│   └── processed/            # Cleaned and pre-processed datasets
│
├── notebooks/                # Jupyter Notebooks for exploratory data analysis 
│   ├── 01_EDA.ipynb          # Initial data analysis and visualization
│   ├── 02_merged.ipynb       # Feature engineering and dataset merging
│   
│
├── prototype/                # Low-fidelity dashboard prototype (Canva files)
│   └── images/               # Screenshots or export of the prototype design
│
├── src/                      # Source code for dashboard scripts
│   ├── utils/                # Helper functions and utilities
│   ├── preprocess.py         # Data cleaning and preprocessing scripts
│   ├── model.py              # Predictive model implementation
│   └── dashboard.py          # Script for dashboard functionalities
│
├── requirements.txt          # List of dependencies
├── README.md                 # Project overview (this file)
└── LICENSE                   # License file for project usage
```

## Setup Instructions
To set up and run the project locally, follow these steps:


**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/GreenCloud.git
cd GreenCloud
```
**2. Install dependencies:**
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```
**3. Run the scripts:**
- Data Preprocessing:
```bash
python src/preprocess.py
```
- Model Training and Prediction:
```bash
python src/model.py
```
- Run the Dashboard:
```bash
python src/dashboard.py
```
**4. View Prototype:**

Navigate to the **prototype/images/** folder to see the low-fidelity design.


## Future Vision
This prototype serves as a foundation for a full-scale **Sustainability Dashboard**.
Future enhancements include:

- **High-Fidelity Implementation:** Develop an interactive dashboard using tools like Streamlit or Dash.
- **Enhanced Predictive Models:** Incorporate real-time energy data and more robust machine learning algorithms.
- **User Feedback Integration:** Test with stakeholders to refine the user interface and functionality.
- **Cloud Integration:** Deploy the dashboard on cloud platforms like Google Cloud or Azure for real-time tracking.


## Results 

### Trends Over Time
*Figure 1: Grid Carbon Intensity Over the Years.*

<img width="757" alt="Captura de pantalla 2024-12-17 a las 12 43 34" src="https://github.com/user-attachments/assets/9e07a6b1-8582-4c6e-8037-30a8e227335b" />

*Figure 2: Google CFE Percentage over the Years.*

<img width="754" alt="Captura de pantalla 2024-12-17 a las 12 43 37" src="https://github.com/user-attachments/assets/654492e5-34e4-48c2-916e-33e9e513a0dd" />

### Correlation Analysis 
*Figure 3: Correlation Matrix of Key Features.*

<img width="754" alt="Captura de pantalla 2024-12-17 a las 12 43 40" src="https://github.com/user-attachments/assets/a48a317b-9d67-4be5-a7fe-6102f38b5750" />

### Model Performance
*Figure 4: Summary of Model Performance Metrics.* 

<img width="642" alt="segunda imagen" src="https://github.com/user-attachments/assets/1ac8f092-d066-4310-b7f6-4c3d0f9a8406" />

Refer to the **`data/` folder** for detailed visualizations and further analysis.
## Acknowledgments

This project was developed as part of my Bachelor's thesis to address sustainability challenges in cloud data centers. Special thanks to my mentors, university faculty, and peers for their valuable guidance and support.
