from django.shortcuts import render, redirect
from django.views.generic.base import View
from paperauthor.forms import PaperForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from paperauthor.models import Paper
from django.core.exceptions import PermissionDenied
from sendfile import sendfile

class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        user=self.request.user
        return user.groups.filter(name='author').exists()


# Create your views here.
class AuthorPortalView(IsAuthorMixin, LoginRequiredMixin, View):
    def get(self, request):
        papers=Paper.objects.filter(author=request.user)
        context={
            "papers":papers
        }
        return render(request, "paperauthor/portal.html", context)

class AddPaperView(IsAuthorMixin, LoginRequiredMixin, View):
    def get(self, request):
        form=PaperForm()
        return render(request, "paperauthor/addpaper.html", {"form":form})
    
    def post(self, request):
        form=PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper=form.save(commit=False)
            paper.author=request.user
            paper.save()
            return redirect('paperauthor:portal')
        return render(request, "paperauthor/addpaper.html", {"form":form})

class ShowPaperView(IsAuthorMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.author != request.user:
            raise PermissionDenied
        return render(request, "paperauthor/showpaper.html", {"paper":paper})

class DownloadPaperView(IsAuthorMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        return sendfile(request,  paper.upload.path, attachment=True)



