from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By

y = input('년:')
m = input('월:').rjust(2, '0')
# s = input('과목(국어: ko, 영어: eng, 수학: math, 과학: sci):')
s= 'math'
#원 숫자 변환 딕셔너리
roundToN = {'①':1,'②':2,'③':3,'④':4,'⑤':5}



#크롬 실행
driver = webdriver.Chrome('chromedriver.exe')

#3초 대기
driver.implicitly_wait(3)

driver.maximize_window()


#EBSi 로그인 페이지 접속
driver.get('http://www.ebsi.co.kr/ebs/pot/potl/login.ebs?destination=/index.jsp&alertYn=N')


#아이디, 비밀번호 입력
driver.find_element(By.NAME,'i').send_keys('jingyu4654')
driver.find_element(By.NAME,'c').send_keys('z8585858')

#로그인 버튼 클릭
driver.find_element(By.CLASS_NAME,'login_wrap').find_element(By.ID,'btnLogin').click()

#기출문제 페이지 접속
driver.get('http://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs')

#Select 박스에서 연도 선택
select = Select(driver.find_element(By.ID,'beginYear'))
select.select_by_value(y)

#체크 박스에서 월 선택
driver.find_element(By.NAME,'monthAll').click()
driver.find_element(By.ID,'month'+m).click()

#ko, math, eng, koh, sci
driver.find_element(By.ID,'subj2').click()

#검색 버튼 클릭
searchBtn = driver.find_element(By.CLASS_NAME, 'btn_L_col7')
driver.execute_script("arguments[0].click();", searchBtn)


sub = ''
if m == 11:
    if s == 'sci':
        sub = input('과목(물리1:1, 물리2:2, 화학1:3, 화학2:4, 생명1:5, 생명2:6, 지구1:7, 지구2:8:')
    elif s == 'ko' or s == 'eng':
        input('(홀수:1, 짝수:2):')
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2, 가형(짝):3, 나형(짝):4):')
elif m == 3:
    if s == 'sci':
        sub = input('과목(물리1:1, 화학1:2, 생명1:3, 지구1:4):')
    elif s == 'ko' or s == 'eng':
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2):')
else: 
    if s == 'sci':
        sub = input('과목(물리1:1, 물리2:2, 화학1:3, 화학2:4, 생명1:5, 생명2:6, 지구1:7, 지구2:8:')
    elif s == 'ko' or s == 'eng':
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2):')
sub = int(sub)
scr = driver.find_elements_by_tag_name('tr')[sub].find_element(By.CLASS_NAME,'btn_apply').get_attribute('href')
driver.execute_script(scr)
sleep(1)
driver.switch_to.window(driver.window_handles[-1]) #창 전환
driver.find_element(By.ID,'mode2').click()
study = driver.find_element(By.CLASS_NAME,'study-mode')
result = []
num = input('번호:')
result = roundToN[study.find_element(By.ID,'boardcorrect_'+num).find_element(By.CLASS_NAME,'red').get_attribute("textContent")]

if s != 'math':
        txt = []
        for text in study.find_element(By.ID,'Explanation_'+num).find_elements(By.CSS_SELECTOR,'span'):
            txt.append(text.get_attribute("textContent"))
        print(str(txt))
print(result)