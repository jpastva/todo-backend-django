from rest_framework import status
from rest_framework.views import APIView

from todo_backend_django.JSONResponse import JSONResponse

from todo_backend_django.models import TodoItem
from todo_backend_django.serializers import TodoItemSerializer


class TodoList(APIView):
    def get(self, request, format=None):
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            saved_item = serializer.save()
            saved_item.url = request.build_absolute_uri(
                '/todo/' + str(saved_item.id))
            saved_item.save()
            serializer = TodoItemSerializer(instance=saved_item)
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        TodoItem.objects.all().delete()
        return JSONResponse(None, status=status.HTTP_204_NO_CONTENT)


class Todo(APIView):
    def get(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
            serializer = TodoItemSerializer(todoItem)
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
            todoItem.delete()
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponse(None, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoItemSerializer(
            data=request.data, instance=todoItem, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' New view for displaying completed tasks '''


class TodoDone(APIView):
    def get(self, request, format=None):
        done_items = TodoItem.objects.filter(completed=True)
        serializer = TodoItemSerializer(done_items, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)


''' New view for displaying pending tasks '''


class TodoPending(APIView):
    def get(self, request, format=None):
        pending_items = TodoItem.objects.filter(completed=False)
        serializer = TodoItemSerializer(pending_items, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)


''' New view to sort tasks by oldest '''


class TodoOldest(APIView):
    def get(self, request, format=None):
        list_items = TodoItem.objects.order_by('-created')
        serializer = TodoItemSerializer(list_items, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)
