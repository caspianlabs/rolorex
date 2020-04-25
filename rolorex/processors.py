from rolorex.launchdarkly import ld, any_user


def get_flags(request):
    """
    Get feature flags from LaunchDarkly and pass them to the global template state.

    :param request: Django HttpRequest object
    :return: Dictionary of all LD feature flags
    """
    flags = ld.all_flags(any_user)
    return {'FLAGS': flags}
