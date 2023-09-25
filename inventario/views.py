from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Loan, User
from .forms import Create_loan, Create_user, Create_book


# Create your views here.
def index(request):
    return render(request, 'index.html')


def books(request):
    book = Book.objects.all()
    return render(request, 'list_books.html', {
        'books': book
    })


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book.html', {
        'book': book
    })


def loan_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = Create_loan(request.POST or None)
    if book.units == 0:
        return render(request, 'error.html', {
            'message': "No hay cantidades disponibles"
        })
    if request.method == 'POST':
        if book.units > 0 and form.is_valid():
            id_b = book
            id_u = request.POST['user_id']
            user = get_object_or_404(User, id=id_u)
            l_d = request.POST['loan_date']
            d_d = request.POST['due_date']
            Loan.objects.create(book_id=id_b, user_id=user,
                                loan_date=l_d, due_date=d_d)
            book.units -= 1
            book.save()
            return render(request, 'loan_book.html', {
                'book': Book.objects.filter(id=book_id),
                'form': form,
                'message': "prestamo con éxito"
            })
    return render(request, 'loan_book.html', {
        'book': book,
        'form': form,
    })


def create_user(request):
    form = Create_user(request.POST or None)
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        User.objects.create(full_name=full_name, email=email)
        return render(request, 'register_user.html', {
            'form': form,
            'message': 'Registro con éxito'
        })
    return render(request, 'register_user.html', {
        'form': form,
        'message': "No se pudo registrar"
    })


def ver_prestamos(request):
    loans = Loan.objects.all()
    
    return render(request, 'ver_prestamos.html', {
        'loan': loans

    })

def return_book(request, id_loan):
    loan_delete = Loan.objects.get(id = id_loan)
    loan = Loan.objects.all()
    loan_delete.delete()
    return render(request, 'ver_prestamos.html', {
        'loan' : loan
    })

def register_book(request):
    form = Create_book(request.POST or None)
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        units = request.POST['units']
        Book.objects.create(name = name, author = author, units = units)
        return render(request, 'create_book.html',{
            'form': form
        })
    return render(request, 'create_book.html',{
            'form': form
        })