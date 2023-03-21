--- creer un index pour les club et une vue pour les club de premier league , serie A , bubdesliga , ligue1 , liga 

CREATE INDEX IF NOT EXISTS "idx_premiere_league" ON spi_global_rankings("league");
CREATE INDEX IF NOT EXISTS "idx_team1" ON spi_matches("team1");
CREATE INDEX IF NOT EXISTS "idx_team2" ON spi_matches("team2");
CREATE INDEX IF NOT EXISTS "idx_league" ON spi_matches("league");
