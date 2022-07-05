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


def lambda1():
        s3_client = boto3.client('s3', 
                      aws_access_key_id=ACCESS_KEY, 
                      aws_secret_access_key=SECRET_KEY, 
                      region_name='us-west-2'
                      )
        
        print("this completed")
        
        session = boto3.Session( 
              aws_access_key_id=ACCESS_KEY, 
              aws_secret_access_key=SECRET_KEY)


#Then use the session to get the resource



        


       #Then use the session to get the resource
        s3 = session.resource('s3')

        my_bucket = s3.Bucket('abcd-test-bucket')

        for my_bucket_object in my_bucket.objects.all():
                     print(my_bucket_object.key)

    
               
