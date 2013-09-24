from django.shortcuts import get_object_or_404
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
import os.path

from verdantdocs.models import Document

def serve(request, document_id, document_filename):
    doc = get_object_or_404(Document, id=document_id)
    wrapper = FileWrapper(doc.file)
    response = HttpResponse(wrapper, content_type='application/octet-stream')

    filename = os.path.basename(doc.file.name)
    # TODO: strip out weird characters like semicolons from the filename
    # (there doesn't seem to be an official way of escaping them)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['Content-Length'] = doc.file.size

    return response
