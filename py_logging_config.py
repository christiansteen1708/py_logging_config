"""Base config for logging with arguments for logfile and loglevel"""
from datetime import datetime
import os #username
import socket #hostname
import logging
import argparse


def log_per_argument(description=None, default_loglevel="debug", 
                     default_logfile=datetime.now().strftime("%Y%m%d_%H%M%S"), 
                     args_dict=None):
    """ Provides input for loglevel and logfile per argument.
        further arguments can be dynamically assigned via args_dict
        returns parsed argument inputs
    """

    def set_log_config (logfile, loglevel, default_loglevel):
        # loglevel
        level_config = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        try:
            level_choice = level_config[loglevel]
        except:
            print(f"not a valid log level, using default {default_loglevel}")
            level_choice = level_config[default_loglevel]

        # set basicConfig for logging
        logging.basicConfig(
            filename=logfile,
            encoding='utf-8',
            level=level_choice,
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


    parser = argparse.ArgumentParser(description=description)
    ##set base arguments for logging: logfile and loglevel
    parser.add_argument('-lf',
                        '--logfile',
                        default=default_logfile,
                        help=f'Provide logging filename | logs in ./log/ | \
                            adds .log extension | Example --logfile foo_log | \
                            default={default_logfile}')
    parser.add_argument('-ll',
                        '--loglevel',
                        default=default_loglevel,
                        help=f'Provide logging level. Example --loglevel debug, \
                            [debug, info, warning, error, critical], default={default_loglevel}')

    #unpack further arguments from args_dict, add as arguments
    if args_dict: 
        for arg in args_dict:
            parser.add_argument(
                arg['action'], 
                arg['namespace'],
                default=arg['default'],
                help=arg['help'],
            )
    
    args = parser.parse_args() #parse arguments

    #handle logging argument input
    logfile = 'log/' + args.logfile + '.log'
    loglevel = args.loglevel.lower()
    set_log_config(logfile, loglevel, default_loglevel) #logging-basiskonfig setzen

    ##log base info (user,hostname)
    logging.info(f'STARTING WITH HOSTNAME:\t{socket.gethostname()}')
    logging.info(f'STARTING WITH USERNAME:\t{os.getlogin()}')

    #unpack and log parsed argument input
    argument_dict = args.__dict__
    def arguments (**kwargs):
        for key, value in kwargs.items():
            logging.info(f'STARTING WITH ARGUMENT:\t{key}:\t{value}')
    arguments (**argument_dict)

    return args