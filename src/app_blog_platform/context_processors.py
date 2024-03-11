from .models import Tags_Level_1, Tags_Level_2, Tags_Level_3, Global_Settings, Page

def tags_context(request):
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()
    global_settings = Global_Settings.objects.first()
    pages = Page.objects.all()
    pages_lv1 = Page.objects.filter(page_tag_level_1__isnull=True)
    pages_lv2 = Page.objects.filter(page_tag_level_1__isnull=False, page_tag_level_2__isnull=True)
    pages_lv3 = Page.objects.filter(page_tag_level_1__isnull=False, page_tag_level_2__isnull=False, page_tag_level_3__isnull=True)
    return {
        'tags_level_1': tags_level_1,
        'tags_level_2': tags_level_2,
        'tags_level_3': tags_level_3,
        'global_settings':global_settings,
        'pages':pages,
        'pages_lv1':pages_lv1,
        'pages_lv2':pages_lv2,
        'pages_lv3':pages_lv3,
    }
