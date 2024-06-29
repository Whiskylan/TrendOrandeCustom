from django.urls import path

from .views import get_hello, get_components, get_about, create_keyboard
from .views import keyboard_delete, get_keyboard_detail, profile
from .views import get_keycap_page, get_keycap_detail, search_keycap
from .views import get_switch_page, get_switch_detail, search_switch
from .views import get_case_page, get_case_detail, search_case
from .views import get_pcb_page, get_pcb_detail, search_pcb
from .views import get_plate_page, get_plate_detail, search_plate
from .views import get_stabs_page, get_stabs_detail, search_stabs
from .views import set_filter_case, reset_filter_case
from .views import edit_keyboard

urlpatterns = [
    path('', get_hello, name='home'),
    path('about/', get_about, name='about'),
    path('components/', get_components, name='components'),
    path('create/', create_keyboard, name='create_keyboard'),
    path('create/<str:component_type>/<int:component_id>/', create_keyboard, name='create_keyboard_with_component'),
    path('reset-filter-case/', reset_filter_case, name='reset_filter_case'),
    path('set-filter-case/', set_filter_case, name='set_filter_case'),
    path('edit/<int:pk>/', edit_keyboard, name='edit_keyboard'),

    #profile and keyboards
    path('profile/<str:username>/', profile, name='profile_user'),
    path('detail_keyboard/<int:pk>/', get_keyboard_detail, name='detail_keyboard'),
    path('keyboard_delete/<int:pk>/', keyboard_delete, name='keyboard_delete'),
    
    #keycap
    path('components/keycap_page/', get_keycap_page, name='keycap_page'),
    path('components/keycap_page/<int:pk>/', get_keycap_detail, name='keycap_detail_page'),
    path('components/keycap_page/search', search_keycap, name='search_keycap'),

    #switch
    path('components/switch_page/', get_switch_page, name='switch_page'),
    path('components/switch_page/<int:pk>/', get_switch_detail, name='switch_detail_page'),
    path('components/switch_page/search', search_switch, name='search_switch'),

    #case
    path('components/case_page/', get_case_page, name='case_page'),
    path('components/case_page/<int:pk>/', get_case_detail, name='case_detail_page'),
    path('components/case_page/search', search_case, name='search_case'),

    #plate
    path('components/plate_page/', get_plate_page, name='plate_page'),
    path('components/plate_page/<int:pk>/', get_plate_detail, name='plate_detail_page'),
    path('components/plate_page/search', search_plate, name='search_plate'),
    

    #pcb
    path('components/pcb_page/', get_pcb_page, name='pcb_page'),
    path('components/pcb_page/<int:pk>/', get_pcb_detail, name='pcb_detail_page'),
    path('components/pcb_page/search', search_pcb, name='search_pcb'),

    #stabs
    path('components/stabs_page/', get_stabs_page, name='stabs_page'),
    path('components/stabs_page/<int:pk>/', get_stabs_detail, name='stabs_detail_page'),
    path('components/stabs_page/search', search_stabs, name='search_stabs'),
]