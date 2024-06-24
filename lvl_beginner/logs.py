import logging
import time

if __name__ == "__main__":
    logging.basicConfig(
        filename='C:\\Users\\nike9\\OneDrive\\Python practice\\log.txt',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # logging.disable(logging.CRITICAL) # disable all msgs

    for i in range(5):
        logging.debug(f'Testing debug log! Num: {i}')
        time.sleep(0.5)
        logging.info(f'Testing debug log! Num: {i}')
        time.sleep(0.5)
        logging.error(f'Testing debug log! Num: {i}')