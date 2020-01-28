# JobSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_non_restored_state** | **bool** |  | [optional] 
**artifact** | [**Artifact**](Artifact.md) |  | [optional] 
**deployment_target** | [**JobDeploymentTarget**](JobDeploymentTarget.md) |  | [optional] 
**flink_configuration** | **dict(str, str)** |  | [optional] 
**kubernetes** | [**KubernetesOptions**](KubernetesOptions.md) |  | [optional] 
**logging** | [**Logging**](Logging.md) |  | [optional] 
**number_of_task_managers** | **int** |  | [optional] 
**parallelism** | **int** |  | [optional] 
**resources** | [**dict(str, ResourceSpec)**](ResourceSpec.md) |  | [optional] 
**savepoint_location** | [**URI**](URI.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


