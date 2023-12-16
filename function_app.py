import azure.functions as func
#import azure.cosmos as db
import datetime
import json
import uuid
# import logging

app = func.FunctionApp()
headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type" : "application/json",
        "Access-Control-Allow-Headers": 
        "Access-Control-Allow-Origin,Origin,Content-Type,Accept,Set-Cookie",
        "Access-Control-Allow-Methods": "GET,PUT,POST",
}


@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')
    req_body = None
    print("header: ",  req.headers.get("Set-Cookie"))
    print("header: ",  req.headers.get("Content-Type"))
    if (req.headers.get("Content-Type") == "application/json"):
        print("yep")
    try:
        # if I don't handle the exception the get_json method does not work
        req_body = req.get_json()
    except ValueError:
        pass
    if (req_body):
        print(req_body)

    json_str = json.dumps({
        "yo" : 1
    })
    # headers["Set-Cookie"] = f"uuid={str(uuid.uuid4())}; SameSite=Strict; visited=true; SameSite=Strict"
    headers["Set-Cookie"] = f"visited=true; SameSite=Strict"
    return func.HttpResponse(body=json_str, headers=headers);

