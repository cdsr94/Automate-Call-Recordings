import os
import logging
from datetime import date
from dotenv import load_dotenv
from twilio.rest import Client
from dateutil.relativedelta import relativedelta

load_dotenv() 
logging.basicConfig(filename = 'example.log', encoding = 'utf-8', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
days = int(os.environ['MAX_DAYS_TO_REMAIN'])


def get_recordings_and_delete(client: Client) -> None:
  recordings = client.recordings.list(
                                      date_created_before = date.today(),
                                      date_created_after = date.today() + relativedelta(days=-days),
                                    )

  for record in recordings:
      if record.status == 'completed':
        record.delete()
        logging.info(f'The Recording SID {record.sid} was deleted.')


client = Client(account_sid, auth_token)
get_recordings_and_delete(client)
