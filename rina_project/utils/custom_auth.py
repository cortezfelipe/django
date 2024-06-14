from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

import requests


class CACustomAuth(BaseBackend):

    def authenticate(self, request, username=None, password=None):

        # Verifica se o usuário existe nas tabelas do Django
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        # Verifica se o usuário existe na Base Petro
        url = "https://spo.petrobras.com.br/carest/api/logonInternalUser"
        headers = {"Content-Type": "application/json"}
        
        data = {
            "regionalId": f"{settings.CA_REGIONAL_ID}",
            "environmentId": f"{settings.CA_ENVIRONMENTAL_ID}",
            "applicationCatalogId": f"{settings.CA_APPLICATION_CATALOG_ID}",
            "applicationPassword": f"{settings.CA_APPLICATION_PASSWORD}",
            "userLogin": f"{user.username}",
            "userPassword": f"{password}"
        }

        response = requests.post(url, json=data, headers=headers, verify=False)

        json_response = response.json()

        if json_response['request']['boolean'] == True:
            return user
        else:
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None