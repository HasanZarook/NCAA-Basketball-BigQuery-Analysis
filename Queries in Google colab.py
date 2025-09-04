# Collaborators: Fill in names and Registration numbers here

def query_one():
    """Query for Stanford's venue"""
    return """
SELECT
  venue_name,
  venue_capacity
FROM
  `taskproj-398609.ncaa_basketball.mbb_teams`
WHERE
  market = 'Stanford'
LIMIT
  1000
    """

def query_two():
    """Query for games in Stanford's venue"""
    return """
SELECT
  COUNT(*) AS games_at_maples_pavilion
FROM
  `taskproj-398609.ncaa_basketball.mbb_games_sr`
WHERE
  venue_name = 'Maples Pavilion'
  AND season = 2013
LIMIT
  1000
    """

def query_three():
    """Query for maximum-red-intensity teams"""
    return """
SELECT
  market,
  color
FROM
  `taskproj-398609.ncaa_basketball.team_colors`
WHERE
  color like'#FF%'
  OR color like  '#ff%'
ORDER BY
  market asc
LIMIT
  1000
    """

def query_four():
    """Query for Stanford's wins at home"""
    return """
SELECT
  COUNT(*) AS number,
  round (AVG(h_points_game),
    2) AS avg_stanford,
  round (AVG(a_points_game),
    2) AS avg_opponent
FROM
  `taskproj-398609.ncaa_basketball.mbb_games_sr`
WHERE
 (season between 2013 and 2017) and h_points_game>a_points_game and h_market='Stanford'
LIMIT
  1000
    """

def query_five():
    """Query for players for birth city""" --NOTE:didn't get correct answer its giving 786 to me instead of 606
    return """
SELECT
  COUNT (distinct Player.player_id) AS num_players
FROM
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` AS Player
left join 
  `bigquery-public-data.ncaa_basketball.mbb_pbp_sr` AS Team
ON
  Player.player_id = Team.player_id
WHERE
  Player.birthplace_city = Team.venue_city
  and Player.birthplace_state = Team.venue_state
    """

def query_six():
    """Query for biggest blowout"""
    return """
      select  win_name, lose_name, win_pts, lose_pts, ((win_pts) - (lose_pts)) as margin
      from `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`
      order by margin desc
      limit 1
    """

def query_seven():
    """Query for historical upset percentage"""
    return """
SELECT
  ROUND(COUNT(*)/(
    SELECT
      COUNT(*)
    FROM
      `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`) * 100, 2) AS upset_percentage
FROM
  `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`
WHERE
  win_seed > lose_seed
LIMIT
  1000
    """

def query_eight():
    """Query for teams with same states and colors"""
    return """
SELECT
  TA.name AS TeamA,
  TB.name AS TeamB,
  TA.venue_state AS State
FROM
  `bigquery-public-data.ncaa_basketball.mbb_teams` AS TA
INNER JOIN
  `bigquery-public-data.ncaa_basketball.team_colors` AS CA
ON
  TA.id = CA.id
INNER JOIN
  `bigquery-public-data.ncaa_basketball.mbb_teams` AS TB
ON
  TA.id <> TB.id
INNER JOIN
  `bigquery-public-data.ncaa_basketball.team_colors` AS CB
ON
  TB.id = CB.id
WHERE
  CA.color = CB.color
  AND TA.venue_state = TB.venue_state
GROUP BY
  State,
  TA.name,
  TB.name
HAVING
  TeamA <= TeamB
ORDER BY
  TeamA asc
LIMIT
  1000
    """

def query_nine():
    """Query for top geographical locations"""
    return """
SELECT
  Player.birthplace_city,
  Player.birthplace_state,
  Player.birthplace_country,
  SUM(Player.points)
FROM
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` AS Player
WHERE
  Player.team_id = (
  SELECT
    id
  FROM
    `bigquery-public-data.ncaa_basketball.mbb_teams`
  WHERE
    venue_city = 'Stanford' )
  AND Player.birthplace_city IS NOT NULL
  AND Player.birthplace_state IS NOT NULL
  AND Player.birthplace_country IS NOT NULL
  AND Player.points IS NOT NULL
  AND Player.season BETWEEN 2013 AND 2017
GROUP BY
  Player.birthplace_city,
  Player.birthplace_state,
  Player.birthplace_country
ORDER BY
  SUM(Player.points) DESC
LIMIT
  3
    """

def query_ten():
    """Query for teams with lots of high-scorers"""
    return """
SELECT
  t.team_market,
  COUNT(DISTINCT t.player_id) AS num_players
FROM (
  SELECT
    pbp.game_id AS game_id,
    pbp.player_id AS player_id,
    pbp.team_market AS team_market,
    SUM(pbp.points_scored) AS points
  FROM
    `bigquery-public-data.ncaa_basketball.mbb_pbp_sr` AS pbp
  WHERE
    pbp.period = 1
    AND pbp.season >= 2013
  GROUP BY
    pbp.game_id,
    pbp.player_id,
    pbp.team_market
  HAVING
    points >= 15) AS t
GROUP BY
  t.team_market
ORDER BY
  num_players DESC,
  t.team_market
LIMIT
  5
    """

def query_eleven():
    """Query for highest-winner teams"""
    return """
SELECT
  t2.market AS top_market,
  COUNT(t2.market) AS top_performer_count
FROM (
  SELECT
    MAX(t1.wins) AS max_wins,
    t1.season AS season
  FROM
    `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` AS t1
  WHERE
    t1.season BETWEEN 1900 AND 2000
  GROUP BY
    t1.season) AS t3
INNER JOIN
  `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` AS t2
ON
  t2.wins = max_wins
  AND t2.season = t3.season
GROUP BY
  t2.market
ORDER BY
  COUNT(t2.market) DESC,
  t2.market
LIMIT
  5
    """