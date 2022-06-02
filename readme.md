# Automate Call Recording Deletion

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This repository is used for automation in the deletion of recorded calls in the Twilio application.

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
