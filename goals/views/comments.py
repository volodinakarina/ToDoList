# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, permissions
# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from rest_framework.pagination import LimitOffsetPagination
#
# from goals.filters import CommentFilter
# from goals.models import Comment
# from goals.permissions import CommentPermissions
# from goals.serializers.comments_serializers import (
#     CommentCreateSerializer,
#     CommentSerializer,
# )
#
#
# class CommentListView(ListAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     pagination_class = LimitOffsetPagination
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_class = CommentFilter
#     ordering = ['-created']
#
#     def get_queryset(self):
#         queryset = Comment.objects.select_related('user').filter(
#             goal__category__board__participants__user=self.request.user,
#         )
#         return queryset
#
#
# class CommentCreateView(CreateAPIView):
#     serializer_class = CommentCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class CommentDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [CommentPermissions]
#
#     def get_queryset(self):
#         return Comment.objects.select_related('user')
