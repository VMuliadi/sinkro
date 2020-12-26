#!/usr/bin/python3
from os import environ
import jira
import json
import todo

def main():
  jira_client = jira.Jira()
  todo_client = todo.Todo()
  todoist_project_name = environ["TODOIST_PROJECT_NAME"]
  todoist_section_name = environ["TODOIST_SECTION_NAME"]
  project_id = todo_client.get_project_id_by_name(todoist_project_name)
  section_id = todo_client.get_section_id_by_name(project_id, todoist_section_name)

  for assigned_issue in jira_client.get_assigned_tasks():
    project_detail = jira_client.get_project_details(assigned_issue)
    if not project_detail["fields"]["status"]["statusCategory"]["name"] == "Done":
      project_title = assigned_issue + " - " + project_detail["fields"]["summary"]
      project_description = project_detail["fields"]["description"]
      todo_client.create_todo_task(project_title, project_description, project_id, section_id)

if __name__ == "__main__":
  main()