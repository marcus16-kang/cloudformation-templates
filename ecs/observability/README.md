# EKS Observability

## Monitoring Each Pod using CloudWatch Logs Metric Filter

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

MetricFilterPrefix=""   # [REQUIRED] The prefix of metric filters.
ClusterName=""          # [REQUIRED] The name of ECS cluster which you want to filtering.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/observability/metric-filter.yaml

aws cloudformation deploy \
    --template-file ./metric-filter.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        MetricFilterPrefix=$MetricFilterPrefix \
        ClusterName=$ClusterName \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

### Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

$MetricFilterPrefix=""   # [REQUIRED] The prefix of metric filters.
$ClusterName=""          # [REQUIRED] The name of ECS cluster which you want to filtering.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/observability/metric-filter.yaml

aws cloudformation deploy `
    --template-file ./metric-filter.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        MetricFilterPrefix=$MetricFilterPrefix `
        ClusterName=$ClusterName `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```

### Metric Syntax

**Task CPU Utilization**

``` sql
SELECT AVG(task_cpu_utilization) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```

**Task Memory Utilization**

``` sql
SELECT AVG(task_memory_utilization) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```

**Task Network Rx**

``` sql
SELECT AVG(task_network_rx_bytes) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```

**Task Network Tx**

``` sql
SELECT AVG(task_network_tx_bytes) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```

**Task Storage Read**

``` sql
SELECT AVG(task_storage_read_bytes) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```

**Task Storage Write**

``` sql
SELECT AVG(task_storage_write_bytes) FROM SCHEMA("ECS/ContainerInsights", ServiceName,TaskId) WHERE ServiceName = '<SERVICE_NAME>' GROUP BY TaskId
```