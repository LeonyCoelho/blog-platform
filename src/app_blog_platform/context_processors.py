from .models import Tags_Level_1, Tags_Level_2, Tags_Level_3, Global_Settings

def tags_context(request):
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()
    global_settings = Global_Settings.objects.first()

    return {
        'tags_level_1': tags_level_1,
        'tags_level_2': tags_level_2,
        'tags_level_3': tags_level_3,
        'global_settings':global_settings,
    }
