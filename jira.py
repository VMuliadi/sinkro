#!/usr/bin/python3
from os import environ
from requests.auth import HTTPBasicAuth
import json
import requests

JIRA_ENDPOINT = environ["JIRA_ENDPOINT"]
JIRA_USER_MAIL = environ["JIRA_USER_MAIL"]
JIRA_ACCESS_TOKEN = environ["JIRA_ACCESS_TOKEN"]c

class Jira:
  def get_assigned_tasks(self):
    tasks = []
    for issue in json.loads(requests.get(JIRA_ENDPOINT + "/search",
      headers={"Accept": "application/json"},
      auth=HTTPBasicAuth(JIRA_USER_MAIL, JIRA_ACCESS_TOKEN),
      params={
        "fields": "description,priority,status,summary",
        "jql": "assignee = currentuser() \
          AND status NOT IN (Done, Review) \
          AND statusCategory != Done"
      }).text)["issues"]:
        task_details = {}
        task_details["key"] = issue["key"]
        task_details["summary"] = issue["fields"]["summary"]
        task_details["priority"] = issue["fields"]["priority"]["id"]
        task_details["description"] = issue["fields"]["description"]
        tasks.append(task_details)
    return tasks
