#!/usr/bin/python3
from os import environ
import json
import todoist

# TODOIST_ACCESS_TOKEN = environ["TODOIST_ACCESS_TOKEN"]
TODOIST_ACCESS_TOKEN = "27b107743d2f40bfb420ef9c2cc5f270e71bc79f"
api = todoist.TodoistAPI(TODOIST_ACCESS_TOKEN)

class Todo:
  def get_projects(self):
    api.sync()
    project_name = []
    for project in api.state["projects"]:
      project_details = {}
      project_details["id"] = project["id"]
      project_details["name"] = project["name"]
      project_details["shared"] = project["shared"]
      project_name.append(project_details)
    return project_name


  def get_project_id_by_name(self, project_name):
    for project in self.get_projects():
      if project_name == project["name"]:
        return project["id"]
    return -1


  def get_project_name_by_id(self, project_id):
    for project in self.get_projects():
      if project_id == project["id"]:
        return project["name"]
    return None


  def get_sections(self):
    api.sync()
    section_ids = []
    for section in api.state["sections"]:
      section_details = {}
      section_details["id"] = section["id"]
      section_details["name"] = section["name"]
      section_details["user_id"] = section["user_id"]
      section_details["sync_id"] = section["sync_id"]
      section_details["collapsed"] = section["collapsed"]
      section_details["project_id"] = section["project_id"]      
      section_details["section_order"] = section["section_order"]
      section_details["date_added"] = section["date_added"]
      section_details["is_deleted"] = section["is_deleted"]
      section_details["is_archived"] = section["is_archived"]
      section_details["date_archived"] = section["date_archived"]
      section_ids.append(section_details)
    return section_ids


  def get_section_id_by_name(self, project_id, section_name):
    for section in self.get_sections():
      if section_name == section["name"] and project_id == section["project_id"]:
        return section["id"]
    return -1


  def create_todo_task(self, ticket_title, ticket_desc, ticket_priority, project_id, section_id):
    item_id = api.items.add(
        content=ticket_title,
        project_id=project_id,
        priority=ticket_priority,
        section_id=section_id
      )["id"]

    print(item_id)
    print(api.notes.add(
      item_id = item_id,
      content = ticket_desc
    ))