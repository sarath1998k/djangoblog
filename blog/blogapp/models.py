from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('blogapp:blogs_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class Blog(models.Model):
    name= models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    desc= models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering=('name',)
        verbose_name='blog'
        verbose_name_plural='blogs'

    def get_url(self):
        return reverse('blogapp:blog', args=[self.category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class Comment(models.Model):
    name = models.CharField(max_length=30)
    cmnt = models.TextField(blank=True,max_length=200)
    commentedon = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return '{}'.format(self.name,self.blog.name)












# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     category_img = models.ImageField(upload_to='media')
#
#     def __str__(self):
#         return self.name
# class Blog(models.Model):
#     heading = models.CharField(max_length=250)
#     img = models.ImageField(upload_to='media')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     desc = models.TextField()
#     date_added=models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.heading