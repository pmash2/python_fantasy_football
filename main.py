import logging
import config
from ff_espn_api import League

logger = logging.getLogger('main.logger')
logger.setLevel('DEBUG')

file_log_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_log_handler)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter)
stderr_log_handler.setFormatter(formatter)

logger.info('Info message')
logger.error('Error message')

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
