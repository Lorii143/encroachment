"""
Data Integration Module
Helper functions for loading and processing encroachment data from various sources
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import osmnx as ox
import numpy as np

class EncroachmentDataLoader:
    """
    Load and process encroachment data for the Streamlit application
    """
    
    def __init__(self, road_name="Outer Ring Road", city="Nairobi, Kenya"):
        self.road_name = road_name
        self.city = city
        self.buildings_gdf = None
        self.road_gdf = None
        
    def load_road_network(self):
        """
        Load road network from OpenStreetMap
        """
        try:
            # Get road network for the area
            place_name = f"{self.road_name}, {self.city}"
            
            # Download road network
            G = ox.graph_from_place(place_name, network_type='drive')
            
            # Convert to GeoDataFrame
            self.road_gdf = ox.graph_to_gdfs(G, nodes=False, edges=True)
            
            return self.road_gdf
            
        except Exception as e:
            print(f"Error loading road network: {e}")
            return None
    
    def load_buildings(self, buffer_distance=100):
        """
        Load buildings within buffer distance of the road
        
        Parameters:
        -----------
        buffer_distance : int
            Distance in meters to buffer around the road
        """
        try:
            # Get buildings from OSM
            place_name = f"{self.road_name}, {self.city}"
            
            # Download building footprints
            buildings = ox.geometries_from_place(
                place_name,
                tags={'building': True}
            )
            
            self.buildings_gdf = buildings
            
            return self.buildings_gdf
            
        except Exception as e:
            print(f"Error loading buildings: {e}")
            return None
    
    def calculate_distances(self):
        """
        Calculate distance of each building from the road centerline
        """
        if self.road_gdf is None or self.buildings_gdf is None:
            print("Please load road and building data first")
            return None
        
        # Create a unified road geometry
        road_union = self.road_gdf.unary_union
        
        # Calculate distances
        self.buildings_gdf['distance_to_road'] = self.buildings_gdf.geometry.apply(
            lambda x: x.distance(road_union)
        )
        
        return self.buildings_gdf
    
    def identify_encroachments(self, threshold=30):
        """
        Identify buildings that encroach on the road reserve
        
        Parameters:
        -----------
        threshold : int
            Distance threshold in meters (default 30m for Nairobi)
        """
        if 'distance_to_road' not in self.buildings_gdf.columns:
            self.calculate_distances()
        
        # Convert distances from degrees to meters (approximate)
        # 1 degree ≈ 111,000 meters at equator
        self.buildings_gdf['distance_meters'] = (
            self.buildings_gdf['distance_to_road'] * 111000
        )
        
        # Identify encroachments
        self.buildings_gdf['is_encroachment'] = (
            self.buildings_gdf['distance_meters'] < threshold
        )
        
        # Categorize severity
        self.buildings_gdf['severity'] = pd.cut(
            self.buildings_gdf['distance_meters'],
            bins=[0, 10, 20, 30, float('inf')],
            labels=['Critical', 'High', 'Moderate', 'Compliant']
        )
        
        return self.buildings_gdf
    
    def export_to_geojson(self, output_path='encroachment_data.geojson'):
        """
        Export processed data to GeoJSON format
        """
        if self.buildings_gdf is not None:
            self.buildings_gdf.to_file(output_path, driver='GeoJSON')
            print(f"Data exported to {output_path}")
        else:
            print("No data to export")
    
    def export_to_csv(self, output_path='encroachment_data.csv'):
        """
        Export processed data to CSV format
        """
        if self.buildings_gdf is not None:
            # Convert to regular DataFrame (without geometry)
            df = pd.DataFrame(self.buildings_gdf.drop(columns='geometry'))
            
            # Add lat/lon columns
            df['latitude'] = self.buildings_gdf.geometry.centroid.y
            df['longitude'] = self.buildings_gdf.geometry.centroid.x
            
            df.to_csv(output_path, index=False)
            print(f"Data exported to {output_path}")
        else:
            print("No data to export")
    
    def get_summary_statistics(self):
        """
        Generate summary statistics for the analysis
        """
        if self.buildings_gdf is None:
            return None
        
        stats = {
            'total_buildings': len(self.buildings_gdf),
            'total_encroachments': self.buildings_gdf['is_encroachment'].sum(),
            'encroachment_rate': (
                self.buildings_gdf['is_encroachment'].sum() / 
                len(self.buildings_gdf) * 100
            ),
            'mean_distance': self.buildings_gdf['distance_meters'].mean(),
            'median_distance': self.buildings_gdf['distance_meters'].median(),
            'critical_count': (self.buildings_gdf['severity'] == 'Critical').sum(),
            'high_count': (self.buildings_gdf['severity'] == 'High').sum(),
            'moderate_count': (self.buildings_gdf['severity'] == 'Moderate').sum()
        }
        
        return stats


def create_sample_data():
    """
    Create sample data for demonstration purposes
    """
    # Sample building data
    np.random.seed(42)
    n_buildings = 100
    
    # Generate random coordinates around Outer Ring Road
    base_lat = -1.2921
    base_lon = 36.8219
    
    data = {
        'building_id': [f'BLD-{i:04d}' for i in range(1, n_buildings + 1)],
        'latitude': base_lat + np.random.normal(0, 0.01, n_buildings),
        'longitude': base_lon + np.random.normal(0, 0.01, n_buildings),
        'building_type': np.random.choice(
            ['Residential', 'Commercial', 'Mixed-Use', 'Industrial'],
            n_buildings,
            p=[0.5, 0.3, 0.15, 0.05]
        ),
        'area_sqm': np.random.randint(100, 800, n_buildings),
        'distance_to_road': np.random.exponential(25, n_buildings),
    }
    
    df = pd.DataFrame(data)
    
    # Calculate encroachment status
    df['is_encroachment'] = df['distance_to_road'] < 30
    
    # Categorize severity
    df['severity'] = pd.cut(
        df['distance_to_road'],
        bins=[0, 10, 20, 30, float('inf')],
        labels=['Critical', 'High', 'Moderate', 'Compliant']
    )
    
    # Add risk scores
    df['risk_score'] = (30 - df['distance_to_road'].clip(0, 30)) / 30 * 100
    
    return df


# Example usage
if __name__ == "__main__":
    print("Encroachment Data Loader - Example Usage")
    print("=" * 50)
    
    # Option 1: Load real data from OSM
    print("\nOption 1: Load from OpenStreetMap")
    print("-" * 50)
    
    loader = EncroachmentDataLoader()
    
    # Uncomment these lines when you want to load real data
    # print("Loading road network...")
    # road_data = loader.load_road_network()
    
    # print("Loading buildings...")
    # building_data = loader.load_buildings()
    
    # print("Calculating distances...")
    # loader.calculate_distances()
    
    # print("Identifying encroachments...")
    # results = loader.identify_encroachments(threshold=30)
    
    # print("\nSummary Statistics:")
    # stats = loader.get_summary_statistics()
    # for key, value in stats.items():
    #     print(f"{key}: {value}")
    
    # Option 2: Create sample data
    print("\nOption 2: Generate Sample Data")
    print("-" * 50)
    
    sample_df = create_sample_data()
    
    print(f"\nGenerated {len(sample_df)} sample buildings")
    print(f"Encroachments: {sample_df['is_encroachment'].sum()}")
    print(f"Encroachment Rate: {sample_df['is_encroachment'].mean() * 100:.1f}%")
    
    # Save sample data
    sample_df.to_csv('sample_encroachment_data.csv', index=False)
    print("\nSample data saved to 'sample_encroachment_data.csv'")
    
    print("\n" + "=" * 50)
    print("For production use:")
    print("1. Uncomment the OSM data loading code above")
    print("2. Ensure you have internet connection")
    print("3. OSMnx will download real building and road data")
    print("4. Process and export the data for use in Streamlit app")
