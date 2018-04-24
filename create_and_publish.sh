zip -r demo.zip * -x@exclude.lst
aws lambda create-function --function-name python-sevilla-demo --runtime python3.6 --handler handler.handler --role arn:aws:iam::xxxxxxxxxxxx:role/python-sevilla-role --tags "Project=PythonSevilla, Service=Demo, Stage=DEV" --description "Lambda de prueba" --timeout 15 --publish --zip-file fileb://demo.zip
