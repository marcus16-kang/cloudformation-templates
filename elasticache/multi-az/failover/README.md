# Failover Automation for ElastiCache Global Datastore

## Create the Lambda layer

You should create a Lambda layer for Lambda function to use `redis-py` library.

Please download [ZIP file](https://github.com/marcus16-kang/cloudformation-templates/files/10886981/redis.zip) and create a layer.

``` shell
aws lambda publish-layer-version --layer-name <LAYER_NAME> --description <DESCRIPTION> --compatible-runtimes "python3.9" --compatible-architectures  "arm64" --zip-file fileb://redis.zip --region <REGION>
```

### Create the layer file

``` shell
mkdir python
pip3 install redis -t ./python
zip -r redis.zip ./python
```