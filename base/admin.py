from django.contrib import admin

from .models import Post, Tag, About


# admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(About)
# admin.site.register(PostComment)
