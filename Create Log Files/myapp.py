import logging
import mylib


def main():
    # logging.basicConfig(filename='myapp.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,
                        handlers=[logging.FileHandler("myapp.log"), logging.StreamHandler()])
    logging.info('Started')
    logging.debug('This message should go to the log file')
    logging.warning('And this, too')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
