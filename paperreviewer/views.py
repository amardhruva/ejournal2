from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.base import View
from paperauthor.models import Paper
from paperreviewer.models import PaperReviewRequest
from django.core.exceptions import PermissionDenied
from sendfile import sendfile
from paperreviewer.forms import ReviewPaperForm, ReviewRequestForm
from django.urls import resolve

class IsReviewerMixin(UserPassesTestMixin):
    def test_func(self):
        user=self.request.user
        return user.groups.filter(name='reviewer').exists()

# Create your views here.
class ReviewerPortalView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request):
        papers=Paper.objects.filter(reviewer=request.user)
        reviewrequests=PaperReviewRequest.objects.filter(reviewer=request.user)
        context={
            "papers": papers,
            "reviewrequests": reviewrequests,
        }
        return render(request, "paperreviewer/portal.html", context)

class ReviewRequestView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperid):
        reviewrequest=get_object_or_404(PaperReviewRequest, id=paperid)
        if reviewrequest.reviewer != request.user:
            raise PermissionDenied
        if reviewrequest.status is not None:
            raise Http404
        paper=reviewrequest.paper
        form=ReviewRequestForm()
        context={
            "paper":paper,
            "reviewrequest":reviewrequest,
            "form":form,
        }
        return render(request, "paperreviewer/reviewrequest.html", context)
    def post(self, request, paperid):
        reviewrequest=get_object_or_404(PaperReviewRequest, id=paperid)
        if reviewrequest.reviewer != request.user:
            raise PermissionDenied
        if reviewrequest.status is not None:
            raise Http404
        paper=reviewrequest.paper
        form=ReviewRequestForm(request.POST)
        if form.is_valid():
            status=form.cleaned_data.get("status")
            if status==PaperReviewRequest.ACCEPTED:
                PaperReviewRequest.objects.filter(paper=paper).update(status=PaperReviewRequest.REJECTED)
                paper.reviewer=request.user
                paper.save()
            reviewrequest.status=status
            reviewrequest.save()
            return redirect('paperreviewer:portal')
        context={
            "paper":paper,
            "reviewrequest":reviewrequest,
            "form":form,
        }
        return render(request, "paperreviewer/reviewrequest.html", context)


class ShowPaperView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        return render(request, "paperreviewer/showpaper.html", {"paper":paper})

class ReviewPaperView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        if paper.is_reviewed():
            raise Http404
        form=ReviewPaperForm()
        return render(request, "paperreviewer/reviewpaper.html",
                       {"paper":paper, "form":form})
    def post(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        if paper.is_reviewed():
            raise Http404
        form=ReviewPaperForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.paper=paper
            review.save()
            return redirect("paperreviewer:showpaper",paperslug=paper.slug)
        return render(request, "paperreviewer/reviewpaper.html",
                       {"paper":paper, "form":form})

class DownloadPaperView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        return sendfile(request,  paper.upload.path, attachment=True)

class DownloadSuggestedCorrectionsView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        return sendfile(request,  paper.paperresubmission.suggested_corrections.path, attachment=True)

class DownloadPerformedCorrectionsView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request, paperslug):
        paper=Paper.objects.get(slug=paperslug)
        if paper.reviewer != request.user:
            raise PermissionDenied
        return sendfile(request,  paper.paperresubmission.performed_corrections.path, attachment=True)

class AnnotateView(IsReviewerMixin, LoginRequiredMixin, View):
    def get(self, request):
        uri=request.GET.get('file','')
        a=resolve(uri)
        paperslug=a.kwargs["paperslug"]
        paper=get_object_or_404(Paper,slug=paperslug)
        return render(request, "annotate/viewer.html", {"paper":paper})


