from datetime import datetime

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id,
                                       )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    query = MovieSession.objects.all()
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        query = query.filter(show_time__date=session_date)
    return query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        raise MovieSession.DoesNotExist


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    try:
        session_to_update = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise MovieSession.DoesNotExist
    if show_time:
        session_to_update.show_time = show_time
    if movie_id:
        session_to_update.movie_id = movie_id
    if cinema_hall_id:
        session_to_update.cinema_hall_id = cinema_hall_id
    session_to_update.save()
    return session_to_update


def delete_movie_session_by_id(movie_session_id: int) -> None:
    try:
        MovieSession.objects.get(id=movie_session_id).delete()
    except MovieSession.DoesNotExist:
        raise ValueError("MovieSession does not exist")