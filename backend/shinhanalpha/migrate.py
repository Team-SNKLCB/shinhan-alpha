import os
import sys
import django

# setup
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shinhanalpha.settings")
django.setup()

# django 사용 가능
# import random
# from member.models. import Stock

# for i in range(1000):
#     price = random.randint(10000,30000)
