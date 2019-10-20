from django.db import models

# Create your models here.
class Newspaper(models.Model):
	news_paper_name = models.CharField(max_length=100)

	def __str__(self):
		return "%s" % (self.news_paper_name)

""" There are multiple readers who read the same newspaper. In this example I assume these readers are childrens, teenagers, middle aged and old. Hence this is an example of one (Newspaper) to many (readers) relationship"""

class readers(models.Model):
	readers = models.CharField(max_length=100)
	newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)

	def __str__(self):
		return "%s" % (self.readers)
