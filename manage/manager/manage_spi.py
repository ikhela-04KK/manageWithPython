
from contextlib import closing , contextmanager
import sqlite3 

class Manages:
    
    #mise en place de la base de donnée 
    # contruction des differentes ligue dans des tables temporaire
    # mettre aussi , le classement de l'équipe dans le top 10
    # avec les differentes dates 

    koffi_table = "koffi.db"    
    list_table = ["spi_matches","spi_global_rankings","spi_global_rankings_intl",]
    team = ["team1", "team2"]
    world_league = ["French Ligue 1","Barclays Premier League","German Bundesliga","Spanish Primera Division","Italy Serie A"]
    league_saison = [2016, 2017 ,2018 , 2020 , 2021 , 2022]


    def st_connect(self):
        # chelsea
        # self.connect()
        with closing(sqlite3.Connection(self.koffi_table)) as conn, conn, \
        closing(conn.cursor()) as self.manage:
            club_select = input("quelle est  le club que vous recherché .........") 
            self.manage.execute(f"select * from {self.list_table[0]} where {self.team[0]}='{club_select}'")
            return self.manage.fetchall()

    def league_prediction(self):
        with closing(sqlite3.Connection(self.koffi_table)) as conn, conn, \
        closing(conn.cursor()) as self.manage:
            self.manage.execute(f"""SELECT DISTINCT {self.league_saison[1]}, date, league_id , team1 , team2 , spi1 , spi2
                                    FROM spi_matches
                                    JOIN spi_global_rankings ON spi_matches.league = spi_global_rankings.league
                                    WHERE spi_matches.league = '{self.world_league[1]}' AND {self.team[0]} = 'Chelsea'
                                """)
            return self.manage.fetchall()

    def percent_victory(self):
        # le pourcentage de victoire à domicile et de match à l'exterieur 
        # afficher les resultats en fonction du nom de l'équipe que l'on rentre 
        with closing(sqlite3.Connection(self.koffi_table)) as conn, conn, \
            closing(conn.cursor()) as self.manage:
                self.manage.execute(f"""SELECT round(avg(s1.spi1),2) as "Match à domicile" , round(avg(s2.spi2),2) as "Match à l'exterieur"
                                       FROM spi_matches as s1
                                       JOIN spi_matches as s2 ON s1.team1 = s2.team2
                                       WHERE s1.team1 ="Fulham" AND s2.team2 ="Fulham" AND s1.season = {self.league_saison[3]} AND s2.season = {self.league_saison[3]} 
                                    """)
                return self.manage.fetchall()

    def stat_club_fail(self):
        with closing(sqlite3.Connection(self.koffi_table)) as conn, conn, closing(conn.cursor()) as self.manage:
            self.manage.execute("""SELECT team1 ,team2, spi1 , spi2 , league
                                    FROM spi_matches
                                    WHERE team1 in(
                                    SELECT prev_rank
                                    FROM spi_global_rankings
                                    WHERE spi < (SELECT avg(spi)
                                    FROM spi_global_rankings)
                                    )AND team2 in(
                                    SELECT prev_rank
                                    FROM spi_global_rankings
                                    WHERE spi < (SELECT avg(spi)
                                    FROM spi_global_rankings)
                                    )
                                    ORDER by league;
                                """)
            return self.manage.fetchone()


chelsea = Manages()
print(chelsea.stat_club_fail())
