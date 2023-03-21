-- ici nus avons les equipes qui ont un pourcentage inferieur à la moyenne de victoire 
-- voir les differents afforontements que ces equipes ont eu entre eux et les differentes victoire de chacun 
-- le bt d'une base de donnée côté utilisateur est de faciliter au mieux les requêtes entre les clients 

SELECT prev_rank , league 
FROM spi_global_rankings
WHERE spi < (SELECT avg(spi)
FROM spi_global_rankings)