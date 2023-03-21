SELECT spi1 ,team2 , spi2
FROM spi_matches 
JOIN spi_global_rankings as s1 ON spi_matches.team1 = s1.prev_rank
JOIN spi_global_rankings as s2 ON spi_matches.team2 = s2.prev_rank
--JOIN spi_global_rankings as s2 ON spi_matches.team2 = s2.prev_rank
WHERE (spi_matches.league = "French Ligue 1" AND team2 ="Paris Saint-Germain") AND (spi_matches.league = "French Ligue 1" AND team1 ="Paris Saint-Germain")



-- quelle est l'équipe qui avait un pourcentage de victoire superieur à la 80
-- quelle est l'équipe qui as une pourcentage > 80 
-- manipulation de donnée et implementation d'une base de donnée 