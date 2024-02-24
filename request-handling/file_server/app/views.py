import os
from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def file_list(request: WSGIRequest, date: datetime = None):
    template_name = 'index.html'
    dir = request.GET.get('dir', 'files')
    context = {
        'files': get_files_data(dir, date),
        'date': date.date() if date is not None else None,
        'dir': dir
    }

    return render(request, template_name, context)


def get_files_data(path: str, date: datetime = None):
    all_data = [{'name': name,
                 'ctime': datetime.fromtimestamp(os.stat(os.path.join(path, name)).st_ctime),
                 'mtime': datetime.fromtimestamp(os.stat(os.path.join(path, name)).st_mtime)} for name in
                os.listdir(path)]
    return filter(
        lambda data: date is None or data['ctime'].date() == date.date() or data['mtime'].date() == date.date(), all_data)


def file_content(request: WSGIRequest, name: str):
    dir = request.GET.get('dir')

    with open(os.path.join(dir, name), "r") as file:
        content = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name,
                 'file_content': content,
                 'dir': dir}
    )
