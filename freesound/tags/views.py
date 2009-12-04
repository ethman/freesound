# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from utils.search.solr import SolrQuery, SolrResponseInterpreter, \
    SolrResponseInterpreterPaginator, SolrException, Solr
from django.conf import settings

def tags(request, multiple_tags=None):
    if multiple_tags:
        multiple_tags = multiple_tags.split('/')
    else:
        multiple_tags = []
    
    multiple_tags = sorted(filter(lambda x:x, multiple_tags))
    
    try:
        current_page = int(request.GET.get("page", 1))
    except ValueError:
        current_page = 1

    solr = Solr(settings.SOLR_URL)
    
    query = SolrQuery()
    if multiple_tags:
        query.set_query(" ".join("tag:\"" + tag + "\"" for tag in multiple_tags))
    else:
        query.set_query("*:*")
    query.set_query_options(start=(current_page - 1) * settings.SOUNDS_PER_PAGE, rows=settings.SOUNDS_PER_PAGE, field_list=["id"], sort=["downloads desc"])
    query.add_facet_fields("tag")
    query.set_facet_options_default(limit=100, sort=True, mincount=1, count_missing=False)
    
    try:
        results = SolrResponseInterpreter(solr.select(unicode(query)))
        paginator = SolrResponseInterpreterPaginator(results, settings.SOUNDS_PER_PAGE)
        page = paginator.page(current_page)
        error = False
    except SolrException, e:
        error = True
    
    tags = [dict(name=f[0], count=f[1]) for f in results.facets["tag"]]

    return render_to_response('sounds/tags.html', locals(), context_instance=RequestContext(request))