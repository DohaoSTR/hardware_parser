import logging
import time

from src.prices.dns.db_mapper.DatabaseMapper import DatabaseMapper

LOG_PATH = "data\\logs\\dns_mapper_main.log"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    encoding='utf-8')
logger = logging.getLogger("dns_mapper_main")
file_handler = logging.FileHandler(LOG_PATH)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_most_actual_prices():
    mapper = DatabaseMapper(logger)
    with mapper:
        start_time = time.time()

        data = mapper.get_most_actual_prices()
        print(data[0].price)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Метод выполнился за {execution_time:.2f} секунд")

get_most_actual_prices()