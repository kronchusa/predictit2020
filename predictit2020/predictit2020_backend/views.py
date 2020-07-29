from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy

from .forms import RegisterForm
from .models import DeclareWinners, Prediction

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime
import json


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prediction_count'] = Prediction.objects.all().count()
        context['declare_winners'] = DeclareWinners.objects.all().count() > 0
        if context['declare_winners']:
            context['winners'] = [p for p in Prediction.objects.exclude(user__username='actual').order_by('user__username') if p.is_winner()]
        return context


class MyMapView(LoginRequiredMixin, TemplateView):

    # TODO - Add winner and loser view

    template_name = 'mymap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.request.META['HTTP_HOST']
        return context


class ShareMapView(TemplateView):

    template_name = 'sharemap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prediction_id'] = self.request.GET.get('id')
        context['base_url'] = self.request.META['HTTP_HOST']
        return context



class RegisterView(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect(reverse_lazy('my_map'))
        else:
            return redirect(reverse_lazy('registration'))

    def get(self, request):
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})


class SaveStatesAPIView(APIView):
    def post(self, request):
        if datetime.date.today() < datetime.date(year=2020, month=11, day=3):
            if request.user:
                try:
                    prediction = request.user.prediction
                except:
                    prediction = Prediction(user=request.user)

                for state, fill_dict in request.data['states'].items():
                    if state == 'ID':
                        state = 'IDA'
                    if fill_dict['fill'] == 'navy':
                        setattr(prediction, state, 'd')
                    else:
                        setattr(prediction, state, 'r')

                prediction.electoral_votes_dem = request.data['electoralVotes']['democrats']
                prediction.electoral_votes_rep = request.data['electoralVotes']['republicans']

                prediction.save()
                return Response(status=200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)


class LoadStatesAPIView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        view_id = request.GET.get('view_id')

        if not view_id:
            try:
                prediction = request.user.prediction
            except AttributeError:
                return Response(status=403)

            dict_obj = model_to_dict(prediction)


        else:
            try:
                prediction = Prediction.objects.get(id=view_id)
            except:
                return Response(status=403)
            dict_obj = model_to_dict(prediction)

        for key, obj in dict_obj.items():
            if obj == 'd':
                fill_color = 'navy'
                dict_obj[key] = {'fill': fill_color}
            elif obj == 'r':
                fill_color = 'red'
                dict_obj[key] = {'fill': fill_color}

        if request.user or view_id:
            return Response(data={
                'username': prediction.user.username,
                'prediction': json.dumps(dict_obj),
                'base_url': request.META['HTTP_HOST']
            }, status=200)
        else:
            return Response(status=403)
