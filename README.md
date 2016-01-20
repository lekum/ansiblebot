# ChatOps bot for running Ansible one-liners through Slack

## Description

Docker image of a Slack bot that enables remote execution of Ansible commands inside a Slack channel

## Usage

1. Enable [Bot Users](https://api.slack.com/bot-users) in your Slack team. Create a bot, retrieve its API token and invite the bot to the channels you want to monitor
2. Build the image or pull [the official one](https://hub.docker.com/r/lekum/ansiblebot/)
3. Run a container using the image, setting the appropriate value for the environment variable `SLACK_API_TOKEN`

In addition, if you want any file to be used by Ansible, you may map that file inside the directory `/opt/bot/` of the container. That way, you can pass an inventory or `ansible.cfg` file, for example.

## Important disclaimer

Using this bot exposes your host to the users of the Slack channel (it may be a good idea to create a private channel for it). In addition, the internal usage of Python's `subprocess.check_output` with `shell=True` may pose security threats. Use at your own responsibility. 
