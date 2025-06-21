from datetime import datetime

import requests


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'cookie': 'enter_pc_once=1; UIFID_TEMP=28ea90c1b0cf804752225259882c701fb12323f08ef828fc1032b615e29efbbe716e945368b22973083114023fdce522fd957c9202bdf1660f80e9cfdbc8e1e972767ec68d096ae057cfa688e5a1c76c; s_v_web_id=verify_mbq8eg6o_yij3nGYA_GiOF_4tdv_AnBU_vniqC8wDiI1o; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; xgplayer_user_id=65493657302; passport_csrf_token=c0b1ab3ff2a86fe61328fd3c9e7a2e24; passport_csrf_token_default=c0b1ab3ff2a86fe61328fd3c9e7a2e24; fpk1=U2FsdGVkX19cVoVnkEaSA396xm2a1k8PFb/1wQjm06f5j3Ti/jegPVhHidzfkMkaCnuusAyLRu9d4OuRvLYElg==; fpk2=0e0369e2813db7deb26e5937c353aab4; __security_mc_1_s_sdk_crypt_sdk=7b131b9e-4fe9-a48b; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; UIFID=28ea90c1b0cf804752225259882c701fb12323f08ef828fc1032b615e29efbbe767aa32157a3bf2ec8ee42f937af2f79766c14ed4ba9b57715cd5e22bf5a80e704d6da37f3369ee1f53826ed4cc45d32c4c3c314e56dd79b0c2fd17ed8b96ddfe628c20b4e44bae7f5dc28ecaaba7dcb4de4ffe3966395c7d8a76c5461d1cb6d063dbfc39f751bfbe0e849ec14ce31594b79ef1818c3e7d7621323e72903feba; is_dash_user=1; xgplayer_device_id=39091573140; passport_mfa_token=CjXtZ0aBvjN2yJMOADNACPGsfVC68NAF3AGuvQ6fHRFXrrEBHYhMxDR09n0PlBQCZf0wCFCcnhpKCjwAAAAAAAAAAAAATx%2F%2FBmuAViC8VvX2qigviYVQUtT5lMBS62SBYZvk8DaCFI%2F9hN2nBO2izT3ueVlcrzQQ1p70DRj2sdFsIAIiAQOzWaSy; d_ticket=7a405d1392f69b629b4003fabc49e5d75ff32; passport_assist_user=Ckvq13C3QIubAM593Gy-d7T5Pz4gbh3MGAsZ_A6I90rAGpAlrecPA2-ETIwgRUnRnhTxDLZI2FBx_sKnKGpRuPFGlGvk_KCmMcvldhEaSgo8AAAAAAAAAAAAAE8fg6pX6n-PtaripGEQ-g35ggiPwF2W36Lj_JaF4eLHd-Heh6RejjGmhqT9Oy3N3AjwENKf9A0Yia_WVCABIgEDFNSbYg%3D%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=b2ed37c8b013bbd8be908996dc33d9db%7C1750063764%7C5184000%7CFri%2C+15-Aug-2025+08%3A49%3A24+GMT; uid_tt=151d2fb6c233faee40e3e7927fac0a1c; uid_tt_ss=151d2fb6c233faee40e3e7927fac0a1c; sid_tt=b2ed37c8b013bbd8be908996dc33d9db; sessionid=b2ed37c8b013bbd8be908996dc33d9db; sessionid_ss=b2ed37c8b013bbd8be908996dc33d9db; is_staff_user=false; sid_ucp_v1=1.0.0-KDUwYTQ3N2ZlZmVlNTJiZTEyNmUzZGQwY2YyNjMyYTc0NzUyODAxZTcKIQiroaCdv83SAxCUtb_CBhjvMSAMMOz0_K0GOAdA9AdIBBoCbGYiIGIyZWQzN2M4YjAxM2JiZDhiZTkwODk5NmRjMzNkOWRi; ssid_ucp_v1=1.0.0-KDUwYTQ3N2ZlZmVlNTJiZTEyNmUzZGQwY2YyNjMyYTc0NzUyODAxZTcKIQiroaCdv83SAxCUtb_CBhjvMSAMMOz0_K0GOAdA9AdIBBoCbGYiIGIyZWQzN2M4YjAxM2JiZDhiZTkwODk5NmRjMzNkOWRi; login_time=1750063764181; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_cookie=794460738fe9517075cfb50bb097aca8; __security_mc_1_s_sdk_sign_data_key_web_protect=e34423bc-4208-9cec; __security_mc_1_s_sdk_cert_key=a64eeac0-45d8-ac67; __security_server_data_status=1; my_rd=2; publish_badge_show_info=%220%2C0%2C0%2C1750063771862%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; strategyABtestKey=%221750122156.208%22; ttwid=1%7CLXuUISFufZqocuAMFwRbeaa5E72KHSW0hmdB7IORtNk%7C1750122156%7C241af550255e15743a24b5d3316c4c4e1e74083afe904f77c96e925d48ea5512; douyin.com; xg_device_score=7.802204888412783; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; passport_fe_beating_status=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; WallpaperGuide=%7B%22showTime%22%3A1750064776167%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A58%2C%22cursor2%22%3A18%2C%22hoverTime%22%3A1750065250509%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; csrf_session_id=aa802e6314fc58b880b81aa980d89b1b; download_guide=%223%2F20250617%2F0%22; __ac_nonce=068520f8f00bfa79041d7; __ac_signature=_02B4Z6wo00f018QEMEwAAIDBJ8vA22BPGrvEJDTAAJlcdc; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTEFDaTliWDRoRnN2RnlBeVQ5YmF0cDZaWTg0UGRHMm5zTjdBY1lkT2dGSmthQ0NvRCtEYThkSTE4R1A4SDlsbmMvbWd0dHFBZ1BDRWluSE5CSHdFQkU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; odin_tt=aae6dd4f5f16e3c321a240353d0224e9335fb5c25c0948b6dde65cb89484438b2502f03369919a8cb4615f42751d125a56a9cd555dcd2f900a7f0f5aafb628de; IsDouyinActive=true',
}

params = {
    'aid': '6383',
    'aweme_id': '7498720869088513337',
    'cursor': '0',
    'count': '10',

 }

def timestamp_to_str(timestamp):
    # 如果时间戳是13位，认为是毫秒，转换为秒
    if len(str(timestamp)) >= 13:
        timestamp = int(timestamp) / 1000
    else:
        timestamp = int(timestamp)

    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_douyin_comment(comment_json,comment_data = None):
    if comment_data is None:
        comment_data = {}
    comment_data['cid'] = comment_json.get('cid')
    comment_data['create_time'] = timestamp_to_str(comment_json.get('create_time'))
    # comment_data['user_id'] = comment_json.get('user').get('unique_id') if comment_json.get('user').get('unique_id') else comment_json.get('user').get('short_id')
    # comment_data['sec_id'] = comment_json.get('user').get('sec_uid')
    # comment_data['user_name'] = comment_json.get('user').get('nickname')
    # comment_data['digg_count'] = comment_json.get('digg_count')
    # comment_data['is_hot'] = comment_json.get('is_hot')
    # comment_data['reply_comment_total'] = comment_json.get('reply_comment_total')
    # comment_data['is_author_digged'] = comment_json.get('is_author_digged')
    comment_data['ip_label'] = comment_json.get('ip_label')
    comment_data['text'] = comment_json['text']
    return comment_data

# 请求a_bogus的参数 type为可选参数 默认为detail 获取二级评论使用reply
params_jieqs = {'user_agent': headers['user-agent'],
                'url_search_params': '&'.join([f"{k}={v}" for k, v in params.items()])}
# 获取 a_bogus
absq = requests.get('https://api.dinging.top/api/abgous', params=params_jieqs, headers=headers)

params['a_bogus'] = absq.json().get('result').get('signature')
# print(params['a_bogus'])
response = requests.get('https://www.douyin.com/aweme/v1/web/comment/list/', params=params, headers=headers)
i = 1
for item in response.json().get('comments', []):

    print(f'{i}:{(parse_douyin_comment(item))}')
    i += 1

