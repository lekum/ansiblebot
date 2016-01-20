# ChatOps bot for running Ansible one-liners through Slack

## Description

Docker image of a Slack bot that enables remote execution of Ansible commands inside a Slack channel

## Usage

1. Enable [Bot Users](https://api.slack.com/bot-users) in your Slack team. Create a bot, retrieve its API token and invite the bot to the channels you want to monitor
2. Build the image
3. Run a container using the image, setting the appropriate value for the environment variable `SLACK_API_TOKEN`

In addition, if you want any file to be used by Ansible, you may map the directory `/opt/bot/` to your host. That way, you can pass an inventory or `ansible.cfg` file, for example.
