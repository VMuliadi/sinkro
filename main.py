#!/usr/bin/python3
from os import environ
from pprint import pprint
import jira
import json
import todo

def main():
  jira_client = jira.Jira()
  todo_client = todo.Todo()
  todoist_project = "Sinkro Testing"
  project_id = todo_client.get_project_id_by_name(todoist_project)
  project_section_placement = "[TECHNICAL] TODO LIST"
  section_id = todo_client.get_section_id_by_name(project_id, project_section_placement)

  for assigned_issue in jira_client.get_assigned_tasks():
    issue_description = assigned_issue["description"]
    issue_title = assigned_issue["key"] + " - " + assigned_issue["summary"]
    issue_priority = assigned_issue["priority"]
    todo_client.create_todo_task(issue_title, issue_description, issue_priority, project_id, section_id)

if __name__ == "__main__":
  main()