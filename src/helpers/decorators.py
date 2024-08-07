from src.helpers.notificators import send_teams_message
import time

def error_decorator(raise_error=True):
    def decorator(function):
        def wrapper(*args, **kwargs):
            error_message = None
            try:
                return function(*args, **kwargs)
            
            except Exception as error:
                error_message = error
                
            # RAISE ERROR
            if raise_error and error_message:
                raise error_message
            else:
                print(error_message)
            
            return {}
    
        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator

def retry_decorator(tries=5, wait=0, raise_error=True, error_default=None):
    default = .4
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return function(*args, **kwargs)
                
                except Exception as err:
                    message = err
                    time.sleep(default + wait)
                    
            if raise_error:
                send_teams_message(str(message))
                raise message
                    
            return error_default
        
        wrapper.__doc__ = function.__doc__
        return wrapper
    
    return decorator