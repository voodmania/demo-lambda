aws lambda update-function-configuration --function-name python-sevilla-demo --environment '{"Variables":{"CONN_STRING":"dbname=test host=test.xxxxxxxxxx.eu-west-1.rds.amazonaws.com port=5432 user=xxxxxxxx password=xxxxxxxxx"}}'