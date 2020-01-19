from django.contrib.syndication.views import Feed
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "blogging news"
    link = "/blognews/"
    description = "The latest blog posts from your favorite person."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_text(self, item):
        return item.text
