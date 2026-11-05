from django.db import models


# 1. რეჟისორრი
class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(s):
        return s.name


# 2. რეჟიშორზე ვან თუ ვანის მაგალითად
class DirectorProfile(models.Model):
    director = models.OneToOneField(Director, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.CharField(max_length=200)

    def __str__(s):
        return f"Profile of {s.director.name}"


# 3.            ჟანრი
class Genre(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(s):
        return s.title


# 4. მსაციობი
class Actor(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_award_winner = models.BooleanField(default=False)

    def __str__(s):
        return s.full_name


# 5. ფილმი ფორეინ კი რეჟისორთან და მენი თუ მენი ფილდებთან ჟანრებთან და მსახიობებთა
class Movie(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    rating = models.FloatField()

    # ფორეინჯი ფილმს ჰყავს ერთი რეჟისორი, რეჟისორს ბევრი ფილმი
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    # მენი თუ მენი ფილმს შეიძლება ჰქონდეს რამდენიმე ჟანრი და მსახიობი
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    def __str__(s):
        return s.title


# 6. მიმოხილვა და შეფასება ფორეინ კი ფილმთან
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(s):
        return f"Review by {s.author_name} for {s.movie.title}"
