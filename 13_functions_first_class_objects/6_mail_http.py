from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


# Even for django you can specify typehints
def emp(request: HttpRequest) -> HttpResponse:
    # if request.method == 'POST':
    #     return emp_post(request)
    # else:
    #     return emp_general(request)

    return emp_post(request) if request.method == 'POST' else emp_general(request)


def emp_post(request: HttpRequest) -> HttpResponse:
    form = EmployeeForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            send_mail(
                "Employee Registration",
                "Hello  we have successfully registered your employee details to our system",
                "binibenny92@gamil.com",
                [request.POST.get('eemail')],
                fail_silently=False,
            )
        except:
            pass

    return redirect('/show')


def emp_general(request):
    form = EmployeeForm()
    return render(request, 'index.html', {'form': form})
