# Air Quality Study in Valencia (2019–2024)

This project analyzes the impact of traffic, meteorology, building emissions, and green spaces on air quality in the city of Valencia, using a comprehensive and multidisciplinary approach.

> Project developed within the framework of the **Project II** course of the Bachelor's Degree in Data Science (ETSINF - UPV).

---

## Authors

- Adriá Aguilar
- Pablo Gandía
- Santiago Font
- Fernando Martínez
- Sergio Ortiz

**Supervisors:** Sara Blanc Clavero, Mª José Ramírez Quintana

---

## Project Objectives

1. **Analyze atmospheric pollution** by zones and specific pollutants.
2. **Study the influence of meteorological factors** on pollution levels.
3. **Characterize traffic** in Valencia and its polluting impact.
4. **Examine CO₂ emissions** from buildings and their relationship with pollution.
5. **Investigate common patterns** between green spaces, weather conditions, and air quality.

---

---

## Tools and Technologies

- **Languages**: R, Python
- **Web Scraping**: BeautifulSoup, Selenium, Requests
- **Analysis**: PCA, Clustering, PLS, Association Rules
- **Visualization**: ggplot2, leaflet, heatmaps, boxplots
- **Version Control**: Git, GitHub
- **Other Tools**: Discord, RStudio, Jupyter Notebooks

---

## Data Sources

- [Atmospheric and meteorological stations (GVA, AVAMET, Tiempo3)](https://valencia.opendatasoft.com/)
- **Traffic data**: Provided by ETRA and the Valencia City Council (non-public).
- **Energy Efficiency Certificates** and cadastral references (GVA, Cadastre).
- **Green spaces** in Valencia.

---

## Key Results by Objective

### Objective 1: Pollutants
- Temporal and spatial analysis of NO, NO₂, NOx, O₃, PM10, PM2.5, SO₂, and CO.
- Detection of hourly, weekly, and seasonal patterns.
- PCA and hierarchical clustering to analyze relationships between pollutants.

### Objective 2: Meteorology
- PCA and clustering on meteorological conditions (temperature, wind, humidity, etc.).
- PLS models to quantify the climate ↔ pollution relationship.

### Objective 3: Traffic
- Hourly traffic analysis based on inductive loop detectors (1,129 sensors).
- Clustering of road types.
- Correlations and joint patterns with pollutants.

### Objective 4: Buildings and CO₂
- Calculation of CO₂ emissions per m² based on energy certificates.
- Grouping of properties and plots by energy behavior.
- Relationship with pollution stations using Voronoi diagrams.

### Objective 5: Green Zones and Associations
- Association rules between meteorology and air quality.
- Spatial analysis of green zones and their correlation with pollutants.

---

## Conclusions

- Significant relationships are observed between air quality and factors such as traffic, weather, and energy emissions.
- Areas with worse conditions tend to coincide with lower energy efficiency and high traffic density.
- The study offers a solid basis for urban, environmental, and public health recommendations.

---

## Lessons Learned

- The importance of validating data viability before defining objectives.
- Version control and efficient collaboration accelerate development.
- Deepening context understanding before analysis is key to avoiding interpretation errors.
- AI can assist, but it does not replace a true understanding of the project.
