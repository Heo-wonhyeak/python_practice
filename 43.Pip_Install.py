# 파이썬에서 개발된것 외에 여러 패키지들을 가져다가 개발하는데 도움을 받을 수 있음

# pip install beautifulsoup4 << 터미널에 입력했음

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list : 입력시 다운되어있는 pip를 확인할 수 있음 
# pip install --upgrade beautifulsoup4 : 해당 pip 버전 업그레이드
# pip uninstall beautifulsoup4 : 해당 pip 삭제 