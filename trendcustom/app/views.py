from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Keycap, Switch, Case, Plata, Stabilizer, Plate, Completed_Keyboard
from .forms import CompletedKeyboardForm

def get_hello(request):
    return render(request, 'home.html')

def get_components(request):
    return render(request, 'components.html')

def get_about(request):
    return render(request, 'about.html')

#profile and completed keyboard
@login_required
def profile(request, username):
    if username!= request.user.username:
        return render(request, 'access_denied.html')  # Предполагается, что у вас есть шаблон access_denied.html

    keyboards = Completed_Keyboard.objects.filter(user=request.user)
    return render(request, 'profile.html', {'keyboards': keyboards})

@login_required
def get_keyboard_detail(request, pk):
    keyboard = get_object_or_404(Completed_Keyboard, pk=pk)
    
    # Проверяем, является ли текущий пользователь владельцем клавиатуры
    if keyboard.user!= request.user:
        # Если нет, перенаправляем на страницу отказа в доступе
        return render(request, 'access_denied.html')
    
    return render(request, 'detail_keyboard.html', context={
        'keyboard': keyboard
    })

def keyboard_delete(request, pk):
    try:
        keyboard = Completed_Keyboard.objects.get(pk=pk)
    except Completed_Keyboard.DoesNotExist:
        raise Http404("Keyboard not found")

    if request.method == 'POST':
        keyboard.delete()
        return redirect('profile_user', username=request.user.username)

    return render(request, 'keyboard_confirm_delete.html', {'keyboard': keyboard})

def edit_keyboard(request, pk):
    keyboard = get_object_or_404(Completed_Keyboard, pk=pk)
    if request.method == 'POST':
        form = CompletedKeyboardForm(request.POST, instance=keyboard)
        if form.is_valid():
            form.save()
            return redirect('detail_keyboard', pk=keyboard.pk)
    else:
        form = CompletedKeyboardForm(instance=keyboard)
    return render(request, 'edit_keyboard.html', {'form': form})

def create_keyboard(request, component_type=None, component_id=None):
    session_key = f'completed_keyboard_{request.session.get("session_key", "")}'
    
    saved_data = request.session.get(session_key, {})
    if not saved_data:
        saved_data = {}
        request.session[session_key] = saved_data
    
    if request.method == 'POST':
        saved_data.update(request.POST.dict())
        del saved_data['csrfmiddlewaretoken']

        form = CompletedKeyboardForm(saved_data, initial={'user': request.user})
        if form.is_valid():
            
            if form.cleaned_data['user']!= request.user:
                form.add_error(None, 'Field User dont can be changed.')
                return render(request, 'create_keyboard.html', {'form': form})
            
            form.save(commit=False)
            if component_type and component_id:
                component = get_object_or_404(eval(component_type.capitalize()), id=component_id)
                setattr(form.instance, component_type.lower(), component)
            form.save()
            
            del request.session[session_key]
            
            return redirect('profile_user', username=request.user.username)
        else:
            return HttpResponseBadRequest(f"Invalid form data: {form.errors}")
        
    else:
        if component_type and component_id:
            component = get_object_or_404(eval(component_type.capitalize()), id=component_id)
            saved_data[component_type] = component_id
            if component_type == 'case':
                saved_data['form_factor'] = component.form_factor.id
            request.session[session_key] = saved_data
            form = CompletedKeyboardForm(initial={**{'user': request.user}, **saved_data})
        else:
            form = CompletedKeyboardForm(initial={'user': request.user})

    return render(request, 'create_keyboard.html', {'form': form, 'session_data': saved_data})

#keycap
def get_keycap_page(request):
    keycap_info = Keycap.objects.all()
    return render(request, 'keycap_page.html', context= {
        'keycap_info': keycap_info,
    })

def get_keycap_detail(request, pk):
    keycap = Keycap.objects.get(pk=pk)
    return render(request, 'detail_keycap.html', context= {
        'keycap': keycap
    })

def search_keycap(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        keycap_info = Keycap.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='keycap_page.html', context= {
            'keycap_info': keycap_info,
            'title': "Keycap"
    })
    return redirect(reverse('home'))

#switch
def get_switch_page(request):
    switch_info = Switch.objects.all()
    return render(request, 'switch_page.html', context= {
        'switch_info': switch_info,
    })

def get_switch_detail(request, pk):
    switch = Switch.objects.get(pk=pk)
    return render(request, 'detail_switch.html', context= {
        'switch': switch
    })

def search_switch(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        switch_info = Switch.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='switch_page.html', context= {
            'switch_info': switch_info,
            'title': "switch"
    })
    return redirect(reverse('home'))
#case
def get_case_page(request):
    case_info = Case.objects.all()
    return render(request, 'case_page.html', context= {
        'case_info': case_info,
    })

def get_case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    return render(request, 'detail_case.html', context= {
        'case': case
    })

def search_case(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        case_info = Case.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='case_page.html', context= {
            'case_info': case_info,
            'title': "case"
    })
    return redirect(reverse('home'))

#filter
@csrf_exempt
def set_filter_case(request):
    if request.method == 'POST':
        session_key = f'completed_keyboard_{request.session.get("session_key", "")}'
        saved_data = request.session.get(session_key, {})
        saved_data['form_factor'] = request.POST.get('form_factor_id')
        request.session[session_key] = saved_data
        return JsonResponse({'status': 'success'})

@csrf_exempt
def reset_filter_case(request):
    if request.method == 'POST':
        session_key = f'completed_keyboard_{request.session.get("session_key", "")}'
        saved_data = request.session.get(session_key, {})
        del saved_data['form_factor']
        request.session[session_key] = saved_data
        return JsonResponse({'status': 'success'})

#pcb
def get_pcb_page(request):
    session_key = f'completed_keyboard_{request.session.get("session_key", "")}'
    saved_data = request.session.get(session_key, {})
    form_factor_id = saved_data.get('form_factor')
    
    if form_factor_id:
        pcb_info = Plata.get_form_factors(form_factor_id)
    else:
        pcb_info = Plata.objects.all()
    
    return render(request, 'pcb_page.html', context={
        'pcb_info': pcb_info,
    })

def get_pcb_detail(request, pk):
    pcb = Plata.objects.get(pk=pk)
    return render(request, 'detail_pcb.html', context= {
        'pcb': pcb
    })

def search_pcb(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        pcb_info = Plata.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='pcb_page.html', context= {
            'pcb_info': pcb_info,
            'title': "pcb"
    })
    return redirect(reverse('home'))

#plate
def get_plate_page(request):
    session_key = f'completed_keyboard_{request.session.get("session_key", "")}'
    saved_data = request.session.get(session_key, {})
    form_factor_id = saved_data.get('form_factor')
    
    if form_factor_id:
        plate_info = Plate.get_form_factors(form_factor_id)
    else:
        plate_info = Plate.objects.all()
    return render(request, 'plate_page.html', context= {
        'plate_info': plate_info,
    })

def get_plate_detail(request, pk):
    plate = Plate.objects.get(pk=pk)
    return render(request, 'detail_plate.html', context= {
        'plate': plate
    })

def search_plate(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        plate_info = Plate.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='plate_page.html', context= {
            'plate_info': plate_info,
            'title': "plate"
    })
    return redirect(reverse('home'))

#stabs
def get_stabs_page(request):
    stabs_info = Stabilizer.objects.all()
    return render(request, 'stabs_page.html', context= {
        'stabs_info': stabs_info,
    })

def get_stabs_detail(request, pk):
    stabs = Stabilizer.objects.get(pk=pk)
    return render(request, 'detail_stabs.html', context= {
        'stabs': stabs
    })

def search_stabs(request):
    
    if request.method == 'GET':
        search = request.GET['search']
        stabs_info = Stabilizer.objects.filter(
            Q(name__icontains = search) | Q(brand__name__icontains = search))
        return render(request, template_name='stabs_page.html', context= {
            'stabs_info': stabs_info,
            'title': "stabs"
    })
    return redirect(reverse('home'))