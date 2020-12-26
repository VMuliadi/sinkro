#!/usr/bin/python3
from os import environ
from requests.auth import HTTPBasicAuth
import json
import requests

JIRA_ENDPOINT = environ["JIRA_ENDPOINT"]
JIRA_USER_MAIL = environ["JIRA_USER_MAIL"]
JIRA_ACCESS_TOKEN = environ["JIRA_ACCESS_TOKEN"]

class Jira:
  def get_assigned_tasks(self):
    tasks = []
    for issue in json.loads(requests.get(JIRA_ENDPOINT + "/search?jql=assignee=currentuser()",
        headers={"Accept": "application/json"},
        auth=HTTPBasicAuth(JIRA_USER_MAIL, JIRA_ACCESS_TOKEN)
      ).text)["issues"]:
      tasks.append(issue["key"])
    return tasks


  def get_project_details(self, issue_id):
    return json.loads(requests.get(JIRA_ENDPOINT + "/issue/" + issue_id,
      auth=HTTPBasicAuth(JIRA_USER_MAIL, JIRA_ACCESS_TOKEN),
      headers={"Accept": "application/json"},
    ).text)
