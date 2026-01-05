from django.db import models
from users.models import Profile


# Talaba qilgan loyihalar
class Project(models.Model):
    title = models.CharField(max_length=100)  # Majburiy
    description = models.TextField(blank=True, null=True)  # Majburiy emas
    image = models.ImageField(upload_to='projects', default='projects/empty.png')
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    source_code = models.CharField(max_length=200, blank=True, null=True)
    vote_count = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)

    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='project_tag')


    @property
    def update_vote_count(self):
        reviews = self.review_set.all()
        print(reviews)
        upVotes = reviews.filter(value=1).count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_count = totalVotes
        self.vote_ratio = ratio

        self.save()


# Loyihaga bildirilgan fikrlar
class Review(models.Model):
    body = models.TextField()
    value = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


# Loyiha qaysi til va freymvorklarda qilingan
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

# Talabaga yuborilgan habarlar
class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='sender_message')
    reciever = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='reciever_message')


# Talaba malakalari. Bilgan freymvork va dasturlash tillari haqida
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)