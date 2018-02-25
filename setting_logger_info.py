#coding:utf-8
"""
    author:cheng star
"""

import logging
import logging.handlers

logger = None

def parse_log_init() :
    """parse log into config text file"""
    log_init = {}
    with open("conf/log_init.conf" , encoding = "utf-8") as f_obj :
        for line in f_obj.readlines() :
            if line.startswith("#") :
                continue
            else :
                [log_key , log_value] = [x.strip() for x in line.split("=")]
                print("log_key -> %s" %log_key)
                print("log_value -> %s" %log_value)

                # setting log level
                if log_key == 'log_level' :
                    if log_value.lower() == 'debug' :
                        log_value = logging.DEBUG
                    elif log_value.lower() == 'info' :
                        log_value = logging.INFO
                    elif log_value.lower() == 'warn' :
                        log_value = logging.WARN
                    elif log_value.lower() == 'error' :
                        log_value = logging.ERROR
                    elif log_value.lower() == 'fatal' :
                        log_value = logging.FATAL
                    else :
                        log_value = logging.DEBUG
                # parse log init config file save to dictionary
                log_init[log_key] = log_value
    return log_init

def logger_init() :
    """set logger info"""
    log_init = parse_log_init()

    # get logger obejct
    logger = logging.getLogger("logger")
    logger.setLevel(log_init["log_level"])

    # create fileHandler object wirte log to file
    # create consoleHandler object output log to console
    # fileHandler = logging.FileHandler(log_init["log_save_path"])
    fileHandler = logging.handlers.RotatingFileHandler(filename = log_init["log_save_path"] ,
                                                       maxBytes = 1024 * 1024 * int(log_init["log_size"]) ,
                                                       backupCount = int(log_init["log_duplicates"])
                                                       )
    consoleHandler = logging.StreamHandler()

    fileHandler.setLevel(log_init["log_level"])
    consoleHandler.setLevel(log_init["log_level"])

    log_format = log_init["log_format"]
    formatter = logging.Formatter(log_format)

    fileHandler.setFormatter(formatter)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger

def get_logger() :
    """get logger object"""
    if logger is None :
        return logger_init()
    else :
        return logger

if __name__ == '__main__' :
    # print(parse_log_init())
    logger = get_logger()
    print(logger)
    logger.info("test")