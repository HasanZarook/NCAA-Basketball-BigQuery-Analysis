# 🏀 NCAA Basketball BigQuery Analysis

This project explores the **NCAA Basketball dataset** from Google BigQuery using SQL queries embedded in Python functions.  
The queries answer different analytical questions about teams, players, venues, and historical performances.

---

## 📊 Dataset
- **Source:** [BigQuery Public Dataset: NCAA Basketball](https://console.cloud.google.com/marketplace/product/ncaa-bb-public/ncaa-basketball)  
- **Dataset ID:** `bigquery-public-data.ncaa_basketball`  
- Includes tables such as:
  - `mbb_teams`
  - `mbb_games_sr`
  - `team_colors`
  - `mbb_players_games_sr`
  - `mbb_pbp_sr`
  - `mbb_historical_tournament_games`
  - `mbb_historical_teams_seasons`

---

## 🎯 Queries Implemented
Each query is wrapped inside a Python function for clarity and reusability.

1. **Stanford’s Venue** – Fetch Stanford’s home venue and its capacity.  
2. **Games at Stanford’s Venue** – Count games played at Maples Pavilion (2013 season).  
3. **Teams with High Red Color Intensity** – List teams with primary colors starting with `#FF`.  
4. **Stanford Wins at Home** – Count home wins and compare average points (2013–2017).  
5. **Players Born in Same City as Venue** – Count players whose birthplace matches the venue city/state.  
6. **Biggest Blowout** – Largest point margin in NCAA tournament history.  
7. **Historical Upset Percentage** – Percentage of games where a lower-seeded team beat a higher seed.  
8. **Teams Sharing State & Colors** – Teams with the same state and team colors.  
9. **Top Birth Locations** – Cities/states contributing the most points to Stanford players (2013–2017).  
10. **Teams with High-Scoring Players** – Teams with the most players scoring 15+ points in first halves.  
11. **Top Historical Winners** – Teams with the highest win counts across seasons (1900–2000).  

---

## 🛠️ Technologies Used
- **Google BigQuery** (dataset & queries)  
- **Python** (query management & function wrapping)  

---

## 📂 Project Structure
```

📁 NCAA-Basketball-BigQuery-Analysis
│── queries.py       # All queries defined as Python functions
│── README.md        # Project documentation

````

---

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/NCAA-Basketball-BigQuery-Analysis.git
   cd NCAA-Basketball-BigQuery-Analysis
````

2. Open `queries.py` and import into your Python environment:

   ```python
   import queries

   print(queries.query_one())
   ```

3. Execute the returned SQL string using your **BigQuery client** in Python or the BigQuery Console.

---

## 👨‍💻 Collaborators

* Hasan Zarook (2021-CE-58)
