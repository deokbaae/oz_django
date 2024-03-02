from django.http import HttpRequest, JsonResponse
from django.views import View

from article.service import create_comment_service

# Create your views here.


class CommentView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        comment = create_comment_service(
            int(request.POST["article_id"]),
            request.POST["author"],
            request.POST["body"],
        )
        return JsonResponse({"comment_id": comment.id})
