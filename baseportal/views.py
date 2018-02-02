from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from paperauthor.models import Paper
from baseportal.models import PublishedJournal

# Create your views here.

class HomePageView(View):
    def get(self, request):
        journals=PublishedJournal.objects.all()
        return render(request, "baseportal/homepage.html", {"journals":journals})

class AboutUsView(View):
    def get(self, request):
        return render(request, "baseportal/aboutus.html")

class TrackView(View):
    def get(self, request):
        track_id=request.GET.get('id','')
        context={"track_id":track_id}
        if track_id == '':
            context["showtrack"]=False
        else:
            try:
                paper=Paper.objects.get(track_id=track_id)

            except (ValidationError, ObjectDoesNotExist) as e:
                context["showerror"]=True
                paper=None

            if paper is not None:
                context["showtrack"]=True
                context["paper"]=paper
                if paper.reviewer is None:
                    context["trackstatus"]=0
                elif paper.is_reviewed() is False:
                    context["trackstatus"]=1
                else:
                    context["trackstatus"]=2
        return render(request, "baseportal/track.html", context)
