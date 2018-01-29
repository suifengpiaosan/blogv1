import xadmin
from article.models import Articles

class ArticleAdmin(object):
    pass
xadmin.site.register(Articles, ArticleAdmin)