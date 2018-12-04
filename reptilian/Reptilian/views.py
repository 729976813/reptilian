from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse

class area_view(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(area_view, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        ret = {'test': 123}
        return JsonResponse(ret)

