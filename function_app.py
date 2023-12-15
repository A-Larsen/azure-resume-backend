import azure.functions as func
#import azure.cosmos as db
import datetime
import json
import logging

app = func.FunctionApp()
headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type" : "application/json",
        "Access-Control-Allow-Headers": "content-type,Access-Control-Allow-Origin"
}


@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    json_str = None

    with open("rest.json", "r") as file: json_str = file.read()
    json_dict = json.loads(json_str)
    json_dict["visitor_count"] = json_dict["visitor_count"] + 1
    json_str = json.dumps(json_dict)
    with open("rest.json", "w") as file: file.write(json_str)

    return func.HttpResponse(body=json_str, headers=headers);
