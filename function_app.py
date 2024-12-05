import azure.functions as func
import datetime
import json
import logging
import datatier
import os
app = func.FunctionApp()

endpoint = "feelxpert495.mysql.database.azure.com"
port = 3306
username = "FeelXpert"
password = "abc123!!"
database = "facedetectapp"
conn = datatier.get_dbConn(endpoint, port, username, password, database)

@app.route(route="upload_image", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
      # Get the request body
      req_body = req.get_json()
      userid = req_body.get('userid')
      status = req_body.get('status')
      originaldatafile = req_body.get('originaldatafile')
      datafilekey = req_body.get('datafilekey')
      emotion = req_body.get('emotion')
      if not userid or not status or not originaldatafile or not datafilekey or not emotion:
          return func.HttpResponse(
              "Please pass userid, status, originaldatafile, datafilekey and emotion in the request body",
              status_code=400
          )
      
      # Insert the data into the database
      sql = "INSERT INTO faces (userid, status, originaldatafile, datafilekey, emotion) VALUES (%s, %s, %s, %s, %s)"
      values = [userid, status, originaldatafile, datafilekey, emotion]
      datatier.perform_action(conn, sql, values)
      return func.HttpResponse(f"Hello, {userid}. Your image record has been uploaded.")
      
    except Exception as e:
      return func.HttpResponse(
          f"Error: {str(e)}",
          status_code=400
      )
        
@app.route(route="get_image", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def http_trigger_2(req: func.HttpRequest) -> func.HttpResponse:
    
    #get the latest image uploaded
    try:
        sql = "SELECT * FROM faces ORDER BY faceid DESC LIMIT 1"
        row = datatier.retrieve_one_row(conn, sql)
        if len(row) == 0:
            return func.HttpResponse("No image found in the database.")
        else:
            # convert row from tuple to dictionary
            row = dict(zip(['faceid', 'userid', 'status', 'originaldatafile', 'datafilekey', 'timestamp', 'emotion'], row))
            # cannot serialize datetime object as JSON
            row['timestamp'] = str(row['timestamp'])
            return func.HttpResponse(json.dumps(row))
    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )
        
@app.route(route="get_images", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def http_trigger_2(req: func.HttpRequest) -> func.HttpResponse:
    
    #get the latest image uploaded
    try:
        sql = "SELECT * FROM faces ORDER BY faceid DESC"
        row = datatier.retrieve_one_row(conn, sql)
        if len(row) == 0:
            return func.HttpResponse("No image found in the database.")
        else:
            # convert row from tuple to dictionary
            row = dict(zip(['faceid', 'userid', 'status', 'originaldatafile', 'datafilekey', 'timestamp', 'emotion'], row))
            # cannot serialize datetime object as JSON
            row['timestamp'] = str(row['timestamp'])
            return func.HttpResponse(json.dumps(row))
    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )
    

        