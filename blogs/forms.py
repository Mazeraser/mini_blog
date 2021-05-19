from django.forms import ModelForm
from .models import Post,Comm

class PostForm(ModelForm):
	class Meta :
		model = Post
		fields = ('Title','Info')
	def clean_Title(self):
		title = self.cleaned_data['Title']
		return title

class Comment(ModelForm):
	class Meta :
		model = Comm
		fields = ('text',)	
	def __init__(self, *args, **kwargs):
		super(Comment, self).__init__(*args, **kwargs)
		self.fields['text'].help_text = ''