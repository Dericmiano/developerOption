from django.shortcuts import render, redirect
from .models import Project, Tag
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects, paginateProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


# projectsList=[
#     {
#         'id':'1',
#         'title':'ecommerce website',
#         'description':"fully function ecommerce website"
#     },
#     {
#         'id':'2',
#         'title':'portfolio website',
#         'description':"this was my project to built my portfolio "
#     },
#     {
#         'id':'3',
#         'title':'social network',
#         'description':"awesome open source project"
#     },
#
# ]

def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)
    context = {'projects': projects, 'search_query': search_query,
               'custom_range ': custom_range}
    return render(request, 'projects/projects.html', context)


# def project(request, pk):
#     projectObj = Project.objects.get(id = pk)
#     tags = projectObj.tags.all()
#     return render(request, 'projects/single-project.html',{'project':projectObj,'tags':tags})
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        # //update project vote count
        projectObj.getVoteTotal
        messages.success(request, 'your review was successfully submitted')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(",", " ").split()

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
        # print(request.POST)
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(",", " ").split()
        print('data', newtags)

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
        # print(request.POST)
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)
