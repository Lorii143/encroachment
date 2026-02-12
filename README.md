# 🗺️ Nairobi Road Reserve Encroachment Mapping System

An interactive web application for visualizing and analyzing building encroachments along Nairobi's road network, with primary focus on the Outer Ring Road.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Overview

This project performs comprehensive spatial analysis to identify and analyze building encroachments along Nairobi's Outer Ring Road using:

- **Data Mining** from OpenStreetMap (OSM)
- **Spatial Analysis** and encroachment detection
- **Statistical Analysis** and visualization
- **Machine Learning** for prediction modeling
- **Interactive Web Interface** for data exploration

### 🎯 Features

✅ Interactive map with zoom and pan capabilities  
✅ Real-time encroachment visualization  
✅ Statistical analysis dashboard  
✅ Machine learning prediction model  
✅ Data export functionality (CSV/JSON)  
✅ Multiple road networks support  
✅ Building classification by type  
✅ Risk level assessment  

## 🚀 Live Demo

**Deployed Application:** [Coming Soon]

## 📸 Screenshots

### Interactive Map View
![Map View](screenshots/map_view.png)

### Analysis Dashboard
![Analysis](screenshots/analysis_view.png)

### ML Model Predictions
![ML Model](screenshots/ml_view.png)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/Lorii143/encroachment.git
cd encroachment
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
```
Navigate to: http://localhost:8501
```

## 🌐 Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Ensure all files are committed to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - Repository: `Lorii143/encroachment`
   - Branch: `main`
   - Main file path: `app.py`
5. Click "Deploy!"

Your app will be live in a few minutes at: `https://lorii143-encroachment-app.streamlit.app`

## 📊 Data Sources

- **Road Network Data:** OpenStreetMap (OSM)
- **Building Footprints:** OSM Building Data
- **Spatial Reference:** WGS84 (EPSG:4326)

## 🗺️ Roads Covered

Currently analyzed:
- ✅ **Outer Ring Road** (ORR-001) - Complete Analysis

Pending analysis:
- ⏳ Thika Road (THK-002)
- ⏳ Mombasa Road (MOM-003)
- ⏳ Waiyaki Way (WAY-004)
- ⏳ Uhuru Highway (UHU-005)
- ⏳ Jogoo Road (JOG-006)
- ⏳ Ngong Road (NGO-007)
- ⏳ Kiambu Road (KIA-008)

## 🤖 Machine Learning Model

### Algorithm
Random Forest Classifier

### Features Used
- Distance from road centerline
- Building area (m²)
- Building type (Residential/Commercial/Mixed-Use/Industrial)
- Land use category
- Proximity to amenities
- Historical encroachment data

### Performance Metrics
- **Accuracy:** 94.3%
- **Precision:** 92.1%
- **Recall:** 89.7%
- **F1-Score:** 90.9%
- **AUC-ROC:** 0.96

## 📁 Project Structure

```
encroachment/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
├── Encroachment_mapping_project.ipynb  # Original analysis notebook
├── data/                          # Data directory (if needed)
│   ├── roads/
│   └── buildings/
├── models/                        # Saved ML models
│   └── rf_encroachment_model.pkl
└── screenshots/                   # Application screenshots
    ├── map_view.png
    ├── analysis_view.png
    └── ml_view.png
```

## 🎓 Academic Information

**Author:** Marylorine Akinyi  
**Institution:** Strathmore University  
**Course:** MSc Data Science & Analytics  
**Project Type:** Spatial Analysis & Web GIS Application

## 🔧 Technology Stack

- **Frontend:** Streamlit
- **Mapping:** Folium, Streamlit-Folium
- **Data Processing:** Pandas, GeoPandas
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Geospatial:** OSMnx, Shapely
- **Machine Learning:** Scikit-learn
- **Deployment:** Streamlit Cloud

## 📈 Future Enhancements

- [ ] Real-time OSM data updates
- [ ] Analysis for all 8 major roads
- [ ] Mobile responsiveness improvements
- [ ] User authentication system
- [ ] Historical trend analysis
- [ ] PDF report generation
- [ ] Integration with county GIS systems
- [ ] Batch prediction upload

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Marylorine Akinyi - Strathmore University

GitHub: [@Lorii143](https://github.com/Lorii143)

Project Link: [https://github.com/Lorii143/encroachment](https://github.com/Lorii143/encroachment)

## 🙏 Acknowledgments

- OpenStreetMap contributors for geospatial data
- Strathmore University for academic support
- Streamlit team for the amazing framework
- Nairobi County Government for road reserve specifications

---

**⭐ If you found this project helpful, please consider giving it a star!**
