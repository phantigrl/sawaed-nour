from django.urls import path
from django.shortcuts import render
from . import views
from .views import (
    home, page1, services, message, ourteam, why_us,
    chairman, ourteam_detail, room_service, reception,
    maintenance, food_beverage, seasonal_labor,
    what_are_we_doing, vision_mission_view, our_aims_view,
    our_projects, contact_view, contact_success_view
)

urlpatterns = [
    # Home & Basic Pages
    path('', home, name='home'),
    path('page1/', page1, name='page1'),
    path('message/', message, name='message'),

    # Team & About
    path('ourteam/', ourteam, name='ourteam'),
    path('ourteam/chairman/', chairman, name='chairman'),
    path('ourteam/details/', ourteam_detail, name='our_team_detail'),

    # Why Us
    path('why_us/', why_us, name='why_us'),

    # Services List & Individual
    path('services/', views.services, name='services'),
    path('services/room-service/', room_service, name='room_service'),
    path('services/reception/', reception, name='reception'),
    path('services/maintenance/', maintenance, name='maintenance'),
    path('services/food-beverage/', food_beverage, name='food_beverage'),
    path('services/seasonal-labor/', seasonal_labor, name='seasonal_labor'),

    # Strategy & Projects
    path('what-are-we-doing/', what_are_we_doing, name='what-are-we-doing'),
    path('vision-mission/', vision_mission_view, name='vision_mission'),
    path('our-aims/', our_aims_view, name='our_aims'),
    path('our-projects/', our_projects, name='our_projects'),
    path('project_case_study/', views.project_case_study, name='project_case_study'),

    # Contact
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),

    
    path('why-us/', views.why_us, name='why_us'),
    path('why-us/trained-labor/', views.trained_labor, name='trained_labor'),
    path('why-us/flexible-solutions/', views.flexible_solutions, name='flexible_solutions'),
    path('why-us/high-quality-service/', views.high_quality_service, name='high_quality_service'),
    path('why-us/continuous-training/', views.continuous_training, name='continuous_training'),
    path('why-us/extensive-experience/', views.extensive_experience, name='extensive_experience'),
    path('apply/', views.apply, name='apply'),
    path('apply/form/', views.apply_form, name='apply_form'),

]
    