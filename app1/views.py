from django.http import HttpResponse
from .tasks import test_func


def test(request):
    test_func.delay()
    return HttpResponse("done")


def mail(request):
    # send_mail_task.delay()
    return HttpResponse("Sent")
