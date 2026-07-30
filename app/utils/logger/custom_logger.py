import logging
from functools import wraps
import os

class Logger:

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(filename='logs/app.log',filemode='a',format='%(asctime)s | [%(name)s] | %(levelname)s | %(message)s',datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

    @staticmethod
    def log_activity(module_name="GENERAL"):

        def decorator(funct):

            @wraps(funct)

            def wrapper(*args, **kwargs):

                Logger = logging.getLogger(module_name)

                args_repr = [repr(a) for a in args]

                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]

                params = ", ".join(args_repr + kwargs_repr)

                try:
                    result = funct(*args, **kwargs)
                    Logger.info(f"SUCCESS: {funct.__name__} returned {result}")
                    return result
                except Exception as e:
                    Logger.error(f"FAILED: {funct.__name__} - Error: {str(e)}", exc_info=True)
                    raise
                    
            return wrapper
        return decorator