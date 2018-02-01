from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from paperauthor.models import Paper

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, "baseportal/homepage.html")

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

            if paper is not None:
                context["showtrack"]=True
                context["trackstatus"]=0
                context["paper"]=paper
                print("DEBUG")
                print(paper)


        return render(request, "baseportal/track.html", context)
