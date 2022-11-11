from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Program
from .forms import ProgramForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


# Create your views here.
def program_main(request):
    programs = Program.objects.filter(is_active=True).order_by('-created')
    context = {'programs': programs}
    return render(request, 'program_main.html', context=context)


def program_desc(request, slug):
    program = Program.objects.get(slug=slug)
    programs = Program.objects.exclude(program_id__exact=program.program_id)[:5]
    context = {'program': program, 'programs': programs}
    return render(request, 'program_desc.html', context=context)


@login_required
def program_create(request):
    if request.user.has_perm('program.program_create'):
        form = ProgramForm
        if request.method == 'POST':
            form = ProgramForm(request.POST, request.FILES)
            if form.is_valid():
                program = form.save(commit=False)
                program.slug = slugify(program.title)
                program.author = request.user
                program.save()
                messages.info(request, 'Program was created successfully')
                return redirect('program_main')
        context = {'form': form}
        return render(request, 'program_create.html', context)
    else:
        return redirect('index')

@login_required
def program_manage(request, slug):
    if request.user.has_perm('program.program_manage'):
        program = Program.objects.get(slug=slug)
        if program.author == request.user:
            context = {'program': program}
            return render(request, 'program_manage.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def program_update(request, slug):
    if request.user.has_perm('post.program_update'):
        program = Program.objects.get(slug=slug)
        if program.author == request.user:
            form = ProgramForm(instance=program)
            if request.method == 'POST':
                form = ProgramForm(request.POST, request.FILES, instance=program)
                if form.is_valid():
                    form.save()
                    messages.info(request, 'Program was updated successfully')
                    return redirect('program_desc', slug=program.slug)
            context = {'form': form}
            return render(request, 'program_update.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def program_delete(request, slug):
    if request.user.has_perm('post.program_delete'):
        program = Program.objects.get(slug=slug)
        if program.author == request.user:
            form = ProgramForm(instance=program)
            if request.method == 'POST':
                program.delete()
                messages.info(request, 'Program was deleted successfully')
                return redirect('program_main')
            context = {'form': form}
            return render(request, 'program_delete.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')

