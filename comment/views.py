from django.shortcuts import render, get_object_or_404
from .models import Comment, Document
from .forms import CommentForm


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
        return redirect('view_document', document_id=comment.document.id)
    else:
        #TODO alert message
        print('You do not have permission to delete this comment')
