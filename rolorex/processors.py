from django.conf import settings


def get_flags(request):
    """
    Get feature flags and pass them to the global template state.

    :param request: Django HttpRequest object
    :return: Dictionary of all feature flags
    """
    return {'FLAGS': settings.FLAGS}
