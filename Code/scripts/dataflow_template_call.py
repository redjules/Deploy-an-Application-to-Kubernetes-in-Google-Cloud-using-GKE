import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

project = "eternal-sylph-336115"
location = "us-central"

credentials = GoogleCredentials.get_application_default()

dataflow = googleapiclient.discovery.build('dataflow', 'v1b3', credentials=credentials)
result = dataflow.projects().templates().launch(
        projectId=project,
        body={
          "environment": {
            "zone": "us-central1-f",
            "tempLocation": "gs://dezyre-bucket/dataflow/temp"
          },
          "parameters": {
              "input_path" : "gs://dezyre-bucket/data/flights_sample.csv",
              "side_input_path": "gs://dezyre-bucket/data/airlines.csv",
              "table" : "dataset1.flights",
              "error_table": "dataset1.error"
          },
          "jobName": "flight-test-batch-bq"
        },
        gcsPath = "gs://dezyre-bucket/batchtemplate"
).execute()