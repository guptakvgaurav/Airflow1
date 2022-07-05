# import requests
# import csv
# import json
import  boto3
import requests as re
import pandas as pd
import csv
import requests

from auth import ACCESS_KEY,SECRET_KEY
#r = 'https://airflow-impressico-bucket.s3.ap-south-1.amazonaws.com/dept_data.csv'


def lambda_execute():
       client = boto3.client('lambda',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,
                             region_name = 'us-west-2')
       print("this is completed sucessfull ")


       #Then use the session to get the resource
       #s3 = client.resource('lambda')

        

    
               
