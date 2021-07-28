# **Finacial-Data-Collector**
## **들어가기**
프로젝트의 시작은 친구의 부탁이었다. 회사마다 자신이 원하는 데이터를 비교하고 싶은데, 자신이 현재 보는 Company Guide라는 사이트에서는 회사를 하나하나 검색해야 한다고 한다. 그렇다 귀찮은 것이다. 이럴 때 개발이 필요하다. 언젠가 대학생 때는 봉사를 많이 하라는 말을 들은 적이 있다. 보수가 없더라도 만들어서 제공하고, 피드백을 받으며 프로젝트를 진행해보라는 의미인 것 같다. 그것과 더불어 나의 첫 프로젝트라는 것이 의미가 크다.

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
### **웹 스크랩핑 방식**  
* selenium

### **클래스**
* **search data**  
1. 재무 데이터 수집(업데이트)  
2. 회사 목록 수집(업데이트)  

* **print data**  
1. 출력할 회사명  
2. 엑셀 틀 구성  
3. 엑셀로 데이터 출력  

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
----
## **참고문서**  
* 마크다운 문법 https://gist.github.com/ihoneymon/652be052a0727ad59601
* xpath https://wkdtjsgur100.github.io/selenium-xpath/