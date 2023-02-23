import os
import sys
import django

# setup
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shinhanalpha.settings")
django.setup()

from apps.models import Apps
from mission.models import Mission
from reward.models import Reward

# from stock.models import Stock
# from bank.models import Bank
# from invite.models import Invite

apps = [
    {
        'a_name':'MMF',
        'a_description':'MMF'
    },
    {
        'a_name':'RP',
        'a_description':'RP'
    },
    {
        'a_name':'국공채/국공채펀드',
        'a_description':'국공채/국공채펀드'
    },
    {
        'a_name':'전단채',
        'a_description':'전단채'
    },
    {
        'a_name':'채권형 펀드',
        'a_description':'채권형 펀드'
    },
    {
        'a_name':'회사채',
        'a_description':'회사채'
    },
    {
        'a_name':'ELS/DLS',
        'a_description':'ELS/DLS'
    },
    {
        'a_name':'ETF',
        'a_description':'ETF'
    },
    {
        'a_name':'혼합형/주식형 펀드',
        'a_description':'혼합형/주식형 펀드'
    },
    {
        'a_name':'해외 펀드',
        'a_description':'해외 펀드'
    },
    {
        'a_name':'국내 주식',
        'a_description':'국내 주식'
    },
    {
        'a_name':'해외 주식',
        'a_description':'해외 주식'
    },
    {
        'a_name':'금',
        'a_description':'금'
    },
]
rewards = [
    {
        'reward_name':'주식 랜덤 1주',
        'tier_name':'브론즈3',
        'tier_point':'0'
    },
    {
        'reward_name':'신한마이포인트 150p',
        'tier_name':'브론즈2',
        'tier_point':'100'
    },
    {
        'reward_name':'신한마이포인트 300p',
        'tier_name':'브론즈1',
        'tier_point':'200'
    },
    {
        'reward_name':'신한마이포인트 1000p or 이디야 아메리카노',
        'tier_name':'실버3',
        'tier_point':'500'
    },
    {
        'reward_name':'신한마이포인트 400p',
        'tier_name':'실버2',
        'tier_point':'800'
    },
    {
        'reward_name':'신한마이포인트 400p',
        'tier_name':'실버1',
        'tier_point':'1100'
    },
    {
        'reward_name':'신한마이포인트 2000p or 스타벅스 아이스 아메리카노',
        'tier_name':'골드3',
        'tier_point':'1600'
    },
    {
        'reward_name':'신한마이포인트 500p',
        'tier_name':'골드2',
        'tier_point':'2100'
    },
    {
        'reward_name':'신한마이포인트 500p',
        'tier_name':'골드1',
        'tier_point':'2600'
    },
    {
        'reward_name':'신한마이포인트 4000p',
        'tier_name':'플래티넘3',
        'tier_point':'3800'
    },
    {
        'reward_name':'신한마이포인트 600p',
        'tier_name':'플래티넘2',
        'tier_point':'5000'
    },
    {
        'reward_name':'신한마이포인트 600p',
        'tier_name':'플래티넘1',
        'tier_point':'6200'
    },
    {
        'reward_name':'주식 랜덤 1주',
        'tier_name':'다이아',
        'tier_point':'11200'
    },
]
missions = [
    {
        'm_name':'로그인',
        'point':'1',
        'm_description':'1'
    },
    {
        'm_name':'7일 연속 로그인',
        'point':'3',
        'm_description':'주식의 기본은 꾸준함! 1주일 연속 신한알파에 로그인해보세요.'
    },
    {
        'm_name':'1개월 연속 로그인',
        'point':'30',
        'm_description':'30'
    },
    {
        'm_name':'추천 상품 이용',
        'point':'10',
        'm_description':'10'
    },
    {
        'm_name':'친구 추천 1회',
        'point':'50',
        'm_description':'50'
    },
    {
        'm_name':'친구 추천 3명',
        'point':'150',
        'm_description':'150'
    },
    {
        'm_name':'거래금액: 10만원',
        'point':'2',
        'm_description':'2'
    },
    {
        'm_name':'거래금액: 30만원',
        'point':'3',
        'm_description':'3'
    },
    {
        'm_name':'거래금액: 50만원',
        'point':'4',
        'm_description':'4'
    },
    {
        'm_name':'거래금액: 100만원',
        'point':'6',
        'm_description':'6'
    },
    {
        'm_name':'거래금액: 300만원',
        'point':'10',
        'm_description':'10'
    },
    {
        'm_name':'거래금액: 500만원',
        'point':'15',
        'm_description':'15'
    },
    {
        'm_name':'거래금액: 1000만원',
        'point':'22',
        'm_description':'22'
    },
    {
        'm_name':'거래금액: 1000만원 이상',
        'point':'30',
        'm_description':'30'
    },
]
for i in apps:
    Apps(name=i['a_name'], description=i['a_description']).save()
for i in rewards:
    Reward(reward_name=i['reward_name'], tier_name=i['tier_name'], tier_point=i['tier_point']).save()
for i in missions:
    Mission(name=i['m_name'], point=i['point'], description=i['m_description']).save()