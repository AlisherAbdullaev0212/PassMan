from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from password.models import FailedLoginAttempt


class BruteForceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if request.user.is_authenticated:
            return None

        if (
            request.method == "POST"
            and "username" in request.POST
            and "password" in request.POST
        ):
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user is None:
                FailedLoginAttempt.objects.create(user=None)
                attempts = FailedLoginAttempt.objects.filter(
                    timestamp__gte=timezone.now()
                    - settings.LOGIN_FAILURE_LIMIT_INTERVAL
                )
                if attempts.count() >= settings.LOGIN_FAILURE_LIMIT:
                    return redirect(reverse("blocked"))

        return None
