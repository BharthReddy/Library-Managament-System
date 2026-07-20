from django.shortcuts import render, redirect
from .models import Book, Member, IssueRecord


# ---------------- Home ----------------
def home(request):
    return render(request, 'user/home.html')


# ---------------- User ----------------
def login(request):
    return render(request, 'user/login.html')


def register(request):
    if request.method == "POST":
        Member.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address']
        )
        return redirect('/login/')

    return render(request, 'user/register.html')


def books(request):
    books = Book.objects.all()
    return render(request, 'user/books.html', {'books': books})


def search(request):
    if request.method == "GET":
        query = request.GET.get('search')
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'user/search.html', {'books': books})

    return render(request, 'user/search.html')


# ---------------- Admin ----------------
def dashboard(request):
    return render(request, 'admin/dashboard.html')


def add_book(request):

    if request.method == "POST":

        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            isbn=request.POST['isbn'],
            category=request.POST['category'],
            quantity=request.POST['quantity'],
            available=request.POST['quantity']
        )

        return redirect('/dashboard/')

    return render(request, 'admin/add_book.html')


def members(request):
    members = Member.objects.all()
    return render(request, 'admin/members.html', {'members': members})


def issue_book(request):

    if request.method == "POST":

        member_name = request.POST['member']
        book_name = request.POST['book']
        status = request.POST['status']

        member = Member.objects.get(name=member_name)
        book = Book.objects.get(title=book_name)

        IssueRecord.objects.create(
            member=member,
            book=book,
            status=status
        )

        if status == "Issued":
            book.available -= 1
            member.borrowed_status = True
        else:
            book.available += 1
            member.borrowed_status = False

        book.save()
        member.save()

        return redirect('/history/')

    return render(request, 'admin/issue_book.html')


def history(request):
    records = IssueRecord.objects.all()
    return render(request, 'admin/history.html', {'records': records})
def update_book(request):
    return render(request, 'admin/update_book.html')


def delete_book(request):
    return render(request, 'admin/delete_book.html')


def borrow(request):
    return render(request, 'user/borrow.html')