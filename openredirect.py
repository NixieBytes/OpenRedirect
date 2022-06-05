print("""   ____                      ____             ____  _                __
  / __ \____  ___  ____     / __ \___        / __ \(_)_______  _____/ /_____  _____
 / / / / __ \/ _ \/ __ \   / /_/ / _ \______/ / / / / ___/ _ \/ ___/ __/ __ \/ ___/
/ /_/ / /_/ /  __/ / / /  / _, _/  __/_____/ /_/ / / /  /  __/ /__/ /_/ /_/ / /
\____/ .___/\___/_/ /_/  /_/ |_|\___/     /_____/_/_/   \___/\___/\__/\____/_/
    /_/                                                                            """)

print("""             A simple Python Program to obfuscate URLs to make phishing urls more difficult to attack.
                        :*: Tool Designed By Nixie_Bytes Security Team :*:""")

url=''

open_redirect=[ 'https://www.google.com/url?q=',
                'https://google.com/accounts/Logout?continue=',
                'https://accounts.google.com/Logout?continue=',
                'https://map.google.com/search?btnI&q=',
                'https://mail.google.com/search?btnI&q=',
                'https://appengine.google.com/_ah/logout?continue=',
                'https://google.com/url?q='     ,
                'https://googleweblight.com/i?u=' ,
                'https://google.com/gwt/x?wsc=eb&u=',
                'https://via.hypothes.is/',
                'https://facebook.com/l.php?u=',
                'https://vk.com/away.php?to=',
                'https://duckduckgo.com/y.js?u3=' ,
                'https://duckduckgo.com/l/?kh=-1&uddg=',
                'https://3g2upl4pq6kufc4m.onion/y.js?u3=',
                'https://3g2upl4pq6kufc4m.onion/l/?kh=-1&uddg=',
                'https://ahmia.fi/search/search/redirect?search_term=cat&redirect_url=' ,
                'http://msydqstlz2kzerdg.onion/search/search/redirect?search_term=cat&redirect_url=',
                'http://l.wl.co/l?u=',

                ]


def get_url():
  print('\n Enter url: ',end='')
  global url
  tmp=input()
  if tmp.startswith('http://') or tmp.startswith('https://'):
     url=tmp
  else:
     url='http://'+tmp

get_url()

def file_w():
  with open('Result_Open Re-direct.txt','w') as f:
     for i in open_redirect:
        f.write(i+url+'\n')

file_w()


def http_basic_auth():
    custom_url=[  'https://myaccount.google.com@',
                 'http://google_competitions_for_college_students@',
                 'http://facebook_led_ai_research_for_indian_college_students@',
                 'http://learn_microsoft_free_certifications@',
                ]
    with open('Result_Open Re-direct.txt','a+')as f:
        for i in custom_url:
            if url.startswith('https://'):
               f.write(i+url.strip('https://')+'\n')
            elif url.startswith('http://'):
               f.write(i+url.strip('http://')+'\n')

http_basic_auth()
x=input('Press enter to Stop & Check Result_Open Re-direct.txt')
