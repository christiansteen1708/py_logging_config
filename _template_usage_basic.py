#! /usr/bin/env python3

"""Template for a minimal logging configuration.
Provides two arguments: --loglevel and --logfile
"""
import py_logging_config
import logging


def main():
    logging.debug('test DEBUG')
    logging.info('test INFO')
    logging.warning('test WARNING')
    logging.error('test ERROR')
    logging.critical('test CRITICAL')

    ###
    # [Code...]
    ###


if __name__ == "__main__":

    args = py_logging_config.log_per_argument(
        description='template for basic usage'
        # default_loglevel =  # default: debug
        # default_logfile =  # default: log/timestamp.log
        #args_dict=dict_args
    )
    main()
