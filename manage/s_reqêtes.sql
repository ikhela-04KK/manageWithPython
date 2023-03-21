-- le pourcentage des equipes qui sont inferieurs à la moyenne par match 
SELECT *
FROM (
	SELECT prev_rank , league 
	FROM spi_global_rankings
	WHERE spi < (SELECT avg(spi)
				FROM spi_global_rankings)
)spi_matches;
