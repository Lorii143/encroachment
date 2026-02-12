# 🚀 Deployment Guide - Step by Step

This guide will walk you through deploying your Nairobi Road Encroachment Mapping System to Streamlit Cloud.

## 📋 Prerequisites

Before you begin, make sure you have:
- ✅ A GitHub account
- ✅ Git installed on your computer
- ✅ Your project files ready

## 🔧 Step 1: Prepare Your Local Repository

### 1.1 Navigate to Your Project Directory

```bash
cd /path/to/your/project
```

### 1.2 Initialize Git (if not already done)

```bash
git init
```

### 1.3 Add All Files

```bash
git add .
```

### 1.4 Commit Your Changes

```bash
git commit -m "Initial commit - Nairobi Road Encroachment Mapping System"
```

## 🌐 Step 2: Push to GitHub

### 2.1 Create a New Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Repository name: `encroachment`
5. Description: "Interactive web application for mapping road encroachments in Nairobi"
6. Choose **Public** (required for free Streamlit Cloud deployment)
7. **Do NOT** initialize with README (you already have one)
8. Click **"Create repository"**

### 2.2 Link Your Local Repo to GitHub

```bash
git remote add origin https://github.com/Lorii143/encroachment.git
git branch -M main
git push -u origin main
```

## ☁️ Step 3: Deploy to Streamlit Cloud

### 3.1 Go to Streamlit Cloud

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub account

### 3.2 Create New App

1. Click **"New app"** button
2. Fill in the deployment settings:
   - **Repository:** `Lorii143/encroachment`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (optional):** `nairobi-encroachment` (or leave default)

### 3.3 Advanced Settings (Optional)

Click "Advanced settings" if you need to:
- Set Python version (3.8+)
- Add secrets/environment variables
- Configure custom subdomain

### 3.4 Deploy!

1. Click **"Deploy!"**
2. Wait 2-5 minutes for deployment
3. Your app will be live at: `https://[your-app-name].streamlit.app`

## 🔄 Step 4: Update Your Deployed App

Whenever you make changes to your code:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Streamlit Cloud will automatically detect changes and redeploy your app!

## 🐛 Step 5: Troubleshooting

### App Not Loading?

**Check the logs:**
1. Go to your app on Streamlit Cloud
2. Click **"Manage app"** in bottom right
3. View **"Logs"** tab for errors

### Common Issues:

#### Issue 1: Module Not Found
**Solution:** Ensure all packages are in `requirements.txt`

#### Issue 2: Memory Limit Exceeded
**Solution:** Optimize data loading, use caching with `@st.cache_data`

#### Issue 3: App Keeps Restarting
**Solution:** Check for infinite loops or heavy computations

## 🎨 Step 6: Customize Your Deployment

### Add Custom Domain (Optional)

1. Go to app settings in Streamlit Cloud
2. Click "Settings" → "General"
3. Add your custom domain
4. Follow DNS configuration instructions

### Add Secrets

For API keys or sensitive data:

1. Go to app settings
2. Click "Secrets"
3. Add secrets in TOML format:
```toml
[passwords]
api_key = "your-secret-key"
```

Access in app:
```python
import streamlit as st
api_key = st.secrets["passwords"]["api_key"]
```

## 📊 Step 7: Monitor Your App

### View Analytics

1. Go to Streamlit Cloud dashboard
2. Select your app
3. View metrics:
   - **Active users**
   - **App usage**
   - **Resource consumption**

### App Health

Check:
- ✅ Uptime status
- ✅ Response times
- ✅ Error rates

## 🔐 Step 8: App Management

### Restart App

If needed:
1. Go to app settings
2. Click **"Reboot app"**

### Delete App

To remove:
1. Go to app settings
2. Click **"Delete app"**
3. Confirm deletion

## 📱 Step 9: Share Your App

Your app URL will be:
```
https://lorii143-encroachment-app.streamlit.app
```

Share it:
- 📧 Via email
- 🐦 On social media
- 📄 In your documentation
- 🎓 In your academic presentation

## 🎯 Step 10: Best Practices

### Performance Optimization

```python
# Use caching for expensive operations
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

# Use session state for persistent data
if 'data' not in st.session_state:
    st.session_state.data = load_data()
```

### Version Control

- ✅ Commit frequently with clear messages
- ✅ Use branches for new features
- ✅ Tag releases (v1.0, v1.1, etc.)

### Security

- ✅ Never commit API keys or passwords
- ✅ Use Streamlit secrets for sensitive data
- ✅ Validate user inputs
- ✅ Sanitize data before display

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Forum](https://discuss.streamlit.io)
- [GitHub Docs](https://docs.github.com)

## 🆘 Need Help?

- **Streamlit Community:** [discuss.streamlit.io](https://discuss.streamlit.io)
- **GitHub Issues:** Create an issue in your repository
- **Email Support:** Contact Streamlit support

## ✅ Deployment Checklist

Before deploying, ensure:

- [ ] All files committed to GitHub
- [ ] `requirements.txt` is complete and accurate
- [ ] `app.py` runs locally without errors
- [ ] No sensitive data in code
- [ ] README.md is comprehensive
- [ ] .gitignore excludes unnecessary files
- [ ] GitHub repository is public
- [ ] All dependencies are compatible

## 🎉 Success!

Once deployed, your app will be accessible worldwide. Share it with:
- Your academic supervisors
- Nairobi County officials
- Urban planning departments
- Research community
- General public

---

**Good luck with your deployment! 🚀**

If you encounter any issues, refer to the troubleshooting section or reach out to the Streamlit community.
