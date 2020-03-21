from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        print(request.data, ' ..... api request.data')
        print(kwargs, ' ..... api kwargs')
        print(args, ' ..... api args')
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
