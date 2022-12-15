from django.urls import reverse

def test_url_patterns_exist():
    url_tutorial_detail = reverse('tutorial_detail', args=[2])
    url_tutorial =  reverse('tutorial_list')
    url_tutorial_published = reverse('tutorial_list_published')
    assert url_tutorial_detail == '/api/tutorials/2'
    assert url_tutorial == '/api/tutorials'
    assert url_tutorial_published == '/api/tutorials/published'