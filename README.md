# AUDIO-SPEECH-TO-SIGN-LANGUAGE 

A 🌐 web application that takes in live audio speech recording as input, converts it into text, and displays the relevant Indian Sign Language (ISL) animations.

*Bridging Speech and Sign for Limitless Communication*

[![last commit](https://img.shields.io/github/last-commit/Tamilarasan-46/Audio-Speech-To-Sign-Language)]()

## 🛠️ Built With
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow)]() [![Python](https://img.shields.io/badge/Python-blue)]() [![Django](https://img.shields.io/badge/Django-green)]() [![NLTK](https://img.shields.io/badge/NLTK-lightgrey)]() [![Blender](https://img.shields.io/badge/Blender-orange)]() [![Cloudinary](https://img.shields.io/badge/Cloudinary-blue)]()

---

## Table of Contents
- [Overview](#overview)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)   
  - [Usage](#usage)  
  - [Testing](#testing)

---

## Overview

**Audio-Speech-To-Sign-Language** is an innovative developer tool that enables real-time conversion of spoken language into Indian Sign Language animations within a web application. It integrates speech recognition, media management, and dynamic UI components to foster accessible communication.

### Why Audio‑Speech‑To‑Sign‑Language?

This project aims to enhance accessibility and inclusivity by translating speech into sign language through a scalable, web‑based platform. The core features include:

- 🗂️ **Media Asset Management**: Centralized handling of sign language videos via Cloudinary, with bulk upload capabilities.  
- 🗣️ **Real‑Time Speech Recognition**: Converts spoken language into animated sign language for immediate visual communication.  
- 💻 **Dynamic Web Interface**: User‑friendly templates for sign‑up, media browsing, and interactive translation.  
- 🛠️ **Developer‑Friendly Tools**: Django management commands, static files handling, and custom template filters for seamless integration.  
- ⚙️ **Admin UI Enhancements**: JavaScript utilities improve responsiveness and usability for content management.

---

## Getting Started

### 🔧 Tech Stack:
- 🎨 **Front-end**: HTML, CSS, JavaScript  
- 🗣️ **Speech Recognition**: JavaScript Web Speech API  
- 🧠 **Text Preprocessing**: Natural Language Toolkit (NLTK)  
- 🕴️ **3D Animation**: Blender 3D Character Animation  

---

## ⚙️ Prerequisites

Ensure the following are available on your system:

- 🐍 **Python** >= 3.7  
- 🌐 **Browser** with Web Speech API support  
- 📦 All required Python packages listed in `A2SL/views.py`

---

## 🚀 Installation Guide

Build **Audio‑Speech‑To‑Sign‑Language** from the source and install dependencies:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tamilarasan-46/Audio-Speech-To-Sign-Language
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Audio-Speech-To-Sign-Language
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---
Follow these steps to get the project up and running locally:

1. 📁 Open your **Downloads** folder (or wherever you've saved the project).  
2. 🖥️ Launch the **terminal** from this folder.  
3. ▶️ Run the project with the command:  
   ```bash
   python manage.py runserver ####
   ```  
   *(Replace `####` with an optional port number, e.g., `8000`)*  
4. 🌐 Open your browser and go to the address shown in terminal (e.g., `http://127.0.0.1:8000/`)  
5. 🔐 Sign up and start exploring!  
6. 🎙️ Click the **mic** button to begin recording your speech.  
7. 💬 The speech is processed and relevant ISL animations are displayed. You can also manually enter text for conversion.

---
### Usage

Run the project with:

Using `pip`:
```bash
python (entrypoint)
```

---

### Testing

**Audio‑Speech‑To‑Sign‑Language** uses the `test_framework` test framework. Run the test suite with:

Using `pip`:
```bash
pytest
```

## 📣 Contributions Welcome!

If you’d like to contribute or improve this project, feel free to fork and submit a pull request.

---

