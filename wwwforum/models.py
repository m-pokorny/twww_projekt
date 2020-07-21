from django.db import models
from django.conf import settings
from django.forms import ModelForm, Textarea

# Create your models here.



class Sekce(models.Model):

	class Meta:
		verbose_name = "Sekce"
		verbose_name_plural = "Sekce"

	def __str__(self):
		return self.nazev
	
	nazev = models.CharField(max_length=50)
	poradi = models.IntegerField(unique=True)


class Vlakno(models.Model):

	class Meta:
		verbose_name = "Vlákno"
		verbose_name_plural = "Vlákna"

	def __str__(self):
		return self.nazev
	
	nazev = models.CharField(max_length=100)
	vytvoreno = models.DateTimeField(auto_now_add=True)
	materska_sekce = models.ForeignKey(Sekce,null = True, on_delete = models.SET_NULL )




class Prispevek(models.Model):

	class Meta:
		verbose_name = "Příspěvek"
		verbose_name_plural = "Příspěvky"

	def __str__(self):
		return str(self.autor)+' | '+str(self.vytvoreno)

	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	obsah = models.TextField(max_length=500)
	vytvoreno = models.DateTimeField(auto_now_add=True)
	materske_vlakno = models.ForeignKey(Vlakno, on_delete = models.CASCADE)


class PrispevekForm(ModelForm):
	class Meta:
		model = Prispevek
		fields = ('obsah',)
		widgets = {
		'obsah': Textarea(attrs={'cols': 60, 'rows': 10,}),
		}