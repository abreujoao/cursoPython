from django.urls import path

# Importamos o módulo 'views' que está no mesmo diretório de 'urls.py'
from .views import posts, comments, tags, values

# namespace
# Dessa maneira conseguimos diferenciar rotas que possuem o mesmo
# nome, porém que estão em pacotes diferentes
app_name = 'blogs'

urlpatterns = [
    # posts
    path('posts/', posts.index, name='index'),
    path('posts/<int:post_id>/', posts.detail, name='detail'),

    #comments
    path('comments/', comments.index, name='index_comments'),
    path('comments/<int:comment_id>/', comments.detail, name='detail_comments'),

    #tag
    path('tags/', tags.IndexView.as_view(), name='tags_index'),
    #path('tags/<int:tag_id>/', tags.detail, name='tags_detail')

    #value
    path('values/', values.index, name='values_index'),
    path('values/', values.detail, name='values.detail')

]
