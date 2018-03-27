# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse

from forms import NewBusiness
from models import get_industry_choices, get_industry_subchoices

def create(request):
    form = NewBusiness()
    choices = get_industry_choices()
    sub_choices = get_industry_subchoices('92')

    context = {
        'form': form,
        'choices': choices,
        'sub_choices': sub_choices
    }
    return render(request, 'business/create.html', context)


def update(request):
    pass


def get_one(request):
    pass


def get_all(request):
    pass


def get_area(request):
    pass