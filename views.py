from django.http import HttpResponse
from django.shortcuts import render_to_response
from BookDB.models import Book,Author
def search_form(request):
    return render_to_response('search_form.htm')
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        author = Author.objects.filter(Name=q)
        books=Book.objects.filter(AuthorID=author)
        dic = {'T':True, 'books':books}
        return render_to_response('title.htm',dic)
    else:
        return render_to_response('noselect.htm')
def fTitle(request):
    q = request.GET['q']
    book = Book.objects.get(Title=q)
    author=Author.objects.get(AuthorID=book.AuthorID)
    dic = {'titled1':book.ISBN, 'titled2':book.Title,'titled3':book.AuthorID,'titled4':book.Publisher,'titled5':book.PublishDate,'titled6':book.Price,'titled7':author.AuthorID,'titled8':author.Name,'titled9':author.Age,'titled10':author.Country}
    return render_to_response('authorandbook.htm',dic)
    
def fDelete(request):
    q = request.GET['q']
    Book.objects.get(Title=q).delete()
    return render_to_response('delete.htm')
def Add_form(request):
    return render_to_response('Add.htm')
    
def Add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=request.GET['c']
    d=request.GET['d']
    e=request.GET['e']
    f=request.GET['f']
    g=request.GET['g']
    h=request.GET['h']
    i=request.GET['i']
    t= Author(AuthorID=a,Name=b,Age=c,Country=d)
    t.save()
    p=Book(ISBN=e,Title=f,AuthorID=t,Publisher=g,PublishDate=h,Price=i)
    p.save()
    return render_to_response('Add_result.htm')
def update_form(request):
    return render_to_response('update_form.htm')
def update(request):
    a=request.GET['a']
    b=request.GET['b']
    c=request.GET['c']
    d=request.GET['d']
    e=request.GET['e']
    Book.objects.filter(Title=a).update(AuthorID=b,Publisher=c,PublishDate=d,Price=e)
    return render_to_response('update.htm')
