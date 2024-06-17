## [[Dacon] KPI 도출 비즈니스 전략 아이디어 경진대회](https://dacon.io/competitions/official/236248/codeshare/10420)

### 🏆 수상 🏆 | 리더보드 2위 / 최종 심사 4위
<img width="70%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/6a4f231b-7919-4571-ae9c-dbc3024a9677">

#### 👩🏻‍💻 주요 데이터 분석 결과
- **고객 평균 주문 가치 (AOV, Average Order Value)**
![image](https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/50d98ac9-f239-4e43-807c-dc619faa74b4)

- **고객 분류**
  - AOV가 0~10 헤아이스인 그룹 `입문 고객 그룹`
  - AOV가 10~60 헤아이스인 그룹 `확장 가능 고객 그룹`
  - AOV가 200~300 헤아이스인 그룹 `고액 소비 고객 그룹`

- **`입문 고객 그룹` 의 구매 패턴과 솔루션**

  <img width="30%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/318a5942-7c98-4c5f-959f-5bbbddb8ea2c">
  
  | 구매 패턴 | 재구매율 0.8%, 타 그룹에 비해 Voucher 사용량 2.2배, 3.72배 높음 |
  |---|---|
  |솔루션|- 이벤트성 Voucher로 재구매율 높임<br>- 이벤트성 Voucher를 제공할 경우 확장 가능 고객 그룹으로 성장하기 위해 N개 이상 구매 시 할인을 적용할 수 있는 Voucher 제공<br>|
    
- **`확장 가능 고객 그룹` 의 구매 패턴과 솔루션**

  <img width="40%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/efe5f6ed-bdf5-40cd-ad30-8e3d6161d659">
  
  |구매 패턴| 95.28%가 물품 1개씩 구매, 재구매율 2.5% |
  |---|---|
  |솔루션|- AOV를 크게 유지하고자 두 개 이상의 제품 구매 시 할인 또는 무료 배송 혜택 제공<br>- 구매 금액에 따른 포인트 적립이나 할인 혜택을 제공하여 지속적인 구매 유도<br>- 고객이 구매한 상품 이력과 크로스 세일즈 프로모션을 진행하여 관련 상품을 함께 구매했을 때 가격을 달리하여 추가 구매 유도|
- **`고액 소비 고객 그룹` 의 구매 패턴과 솔루션**

  <img width="40%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/88f37bf7-6d32-48e3-b21d-9d5755bf721f">

  | 구매 패턴 | 무할부 구매도 많았지만, 2~6개월, 8개월, 10개월 할부의 경우 500건 이상의 주문에서 사용됨, 신용카드를 주로 사용함 |
  |---|---|
  |솔루션|- 무이자 할부 프로모션을 제공하여 경쟁사에 가지 않고 지속적인 결제를 하도록 유도<br>- 할부 이벤트나 추가 혜택을 제공하여 재결제 유도 (ex. 2개월 이상 할부를 선택한 고객에게 추가 할인 혹은 적립금 제공)|

#### 📊 데이터세트 : 브라질 이커머스 기업의 데이터
- [데이터](https://dacon.io/competitions/official/236248/data)
  - customers.csv (고객과 관련된 정보)
  - locations.csv (지역과 관련된 정보)
  - order_items.csv (주문 아이템과 관련된 정보)
  - orders.csv (주문과 관련된 정보)
  - payments.csv (지불과 관련된 정보)
  - products.csv (제품과 관련된 정보)
  - reviews.csv (리뷰와 관련된 정보)
  - sellers.csv (판매자와 관련된 정보)
<img width="80%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/02adbfd4-25b7-4e92-8c51-69be6854e59f">


### 💻 데이터분석 연습 :: 이커머스 고객 세분화 분석 아이디어 경진대회
#### 📊 데이터세트
- [데이터](https://dacon.io/competitions/official/236222/data)
  - Onlinesales_info.csv (온라인거래와 관련된 정보)
  - Customer_info.csv (고객과 관련된 정보)
  - Discount_info.csv (할인과 관련된 정보)
  - Marketing_info.csv (마케팅비용과 관련된 정보)
  - Tax_info.csv (세금과 관련된 정보)
<img width="80%" alt="image" src="https://github.com/SeyeonJang/Data-Analysis-Study/assets/47477205/8fdecff7-11f8-4b27-8b9c-0b41b32ab801">
