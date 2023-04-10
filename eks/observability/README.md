# EKS Observability

## Monitoring Each Pod using CloudWatch Logs Metric Filter

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

MetricFilterPrefix=""   # [REQUIRED] The prefix of metric filters.
PodName=""              # [REQUIRED] The name of pod which you want to filtering.
NamespaceName=""        # [REQUIRED] The name of namespace which you want to filtering.
ClusterName=""          # [REQUIRED] The name of EKS cluster which you want to filtering.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/observability/metric-filter.yaml

aws cloudformation deploy \
    --template-file ./metric-filter.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        MetricFilterPrefix=$MetricFilterPrefix \
        PodName=$PodName \
        NamespaceName=$NamespaceName \
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
$PodName=""              # [REQUIRED] The name of pod which you want to filtering.
$NamespaceName=""        # [REQUIRED] The name of namespace which you want to filtering.
$ClusterName=""          # [REQUIRED] The name of EKS cluster which you want to filtering.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/observability/metric-filter.yaml

aws cloudformation deploy `
    --template-file ./metric-filter.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        MetricFilterPrefix=$MetricFilterPrefix `
        PodName=$PodName `
        NamespaceName=$NamespaceName `
        ClusterName=$ClusterName `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```

## Monitopring Pods using Container Insights (Not each pod)

### Pod CPU Utilization

``` json
{
    "metrics": [
        [ { "id": "expr1m0", "label": "<NAMESPACE NAME> <POD NAME>", "expression": "mm1m0 + mm1farm0", "region": "<REGION CODE>", "period": 60 } ],
        [ "ContainerInsights", "pod_cpu_utilization_over_pod_limit", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "ClusterName", "<CLUSTER NAME>", { "id": "mm1m0", "visible": false, "region": "<REGION CODE>", "label": "ec2" } ],
        [ ".", ".", "ClusterName", "<CLUSTER NAME>", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "LaunchType", "fargate", { "id": "mm1farm0", "visible": false, "region": "<REGION CODE>", "label": "fargate" } ]
    ],
    "region": "<REGION CODE>",
    "title": "Pod CPU Utilization",
    "legend": {
        "position": "bottom"
    },
    "timezone": "UTC",
    "liveData": false,
    "period": 60,
    "view": "timeSeries",
    "stacked": false,
    "stat": "Average",
    "yAxis": {
        "left": {
            "min": 0,
            "max": 100,
            "label": "Percent",
            "showUnits": false
        }
    }
}
```

### Pod Memory Utilization

``` json
{
    "metrics": [
        [ { "id": "expr1m0", "label": "<NAMESPACE NAME> <POD NAME>", "expression": "mm1m0 + mm1farm0", "region": "<REGION CODE>", "period": 60 } ],
        [ "ContainerInsights", "pod_memory_utilization_over_pod_limit", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "ClusterName", "<CLUSTER NAME>", { "id": "mm1m0", "visible": false, "region": "<REGION CODE>", "label": "ec2" } ],
        [ ".", ".", "ClusterName", "<CLUSTER NAME>", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "LaunchType", "fargate", { "id": "mm1farm0", "visible": false, "region": "<REGION CODE>", "label": "fargate" } ]
    ],
    "region": "<REGION CODE>",
    "title": "Pod Memory Utilization",
    "legend": {
        "position": "bottom"
    },
    "timezone": "UTC",
    "liveData": false,
    "period": 60,
    "view": "timeSeries",
    "stacked": false,
    "stat": "Average",
    "yAxis": {
        "left": {
            "min": 0,
            "max": 100,
            "label": "Percent",
            "showUnits": false
        }
    }
}
```

### Pod Network Rx/Tx

``` json
{
    "metrics": [
        [ { "id": "expr0m0", "label": "<NAMESPACE NAME> <POD NAME> pod_network_rx_bytes", "expression": "mm0m0 + mm0farm0", "stat": "Average", "yAxis": "left", "region": "<REGION CODE>", "period": 60 } ],
        [ { "id": "expr1m0", "label": "<NAMESPACE NAME> <POD NAME> pod_network_tx_bytes", "expression": "mm1m0 + mm1farm0", "stat": "Average", "yAxis": "right", "region": "<REGION CODE>", "period": 60 } ],
        [ "ContainerInsights", "pod_network_rx_bytes", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "ClusterName", "<CLUSTER NAME>", { "id": "mm0m0", "visible": false, "yAxis": "left", "region": "<REGION CODE>" } ],
        [ ".", ".", "ClusterName", "<CLUSTER NAME>", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "LaunchType", "fargate", { "id": "mm0farm0", "visible": false, "yAxis": "left", "region": "<REGION CODE>" } ],
        [ ".", "pod_network_tx_bytes", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "ClusterName", "<CLUSTER NAME>", { "id": "mm1m0", "visible": false, "yAxis": "right", "region": "<REGION CODE>" } ],
        [ ".", ".", "ClusterName", "<CLUSTER NAME>", "PodName", "<POD NAME>", "Namespace", "<NAMESPACE NAME>", "LaunchType", "fargate", { "id": "mm1farm0", "visible": false, "yAxis": "right", "region": "<REGION CODE>" } ]
    ],
    "region": "<REGION CODE>",
    "title": "Network",
    "legend": {
        "position": "right"
    },
    "timezone": "UTC",
    "liveData": false,
    "period": 60,
    "view": "timeSeries",
    "stacked": false,
    "stat": "Average",
    "yAxis": {
        "left": {
            "label": "Bytes",
            "showUnits": false
        },
        "right": {
            "showUnits": false
        }
    }
}
```