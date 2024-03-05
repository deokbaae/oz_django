import json

from django.http import HttpRequest, JsonResponse
from django.views import View

from article.services import create_comment_service

# Create your views here.


class CommentView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)
        comment = create_comment_service(
            int(body["article_id"]),
            body["author"],
            body["body"],
        )
        return JsonResponse({"comment_id": comment.id})
