import googleapiclient.discovery
from oauth2client.client import GoogleCredentials
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

project = "eternal-sylph-336115"
location = "us-central"

credentials = GoogleCredentials.get_application_default()
@app.post("/run/")
async def run_template(input_path: str, side_input_path: str, table: str, error_table: str):
    dataflow = googleapiclient.discovery.build('dataflow', 'v1b3', credentials=credentials)
    result = dataflow.projects().templates().launch(
            projectId=project,
            body={
              "environment": {
                "zone": "us-central1-f",
                "tempLocation": "gs://dezyre-bucket/dataflow/temp"
              },
              "parameters": {
                  "input_path" : input_path,
                  "side_input_path": side_input_path,
                  "table" : table,
                  "error_table": error_table
              },
              "jobName": "flight-test-batch-bq-service-gke-"+input_path.split("/")[-1]
            },
            gcsPath = "gs://dezyre-bucket/batchtemplate"
    ).execute()
    return result