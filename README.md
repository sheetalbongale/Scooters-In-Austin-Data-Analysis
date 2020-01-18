##  Scooters in Austin Data Analysis | JSON-and-team 
### Team Members: Erin Bentley, Jason Jones, Sana Khan, Sheetal Bongale
#### UT Data Analysis & Visualization Bootcamp | Python Project 1 | January 2020
---
![Austin Scooter](resources/austin.png)

### Project Requirements:
- Two to three plots (and think about getting information visualized onto fewer plots). NO PIE CHARTS
- Greater than or equal to two datasets
- At least one dataset comes from merging different tables/sources (deliverable)
- At least 1 dirty dataset (not Kaggle)
- At least one API used
- Export dataframe to SQL Database (explained 1/4/2020)
- 10 minute presentation
- Use Jupyter Lab to present...no PPT.
---
### Project Description: 

#### Our Question:

- Do the most popular zip codes to start or end rides also have the most complaints?
- Does frequency of ending scooter rides in zipcode impact complaints when adjusted on per capita basis?
- Number of rides in certain months of the year vs Number of complains
- Does the distance of the trip impact the method of transportation (scooter vs. bicycle)
- What are the 10 most frequent routes for all methods?


#### Hypothesis:

While we thought that obviously the neighborhoods with the most rides would likely have the most complaints, we also thought that some neighborhoods complain about a higher percent of the scooters that enter their area than other neighborhoods do.
We figured these would be neighborhoods that are not as popular start points, who see the scooters longer and thus are more likely to complain.

### Data Set:
* City of Austin 311 OpenData: https://data.austintexas.gov/City-Government/311-Unified-Data-Test-Site-2019/i26j-ai4z
    - API Endpoint: https://data.austintexas.gov/resource/i26j-ai4z.json
    
* Austin Shared Mobility API: https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r
    - API Endpoint: https://data.austintexas.gov/resource/7d8e-dm7r.json
    
* FCC API call for lat/long to census tract conversion: https://geo.fcc.gov/api/census/

### Actions and Tasks:
- Data Extraction
- Data Cleaning and Exploration
- Data Story and Visualization
- Writing Analysis and Conclusions

### Conclusions:
**Major limitations in our data:**
1. One data set is limited by geography, we can’t get more specific than census tract
2. 311 data was not clear about what the complaints were specifically about — you would have to manually find them on the 311. We also couldn’t see if it was business, resident, or passerby.
3. Joyriding, some rides are really short— some people just turn scooters on and don’t seem to take it anywhere. 
4. We’d like to isolate the music festival dates out and see how much those specific dates impact the data.
5. 78701: Neighborhoods that are mostly commercial have a lot of people who work there, own businesses there, walk around there, but do not show up in the population. It is possible that business owners are more likely to complain because they are made less available to customers due to scooter issues. Nearly 100k people work in downtown Austin which is drastically different from the number of people who are living there. We saw rush hour right after work.

### Resources:
- https://dev.socrata.com/foundry/data.austintexas.gov/7d8e-dm7r
- https://dev.socrata.com/foundry/data.austintexas.gov/i26j-ai4z
- https://austintexas.gov/micromobility


![Scooter meme](resources/scooters_meme.png)