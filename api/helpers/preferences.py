from django.db import connection


def choose_preference(request, site, wish):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            UPDATE accountview_profilepreferences
            SET {site} = {wish}
            WHERE profile_username_id = {request.user.id}
            """)



