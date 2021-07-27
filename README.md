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

### **준비 운동**  
* 프로그램을 만들기 전에 확인해야 하는 점이 있다.  
  1. 회사가 달라도 동일한 코드로 원하는 데이터를 얻을 수 있는가?  

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

### **에러**  

----
## **참고문서**  
* 마크다운 문법 https://gist.github.com/ihoneymon/652be052a0727ad59601