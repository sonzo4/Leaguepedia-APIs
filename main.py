import mwclient

site = mwclient.Site('lol.fandom.com', path='/')
response = site.api('cargoquery',
	limit = "max",
	tables = "ScoreboardGames=SG, ScoreboardPlayers=SP",
	join_on = "SG.GameId=SP.GameId",
	fields = "SG.Tournament, SG.DateTime_UTC, SG.Team1, SG.Team2, SG.Winner, SG.Patch, SP.Link, SP.Team, SP.Champion, SP.SummonerSpells, SP.KeystoneMastery, SP.KeystoneRune, SP.Role, SP.UniqueGame, SP.Side",
	where = "SG.DateTime_UTC >= ' 2022-01-01 00:00:00'"
                    )
