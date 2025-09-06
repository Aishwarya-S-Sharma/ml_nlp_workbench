import my_logger  # This sets up logging config
import logging

def add(a, b):
    logging.debug("The addition operation is taking place")
    return a + b

logging.debug("The addition function is called")
result = add(10, 15)
logging.debug(f"Result of addition: {result}")

# Ensure logs are written immediately
logging.shutdown()
