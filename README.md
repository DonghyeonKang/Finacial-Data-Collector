# **Finacial-Data-Collector**
## **들어가기**
프로젝트의 시작은 친구의 부탁이었다. 회사마다 자신이 원하는 데이터를 비교하고 싶은데, 자신이 현재 보는 Company Guide라는 사이트에서는 회사를 하나하나 검색해야 한다고 한다. 그렇다 귀찮은 것이다. 이럴 때 개발이 필요하다. 언젠가 대학생 때는 봉사를 많이 하라는 말을 들은 적이 있다. 보수가 없더라도 만들어서 제공하고, 피드백을 받으며 프로젝트를 진행해보라는 의미인 것 같다. 그것과 더불어 나의 첫 프로젝트라는 것이 의미가 크다. 참고로 아래 프로그램은 크롤러가 아니다. 특정 웹사이트의 데이터만을 필요로 하며, 단 몇 페이지에 있는 데이터만을 수집하는 프로그램이다.   

----  
## **사용법**
* 2개의 버튼이 있다. 왼쪽 버튼은 회사 리스트를 웹에서 받아오는 버튼이고, 오른쪽 버튼은 자신이 선택한 회사의 데이터를 웹에서 받아오는 버튼이다. 
* 데이터를 보고자 하는 회사를 선택하기 위해 왼쪽 리스트에서 원하는 회사를 더블클릭하면, 오른쪽 테이블에 회사명이 추가되고, 반대로 테이블에서 회사를 더블클릭하면, 선택이 취소되어 테이블에서 지워진다. 
* 버튼을 누르면, 데이터를 받아오기 위해 로딩 시간이 요구되고, 이때 프로그램이 (응답없음) 표시를 하지만, 데이터를 수집하는 중이니 기다리면 된다. 차후에 로딩바를 추가할 계획이다. 
* 너무 많은 회사를 선택하여 불러오기를 하면, 데이터를 불러오는 Company Guide 서버에 지장을 줄 수 있으므로, 다음 업데이트에 이를 제한할 것이다. 
* 검색 기능은 회사 목록이 업데이트 된 후에 사용이 가능하다. 기업명은 company guide에 올라온 회사명을 기준으로 찾을 수 있다. 아무것도 입력하지 않은 채 검색 버튼은 누르면 전체 목록이 나온다. 
* 엑셀에 출력하는 기능은 데이터가 모두 로딩이 된 후에 작동한다. 파일에 엑셀 파일이 없다면 새로 출력하고, 있다면 새로 쓴다. 
----
## **업데이트**
#### **FDC_ver.1.0**
    정말 필요한 기능만을 구성하여 만들어보았다. 
    데모버전. 상장 회사 목록 수집기능, 특정 데이터 수집 기능

    1.0 버전 피드백
    1. 회사 목록이 2411개 중 500개만 로딩이 된다. 
    2. 엑셀에 복사하려 했지만, 테이블의 데이터를 복사할 수 없다. 
    3. 회사 목록이 너무 많아 찾기가 힘들다. 
#### **FDC_ver.2.0**    
    기능 추가(엑셀 출력 기능, 검색 기능), 버그 수정(회사 목록 500개만 로딩이되는 버그), 설정 추가(데이터 불러오기 회사 개수 제한. 25개), 아이콘 추가, 대화상자명 추가

    2.0 버전 피드백 
    1. EPS 추가
#### **FDC_ver.3.0**
    EPS 추가
----
## **프로젝트 개요**  
[Company Guide](https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701)에서 제공하는 데이터를 수집하여 엑셀로 제공한다. 

--------
## **설계**  

### **기능 요구사항**  
1. 재무 데이터를 수집 기능
2. 데이터를 제공 기능  

### **필요한 데이터**  
1. 주가
2. 시가총액
3. per
4. bps
5. 장기부채
6. 단기차입금  
### **데이터 수집 위치** 
* [Company Guide](https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701), [robots.txt](https://comp.fnguide.com/robots.txt)  
### **웹 스크랩핑 프레임워크**  
* selenium

### **GUI 툴킷**  
* PyQt

### **클래스**
* **FDC**  
~~1. 재무 데이터 업데이트~~  
~~2. 회사 목록 업데이트~~  
~~3. 출력할 회사명~~  
~~4. 엑셀 틀 구성~~  
~~5. 엑셀로 데이터 출력~~  
1. 회사 목록 가져오기 
2. 데이터 업데이트 하기
3. 데이터 가져오기 

* **My app**  
1. UI
2. 업데이트 리스트
3. 검색 리스트
4. 업데이트 테이블
5. 테이블에 추가
6. 테이블에서 제거
7. 검색하기
8. 엑셀에 출력하기

이었으나, 중간에 구조를 바꾸었다. 굳이 엑셀로 데이터를 출력하지 않아도 되며, 모든 회사의 데이터를 가져올 필요가 없었다. 보고 싶은 회사만 조금씩 데이터를 수집하여 출력하면, Company Guide 서버에 지장을 줄일 수 있을 것이다. 
* **FDC**  
1. 재무 데이터 업데이트
2. 회사 목록 업데이트


### **테스트**  
* 프로그램을 만들기 전에 확인해야 하는 점이 있다.  
  1. 검색 시 생기는 경고창 처리는 어떻게 해야 하는가?  
      * 검색을 하지 않는다. 
  2. 특정 요소 찾기는 어떻게 해야 하는가?  
      * xpath를 이용한다. 
  3. 회사가 달라도 동일한 코드로 원하는 데이터를 얻을 수 있는가?  

--------
## **프로젝트 진행**  
### **궁금한 것**  

* selenium 말고 더 적합한 툴이 있는가? 
    ```
    requests 와 Beautiful Soup?
    ```

* 마크 다운 문법에 개행은 뭐지? 
    ```
    문장 끝에 공백을 두 개 넣는다. 
    엔터를 두 번 누른다. 
    ```

* 웹 페이지에서 특정 클래스의 값을 어떻게 가져올까?  
    ```
    selenium에서는 xpath를 이용해서 특정 값에 쉽게 접근할 수 있다. 
    ```
* xpath는 어떻게 쓰지? 
    ```
    https://testmanager.tistory.com/121
    xpath 문법
    ```
* html은 쌍따옴표와 따옴표 구분이 있을까? 
* selenium 과 beautifulsoup의 차이가 뭘까? 
    ```
    https://namu.wiki/w/%ED%81%AC%EB%A1%A4%EB%A7%81
    selenium은 javascript로 쓰여진 동적 웹페이지 탐색에 쓰이고, beautifulsoup은 정적 웹페이지 탐색에 쓰인다.
    ```
* 페이지 로딩 대기 시간을 줄일 수는 없을까? 
    ```
    지금은 페이지 로딩 대기 시간을 임의로 7초로 정하였다. 하지만 네트워크 상황에 따라 그보다 먼저 될 수 있고, 나중에 될 수도 있는 것이다. selenium에서는 두 가지 방법이 있다. Implicitly wait: 정해진 시간만큼 기다리는 것과 Explicitly wait: 어떤 조건이 만족할 때까지 기다리는 것. 내가 원하는 방법은 Explicitly wait이 될 것 같다. 
    ```
* 새로운 탭을 만들수 있을까? 
    ```
    https://www.selenium.dev/documentation/ko/webdriver/keyboard/
    https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python/28432939#28432939?newreg=4b06c2a9b80d42a3928fce7fe165ade2
    키다운이나, 두 개의 키를 보내면 된다. 
    ```
* pyinstaller 패키지로 실행 파일을 생성할 때, noconsole 옵션을 사용해도, webdriver을 사용할 때 콘솔 창이 생긴다. 어떻게 해야할까..?
    ```
    https://m.blog.naver.com/kibani/221921810439
    
    ```
* 응답 없음을 어떻게 없앨 수 있을까?
    ```
    데이터 탐색 중 응답 없음이 작동한다. 이는 멀티스레드로 해결할 수 있다고 한다. GUI와 Webdriver를 다른 스레드로 구현해야 한다고 한다. 하지만 파이썬에서는 결국 1개의 스레드를 사용하지만, 여러 개의 스레드를 사용하는 것처럼 보이게 한다고 한다. 
    ```

### **에러**  
* DeprecationWarning: use driver.switch_to.alert instead driver.switch_to_alert()
    ```
    앞으로 지원되지 않을 것이므로 사용을 자제해달라는 경고이다. 
    그런데, driver.switch.to_alert() 이렇게 바꾸니 작동하지 않는다. 왜 그런걸까?
    ```   
* USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다.
    ```
    https://stackoverflow.com/questions/64927909/failed-to-read-descriptor-from-node-connection-a-device-attached-to-the-system
    크롬 드라이버에서 생기는 문제인 것 같다. 해가되지 않는 에러라고 한다. 모두들 경고창을 무시하는 듯 하다. 
    ```
* selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: ...
    ```
    분명 경고창에 확인을 눌렀는데 계속 알림이 뜬다. 생겼다가 안 생겼다가 한다. 웹페이지의 로딩 시간의 차이 때문에 생기는 것일까? 3시간째 찾아보는 중이다.. 
    아무리 해도 안 고쳐져서 검색 방식을 변경했다. 
    ```
* Message: stale element reference: element is not attached to the page document
    ```
    element를 찾을 수 없다는 에러이다. 로딩 시간을 충분히 줘보았지만, 똑같은 에러가 발생했다. 
    element를 몇 번 출력해서 비교해보니, webdrive에서 제공하는 element가 매번 달랐다. 즉 새로고침을 하면, 새로 element를 찾아서 진행해야지 싶다. 
    ```
* Mixed Content: The page at '' was loaded over HTTPS, but requested an insecure element ''. This request was automatically upgraded to HTTPS, For more information see https://blog.chromium.org/2019/10/no-more-mixed-messages-about-https.html", source: 
    ```
    headless로 크롬창을 끄고 실행하려하니 이러한 경고가 출력되었다. 그러나 정상적으로 실행되기는 한다. 
    ```
* The Python Tools server crashed 5 times in the last 3 minutes. The server will not be restarted.
    ```
    openpyxl을 import 하면, 이러한 경고가 생기고, python language server가 crashed하여 자동 완성 기능과 문법오류 red line 기능이 없어진다. 아래 시도를 모두 해보았지만, 모두 되지 않았다. 
    1. python language server 을 삭제하고, 다시 vscode의 python 파일을 실행시켜 다시 자동으로 다운받도록 하였다. 
    2. pip를 update하고, openpyxl을 최신 버전으로 업데이트 하였다. 
    3. from openpyxl import load_workbook 으로 하위 항목만을 import 하였다. 
    4. vscode 의 모든 extension 을 삭제하고 다시 설치하였다.  
    이외에 로그를 확인하여 파악하는 법이 있었지만, 아직 로그를 분석하지 못한다. pylence 와 특정 package 간의 연관성이 있는 걸까? 
    ```
* 랜덤 위치에서 element를 찾을 수 없다는 에러와 함께 중간에 멈춘다. 
    ```
    인터넷 상황에 따라 로딩 시간이 달라서 딜레이를 주고 실행해도 똑같이 중간에 멈추었다. 
    어쩌면 스크래핑 봇으로 인하여 서버에 부하가 생겨 서버 측에서 조치를 취한 게 아닐까 생각이 든다. 이 때 크롤러나 스크래핑 봇으로 데이터를 수집할 때 중요한 점을 알게 되었다. 1. 허용된 루트 2. 서버 부하. 접근을 허용하는 루트는 robots.txt.에 있듯이 명시해두었고, 서버 부하는 봇이 해당 서버에 너무 많은 요청을 보내면 서버에 부하가 생겨 지장을 줄 수 있다는 것이다. 그래서 크롤러와 스크래핑 봇에 대한 부정적인 인식이 크다. 그러므로 요청 속도를 조절하고, 요쳥량이 최대한 적도록 설계해야 한다. 
    ```
----
## **참고문서**  
* 마크다운 문법 https://gist.github.com/ihoneymon/652be052a0727ad59601
* xpath https://wkdtjsgur100.github.io/selenium-xpath/
