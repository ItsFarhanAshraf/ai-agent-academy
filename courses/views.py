from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .butter import get_home_page, list_courses, get_course_by_slug

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    data = get_home_page() or {}
    try:
        hero_title = data.get('fields', {}).get('hero_title', 'AI Agent Academy')
        overview = data.get('fields', {}).get('overview_text', '')
        hero_image = data.get('fields', {}).get('hero_image', {}).get('url', '')
    except Exception:
        hero_title, overview, hero_image = 'AI Agent Academy', '', ''
    return render(request, 'home.html', {'hero_title': hero_title, 'overview': overview, 'hero_image': hero_image})

@login_required
def courses_list(request):
    courses = list_courses()
    simplified = []

    for c in courses:
        fields = c.get('fields', {})

        thumbnail_field = fields.get('thumbnail')
        if isinstance(thumbnail_field, dict):
            thumbnail_url = thumbnail_field.get('url', '')
        else:
            thumbnail_url = thumbnail_field or ''

        simplified.append({
            'title': fields.get('title', 'No title'),
            'slug': c.get('slug') or fields.get('slug'),
            'description': fields.get('description', ''),
            'video_url': fields.get('video_url', ''),
            'thumbnail': thumbnail_url,
        })

    return render(request, 'courses_list.html', {'courses': simplified})


@login_required
def course_detail(request, slug):
    course = get_course_by_slug(slug)
    if not course:
        return render(request, 'course_not_found.html', status=404)

    fields = course.get('fields', {})

    # Handle thumbnail (string or dict)
    thumbnail_field = fields.get('thumbnail')
    thumbnail_url = thumbnail_field.get('url', '') if isinstance(thumbnail_field, dict) else thumbnail_field or ''

    # Handle video URL
    video_url = fields.get('video_url', '')
    if "watch?v=" in video_url:
        video_url = video_url.replace("watch?v=", "embed/")

    context = {
        'title': fields.get('title', ''),
        'description': fields.get('description', ''),
        'video_url': video_url,
        'thumbnail': thumbnail_url,
        'slug': slug,
    }

    return render(request, 'course_detail.html', context)



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
