import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static
from shapely.geometry import Point, LineString
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Nairobi Road Encroachment Mapper",
    page_icon="🗺️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🗺️ Nairobi Road Encroachment Mapper</div>', unsafe_allow_html=True)
st.markdown("**Real-time monitoring and analysis of road encroachments in Nairobi**")

# Sample data function (lightweight)
@st.cache_data
def load_sample_data():
    """Generate sample encroachment data for demonstration"""
    np.random.seed(42)
    
    # Sample coordinates around Nairobi (Outer Ring Road area)
    n_points = 50
    lat_base = -1.2921
    lon_base = 36.8219
    
    data = {
        'id': range(1, n_points + 1),
        'latitude': lat_base + np.random.uniform(-0.05, 0.05, n_points),
        'longitude': lon_base + np.random.uniform(-0.05, 0.05, n_points),
        'distance_to_road_m': np.random.uniform(0, 45, n_points),
        'building_type': np.random.choice(['Residential', 'Commercial', 'Industrial', 'Mixed'], n_points),
        'estimated_date': pd.date_range(start='2020-01-01', periods=n_points, freq='W')
    }
    
    df = pd.DataFrame(data)
    
    # Add severity classification
    def classify_severity(distance):
        if distance < 5:
            return 'Low'
        elif distance < 15:
            return 'Moderate'
        elif distance < 30:
            return 'High'
        else:
            return 'Critical'
    
    df['severity'] = df['distance_to_road_m'].apply(classify_severity)
    df['encroachment_depth_m'] = np.maximum(0, 50 - df['distance_to_road_m'])
    df['area_m2'] = df['encroachment_depth_m'] * np.random.uniform(10, 30, n_points)
    
    return df

# Load data
with st.spinner('Loading data...'):
    df = load_sample_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
severity_filter = st.sidebar.multiselect(
    "Severity Level",
    options=['Critical', 'High', 'Moderate', 'Low'],
    default=['Critical', 'High', 'Moderate', 'Low']
)

building_filter = st.sidebar.multiselect(
    "Building Type",
    options=df['building_type'].unique(),
    default=df['building_type'].unique()
)

# Apply filters
filtered_df = df[
    (df['severity'].isin(severity_filter)) &
    (df['building_type'].isin(building_filter))
]

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📍 Total Encroachments", len(filtered_df))
with col2:
    critical = len(filtered_df[filtered_df['severity'] == 'Critical'])
    st.metric("⚠️ Critical Cases", critical)
with col3:
    avg_depth = filtered_df['encroachment_depth_m'].mean()
    st.metric("📏 Avg Depth (m)", f"{avg_depth:.1f}")
with col4:
    total_area = filtered_df['area_m2'].sum()
    st.metric("🏗️ Total Area (m²)", f"{total_area:,.0f}")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Interactive Map", "📊 Analytics", "🔮 Insights", "📥 Data Export"])

with tab1:
    st.subheader("Interactive Encroachment Map")
    
    # Create map
    center_lat = filtered_df['latitude'].mean()
    center_lon = filtered_df['longitude'].mean()
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles='OpenStreetMap'
    )
    
    # Add markers
    severity_colors = {
        'Critical': 'red',
        'High': 'orange',
        'Moderate': 'yellow',
        'Low': 'green'
    }
    
    for idx, row in filtered_df.iterrows():
        popup_text = f"""
        <b>ID:</b> {row['id']}<br>
        <b>Severity:</b> {row['severity']}<br>
        <b>Distance:</b> {row['distance_to_road_m']:.1f}m<br>
        <b>Depth:</b> {row['encroachment_depth_m']:.1f}m<br>
        <b>Type:</b> {row['building_type']}<br>
        <b>Area:</b> {row['area_m2']:.0f}m²
        """
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            popup=folium.Popup(popup_text, max_width=200),
            color=severity_colors.get(row['severity'], 'gray'),
            fill=True,
            fillColor=severity_colors.get(row['severity'], 'gray'),
            fillOpacity=0.7
        ).add_to(m)
    
    folium_static(m, width=1200, height=600)

with tab2:
    st.subheader("Statistical Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Severity distribution
        severity_counts = filtered_df['severity'].value_counts()
        fig1 = px.pie(
            values=severity_counts.values,
            names=severity_counts.index,
            title="Severity Distribution",
            color=severity_counts.index,
            color_discrete_map={'Critical': '#d62728', 'High': '#ff7f0e', 'Moderate': '#ffbb00', 'Low': '#2ca02c'}
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Building type distribution
        building_counts = filtered_df['building_type'].value_counts()
        fig2 = px.bar(
            x=building_counts.index,
            y=building_counts.values,
            title="Encroachments by Building Type",
            labels={'x': 'Building Type', 'y': 'Count'}
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Encroachment depth histogram
        fig3 = px.histogram(
            filtered_df,
            x='encroachment_depth_m',
            nbins=20,
            title="Distribution of Encroachment Depth",
            labels={'encroachment_depth_m': 'Depth (m)', 'count': 'Frequency'}
        )
        st.plotly_chart(fig3, use_container_width=True)
        
        # Scatter plot
        fig4 = px.scatter(
            filtered_df,
            x='distance_to_road_m',
            y='area_m2',
            color='severity',
            size='encroachment_depth_m',
            title="Distance vs Area by Severity",
            labels={'distance_to_road_m': 'Distance to Road (m)', 'area_m2': 'Area (m²)'},
            color_discrete_map={'Critical': '#d62728', 'High': '#ff7f0e', 'Moderate': '#ffbb00', 'Low': '#2ca02c'}
        )
        st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("🔮 Key Insights & Recommendations")
    
    critical_pct = (critical / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
    
    st.info(f"""
    **Current Status:**
    - {critical_pct:.1f}% of encroachments are classified as Critical
    - Most affected building type: {filtered_df['building_type'].mode()[0] if len(filtered_df) > 0 else 'N/A'}
    - Average encroachment depth: {avg_depth:.1f} meters
    """)
    
    st.warning("""
    **Recommended Actions:**
    1. Prioritize Critical severity cases for immediate action
    2. Conduct detailed surveys in high-density encroachment areas
    3. Implement early warning systems for new constructions
    4. Strengthen enforcement of Right of Way regulations
    """)
    
    # Timeline
    if len(filtered_df) > 0:
        timeline = filtered_df.groupby(filtered_df['estimated_date'].dt.to_period('M')).size()
        fig_timeline = px.line(
            x=timeline.index.astype(str),
            y=timeline.values,
            title="Encroachment Trend Over Time",
            labels={'x': 'Month', 'y': 'New Encroachments'}
        )
        st.plotly_chart(fig_timeline, use_container_width=True)

with tab4:
    st.subheader("📥 Export Data")
    
    st.write("Download filtered data for further analysis:")
    
    col1, col2 = st.columns(2)
    with col1:
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📄 Download as CSV",
            data=csv,
            file_name=f"encroachments_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col2:
        st.write(f"**Rows:** {len(filtered_df)}")
        st.write(f"**Columns:** {len(filtered_df.columns)}")
    
    st.dataframe(filtered_df, use_container_width=True, height=400)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Nairobi Road Encroachment Monitoring System | Demo Version with Sample Data</p>
    <p>For production use, integrate with live OpenStreetMap data and local databases</p>
</div>
""", unsafe_allow_html=True)
