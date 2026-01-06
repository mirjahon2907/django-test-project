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


    def update_vote_count(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value=1).count()
        totalVotes = reviews.count()

        if totalVotes > 0:
            self.vote_ratio = int((upVotes / totalVotes) * 100)
        else:
            self.vote_ratio = 0

        self.vote_count = totalVotes
        self.save()

    def __str__(self):
        return self.title



# Loyihaga bildirilgan fikrlar
class Review(models.Model):

    VOTE_TYPE = (
        (1, 'Up Vote'),
        (-1, 'Down Vote'),
    )

    body = models.TextField()
    value = models.IntegerField(choices=VOTE_TYPE)
    created = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True,related_name='reviews')
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


# Loyiha qaysi til va freymvorklarda qilingan
class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

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