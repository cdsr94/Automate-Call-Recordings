# Automate Call Recording Deletion

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This script automates the process of deleting calls recorded in Twilio in a time range.

Since we still do not have the scope on the Calabrio side, once they provide us with information, the recordings can be validated on both platforms and proceed to eliminate those that are already in Calabrio.

A grace period is proposed with an environment variable called "MAX_DAYS_TO_REMAIN", which takes as reference the day of execution of the script minus the days of the variable; so we will get all the recordings that started before that day and delete it

## Features

- Get all recordings in a time range
- Delete recordings in a time range

## Tech

Automate Call Recordings uses a number of open source projects to work properly:

- [Python] - Python is a programming language that lets you work quickly!
- [Twilio] - Twilio's Voice API helps you to make, receive, and monitor calls around the world.
- [Pipenv] - Aims to bring the best of all packaging worlds.

## Installation

Requires [Python] v3.10.1+ and Pipenv to run.

Install the dependencies and devDependencies and run the script.

```sh
cd Automate-Call-Recordings
pipenv shell
pipenv install
python main.py
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python]: <https://www.python.org/>
   [Twilio]: <https://www.twilio.com/docs/voice/api/recording#fetch-a-recording-media-file>
   [Pipenv]: <https://pipenv.pypa.io/en/latest/>
