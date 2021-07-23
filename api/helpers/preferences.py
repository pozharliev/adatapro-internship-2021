from ..accountView.models import ProfilePreferences


def choose_preference(request, site, wish):
    ProfilePreferences.objects.raw(f"""
        UPDATE accountview_profilepreferences
        SET {site} = {wish}
        WHERE profile_username_id = {request.user.id}
    """)


