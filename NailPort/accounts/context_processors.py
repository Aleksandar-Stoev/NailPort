def profile_incomplete(request):
    user = request.user
    if user.is_authenticated:
        profile = getattr(user, 'profile', None)
        incomplete = not (profile and profile.first_name and profile.last_name and profile.phone_number)
    else:
        incomplete = False
    return {'show_profile_banner': incomplete}
