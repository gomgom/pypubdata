.. image:: https://gom2.net/blog/wp-content/uploads/2016/05/pypubdata_logo_160514.png
    :align: center
    :alt: pypubdata Logo image

**pypubdata: 대한민국 공공데이터 OpenAPI가 Python 3로 포팅된 파이썬 OpenAPI 활용 모듈 라이브러리**

.. image:: https://img.shields.io/pypi/l/pypubdata.svg?maxAge=2592000
    :target: http://www.gnu.org/licenses/lgpl-3.0.html
    :alt: license - lGPL v3
.. image:: https://img.shields.io/pypi/v/pypubdata.svg?maxAge=2592000
   :target: https://github.com/gom2dev/pypubdata
   :alt: pypi version - check Github


===============
들어가며
===============

이 모듈은 파이썬을 통해 대한민국 공공데이터포털(https://data.go.kr) OpenAPI에 손쉽게 접근할 수 있도록 하기 위하여 만들어진 모듈 패키지입니다.

개인적으로 개발하며 사용하기 위해 만든 간단한 국가대기오염정보 OpenAPI 처리 모듈을, 부끄럽지만 많이 손봐서 내놓습니다.

현재까지는 한국환경공단의 **국가대기오염정보**를 **부분적**으로 지원하고 있습니다.

시간 날 때마다 조금씩 조금씩 손봐서 좀 더 다양한 OpenAPI를 지원할 수 있는 모듈 패키지가 되었으면 좋겠습니다.


===============
각 모듈의 저작권
===============

OpenAPI를 포팅하기 위한 모듈 소스 코드는 모두 GNU 약소 일반 공중 사용 허가서(GNU Lesser General Public License) version 3에 따라 저작권이 보호되고 있습니다.

lGPL v3에 관한 자세한 정보는 GNU.org를 참고하여 주십시오.

ⓒ 모든 데이터의 저작권 및 OpenAPI 접근에 관한 방법에 대한 방법 일체에 대해서는 공공데이터포털 저작권을 따릅니다.

ⓒ 기타 개인적으로 쓰여진 코드는 lGPL v3 라이센스에 준거하여 공개합니다.

ⓒ Copyright of every data and OpenAPI of Republic of Korea Public Data Portal and OpenAPI are under their own license.
ⓒ Copyright of pypubdata's code is under the lGPL v3 license.
ⓒ The Python logo is a trademark of the PSF


======================================
국가대기오염정보 OpenAPI 모듈 사용법 (pdairp)
======================================

*(ver 0.1.2 기준, c한국환경공단, c환경부)*

'pdairp' 모듈을 통해 현재 지원하고 있는 서비스는 '측정소정보 조회 서비스'와 '대기오염정보조회 서비스'입니다.

모든 데이터는 공공데이터포털에서 제공하는 'IROS3_OA_DV_0701_OpenAPI활용가이드_한국환경공단_국가대기오염정보_v1.3.docx'에 기재되어 있는 결과값을 받아오도록 기본 구조가 형성되어있습니다.

영어로 기재되어 있는 서비스명들은 사용하기 용이하도록 이름을 임의로 수정하였으며, 데이터가 정상적이지 못한 또는 적용할 필요가 없는 API는 과감하게 제거하였습니다.

------------------
개요
------------------

사용을 위해서는 먼저 pypubdata 패키지에서 pdairp(국가대기오염정보 모듈)을 import합니다.

그 이후, pdairp에서 이용하고자 하는 서비스를 찾으신 뒤, 공공데이터포털에서 지급받으신 비밀키(utf-8 엑세스 키)를 입력해 인스턴스를 초기화 해 줍니다.

.. code:: python

  >>> import pdairp
  >>> a = pdairp.PollutionInfo("ACCESS_KEY")

pdairp 모듈을 초기화 다양한 기능을 하는 메소드를 불러와서 사용하시면 됩니다.

.. code:: python

  >>> print(a.stationdata("문창동", "DAILY"))
  {'totalCount': 23, '9': {'pm10Value24': '23', 'pm25Value': '-', ...

모든 데이터는 파이썬 딕셔너리(Dictionary) 구조로 반환되며, 키 값의 구조는 다음과 같습니다.

- 딕셔너리 안에는: 'totalCount'와 숫자로 구성된 딕셔너리를 반환합니다. totalCount는 반환된 데이터의 총 갯수이며, 그 갯수별로 딕셔너리가 존재합니다.
- 숫자 키 값 안에는: '0'번 딕셔너리부터 가장 최근값이 들어가 있습니다. 숫자 키 값을 갖는 딕셔너리 안에는 {'반환 내용', 반환값}으로 구성된 딕셔너리가 존재합니다.
- 사용 예) 문창동측정소의 하루치 자료 중 가장 최신 자료의 PM10 값

.. code:: python

  >> pm10 = a.stationdata("문창동", "DAILY")['0']['pm10Value']
  >> print(pm10)

아래 서비스 목록에는 서비스 목록과 결과값만 간단하게 기재해 두었으므로, 자세한 정보는 OpenAPI 신청 시 동봉되어 있는 워드문서를 참고해 주세요.

----------------------------------
측정소정보 조회 서비스 (StationInfo 클래스)
----------------------------------

- **근접측정소 목록 조회(nearby)**

.. code:: python

  >> StationInfo.nearby(tm_x, tm_y, page_no='1', num_of_rows='10')

*tmX 코드*와 *tmY 코드*를 받아 그 주변의 근접측정소 목록을 조회해줍니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
stationName      측정소 이름
addr             측정소 주소
tm               측정소까지 거리
=============    ================

- **측정소 목록 조회 -상세정보조회- (detail)**

.. code:: python

  >> StationInfo.detail(addr, station_name, page_no='1', num_of_rows='10')

*지역명*과 *측정소명*을 입력받아 그 측정소의 정보를 자세하게 조회해줍니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
addr             측정소 주소
dmX              WGS84 기반 위도
dmY              WGS84 기반 경도
item             측정항목
mangName         측정망
map              지도
oper             관리기관명
photo            전경 사진
stationName      측정소 이미지
vrml             측정소 전경
year             운영년도
=============    ================

- **TM 기준좌표 조회 (tmcode)**

.. code:: python

  >> StationInfo.tmcode(umd_name, page_no='1', num_of_rows='10')

*읍면동* 이름을 입력받아 그 읍면동과 가장 가까운 측정소를 안내해 줍니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
sidoName         시도 이름
sggName          시군구 이름
umdName          읍면동 이름
tmX              읍면동의 tm_X 좌표
tmY              읍면동의 tm_Y 좌표
=============    ================


----------------------------------
대기오염정보조회 서비스 (PollutionInfo 클래스)
----------------------------------

- **측정소별 실시간 측정정보조회 (stationdata)**

.. code:: python

  >> PollutionInfo.stationdata(station_name, data_term, page_no='1', num_of_rows='10', ver='1.2')

*측정소 이름*과 *요청 데이터 기간*를 받아 데이터 기간 동안의 측정정보를 제공합니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
dataTime         측정일
mangName         측정망
khaiGrade        통합대기환경 지수
khaiValue        통합대기환경 수치
coGrade          일산화탄소 지수
coValue          일산화탄소 농도
no2Grade         이산화질소 지수
no2Value         이산화질소 농도
o3Grade          오존 지수
o3Value          오존 농도
so2Grade         아황산가스 지수
so2Value         아황산가스 농도
pm10Grade        PM10(미세먼지) 지수
pm10Value        PM10 농도
pl10Value24      PM10 24시간 예측농도
pm25Grade        PM2.5(초미세먼지) 지수
pm25Value        PM2.5 농도
pm25Value24      PM2.5 24시간 예측농도
=============    ================

- **통합대기환경지수 민감군 이상 측정소 목록 조회 (strangelist)**

.. code:: python

  >> PollutionInfo.strangelist(page_no='1', num_of_rows='10')

현재 통합대기환경지수가 나쁨 이상으로 이상한 측정소의 목록을 조회해줍니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
addr             측정소 주소
stationName      측정소 이름
=============    ================

- **시도별 실시간 측정정보조회 (sidodata)**

.. code:: python

  >> PollutionInfo.sidodata(sido_name, page_no='1', num_of_rows='10', ver='1.2')

*광역자치단체(시, 도)* 이름을 받아 광역자치단체 대표 시군구에 위치한 측정소 측정정보를 제공합니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
dataTime         측정일
mangName         측정망
stationName      측정소 이름
khaiGrade        통합대기환경 지수
khaiValue        통합대기환경 수치
coGrade          일산화탄소 지수
coValue          일산화탄소 농도
no2Grade         이산화질소 지수
no2Value         이산화질소 농도
o3Grade          오존 지수
o3Value          오존 농도
so2Grade         아황산가스 지수
so2Value         아황산가스 농도
pm10Grade        PM10(미세먼지) 지수
pm10Value        PM10 농도
pl10Value24      PM10 24시간 예측농도
pm25Grade        PM2.5(초미세먼지) 지수
pm25Value        PM2.5 농도
pm25Value24      PM2.5 24시간 예측농도
=============    ================

- **미세먼지/오존 예보통보 조회 (forecastlist)**

.. code:: python

  >> PollutionInfo.forecastlist(inform_code, search_date='0', page_no='1', num_of_rows='10')

*조회코드(PM10, PM25, O3)*와 *조회날짜(예: 2016-05-14)*를 받아 그 시각 예보가 있는 곳을 확인해줍니다.

결과로는 다음과 같은 값을 활용할 수 있습니다.

=============    ================
항목명(영문)          항목명(국문)
=============    ================
dataTime         자료 일자
imageUrl1        모델 결과(PM10 12시)
imageUrl2        모델 결과(PM10 18시)
imageUrl3        모델 결과(PM10 24시)
imageUrl4        모델 결과(PM2.5 12시)
imageUrl5        모델 결과(PM2.5 18시)
imageUrl6        모델 결과(PM2.5 24시)
informCause      발생원인
informData       에측통보 시간
informGrade      예보등급
informOverall    예보개황
actionKnack      행동요령 (필요시)
=============    ================


======================================
모듈 문서 (Documentation)
======================================

아직 준비하지 못했습니다. 현재까지 개발된 모듈은 Github 내 pypubdata 저장소의 README.rst를 참조해 주시기 바랍니다.

(https://github.com/gom2dev/pypubdata)


======================================
도움이 필요한 경우 및 기타 문의 안내 (Contact)
======================================

Github 저장소 내 Issues에서 각종 버그와 기타 문의를 추적하고자 합니다.

프로그래밍이 본업이 아닌 쌩초보 개발자이므로 살살 다뤄주세요... (^^;)

(https://github.com/gom2dev/pypubdata)
