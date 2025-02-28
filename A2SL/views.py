from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import json

# Home Page
def home_view(request):
    return render(request, 'home.html')

# About Page
def about_view(request):
    return render(request, 'about.html')

# Contact Page
def contact_view(request):
    return render(request, 'contact.html')

# Media Gallery (Handles Missing Files Gracefully)
def media_gallery(request):
    try:
        with open("cloudinary_urls.json", "r") as file:
            media_files = json.load(file)
    except FileNotFoundError:
        media_files = {}  # Prevent crash if file is missing

    return render(request, "media_gallery.html", {"media_files": media_files})

# Animation Page (Loads Cloudinary URLs for Words)
@login_required(login_url="login")

def animation_view(request):
    # Load Cloudinary URLs
    with open("cloudinary_urls.json", "r") as file:
        cloudinary_videos = json.load(file)

    text = request.POST.get("sen", "").strip()  # Get user input
    words = text.split()  # Split words by space

    processed_words = []  # Stores final words/letters
    video_urls = {}  # Stores corresponding video URLs

    for word in words:
        capitalized_word = word.capitalize()  # Ensure first letter is uppercase
        key = f"{capitalized_word}.mp4"  # Example: "Hai.mp4"

        if key in cloudinary_videos:
            processed_words.append(word)  # ✅ Use full word if available
            video_urls[word] = cloudinary_videos[key]
        else:
            # 🔥 If the word is missing, split into letters
            for letter in word:
                letter_key = f"{letter.upper()}.mp4"  # Example: "H.mp4"
                if letter_key in cloudinary_videos:
                    processed_words.append(letter)  # ✅ Store each letter separately
                    video_urls[letter] = cloudinary_videos[letter_key]

    print("DEBUG: processed_words =", processed_words)
    print("DEBUG: video_urls =", video_urls)  # 🔍 Check output

    return render(request, "animation.html", {"words": processed_words, "video_urls": video_urls})

# User Signup (Redirects to Home Page)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User Login (Redirects to Previous Page or Home)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.POST.get('next', 'home'))  # Default to home if 'next' is missing
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout (Redirects to Home)
def logout_view(request):
    logout(request)
    return redirect("home")
