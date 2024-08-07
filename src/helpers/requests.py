from requests import Session
from typing import Dict, List, Union

def set_session_cookies(session: Session, cookies: List) -> None:
    for cookie in cookies:
        if 'httpOnly' in cookie:
            cookie['rest'] = {'httpOnly': cookie.pop('httpOnly')}
        if 'expiry' in cookie:
            cookie['expires'] = cookie.pop('expiry')
        if 'sameSite' in cookie:
            cookie.pop('sameSite')
            
        session.cookies.set(**cookie)

def get_session_cookies(session: Session, filters: List = [], is_list: bool = False) -> Union[List, Dict]:
    cookies = []
    if session:
        for cookie in session.cookies:
            if filters and cookie.name not in filters:
                continue
            cookie_dict = {'name': cookie.name, 'value': cookie.value}
            if cookie.domain:
                cookie_dict['domain'] = cookie.domain
            cookies.append(cookie_dict)
    
    if is_list:
        cookies = {a['name']: a['value'] for a in cookies}
            
    return cookies
