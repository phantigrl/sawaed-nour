from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from django.core.files.storage import FileSystemStorage
from .models import Application




# ---------- Static Page Views ----------

def home(request):
    return render(request, 'pages/home.html')

def page1(request):
    return render(request, 'pages/page1.html')

def ourteam(request):
    return render(request, 'pages/ourteam.html')

def ourteam_detail(request):
    return render(request, 'pages/our_team_detail.html')

def chairman(request):
    return render(request, 'pages/chairman.html')

def what_we_do(request):
    return render(request, 'pages/what_we_do.html')

def vision(request):
    return render(request, 'pages/vision.html')

def message(request):
    return render(request, 'pages/message.html')

def projects(request):
    return render(request, 'pages/projects.html')

def case_study(request):
    return render(request, 'pages/case_study.html')

def strategy(request):
    return render(request, 'pages/strategy.html')

def thanks(request):
    return render(request, 'pages/thanks.html')

def what_are_we_doing(request):
    return render(request, 'pages/what_are_we_doing.html')

def our_aims_view(request):
    return render(request, 'pages/our_aims.html')

def vision_mission_view(request):
    return render(request, 'pages/vision_mission.html')

def our_projects(request):
    return render(request, 'pages/our_projects.html')


# ---------- Services View ----------

def services(request):
    services = [
        {
            'title_ar': 'خدمة الغرف',
            'title_en': 'Room Service',
            'description_ar': 'موظفي تنظيف وترتيب الغرف وتوفير بيئة مريحة للنزلاء',
            'description_en': 'Trained staff to clean and organize rooms, ensuring guest comfort and satisfaction.',
            'url_name': 'room_service'
        },
        {
            'title_ar': 'استقبال',
            'title_en': 'Reception & Bellboy',
            'description_ar': 'موظفي حامل حقائب على أعلى مستوى من التدريب لتقديم خدمة متميزة للضيوف',
            'description_en': 'Highly trained receptionists and bellboys to ensure a warm welcome and seamless check-in experience.',
            'url_name': 'reception'
        },
        {
            'title_ar': 'صيانة',
            'title_en': 'Maintenance',
            'description_ar': 'فنيين متخصصين في صيانة الأجهزة والمرافق لضمان سير العمل بسلاسة',
            'description_en': 'Specialized technicians for equipment and facility maintenance, ensuring smooth operation.',
            'url_name': 'maintenance'
        },
        {
            'title_ar': 'خدمات الطعام والشراب',
            'title_en': 'Food & Beverage',
            'description_ar': 'طاقم طهاة، نُدُل، ومتخصصي الطعام يوفرون تجربة طعام استثنائية',
            'description_en': 'Chefs, waiters, and catering experts offering high-quality dining experiences for guests.',
            'url_name': 'food_beverage'
        },
        {
            'title_ar': 'عمالة موسمية',
            'title_en': 'Seasonal Labor',
            'description_ar': 'نوفر عمالة موسمية مدربة لتغطية فترات الذروة وتقديم خدمات عالية الجودة',
            'description_en': 'Trained seasonal workers to cover peak periods in hotels, restaurants, and resorts.',
            'url_name': 'seasonal_labor'
        },
    ]
    return render(request, 'pages/our_services.html', {'services': services})


# ---------- Why Us Section ----------






# ---------- Individual Service Pages ----------

def room_service(request):
    return render(request, 'pages/room_service.html')

def reception(request):
    return render(request, 'pages/reception.html')

def maintenance(request):
    return render(request, 'pages/maintenance.html')

def food_beverage(request):
    return render(request, 'pages/food-beverage.html')

def seasonal_labor(request):
    return render(request, 'pages/seasonal-labor.html')


# ---------- Contact Form Views ----------

def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Save to DB only
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            company=company,
            service=service,
            message=message
        )

        return redirect('contact_success')

    return render(request, 'pages/contact.html')

def contact_success_view(request):
    return render(request, 'pages/contact_success.html')
def project_case_study(request):
    return render(request, 'pages/project_case_study.html')



def why_us(request):
    features = [
    {
        "title": "Trained and Qualified Labor",
        "title_ar": "عمالة مدربة ومؤهلة",
        "desc": "We ensure that all the labor we provide is highly skilled and experienced in hospitality. Our team undergoes rigorous training programs tailored to each service domain, from housekeeping to food service, guaranteeing professionalism and excellence on-site.",
        "desc_ar": "نحن نضمن أن جميع العمالة التي نوفرها تتمتع بكفاءة عالية وخبرة كبيرة في مجال الخدمات الفندقية. يخضع فريقنا لبرامج تدريب صارمة ومخصصة لكل مجال خدمة، من تنظيف الغرف إلى تقديم الطعام، لضمان الاحترافية والتميز في الموقع."
    },
    {
        "title": "Flexible Solutions",
        "title_ar": "حلول مرنة",
        "desc": "Our staffing solutions are customized to meet the unique and changing demands of your business. Whether you require seasonal staff, temporary replacements, or long-term partners, we adapt our workforce quickly and efficiently.",
        "desc_ar": "نقدم حلول توظيف مرنة ومخصصة لتلبية الاحتياجات الفريدة والمتغيرة لأعمالكم. سواء كنتم بحاجة إلى عمالة موسمية أو بدلاء مؤقتين أو شركاء طويلين الأمد، نحن نكيف فريق العمل بسرعة وكفاءة."
    },
    {
        "title": "Ongoing Training",
        "title_ar": "تدريب مستمر",
        "desc": "We invest continuously in upgrading the skills of our workforce with the latest industry practices, health and safety protocols, and customer service excellence, ensuring your guests receive top-tier experiences.",
        "desc_ar": "نستثمر باستمرار في تطوير مهارات موظفينا من خلال أحدث ممارسات الصناعة وبروتوكولات الصحة والسلامة وامتياز خدمة العملاء، لضمان حصول ضيوفكم على أفضل تجربة."
    },
    {
        "title": "High-Quality Service",
        "title_ar": "خدمة عالية الجودة",
        "desc": "Our strict quality control mechanisms and feedback-driven approach guarantee consistent superior service delivery. We monitor performance and promptly address any issues to maintain your brand's reputation.",
        "desc_ar": "آلياتنا الصارمة لمراقبة الجودة ونهجنا المعتمد على التغذية الراجعة يضمنان تقديم خدمة عالية المستوى بشكل مستمر. نراقب الأداء ونتعامل بسرعة مع أي مشكلات للحفاظ على سمعة علامتكم التجارية."
    }
]



    gallery_images = [
        "hat.png", "bus.png", "card.png", "car.png",
        "shirt.png", "sign.png", "brochure.png", "poster.png",
        "letter.png", "hos.png", "boo.png", "ca.png"
    ]

    return render(request, 'pages/why_us.html', {
        'features': features,
        'gallery_images': gallery_images
    })


def trained_labor(request):
    return render(request, 'pages/trained_labor.html')

def flexible_solutions(request):
    return render(request, 'pages/flexible_solutions.html')

def high_quality_service(request):
    return render(request, 'pages/high_quality_service.html')

def continuous_training(request):
    return render(request, 'pages/continuous_training.html')

def extensive_experience(request):
    return render(request, 'pages/extensive_experience.html')
def apply(request):
    return render(request, 'pages/apply.html')

def apply_form(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('cv'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        cv = request.FILES['cv']

        # Save to database
        Application.objects.create(full_name=name, email=email, cv=cv)

        context['success'] = True

    return render(request, 'pages/apply_form.html', context)