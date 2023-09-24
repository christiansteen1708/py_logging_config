#!/usr/bin/python3
"""Template for advanced logging configuration.
Provides two arguments: --loglevel and --logfile
Further provides more dynamic arguments (--foo, --bar, ...)
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

    #arguments can be provided via list-entries
    dict_args=[{'action': '-f', 
                'namespace': '--foo',
                'default': 'foo', 
                'help': 'foo'},
                {'action':'-b',
                 'namespace': '--bar',
                 'default': 'bar',
                 'help': 'bar' 
                 }]

    args = py_logging_config.log_per_argument(
        description='template for advanced usage',
        # default_loglevel =  # default: debug
        # default_logfile =  # default: log/timestamp.log
        args_dict=dict_args
    )

    #parsed argument-inputs can be accessed like this
    print(args.foo)
    print(args.bar)
    main()
