import sys
import logging
from crhelper import CfnResource

log = logging.getLogger()
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.INFO)

helper = CfnResource(
	json_logging=False,
	log_level='DEBUG',
	boto_level='CRITICAL'
)

def handler(event, context):
    helper(event, context)

@helper.create
def create_database(event, context):
    log.info("Creating database")
    log.info("Event = " % event)
    log.info("Context = " % context)
    return "arn:aws:create-database-lambda:rds-database"

@helper.update
def update_database(event, context):
    log.info("Updating database")
    log.info("Event = " % event)
    log.info("Context = " % context)
    return "arn:aws:create-database-lambda:rds-database"

@helper.delete
def delete_database(event, context):
    log.info("Deleting database")
    log.info("Event = " % event)
    log.info("Context = " % context)
    return "arn:aws:create-database-lambda:rds-database"