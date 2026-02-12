<<<<<<< HEAD
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
=======
# 🗺️ Nairobi Road Encroachment Mapping System

An interactive Web GIS application for mapping and analyzing building encroachments along Nairobi's road reserves, with a focus on the Outer Ring Road.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## 📋 Overview

This system provides comprehensive spatial analysis and visualization of urban road reserve encroachments in Nairobi, Kenya. Using OpenStreetMap data and advanced geospatial analysis, it identifies buildings that encroach on designated road reserves and provides actionable insights for urban planning and enforcement.

### Key Features

- 🗺️ **Interactive Mapping** - Zoom, pan, and explore encroachments with Google Maps-like interface
- 📊 **Statistical Analysis** - Comprehensive charts and metrics on encroachment patterns
- 🤖 **Predictive Modeling** - Machine learning-based risk assessment
- 📍 **Multi-Road Support** - Expandable framework for analyzing major roads across Nairobi
- 📥 **Data Export** - Download analysis results in CSV format
- 🎨 **Drawing Tools** - Add custom annotations and measurements
- 📐 **Measurement Tools** - Measure distances directly on the map

## 🚀 Live Demo

Visit the live application: [Nairobi Encroachment Mapper](https://your-app-url.streamlit.app)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web Interface                    │
├─────────────────────────────────────────────────────────────┤
│  Interactive Map  │  Analytics  │  ML Models  │  Data Explorer│
├─────────────────────────────────────────────────────────────┤
│                    Data Processing Layer                      │
│  • Spatial Analysis (GeoPandas, Shapely)                     │
│  • Visualization (Folium, Plotly)                            │
│  • Machine Learning (Scikit-learn)                           │
├─────────────────────────────────────────────────────────────┤
│                    Data Sources                               │
│  • OpenStreetMap (OSMnx)                                     │
│  • Road Networks                                             │
│  • Building Footprints                                       │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Mapping**: Folium, streamlit-folium
- **Geospatial Analysis**: GeoPandas, OSMnx, Shapely
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn

## 📦 Installation
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92

### Prerequisites

- Python 3.8 or higher
<<<<<<< HEAD
- pip package manager
=======
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92
- Git

### Local Setup

1. **Clone the repository**
<<<<<<< HEAD
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
=======
   ```bash
   git clone https://github.com/yourusername/nairobi-encroachment-mapper.git
   cd nairobi-encroachment-mapper
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
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
   Navigate to `http://localhost:8501`

## 🌐 Deployment on Streamlit Cloud

### Step-by-Step Deployment

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/nairobi-encroachment-mapper.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Configure Settings (Optional)**
   - In Streamlit Cloud, go to App settings
   - Set Python version to 3.9 or higher
   - Adjust memory if needed (recommended: 1GB minimum)

## 📊 Features & Usage

### 1. Interactive Map Tab

The main mapping interface provides:

- **Layer Control**: Toggle between different map styles (Street, Satellite, Light, Dark)
- **Encroachment Visualization**: Color-coded buildings by severity
  - 🔴 Critical: >30m encroachment
  - 🟠 High: 15-30m encroachment
  - 🟡 Moderate: 5-15m encroachment
  - 🟨 Low: <5m encroachment
- **Road Reserve Buffer**: Visual representation of 50m right-of-way
- **Building Details**: Click on any building for detailed information
- **Drawing Tools**: Add custom markers, lines, and shapes
- **Measurement**: Measure distances between points

### 2. Statistical Analysis Tab

Comprehensive analytics including:

- Severity distribution charts
- Building type analysis
- Encroachment depth distribution
- Area vs depth correlation
- Summary statistics

### 3. Predictive Model Tab

Machine learning insights:

- Feature importance analysis
- Risk score distribution
- Correlation matrices
- Model performance metrics

### 4. Data Explorer Tab

Interactive data table with:

- Multi-criteria filtering
- Sortable columns
- Data export functionality
- Real-time statistics

## 🎯 Use Cases

1. **Urban Planning**
   - Identify priority areas for enforcement
   - Plan road expansion projects
   - Assess compliance with building codes

2. **Policy Making**
   - Data-driven decision making
   - Evidence-based policy formulation
   - Resource allocation planning

3. **Research**
   - Academic research on urban development
   - Spatial analysis studies
   - Machine learning applications in GIS

4. **Enforcement**
   - Targeted enforcement campaigns
   - Priority case identification
   - Progress tracking

## 📈 Data Sources

- **Road Networks**: OpenStreetMap via OSMnx
- **Building Footprints**: OpenStreetMap building data
- **Coordinate System**: WGS84 (EPSG:4326) for mapping, UTM 37S (EPSG:32737) for analysis

## 🔧 Configuration

### Adjustable Parameters

In the sidebar, you can configure:

- **Road Selection**: Choose from major Nairobi roads
- **Buffer Distance**: Adjust the right-of-way buffer (20-100m)
- **Building Display**: Toggle all buildings visibility

### Adding New Roads

To analyze additional roads, update the `load_kenya_roads()` function in `app.py`:

```python
kenya_roads = {
    'Your Road Name': {
        'city': 'Nairobi', 
        'type': 'Highway', 
        'analyzed': False
    },
    # ... existing roads
}
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<<<<<<< HEAD
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
=======
## 📝 Future Enhancements

- [ ] Real-time data updates
- [ ] Multi-city support
- [ ] Mobile app version
- [ ] Advanced ML models (deep learning)
- [ ] Integration with government databases
- [ ] Automated reporting system
- [ ] Historical trend analysis
- [ ] 3D building visualization
- [ ] User authentication and roles
- [ ] API for external integrations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

**Marylorine Akinyi**
- Institution: Strathmore University
- Program: MSc Data Science & Analytics
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- OpenStreetMap contributors for the geospatial data
- Streamlit team for the amazing framework
- Strathmore University for academic support
- Nairobi City County for urban planning insights

## 📞 Contact

For questions, suggestions, or collaboration:

- Email: your.email@example.com
- GitHub Issues: [Create an issue](https://github.com/yourusername/nairobi-encroachment-mapper/issues)
- LinkedIn: [Connect with me](https://linkedin.com/in/yourprofile)

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

---

**Built with ❤️ for better urban planning in Nairobi**
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92
