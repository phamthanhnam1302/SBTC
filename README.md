## SBTC - Photo Social Network
### Decription
Mini-social network for blogging: posts, comments, likes, follow
### Technologies used:
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![image](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
### Available Features
- Pages: main page, author profile with posts
- Create, edit posts with images attached and delete posts
- Ability to generate images automatically with keywords (GAN)
- Create comments on posts
- Possibility to follow the author (subscription feed with transition to the main page)
- Custom admin panel
- Working with users: new registration, login/logout, password change and password recovery (emulator)
- Pages: group and author navigation with top authors by posts and comments
- Personal account with fields: avatar (custom), additional information about the author
- The system likes posts like
- Reflect information about likes and comments in a post's feed
- Search articles by keyword
- Display articles as a tag system

### Installation
**How to start the project:**
```
>>> Clone the repository and change into it on the command line:
git clone https://github.com/phamthanhnam1302/SBTC
cd sbtc
```
```
>>> Create and activate virtual environment:
py -m venv venv (for Windows) /python3 -m venv venv (for MacOS)
source venv/bin/activate (for Windows) / source venv/bin/activate (for MacOS)
```
```
>>> Install dependencies from requirements.txt:
cd ../
python -m pip install --upgrade pip (MacOS python3 -m pip install --upgrade pip for MacOS)
pip install -r requirements.txt (python3 pip install -r requirements.txt for MacOS)
```
```
>>> Run migrations:
cd sbtc
python manage.py migrate (if you are a MacOS user python3 manage.py migrate)
```
```
>>> Run project:
python manage.py runserver (if you are a MacOS user python3 manage.py runserver)
```
