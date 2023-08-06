
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'recipeestorage' # Must be replaced by your <storage_account_name>
    account_key = 'SlfjXqpsiUuyfSfwIvSLbEu5oSK9Dp3t0bRGVEKdbzuwXhRTkNP0FXGTzQbvujZuWvtiXC749u6D+AStzdqtCg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'recipeestorage' # Must be replaced by your storage_account_name
    account_key = 'SlfjXqpsiUuyfSfwIvSLbEu5oSK9Dp3t0bRGVEKdbzuwXhRTkNP0FXGTzQbvujZuWvtiXC749u6D+AStzdqtCg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None