SELECT first_name, last_name, salary FROM players
JOIN salaries ON players.id = salaries.player_id
WHERE salaries.year = 2001
GROUP BY player_id
ORDER BY salary , first_name ASC , last_name ASC, player_id
LIMIT 50;

