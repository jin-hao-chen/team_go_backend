from users.models import User
from clubs.models import Club


def get_user_number(club_id):
    club = Club.objects.filter(id=club_id).first()
    print(User.objects.filter(clubs=club).count())
    return User.objects.filter(clubs=club).count()


def put_user_number(club_serializer):
    club_list = club_serializer.data
    for club in club_list:
        club['userNumber'] = get_user_number(club['id'])
    return club_list
