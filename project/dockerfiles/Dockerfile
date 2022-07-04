FROM puckel/docker-airflow:1.10.9
RUN pip install requests
RUN pip install pandas
#RUN pip install sqlalchemy==1.3.24

#RUN pip install boto3
#RUN pip install apache-airflow-providers-amazon

ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
