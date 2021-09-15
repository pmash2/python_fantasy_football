import logging
import config

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
