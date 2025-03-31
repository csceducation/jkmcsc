def global_context(request):
    return {
        "company": "JayamKondam",
        "user_ip": request.META.get("REMOTE_ADDR", "Unknown"),
    }
    
company = "JayamKondam"
site_pass = "621205"
site_user = "jkmcsc"