/home/zhutao/anaconda3/bin/python manage.py startapp polls
/home/zhutao/anaconda3/bin/python manage.py makemigrations polls
/home/zhutao/anaconda3/bin/python manage.py migrate
/home/zhutao/anaconda3/bin/python manage.py createsuperuser
python -c "
import sys
sys.path = sys.path[1:]
import django
print(django.__path__)"
/home/zhutao/anaconda3/bin/python manage.py startapp MachineLearningService
