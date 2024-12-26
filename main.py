from google.auth.transport.requests import Request
from google.oauth2.service_account import IDTokenCredentials
from googleapiclient.discovery import build

def list_buckets(request):
    impersonated_service_account = "189614076516-compute@developer.gserviceaccount.com"
    target_project = "sanath"
    
    # Get credentials for the impersonated service account
    credentials = IDTokenCredentials.from_target_principal(
        impersonated_service_account,
        target_scopes=["https://www.googleapis.com/auth/cloud-platform"],
        request=Request(),
    )
    
    # Use the impersonated credentials to call Cloud Storage
    storage_client = build('storage', 'v1', credentials=credentials)
    buckets = storage_client.buckets().list(project=target_project).execute()
    
    return {"buckets": buckets.get('items', [])}
