import os, yaml, logging, watchtower, functools

class CloudWatch:

    def __init__(self, stream, level='DEBUG'):
        """ constructs new 'CloudWatch' object.

            :param stream: stream name for log handler
            :param level: sets logging level (default: DEBUG)

            :return: none
        """
        root_handler = watchtower.CloudWatchLogHandler(
            create_log_group=True,
            create_log_stream=True,

            log_group='datalake',
            stream_name='root',
        )
        handler = watchtower.CloudWatchLogHandler(
            create_log_group=True,
            create_log_stream=True,

            log_group='datalake',
            stream_name=stream,
        )

        logging.basicConfig(level=level, format='[%(asctime)s] %(process)d %(levelname)s %(name)s:%(funcName)s:%(lineno)s - %(message)s')
        
        self.logger = logging.getLogger(stream)
        self.logger.addHandler(root_handler)
        self.logger.addHandler(handler)

    def debug(self, func):
        """ sends general debug log to cloudwatch
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            self.logger.debug(f'{os.getpid()} {func.__qualname__} {args}')

            return func(*args,**kwargs)
        return wrapper

    def info(self, msg):
        """ sends info msg to cloudwatch
        """
        self.logger.info(msg)
    
    def critical(self, msg):
        """ sends critical msg to cloudwatch
        """
        self.logger.critical(msg)