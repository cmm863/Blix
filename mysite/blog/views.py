from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Blog, Category
from blog.forms import BlogForm, CategoryForm
from django.core.context_processors import csrf
from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all().order_by('posted').reverse()
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })


def create_category(request):
    warn_already_made = False
    if request.POST:
        formf = CategoryForm(request.POST)

        form = formf.save(commit=False)
        if Category.objects.filter(title=form.title).count() == 0:
            form.slug = slugify(form.title)
            form.save()
            return HttpResponseRedirect('/')
        else:
            warn_already_made = True
            form = CategoryForm()
    else:
        form = CategoryForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['throw_duplicity_error'] = warn_already_made

    return render_to_response('create_category.html', args)


def create_post(request):
    warn_already_made = False
    if request.POST:
        formf = BlogForm(request.POST)

        form = formf.save(commit=False)
        if Blog.objects.filter(title=form.title).count() == 0:
            form.slug = slugify(form.title)
            form.save()
            return HttpResponseRedirect('/')
        else:
            warn_already_made = True
            form = BlogForm()
    else:
        form = BlogForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['throw_duplicity_error'] = warn_already_made

    return render_to_response('create_post.html', args)
