zip -r demo.zip * -x@exclude.lst
aws lambda update-function-code --function-name python-sevilla-demo --publish --zip-file fileb://demo.zip
