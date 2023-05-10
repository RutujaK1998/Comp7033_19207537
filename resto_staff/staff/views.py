from rest_framework import viewsets
from .models import Staff
from .serializers import StaffSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from .forms import StaffForm
from rest_framework.decorators import api_view
from rest_framework.response import Response


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff/staff-list.html', {'staff': staff})

def staff_create(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('staff:staff_list')
    return render(request, 'staff/staff-form.html', {'form': form})


def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/staff-form.html', {'form': form})




def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff:staff_list')
    return render(request, 'staff/staff-delete-confirm.html', {'staff': staff})


@api_view(['GET'])
def staff_detail(request, pk):
    """
    Retrieve a single staff member by ID
    """
    staff_member = get_object_or_404(Staff, pk=pk)
    serializer = StaffSerializer(staff_member)
    return Response(serializer.data)



