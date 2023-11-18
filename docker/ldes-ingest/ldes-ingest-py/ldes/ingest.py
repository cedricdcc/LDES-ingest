import logging
from dotenv import load_dotenv
from .helpers import enable_logging, resolve_path


log = logging.getLogger(__name__)
URN_BASE = "urn:lwua:INGEST"


def run_ingest():
    log.info(f"run_ingest started")
    # log all the variables that are set in the environment
    env_vars = load_dotenv()
    log.info(f"environment variables: {env_vars}")
    # TODO -- implement steps
    # list the uri to start harvesting from
    # list the property paths to get data from 
    
def main():
    load_dotenv()
    enable_logging()
    run_ingest()

if __name__ == '__main__':
    main()