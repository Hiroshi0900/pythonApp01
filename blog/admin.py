from django.contrib import admin
from .models import Post #postって名前でモデルクラスをインポート

admin.site.register(Post)
