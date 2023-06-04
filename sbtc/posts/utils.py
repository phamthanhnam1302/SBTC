from django.conf import settings
from django.core.paginator import Paginator
from datetime import datetime, timedelta
import pytz

def get_posts_context(queryset, request):
    paginator = Paginator(queryset, settings.POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    datetime_now = datetime.now().replace(tzinfo=pytz.UTC)
    post_available = []
    for post in page_obj:
        comments = post.comments.all()
        new_comment = post.pub_date
        for comment in comments:
            if comment.created > new_comment:
                new_comment = comment.created
        if (new_comment > datetime_now - timedelta(hours=12, minutes=0)):
            post_available.append(post)
    return {
        'page_obj': post_available,
    }


def get_authors_context(queryset, request):
    paginator = Paginator(queryset, settings.AUTHORS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'page_obj': page_obj,
    }
