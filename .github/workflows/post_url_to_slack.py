import os
import requests
import sys


def main(dev_build_url):
    """
    Post the development build URL to a Slack channel.

    Args:
        dev_build_url (str): The URL of the development build to post.
    """
    if not dev_build_url:
        raise ValueError("The development build URL must be provided.")

    # Webhooks for the SWTeam Notifier Slack App
    # https://api.slack.com/apps/AU8B2DWMQ/incoming-webhooks?
    resp = requests.post(
        f"https://hooks.slack.com/services/TC8CFSF4K/B097SGG73FF/{os.environ['SLACK_API_TOKEN']}",
        headers={
            "Content-Type": "application/json; charset=utf-8"
        },
        json={
            "text": f':invest: {dev_build_url}'
        })
    resp.raise_for_status()


if __name__ == '__main__':
    main(sys.argv[1])
