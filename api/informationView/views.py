from django.views.generic import TemplateView


class InformationView(TemplateView):
    template_name = "templates/info.html"