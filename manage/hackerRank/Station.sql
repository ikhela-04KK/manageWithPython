

-- CONSEIL: le min et le max s'utilise avec la clause group by
-- sous requetes qui permet de determiner la ville ayant la plus petite longueur 

SELECT LENGTH((SELECT CITY FROM STATION ORDER BY LENGTH(CITY) ASC LIMIT 1));

-- utilisant d'une clause having et d'une sous requête dans cette clause 

SELECT CITY, LENGTH(CITY)
FROM STATION 
GROUP BY CITY 
HAVING LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION)
 OR LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION);



-- deux sous requête dans le where de telle sorte à pouvoir faire resortir le min , max des noms des villes 
SELECT CITY, LENGTH(CITY)
FROM STATION 
WHERE (CITY LIKE "A%" AND LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION))
   OR (LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION));