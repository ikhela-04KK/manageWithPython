-- ici nus avons les equipes qui ont un pourcentage inferieur à la moyenne de victoire 
-- voir les differents afforontements que ces equipes ont eu entre eux et les differentes victoire de chacun 
-- le but d'une base de donnée côté utilisateur est de faciliter au mieux les requêtes entre les clients 

SELECT prev_rank , league 
FROM spi_global_rankings
WHERE spi < (SELECT avg(spi)
FROM spi_global_rankings)

--  recuperer les 10 lignes suivante des équipes qui ont un pourcentage à la moyenne de victoire

SELECT prev_rank, league
FROM spi_global_ranking
WHERE spi < (SELECT avg(spi)
FROM spi_global_rankings)
LIMIT 10
OFFSET 7

-- utilisation de MOD et % pour faire le modulo 
SELECT prev_rank, league 
FROM spi_global_ranking 
WHERE spi(SELECT avg(spi)
FROM spi_global_ranking)

-- une façon d'inclure un systeme d'exclusion dans un compte 
-- Faore la difference entre le nombre total d'equipe qui sont dans 
-- la base de donnée avec le nombre d'equipe unique 
-- sans me cas il comptera aussi les valeurs null de la colone client c'est une façon de l'eviter 

SELECT COUNT(CASE WHEN prev_rank IS NOT NULL THEN 1 END) - COUNT(prev_rank) AS resuslt 
FROM spi_global_rankings

-- Voici quelques alternatives à la clause LIMIT que vous pouvez utiliser :
-- Utilisez la fonction TOP pour les bases de données Microsoft SQL Server 
-- TOP 
SELECT TOP 1 pre_rank, league
FROM spi_global_ranking
WHERE spi < (SELECT avg(spi) 
FROM spi_global_rankings);

-- ROWNUM 
SELECT pre_rank, league
FROM spi_global_ranking
WHERE spi < (SELECT avg(spi) 
FROM spi_global_rankings) AND ROWNUM <= 1;

-- Encore plus complexe ça sais en DB2 base de donnée IBM 
SELECT pre_rank, league
FROM spi_global_ranking
WHERE spi < SELECT avg(spi) 
FROM spi_global_rankings)
FETCH FIRST 1 ROWS ONLY;

-- Group by permet de regrouper les valeurs d'une ou pluisieurs colonnes rn fonction des valeurs 
-- Afficher les villes qui ont au moins trois clients fidèle dans les secteur 
-- GROUP BY permet de regrouper les clients par ville 
-- HAVING qui agit comme une clause where sur group by permet d'afficher que les villes 
-- qui ont au moins trois clients 

SELECT ville, COUNT(*) as nb_clients
FROM clients 
GROUP BY ville 
HAVING COUNT(*) >= 3;