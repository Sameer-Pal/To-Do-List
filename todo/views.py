from django.shortcuts import render,redirect 
from .models import Todo
def index(request):
   todo = Todo.objects.all()
   if request.method == 'POST':
      new_todo = Todo(
         title = request.POST['title']
      ) # this is  models.py 's title
      new_todo.save()
      return redirect('/')
   return render(request, 'index.html', {'todos': todo})

def delete(request, pk):
   todo = Todo.objects.get(id=pk)
   todo.delete()
   return redirect('/')