from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    available = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    borrowed_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class IssueRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Issued", "Issued"),
            ("Returned", "Returned"),
        ],
        default="Issued",
    )

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"