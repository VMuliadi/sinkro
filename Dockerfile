FROM python:3.7.9-slim-buster
ENV TODOIST_ACCESS_TOKEN
ENV TODOIST_PROJECT_NAME
ENV TODOIST_SECTION_NAME
ENV JIRA_ACCESS_TOKEN
ENV JIRA_USER_MAIL
RUN pip install -r requirements.txt 
ENTRYPOINT ["python", "main.py"]