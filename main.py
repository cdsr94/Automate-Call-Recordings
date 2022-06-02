import os
import logging
from datetime import date
from dotenv import load_dotenv
from twilio.rest import Client
from dateutil.relativedelta import relativedelta


logging.basicConfig(filename = 'call_recordings.log', encoding = 'utf-8', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
load_dotenv() 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
days = os.environ.get("MAX_DAYS_TO_REMAIN")


def get_recordings_and_delete(client: Client) -> None:
  days_before = None
  seven_days_before = None
  if days:
    days_before = date.today() + relativedelta(days=-int(days))
    seven_days_before = days_before + relativedelta(days=-7)
  try:
    recordings = client.recordings.list(
                                        date_created_before = days_before,
                                        date_created_after = seven_days_before,
                                      )
  except Exception as e:
    recordings = []
    logging.error(e)

  for record in recordings:
    if record.status == 'completed':
      record.delete()
      logging.info(f'The Recording SID {record.sid} was deleted.')


client = Client(account_sid, auth_token)
get_recordings_and_delete(client)
