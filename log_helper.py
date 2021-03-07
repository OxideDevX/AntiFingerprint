import logging


def setup_logger(name, level, log_to_file):
    """
   Создать и настроить логгер.
    Создание обработчика консоли и обработчиков файлов журнала
    : param name: имя регистратора и имя файла журнала, если также войти в файл
    : уровень параметров: перейти на logging.DEBUG для подробного вывода, перейти на logging.INFO для стандартного вывода
    : param log_to_file: логический
    : return: создан и настроен объект регистратора
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter('[%(asctime)s - %(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)
    if log_to_file:
        logfile = logging.FileHandler('{0}.log'.format(name), mode='w')
        logfile.setLevel(logging.DEBUG)
        logfile.setFormatter(formatter)
        logger.addHandler(logfile)
    return logger
