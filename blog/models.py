from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
   
    def summary(self):
        if (len(self.body)) < 100:
            return self.body
        else: 
            body = self.body.split()[:20]
            return " ".join(body) + "..."

    def pub_date(self):
        return self.date.strftime('%e %b %Y')
       