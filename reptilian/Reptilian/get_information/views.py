from reptilian.Reptilian.config import COMPANY_COLLECTION_AREA, COLLECTION_AREA, COMPANY_COLLECTION_INDUSTRY, \
    COLLECTION_INDUSTRY
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse
import pymongo
import re


class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CompanyView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        name = request.GET.get('name')
        code = request.GET.get('code')
        ret = list(COMPANY_COLLECTION_AREA.find({'$or': [{'name': name}, {'code': code}]}, {'_id': 0}))
        return JsonResponse(ret, safe=False)


class CreateCompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateCompanyView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        ret = list(COMPANY_COLLECTION_AREA.find({}, {'_id': 0}))
        return JsonResponse(ret, safe=False)


class TotalAreaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TotalAreaView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        ret = list(COLLECTION_AREA.find({}, {'plate': 1, 'volume': 1, 'average': 1, '_id': 0}))
        return JsonResponse(ret, safe=False)


class OneIndustryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OneIndustryView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = request.GET.get('content')
        ret = list(COMPANY_COLLECTION_INDUSTRY.find({'content': content}, {'name': 1, 'current_price': 1, '_id': 0}))
        return JsonResponse(ret, safe=False)


class OneAreaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OneAreaView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = request.GET.get('content')
        ret = list(COMPANY_COLLECTION_AREA.find({'content': content}, {'name': 1, 'current_price': 1, '_id': 0}))
        return JsonResponse(ret, safe=False)


class AnalysisView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AnalysisView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        name = request.GET.get('name')
        company = list(
            COMPANY_COLLECTION_INDUSTRY.find({'name': name}, {'content': '1', '_id': 0}))
        content = company.pop()['content']
        ret = list(
            COMPANY_COLLECTION_INDUSTRY.find({'content': content},
                                             {'name': 1, 'circulation_mkvalue': 1, 'circulation_shares': 1, '_id': 0}))
        regnex = re.compile("(.*)亿")
        for item in ret:
            item['circulation_mkvalue'] = regnex.match(item['circulation_mkvalue']).group(1)
            item['circulation_shares'] = regnex.match(item['circulation_shares']).group(1)
            item['content'] = content
        return JsonResponse(ret, safe=False)


class AreaMapView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AreaMapView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = list(COLLECTION_AREA.find({}, {'plate': 1, 'rise_expon': 1, 'fall_expon': 1, '_id': 0}))
        for item in data:
            if item['plate'] == '上海其它':
                item['plate'] = '上海'
            if item['plate'] == '广东其它':
                item['plate'] = '广东'
        ret = []
        for item in data:
            ret.append({'plate': item['plate'], 'expon': int(item['rise_expon']) + int(item['fall_expon'])})
        return JsonResponse(ret, safe=False)


class TotalIndustryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TotalIndustryView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        ret = list(COLLECTION_INDUSTRY.find({}, {'plate': 1, 'volume': 1, 'average': 1, '_id': 0}))
        return JsonResponse(ret, safe=False)
