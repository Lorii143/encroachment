# 🚀 Deployment Guide

Complete guide to deploying your Nairobi Road Encroachment Mapping System to Streamlit Cloud.

## Prerequisites

- GitHub account
- Git installed on your local machine
- Your project files ready

## Step 1: Prepare Your GitHub Repository

### 1.1 Create a New Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `nairobi-encroachment-mapper` (or your preferred name)
5. Add a description: "Interactive Web GIS for mapping road encroachments in Nairobi"
6. Choose "Public" (required for free Streamlit Cloud deployment)
7. **Do NOT** initialize with README (we already have one)
8. Click "Create repository"

### 1.2 Push Your Code to GitHub

Open your terminal/command prompt in the project directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: Nairobi Encroachment Mapping System"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/nairobi-encroachment-mapper.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

## Step 2: Deploy to Streamlit Cloud

### 2.1 Sign Up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign up" or "Continue with GitHub"
3. Authorize Streamlit to access your GitHub account

### 2.2 Deploy Your App

1. Click the "New app" button
2. Fill in the deployment form:
   - **Repository**: Select `YOUR_USERNAME/nairobi-encroachment-mapper`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Choose a custom subdomain or use the auto-generated one

3. Click "Deploy!"

### 2.3 Wait for Deployment

- Initial deployment takes 5-10 minutes
- You'll see a deployment log showing progress
- The app will automatically start once deployment is complete

## Step 3: Configure Advanced Settings (Optional)

### 3.1 Adjust Python Version

1. In your app settings, click "⋮" (three dots)
2. Select "Settings"
3. Under "Python version", select `3.9` or higher
4. Click "Save"

### 3.2 Increase Memory (If Needed)

For handling large datasets:

1. Go to Settings
2. Under "Resources", increase memory to 1GB or higher
3. Save changes

### 3.3 Set Environment Variables (If Needed)

If you need API keys or secrets:

1. Go to Settings
2. Click "Secrets"
3. Add your secrets in TOML format:
   ```toml
   API_KEY = "your-api-key"
   DATABASE_URL = "your-database-url"
   ```

## Step 4: Verify Deployment

### 4.1 Check Your App

1. Once deployed, click on your app URL
2. Verify all features work:
   - ✅ Map loads correctly
   - ✅ Data loads from OpenStreetMap
   - ✅ All tabs are functional
   - ✅ Charts render properly
   - ✅ Download buttons work

### 4.2 Monitor Logs

1. In Streamlit Cloud, click "Manage app"
2. View logs for any errors
3. Common issues and fixes:
   - **Memory errors**: Increase allocated memory
   - **Module not found**: Check requirements.txt
   - **Timeout errors**: Optimize data loading with caching

## Step 5: Update Your App

### 5.1 Make Changes Locally

```bash
# Make your changes to the code
# Then commit and push

git add .
git commit -m "Description of your changes"
git push origin main
```

### 5.2 Automatic Redeployment

- Streamlit Cloud automatically detects changes
- App will redeploy within 1-2 minutes
- No manual intervention needed!

## Troubleshooting

### Common Issues and Solutions

#### 1. App Won't Load / Timeout Errors

**Problem**: Data loading takes too long

**Solution**:
- Add `@st.cache_data` decorators to functions
- Reduce initial data load
- Use data sampling for preview

#### 2. ModuleNotFoundError

**Problem**: Missing dependencies

**Solution**:
```bash
# Add missing package to requirements.txt
echo "missing-package==version" >> requirements.txt
git add requirements.txt
git commit -m "Add missing dependency"
git push
```

#### 3. Memory Errors

**Problem**: App crashes due to memory limits

**Solution**:
- Increase memory allocation in Streamlit Cloud settings
- Optimize data structures
- Use data chunking

#### 4. Map Not Rendering

**Problem**: Folium map doesn't display

**Solution**:
- Check streamlit-folium version compatibility
- Ensure proper folium initialization
- Check browser console for errors

### Getting Help

If you encounter issues:

1. **Check Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
2. **Streamlit Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
3. **GitHub Issues**: Create an issue in your repository

## Best Practices

### 1. Performance Optimization

```python
# Use caching for expensive operations
@st.cache_data
def load_data():
    # Your data loading code
    return data

# Use session state for user interactions
if 'data' not in st.session_state:
    st.session_state.data = load_data()
```

### 2. Error Handling

```python
try:
    data = load_data()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()
```

### 3. User Feedback

```python
with st.spinner('Loading data...'):
    data = expensive_operation()
    
st.success('Data loaded successfully!')
```

## Monitoring & Analytics

### 1. Built-in Analytics

- Streamlit Cloud provides basic usage analytics
- View in your app dashboard
- Track: visitors, load times, errors

### 2. Custom Analytics (Optional)

Add Google Analytics or other tracking:

```python
# In app.py, add to the HTML header
st.markdown("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
    <!-- GA code -->
""", unsafe_allow_html=True)
```

## Security Considerations

### 1. API Keys & Secrets

- Never commit API keys to GitHub
- Use Streamlit Cloud secrets management
- Access secrets in code:

```python
import streamlit as st
api_key = st.secrets["API_KEY"]
```

### 2. Rate Limiting

- Be mindful of OpenStreetMap usage limits
- Implement caching to reduce API calls
- Consider using OSM data extracts for frequent use

## Scaling Up

### When Your App Grows

1. **Consider Streamlit Cloud Teams** for:
   - Private repositories
   - More resources
   - Better support
   - Custom domains

2. **Alternative Hosting**:
   - AWS EC2
   - Google Cloud Run
   - Heroku
   - DigitalOcean

## Next Steps

After successful deployment:

1. ✅ Share your app URL with stakeholders
2. ✅ Update README with live link
3. ✅ Gather user feedback
4. ✅ Plan feature enhancements
5. ✅ Monitor usage and performance

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [GeoPandas Documentation](https://geopandas.org/)

---

**Congratulations! Your app is now live! 🎉**

Share your app URL:
`https://your-app-name.streamlit.app`
