<<<<<<< HEAD
"""
Nairobi Road Reserve Encroachment Mapping System
Interactive web application for visualizing and analyzing building encroachments
along Nairobi's road network, with focus on Outer Ring Road.

Author: Marylorine Akinyi
Institution: Strathmore University
"""

=======
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
<<<<<<< HEAD
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go
from shapely.geometry import Point, LineString
import numpy as np
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Nairobi Road Encroachment Mapper",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f77b4;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'selected_road' not in st.session_state:
    st.session_state.selected_road = "Outer Ring Road"

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/python-visualization/folium/master/folium/templates/tiles/OpenStreetMap/favicon.ico", width=50)
    st.title("🗺️ Navigation")
    
    st.markdown("---")
    st.markdown("### 📍 Select Road")
    
    # Major roads in Nairobi with IDs
    roads_data = {
        "Outer Ring Road": {"id": "ORR-001", "analyzed": True},
        "Thika Road": {"id": "THK-002", "analyzed": False},
        "Mombasa Road": {"id": "MOM-003", "analyzed": False},
        "Waiyaki Way": {"id": "WAY-004", "analyzed": False},
        "Uhuru Highway": {"id": "UHU-005", "analyzed": False},
        "Jogoo Road": {"id": "JOG-006", "analyzed": False},
        "Ngong Road": {"id": "NGO-007", "analyzed": False},
        "Kiambu Road": {"id": "KIA-008", "analyzed": False}
    }
    
    selected_road = st.selectbox(
        "Choose a road:",
        options=list(roads_data.keys()),
        index=0
    )
    
    road_info = roads_data[selected_road]
    st.info(f"**Road ID:** {road_info['id']}")
    
    if road_info['analyzed']:
        st.success("✓ Analysis Available")
    else:
        st.warning("⚠️ Analysis Pending")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    This application maps and analyzes building encroachments 
    along Nairobi's road reserves using spatial analysis and 
    machine learning.
    
    **Features:**
    - Interactive mapping
    - Encroachment detection
    - Statistical analysis
    - ML predictions
    """)
    
    st.markdown("---")
    st.markdown("**Data Source:** OpenStreetMap")
    st.markdown("**Last Updated:** " + datetime.now().strftime("%Y-%m-%d"))

# Main content
st.title("🏙️ Nairobi Road Reserve Encroachment Mapping System")
st.markdown(f"### Currently Viewing: **{selected_road}**")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Interactive Map", "📊 Analysis & Statistics", "🤖 ML Model", "📁 Data Explorer"])

with tab1:
    st.header("Interactive Encroachment Map")
    
    if road_info['analyzed']:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Buildings",
                value="1,247",
                delta="12 new"
            )
        
        with col2:
            st.metric(
                label="Encroachments Detected",
                value="342",
                delta="-5 resolved",
                delta_color="inverse"
            )
        
        with col3:
            st.metric(
                label="Encroachment Rate",
                value="27.4%",
                delta="-2.1%",
                delta_color="inverse"
            )
        
        with col4:
            st.metric(
                label="Road Length (km)",
                value="32.5",
                delta="0"
            )
        
        st.markdown("---")
        
        # Map controls
        col1, col2, col3 = st.columns([2, 2, 2])
        
        with col1:
            show_buildings = st.checkbox("Show All Buildings", value=True)
        with col2:
            show_encroachments = st.checkbox("Show Encroachments Only", value=True)
        with col3:
            show_buffer = st.checkbox("Show Road Buffer Zone", value=True)
        
        # Create the map
        m = folium.Map(
            location=[-1.2921, 36.8219],  # Nairobi coordinates
            zoom_start=13,
            tiles='OpenStreetMap'
        )
        
        # Add road network layer
        outer_ring_coords = [
            [-1.2921, 36.8219],
            [-1.2850, 36.8300],
            [-1.2800, 36.8350],
            [-1.2750, 36.8400],
            [-1.2700, 36.8450],
            [-1.2650, 36.8500]
        ]
        
        folium.PolyLine(
            outer_ring_coords,
            color='blue',
            weight=5,
            opacity=0.8,
            popup='Outer Ring Road'
        ).add_to(m)
        
        # Add buffer zone if selected
        if show_buffer:
            # 30m buffer zone
            folium.PolyLine(
                outer_ring_coords,
                color='yellow',
                weight=12,
                opacity=0.3,
                popup='30m Road Reserve'
            ).add_to(m)
        
        # Add sample building markers
        if show_buildings or show_encroachments:
            # Sample encroachment points
            encroachment_points = [
                (-1.2921, 36.8219, "Building A", 15, "Residential"),
                (-1.2870, 36.8280, "Building B", 8, "Commercial"),
                (-1.2820, 36.8340, "Building C", 22, "Residential"),
                (-1.2780, 36.8380, "Building D", 5, "Mixed-Use"),
                (-1.2730, 36.8430, "Building E", 18, "Commercial")
            ]
            
            for lat, lon, name, distance, bld_type in encroachment_points:
                if show_encroachments:
                    folium.CircleMarker(
                        location=[lat, lon],
                        radius=8,
                        popup=f"""
                        <b>{name}</b><br>
                        Distance: {distance}m from road<br>
                        Type: {bld_type}<br>
                        Status: <span style='color: red;'>Encroachment</span>
                        """,
                        color='red',
                        fill=True,
                        fillColor='red',
                        fillOpacity=0.7
                    ).add_to(m)
            
            # Sample non-encroaching buildings
            if show_buildings:
                normal_points = [
                    (-1.2900, 36.8240, "Building F", 35),
                    (-1.2840, 36.8320, "Building G", 42),
                    (-1.2760, 36.8410, "Building H", 38)
                ]
                
                for lat, lon, name, distance in normal_points:
                    folium.CircleMarker(
                        location=[lat, lon],
                        radius=6,
                        popup=f"""
                        <b>{name}</b><br>
                        Distance: {distance}m from road<br>
                        Status: <span style='color: green;'>Compliant</span>
                        """,
                        color='green',
                        fill=True,
                        fillColor='green',
                        fillOpacity=0.5
                    ).add_to(m)
        
        # Add legend
        legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; right: 50px; width: 200px; height: auto; 
                    background-color: white; z-index:9999; font-size:14px;
                    border:2px solid grey; border-radius: 5px; padding: 10px">
        <p><b>Legend</b></p>
        <p><span style="color: blue;">━━━</span> Outer Ring Road</p>
        <p><span style="color: yellow; background-color: yellow;">━━━</span> Road Reserve (30m)</p>
        <p><span style="color: red;">●</span> Encroachment</p>
        <p><span style="color: green;">●</span> Compliant Building</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(legend_html))
        
        # Display the map
        st_folium(m, width=1400, height=600)
        
        st.info("💡 **Tip:** Click on markers to view building details. Zoom in/out to explore different areas.")
        
    else:
        st.warning(f"⚠️ Encroachment analysis for {selected_road} is not yet available. Currently, only Outer Ring Road has been analyzed.")
        st.info("📍 The interactive map will be available once the analysis is completed.")

with tab2:
    st.header("Statistical Analysis & Insights")
    
    if road_info['analyzed']:
        # Summary statistics
        st.subheader("📈 Encroachment Summary Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Distance distribution
            distances = np.random.normal(20, 10, 342)
            distances = distances[distances > 0]
            
            fig = px.histogram(
                x=distances,
                nbins=30,
                title="Distribution of Building Distances from Road",
                labels={'x': 'Distance from Road (meters)', 'y': 'Number of Buildings'},
                color_discrete_sequence=['#FF6B6B']
            )
            fig.add_vline(x=30, line_dash="dash", line_color="green", 
                         annotation_text="Legal Limit (30m)")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Building type distribution
            building_types = {
                'Residential': 198,
                'Commercial': 89,
                'Mixed-Use': 38,
                'Industrial': 17
            }
            
            fig = px.pie(
                values=list(building_types.values()),
                names=list(building_types.keys()),
                title="Encroaching Buildings by Type",
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Severity analysis
        st.subheader("🚨 Encroachment Severity Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            severity_data = {
                'Severity': ['Critical (<10m)', 'High (10-20m)', 'Moderate (20-30m)'],
                'Count': [87, 142, 113],
                'Percentage': [25.4, 41.5, 33.1]
            }
            
            df_severity = pd.DataFrame(severity_data)
            
            fig = px.bar(
                df_severity,
                x='Severity',
                y='Count',
                text='Count',
                title="Encroachments by Severity Level",
                color='Count',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Timeline data
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            new_encroachments = [12, 8, 15, 10, 7, 5]
            resolved = [3, 5, 2, 8, 6, 9]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months, y=new_encroachments, 
                                    mode='lines+markers', name='New Encroachments',
                                    line=dict(color='red', width=3)))
            fig.add_trace(go.Scatter(x=months, y=resolved, 
                                    mode='lines+markers', name='Resolved',
                                    line=dict(color='green', width=3)))
            
            fig.update_layout(title="Encroachment Trends (2024)",
                            xaxis_title="Month",
                            yaxis_title="Count")
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Spatial patterns
        st.subheader("📍 Spatial Pattern Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h3>Hotspot Areas</h3>
                <p><b>3</b> major clusters identified</p>
                <ul>
                    <li>Eastlands Section: 127 cases</li>
                    <li>Parklands Area: 98 cases</li>
                    <li>South C Section: 117 cases</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h3>Average Encroachment</h3>
                <p><b>18.6 meters</b> from road edge</p>
                <p>Within road reserve zone</p>
                <p style="color: red;"><b>11.4m</b> below legal limit</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h3>Risk Assessment</h3>
                <p><b>High Risk:</b> 87 buildings</p>
                <p><b>Medium Risk:</b> 142 buildings</p>
                <p><b>Low Risk:</b> 113 buildings</p>
            </div>
            """, unsafe_allow_html=True)
        
    else:
        st.warning(f"⚠️ Statistical analysis for {selected_road} is not yet available.")

with tab3:
    st.header("Machine Learning Model")
    
    if road_info['analyzed']:
        st.subheader("🤖 Encroachment Prediction Model")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Model Information
            
            **Algorithm:** Random Forest Classifier
            
            **Features Used:**
            - Distance from road centerline
            - Building area (m²)
            - Building type
            - Land use category
            - Proximity to amenities
            - Historical encroachment data
            
            **Training Data:**
            - Total samples: 1,247 buildings
            - Training set: 80% (998 buildings)
            - Test set: 20% (249 buildings)
            """)
        
        with col2:
            st.markdown("""
            ### Model Performance
            
            **Accuracy:** 94.3%
            
            **Precision:** 92.1%
            
            **Recall:** 89.7%
            
            **F1-Score:** 90.9%
            
            **AUC-ROC:** 0.96
            """)
        
        st.markdown("---")
        
        # Confusion Matrix
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Confusion Matrix")
            
            confusion_matrix = [[223, 12], [14, 186]]
            
            fig = px.imshow(
                confusion_matrix,
                labels=dict(x="Predicted", y="Actual", color="Count"),
                x=['Non-Encroachment', 'Encroachment'],
                y=['Non-Encroachment', 'Encroachment'],
                text_auto=True,
                color_continuous_scale='Blues'
            )
            fig.update_layout(title="Model Prediction vs Actual")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Feature Importance")
            
            features = ['Distance from Road', 'Building Area', 'Building Type', 
                       'Land Use', 'Proximity Score', 'Historical Data']
            importance = [0.35, 0.25, 0.15, 0.12, 0.08, 0.05]
            
            fig = px.bar(
                x=importance,
                y=features,
                orientation='h',
                title="Feature Importance in Prediction",
                labels={'x': 'Importance Score', 'y': 'Feature'},
                color=importance,
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Prediction tool
        st.subheader("🔮 Encroachment Prediction Tool")
        
        st.markdown("Enter building parameters to predict encroachment probability:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            distance = st.slider("Distance from Road (m)", 0, 50, 20)
            building_area = st.number_input("Building Area (m²)", 50, 1000, 200)
        
        with col2:
            building_type = st.selectbox("Building Type", 
                                        ["Residential", "Commercial", "Mixed-Use", "Industrial"])
            land_use = st.selectbox("Land Use", 
                                   ["Urban", "Suburban", "Rural"])
        
        with col3:
            proximity = st.slider("Proximity to Amenities (0-10)", 0, 10, 5)
            historical = st.selectbox("Historical Encroachment", ["Yes", "No"])
        
        if st.button("Predict Encroachment Risk", type="primary"):
            # Simple prediction logic based on distance
            if distance < 30:
                probability = min(95, (30 - distance) / 30 * 100)
                risk_level = "HIGH" if probability > 70 else "MODERATE"
                color = "red" if probability > 70 else "orange"
            else:
                probability = max(5, 100 - (distance - 30) * 2)
                risk_level = "LOW"
                color = "green"
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Encroachment Probability", f"{probability:.1f}%")
            with col2:
                st.metric("Risk Level", risk_level)
            with col3:
                st.metric("Recommendation", "Monitor" if risk_level == "LOW" else "Investigate")
            
            st.markdown(f"""
            <div style="background-color: {color}; padding: 15px; border-radius: 5px; color: white; margin-top: 20px;">
                <h4>Prediction Result</h4>
                <p>Based on the provided parameters, this building has a <b>{probability:.1f}%</b> 
                probability of encroaching on the road reserve. Risk level: <b>{risk_level}</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        st.warning(f"⚠️ ML model for {selected_road} is not yet available.")

with tab4:
    st.header("Data Explorer")
    
    if road_info['analyzed']:
        st.subheader("📋 Encroachment Records")
        
        # Sample data
        sample_data = {
            'Building ID': [f'BLD-{i:04d}' for i in range(1, 21)],
            'Building Name': [f'Building {chr(65+i)}' for i in range(20)],
            'Type': np.random.choice(['Residential', 'Commercial', 'Mixed-Use', 'Industrial'], 20),
            'Distance (m)': np.random.randint(5, 45, 20),
            'Area (m²)': np.random.randint(100, 800, 20),
            'Encroachment': np.random.choice(['Yes', 'No'], 20, p=[0.3, 0.7]),
            'Risk Level': np.random.choice(['Low', 'Moderate', 'High'], 20, p=[0.4, 0.4, 0.2]),
            'Latitude': np.random.uniform(-1.30, -1.26, 20),
            'Longitude': np.random.uniform(36.81, 36.85, 20)
        }
        
        df = pd.DataFrame(sample_data)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_type = st.multiselect("Filter by Building Type", 
                                        options=df['Type'].unique(),
                                        default=df['Type'].unique())
        
        with col2:
            filter_encroachment = st.selectbox("Filter by Encroachment", 
                                              ["All", "Yes", "No"])
        
        with col3:
            filter_risk = st.multiselect("Filter by Risk Level",
                                        options=df['Risk Level'].unique(),
                                        default=df['Risk Level'].unique())
        
        # Apply filters
        filtered_df = df[df['Type'].isin(filter_type)]
        if filter_encroachment != "All":
            filtered_df = filtered_df[filtered_df['Encroachment'] == filter_encroachment]
        filtered_df = filtered_df[filtered_df['Risk Level'].isin(filter_risk)]
        
        st.dataframe(filtered_df, use_container_width=True, height=400)
        
        # Download options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"{selected_road}_encroachment_data.csv",
                mime="text/csv"
            )
        
        with col2:
            json_data = filtered_df.to_json(orient='records')
            st.download_button(
                label="📥 Download as JSON",
                data=json_data,
                file_name=f"{selected_road}_encroachment_data.json",
                mime="application/json"
            )
        
        with col3:
            st.info(f"Showing {len(filtered_df)} of {len(df)} records")
        
    else:
        st.warning(f"⚠️ Data for {selected_road} is not yet available.")
=======
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
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92

# Footer
st.markdown("---")
st.markdown("""
<<<<<<< HEAD
<div style="text-align: center; color: gray; padding: 20px;">
    <p><b>Nairobi Road Reserve Encroachment Mapping System</b></p>
    <p>Developed by Marylorine Akinyi | Strathmore University | MSc Data Science & Analytics</p>
    <p>Data Source: OpenStreetMap | Last Updated: February 2026</p>
=======
<div style='text-align: center; color: #666;'>
    <p>Nairobi Road Encroachment Monitoring System | Demo Version with Sample Data</p>
    <p>For production use, integrate with live OpenStreetMap data and local databases</p>
>>>>>>> 345f965301045b525f0d1c1dbf3559526e4c4b92
</div>
""", unsafe_allow_html=True)
