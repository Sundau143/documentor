from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Document
from comment.models import Comment
from comment.forms import CommentForm
from .forms import DocumentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

@login_required
def documents_view(request):
    document_list = Document.objects.order_by("updated")
    context = {"document_list": document_list}
    return render(request, "document/document_list.html", context)

@login_required
def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document/create.html', {'form': form})

@login_required
def remove_document(request, document_id):
    if request.method == 'POST':
        document = get_object_or_404(Document, id=document_id)
        document.delete()
        return redirect('document_list')

    return redirect('document_list')

@login_required
def view_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)

    comments = Comment.objects.filter(document=document)
    comment_form = CommentForm()

    return render(request, "document/view.html", {"document": document, 'comments': comments, 'comment_form': comment_form})

@login_required
def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document/create.html', {'form': form})

@login_required
def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)

    return render(request, 'document/edit.html', {'form': form, 'document': document})

# === COMMENTS ===
@login_required
def create_comment(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            Comment.objects.create(
                content=form.cleaned_data['content'],
                user=user,
                document=document
            )

            return redirect('view_document', document_id=document_id)

    else:
        form = CommentForm()

    return render(request, 'document/view.html', {'document': document, 'comments': Comment.objects.filter(document=document), 'comment_form': form})
