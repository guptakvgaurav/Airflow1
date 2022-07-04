# import requests
# import csv
# import json
import  boto3
import requests as re
import pandas as pd
import csv
import requests

#from auth import ACCESS_KEY,SECRET_KEY
r = 'https://airflow-impressico-bucket.s3.ap-south-1.amazonaws.com/dept_data.csv'


def lambda1():
    #data=pd.read_csv(r)
    #print(r.headers['Content-Type'])
    with requests.Session() as s:
        download = s.get(r)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=' ')
        my_list = list(cr)
        for row in my_list:
                print(row)
    
    
    

        #session = boto3.Session( 
         #       aws_access_key_id='<ASIAV4LJIJSIXM7FHAUC>', 
          #      aws_secret_access_key='<bgPN4/9P8etNT78Wlh6DuF5H7Fwu5YRRu7xXRsnN>')


#Then use the session to get the resource
        #s3 = session.resource('s3')

        #my_bucket = s3.Bucket('airflow-impressico-bucket')

        #for my_bucket_object in my_bucket.objects.all():
          #       print(my_bucket_object.key)

    


    print("Upload Completed")
