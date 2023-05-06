-- les equipes qui ont un stat superieur à la moyenne 
-- on parle de sous-reqputes scalaires , lorqu'une requête renvoi qu'une seul valeur ou une seul ligne 
SELECT league
FROM spi_global_rankings
WHERE league ="French Ligue 1" IN(
    SELECT *
    FROM spi_global_rankings
    WHERE off > ( 
      SELECT avg(off)
      FROM spi_global_rankings
    )			
)
-- essayer de voir la note moyenne 
-- 


--ALTER TABLE spi_global_rankings RENAME prev_ranks To prev_rank;
--- il faut que je supprimes , une ligne en question 
---DELETE FROM spi_matches WHERE season = 0;
-- voir le nombre d'équipes qui ont une attaque offensive superieur à la moyenne  
