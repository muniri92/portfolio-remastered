from django.views.generic import TemplateView
from portfolio_app.models import About, Portfolio, Education, Experience
# Create your views here.


class ClassView(TemplateView):
    """Home page template."""

    template_name = 'index.html'

    def get_context_data(self):
        """Pass image to the homepage."""
        about = About.objects.all()
        portfolio = Portfolio.objects.all()
        education = Education.objects.all()
        experience = Experience.objects.all()
        return {'about': about, 'portfolio': portfolio, 'education': education, 'experience': experience}
