from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Post
from api.serializers import PostSerializer
from api.permissions import IsAdminAuthenticated, IsAuthorAuthenticated


class PostViewset(ReadOnlyModelViewSet):
    permission_classes = [IsAdminAuthenticated | IsAuthorAuthenticated]

    serializer_class = PostSerializer
 
    def get_queryset(self):
        return Post.objects.all()