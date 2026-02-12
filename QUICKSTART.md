# ⚡ Quick Start Guide

Get the Nairobi Road Encroachment Mapping System running in 5 minutes!

## 🎯 For First-Time Users

### Option 1: Quick Run (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lorii143/encroachment.git
   cd encroachment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - Automatically opens at `http://localhost:8501`
   - If not, manually navigate to the URL shown in terminal

### Option 2: Using Virtual Environment (Best Practice)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lorii143/encroachment.git
   cd encroachment
   ```

2. **Create virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 🖥️ System Requirements

- **Python:** 3.8 or higher
- **RAM:** Minimum 4GB (8GB recommended)
- **Storage:** 500MB free space
- **Internet:** Required for map tiles

## 🎨 Using the Application

### Navigation

1. **Select Road:** Use the sidebar dropdown to choose which road to analyze
2. **Explore Tabs:**
   - 🗺️ **Interactive Map:** View encroachments on the map
   - 📊 **Analysis:** See statistics and trends
   - 🤖 **ML Model:** Use predictive tools
   - 📁 **Data Explorer:** Browse and download data

### Interactive Map Features

- **Zoom:** Use mouse wheel or +/- buttons
- **Pan:** Click and drag the map
- **Marker Info:** Click on markers to see building details
- **Toggle Layers:** Use checkboxes to show/hide layers

### Making Predictions

1. Go to **ML Model** tab
2. Scroll to **Prediction Tool**
3. Enter building parameters
4. Click **Predict** button
5. View results and recommendations

### Exporting Data

1. Go to **Data Explorer** tab
2. Apply filters as needed
3. Click **Download as CSV** or **Download as JSON**
4. File saves to your Downloads folder

## 🔧 Troubleshooting

### App Won't Start?

**Error: "Module not found"**
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

**Error: "Port already in use"**
```bash
# Use different port
streamlit run app.py --server.port 8502
```

**Error: "Python version"**
```bash
# Check Python version
python --version  # Should be 3.8+
```

### Map Not Loading?

- ✅ Check internet connection
- ✅ Refresh browser (F5)
- ✅ Clear browser cache
- ✅ Try different browser

### Performance Issues?

- ✅ Close other applications
- ✅ Reduce browser tabs
- ✅ Restart the app
- ✅ Check system resources

## 📱 Accessing the Live Demo

Don't want to run locally? Access the live version:

🌐 **Live App:** https://lorii143-encroachment-app.streamlit.app

## 🆘 Getting Help

### Documentation
- 📖 [Full README](README.md)
- 🚀 [Deployment Guide](DEPLOYMENT.md)
- 📊 [Jupyter Notebook](Encroachment_mapping_project.ipynb)

### Support
- 💬 Open an issue on GitHub
- 📧 Contact: [Your Email]
- 🎓 Academic Support: Strathmore University

## 🎓 For Academic Use

### Citing This Work

If using this project for academic purposes:

```
Akinyi, M. (2024). Nairobi Road Reserve Encroachment Mapping System. 
MSc Data Science & Analytics, Strathmore University.
GitHub: https://github.com/Lorii143/encroachment
```

### Presentation Tips

1. **Demo the Live Site:** Show real-time interaction
2. **Explain the Analysis:** Walk through statistical insights
3. **Showcase ML Model:** Demonstrate predictions
4. **Discuss Impact:** Urban planning implications

## 🚀 Next Steps

After getting the app running:

1. ✅ Explore all features
2. ✅ Try the prediction tool
3. ✅ Download sample data
4. ✅ Read the full documentation
5. ✅ Consider deploying your own version

## 📊 Sample Workflows

### Workflow 1: Quick Analysis
1. Open app
2. Select "Outer Ring Road"
3. View map
4. Check statistics in Analysis tab
5. Export data

### Workflow 2: Make Predictions
1. Navigate to ML Model tab
2. Enter building parameters
3. Click Predict
4. Review risk assessment
5. Save results

### Workflow 3: Data Export
1. Go to Data Explorer
2. Apply filters (type, risk, etc.)
3. Review filtered results
4. Download as CSV
5. Use in your analysis

## ⚙️ Advanced Configuration

### Change Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor="#your-color"
backgroundColor="#your-color"
```

### Add Custom Data

1. Prepare your GeoJSON/CSV
2. Modify data loading in `app.py`
3. Update visualizations
4. Test locally
5. Deploy

### Extend Functionality

- Add new roads
- Integrate additional data sources
- Customize ML models
- Add new visualization types

## 🎉 You're Ready!

Your Nairobi Road Encroachment Mapping System is now running. 

**Happy mapping! 🗺️**

---

*Last updated: February 2026*
