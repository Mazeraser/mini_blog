from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	class Meta :
		model = Post
		fields = ('Title','Info')
	def clean_Title(self):
		title = self.cleaned_data['Title']
		return title
