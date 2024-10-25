#!/bin/bash
PROJECT_ID="gcp-project-id"
REGION="gcp-region"
gcloud builds submit --tag gcr.io/$PROJECT_ID/weather-data-api
gcloud run deploy weather-data-api --image gcr.io/$PROJECT_ID/weather-data-api --platform managed --region $REGION
