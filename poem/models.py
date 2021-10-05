from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    year_of_birth = models.PositiveIntegerField(null=False)
    year_of_death = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Poem(models.Model):
    name = models.CharField(max_length=150, null=False)
    text = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.author} - {self.name}'
