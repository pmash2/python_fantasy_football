import logging
import config
import pandas as pd
from ff_espn_api import League

logger = logging.getLogger('main.logger')
logger.setLevel('DEBUG')

file_log_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_log_handler)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter)
stderr_log_handler.setFormatter(formatter)

league_id = config.league_id
swid = config.swid
espn_s2 = config.espn_s2
year = 2020
league = League(league_id, year, espn_s2, swid)

logger.info(f'Fantasy League info for the {year} season')
logger.info('***********************')
logger.info('FINAL STANDINGS')
logger.info('***********************')

for i, team in enumerate(league.standings()):
    logger.info(f'{i+1}. {team.team_name}')


logger.info('')
logger.info('')

top_scoring_team = league.top_scorer()
logger.info(
    f'Top scoring team: {top_scoring_team.team_name} - {round(top_scoring_team.points_for, 1)}')

league_2020 = pd.DataFrame()
df_columns = list(league.teams[0].__dict__.keys())
df_columns.remove('roster')
df_columns.remove('owner')

for d in range(len(league.teams)):
    team_df = pd.DataFrame(league.teams[d].__dict__,
                           columns=df_columns)
    league_2020 = league_2020.append(team_df)
logger.info(league_2020.to_html())
