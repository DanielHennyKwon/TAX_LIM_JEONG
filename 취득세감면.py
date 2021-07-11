# -*- coding: utf-8 -*-
#Created on Thu Jan  3 00:54:44 2019@author: 권달현
import 지방세법,지방세법시행령,지방세특례제한법,지방세특례제한법시행령
합병취득재산과세표준={
                    "합병에 따른 취득을 유상취득과 무상취득 중 어느 것으로 보는지 여부에 따라서 과세표준과 세율 적용이 상이한바, 합병에 따른 취득은 무상취득으로 보기 때문에 과세표준은 법인장부가액 기준이 아닌 시가표준액 기준이 적용되고, ‘부동산’ 취득시 적용되는 표준세율은 3.5%가 된다. ":{},
                    "합병":{
                        "유무상 판단 : 무상":{},
                        "근거 : 대법98두19193, 2000.10.13":{
                            "대법98두19193, 2000.10.13. 법인의 합병으로 인하여 취득한 토지가 법인의 비업무용 토지로 되어 그 합병으로 인한 취득이 취득세 중과대상 인 취득에 해당한다고 하더라도, 이때의 취득은 무상취득으로 봄이 상당하므로, 합병 당시 법인장부에 기재된 당해 토지의 가격을 사실상의 취득가격으로 보아 취득세의 과세표준으로 삼을 수는 없다. 같은 취지에서 원심이, 원고가 소외 ○○전자계산 주식회사를 흡수합병함에 따라 취득한 이 사건 토지가 법 제112조 제2항의 규정에 의한 법인의 비업무용 토지로 되어 취득세를 중과하되, 그 합병으로 인한 이 사건 토지의 취득이 무상취득에 해당하여 취득가액이 있을 수 없으므로, 시가표준액에 의하여 취득세 과세표준을 산정하여야 한다고 판단한 것은 정당하다.":{},
                        },
                        "과세표준 :  시가표준액 ":{},
                        "부동산취득 표준세율 : 3.5%":{},
                    },
                    "분할합병":{
                        "유무상 판단 : 무상": {},
                        "근거 : 세정13407-60, 2002.01.17. ": {
                            "세정13407-60, 2002.01.17. 분할합병으로 취득등기한 부동산이 조세특례제한법 제119조 제1항 제10호의 규정에 해당된 경우라면 등록세 가 면제되고 여기에 해당되지 않은 경우라면 지방세법 제131조 제1항 제2호의 규정에 의한 1000분의 15(무상 취득세율)의 세율이 적용되나 이의 해당여부는 과세권자가 사실관계를 조사하여 판단할 사항임.":{},
                        },
                        "과세표준 :  시가표준액 ": {},
                        "부동산취득 표준세율 : 3.5%": {},
                    },
                    "참고: 법인의 합병으로 인하여 존속하는 법인이 소멸하는 법인의 소유이던 부동산을 취득하는 경우 에 그 취득일은 합병기일이다(서울행법 99구5152, 1999.9.30., 지방세운영과-1553, 2016.06.17.).":{},
                }
시가표준액={
    "지방세법 제4조 【부동산 등의 시가표준액】 ":지방세법.제4조,
    "지방세법시행령 제2조 【토지 및 주택의 시가표준액】 ":지방세법시행령.제2조,
    "지방세법시행령 제4조 【건축물 등의 시가표준액 결정 등】 ":지방세법시행령.제4조,
    " 과세물건에 대한 시가표준액 정보는 과세물건의 소재지･등록지 별로 관할 지 방자치단체의 홈페이지에서 시가표준액에 대한 정보를 수집하는 것이 원칙이며, 시가표준액 정보를 제공하는 홈페이지를 예시하면 아래와 같다.":{},
    "토지, 단독주택, 공동주택":{
        "정보제공 홈페이지 : 국토교통부 부동산 공시가격 알리미 http://www.realtyprice.kr/notice/":{},
        "제공하는 서비스 : 공시된 개별공시지가, 개별주택가격에 대하여 해당 시･군･구청 홈페이지 연결 서비스 및 공동주택가격 열람서비스":{},
    },
    "단독/공동주택을 제외한 일반건축물 (상가, 오피 스텔 등), 회원권":{
        "정보제공 홈페이지 : 위텍스 http://wetax.go.kr/ HOME > 지방세정보 > 시가표준액조회": {},
        "제공하는 서비스 : 시가표준액조회 서비스": {},
    },
    "기타":{
        "정보제공 홈페이지 : 서울특별시의 서울재정포털 http://finance.seoul.go.kr/ HOME > 세금 > 세금자료실 > 시가표준액 표(건물,기타)": {},
        "제공하는 서비스 :연도별로 시가표준액표를 제공": {},
        " 건축물, 회원권, 차량, 기계장비, 선박, 항공기 및 그 밖의 과세대상에 대한 시가표준액은 매년 1월 1일 현재 시장･군수 또는 구청장이 행정자치부장관이 정하는 기준에 따라 산정하여 특별시장･광역시장 또는 도지사의 승인을 받아 결정함. 따라서 과세물건의 소재지･등록지 별로 관할 지방자치단체의 홈페이지에서 시가표준액에 대한 정보를 수집해야 함":{},
    },
}
지방세감면일반={
        '지방세 특례 제도': {
            '지방세 특례제도의 개요': {},
            '지방세 특례와 그 밖의 지원제도의 개념': {},
            '지방세 특례 등의 사후관리': {},
        },
        '지방세 감면 구성': {
            '개요': {},
            '감면의 대상범위': {},
            '근거법령별 감면 법령체계': {},
            '근거법령(지방세특례제한법,,조례)간의 적용체계': {},
        },
        '지방세법(취득세편) 및 지방세특례제한법의 주요 용어 정의': {
            '지방세특례제한법(제2조)': {},
            '지방세법(제6조)': {},
        },
    }
취득세감면공통사항={
        '지방세 감면제례 검토': {
            '지방세 감면조례 검토의 의의': {},
            '지방세 감면조례 사례': {},
        },
        '지방세특례제한법 보칙 검토': {
            '감면 제외대상': {},
            '지방세 감면 특례의 제한:최소납부세액제도': {},
            '중복감면의 배제': {},
            '감면된 취득세 추징': {},
            '지방세 중과세율 적용 배제 및 중과세율 적용시기 유예 특례': {},
        },
        '취득세 감면분에 대한 농어촌특별세 검토': {
            '취득세 특례세율 적용분의 농어촌 특별세 비과세 여부': {},
            '중과세율 내지 중과세의 배제시 농어촌특별세 적용': {},
            '취득세 중과 적용시 농어촌특별세 과세표준': {},
            '기업분할 합병 등에 대한 감면분에[ 대한 농어촌특별세 비과세여부': {},
        },
        '부동산 취득세 중과 검토': {
            '현행 지방세법에서 규정하고 있는 취득세율의 종류': {},
            '취득세 중과 상세 계산구조': {},
            '취득세 과세시 지방교육세 과세표준 산정요령': {},
            '취득세 과세시 농어촌특별세(부과분) 과세표준 산정요령': {},
        },
    }
법인전환취득세감면= {
            '감면의 내용 및 관련 쟁점 사항': {},
            '감면의 요건': {},
            '사후관리': {},
            '보칙 검토': {},
            '검토사례': {},
        }
사업시행자외의자산업단지감면={
            '감면의 내용 및 관련 쟁점 사항': {},
            '감면의 요건': {},
            '사후관리': {},
            '보칙 검토': {},
            '검토사례': {},
        }
물류사업용부동산취득세감면={
            '감면의 내용 및 관련 쟁점 사항': {},
            '감면의 요건': {},
            '사후관리': {},
            '보칙 검토': {},
            '검토사례': {},
        }
기업부설연구소용부동산취득세감면={
            '감면의 내용 및 관련 쟁점 사항': {},
            '감면의 요건': {},
            '사후관리': {},
            '보칙 검토': {},
            '검토사례': {},
        }
창업중소기업부동산취득세감면={
            '감면의 내용 및 관련 쟁점 사항': {},
            '감면의 요건': {},
            '사후관리': {},
            '보칙 검토': {},
            '검토사례': {},
            '창업여부 자가진단표(출처:중소벤처기업부)': {},
        }
적격합병취득세감면={
            "요지":{
                "지방세특례제한법 제177조의 2 【지방세 감면 특례의 제한】":지방세특례제한법.제177_02조,
                "지방세특례제한법 제177조의 2 【지방세 감면 특례의 제한】의 최소납부세액 제도는 취득세와 재산 세가 100% 면제되거나 100% 경감되더라도 최소한 15%의 취득세와 재산세를 납부해야 하는 제도 로서, 2016.1.1이후 적격합병 및 적격분할로 재산을 취득하여 취득세가 100%면제되더라도 최소한 15%의 취득세는 납부해야 한다. ": {},
                " 따라서 2016.1.1이후 적격합병 및 적격분할의 경우에는 취득세 과 세표준, 세율(중과여부 판단 포함), 감면방법에 대한 면밀한 검토가 필요하다. ": {},
                "제57조의 2 제1항 :적격합병(서비스업종 제외) 취득 재산 *적용시기:2016.1.1. ": {},
                "제57조의 2 제3항 제1호･제2호･제3호･제4호 ･제6호 :(제1호)정부출자기업이 취득하는 현물출자 국유재산 (제2호)적격분할 재산, (제3호)현물출자 재산, (제4호)자산교환 재 산, (제6호)자산의 포괄적 양도로 취득하는 재산 *적용시기:2016.1.1.": {},
                "": {},
            },
            '합병으로 인하여 취득하는 재산의 과세표준': {
                "가. 합병에 따른 취득시 적용할 과세표준":합병취득재산과세표준,
                "나. 시가표준액의 산정 ":시가표준액,
            },
            '합병으로 인하여 취득한 과세물건에 적용하는 취득세율': {
                "지방세법 제11조 【부동산 취득의 세율】1항2호 ": 지방세법.제11조,
                "지방세법 지방세법 제12조 【부동산 외 취득의 세율】 ": 지방세법.제12조,
                "지방세법 제15조 【세율의 특례】":지방세법.제15조,
                "요지":{
                    "①｢법인세법｣ 제44조 제2항 또는 제3항에 해당하는 법인의 합병(적격합병)으로 인한 취득에 해당 하고, ":{},
                    "② 합병등기일부터 3년 이내에 ｢법인세법｣ 제44조의 3 제3항 각 호의 어느 하나에 해당하는 사유(적격합병의 사후관리요건 위배 사유)가 발생하지 않고(단, 법인세법 시행령 제80조의4 제7항의 부득이한 사유가 있는 경우 제외), ":{},
                    " ③법인의 합병으로 인하여 취득한 과세물건이 ‘합병 후’에 지방세 법 제13조 제1항 및 제5항에 따른 과세물건에 해당하지 않는 경우에는 ":{},
                    "지방세법 제15조 제1항에 따라 세율의 특례를 적용한다. ":{},
                    " 해당 세율의 특례가 적용되는 경우 (구)취득세 상당액이 비과세되는 것 과 동일한 효과가 발생된다.":{},
                },
                "세율의 특례 적용 여부를 요약하면 ":{
                    "참고 : 지방세법 제13조(과밀억제권역 안 취득 등 중과)": 지방세법.제13조,
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병당시 그리고 합병등기일 로부터 5년 이내에 제13조 제1항, 제2항, 제5항의 과세물건에 해당하 지 않는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 제15조 세율의 특례 적용 (제11조 및 제12조에 따른 세율-2%) 를 취득세액으로 함":{},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제11조 및 제12조에 따른 세율 적용":{},
                    },
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병당시 제13조 제2항의 과세물건에 해당하는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 제15조 세율의 특례 적용 (제11조에 따른 세율-2%)*3을 취 득세액으로 함": {},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제13조에 따라 취득세 중과": {},
                    },
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병전부터 제13조 제5항의 과세물건에 해당하는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 제15조 세율의 특례 적용 (제11조에 따른 세율-2%)을 취 득세액으로 함": {},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제13조에 따라 취득세 중과": {},
                    },
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병등기일로부터 5년 이내 에 제13조 제2항의 과세물건에 해당 하는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 제15조 세율의 특례 적용 (제11조에 따른 세율-2%)*3을 취 득세액으로 함": {},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제16조에 따라 취득세 중과분 추징": {},
                    },
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병등기일로부터 5년 이내 에 제13조 제1항의 과세물건에 해당 하는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 세율의 특례적용 없음 제16조에 따른 취득세를 취득세액으로 함": {},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제16조에 따라 취득세 중과분 추징": {},
                    },
                    "법인의 합병으로 인하여 취득한 과세 물건이 합병등기일로부터 5년 이내 에 제13조 제5항의 과세물건에 해당 하는 경우":{
                        "적격합병 취득 and 적격합병 사후관리 요건 위배 없음 : 세율의 특례적용 없음 제16조에 따른 취득세를 취득세액으로 함": {},
                        "비적격합병 취득 or 적격합병 사후관리요건 위배 : 세율의 특례적용 없음, 제16조에 따라 취득세 중과분 추징": {},
                    },
                },
                "지방세법 제11조 및 제12조에 따른 표준세율을 적용할 때 합병을 원인으로 한 취득은 무상 취득에 해당하는바, ":{},
                "취득세 과세물건 중 ①부동산(무상취득 세율: 3.5%, 단, 비영리사업자의 취득은 2.8%) 및 ②소형선박을 제외한 등기･등록 대상인 선박(무상취득 세율: 3.0%)의 경우에만 취득원인별 로 취득세 표준세율이 상이하고, 나머지 취득세 과세물건(미등기･등록 선박, 소형선박, 차량, 기계장 비, 항공기, 입목, 광업권, 어업권, 골프회원권, 승마회원권, 콘도미니엄 회원권, 종합체육시설 이용 회원권, 요트회원권)은 취득원인별로 취득세 표준세율차이가 없다.":{},
                "세제과-6387(2016.05.03.). 법령상 요건을 충족하는 합병에 따라 부동산을 취득하는 경우라면 지방세법에 따라 세율특례(3.5% - 2% = 1.5%)가 적용되어 산출된 세액이 지방세특례제한법상 합병에 대한 감면이 적용되어 전액 감면되는 것이고, 전액 감면된 세액에 지방세 감면 특례제한 규정인 지방세특례제한법 177조의2 규정이 적용되는 것이므로 최종 1.5% 세율을 적용하여 산출된 세액에 100분의 85의 감면율을 적용하는 것이 타당하다고 판단됨": {},
            },
            '합병으로 인하여 취득한 과세물건에 대한 취득세 중과여부 판단': {
                "가. 법인 또는 사무소등이 대도시에서 법인의 지점 또는 분사무소를 설치한 이후 5년 이내에 하는 업무용･비업무용 또는 사업용･비사업용의 모든 대도시의 부동산 취 득중과에 해당하는 경우: 법인의 합병으로 인하여 취득한 과세물건이 합병당시 지방세법 제13조 제2항의 과세물건에 해당하는 경우 ":{
                    "흡수합병으로 피합병법인의 대도시 내 본점･지점을 소속만 합병법인의 지점으로 바꾸어 유지･존 속한 것은 원칙적으로 ‘합병법인’이 대도시 내에서 지점을 설치한 것에 해당한다(대법원2003두 6566, 2004.9.3.참조). ":{
                        "만약, 종전 피합병법인의 대도시 내 본점･지점 사업장을 합병법인의 지점 사 업장으로 사용하는 경우 별도의 사업장이 새로이 신설되는 것이 없기 때문에 새로운 지점의 설치로 보지 않는 다면, 종전 ‘피합병법인’의 대도시 내 본점 전입일 또는 지점설치일로부터 5년 이내 대도 시 내 부동산 취득에 해당되어 취득세가 중과될 것이다. ":{},
                        " 이 경우 과밀억제권역 내 인구집중 억제 취 지와 맞지 않게 중과제외범위가 과도하게 확대되는 문제점이 있는바, 이러한 해석은 타당하지 않다. ":{},
                        "따라서, 흡수합병으로 피합병법인의 대도시 내 본점･지점을 소속만 합병법인의 지점으로 바꾸어 유 지･존속하면서 합병법인이 합병으로 취득하는 피합병법인 소유 대도시 내 부동산은 지방세법 시행령 제27조 제5항이 적용되는 경우(ex: 대도시에서 설립 후 5년이 경과한 법인(“기존법인”)이 다른 기존 법인과 합병하는 경우)를 제외하고는 합병법인이 대도시 내에서 지점을 설치한 이후 5년 이내 취득 하는 부동산에 해당되어 중과되는 것이 원칙이다. ":{},
                    },
                    "즉, 지방세법 제13조 제1항 제1호에 따른 중과를 적용할 때 지방세법 시행령 제27조 제5항에 따 라 대도시에서 설립 후 5년이 경과한 법인(이하 “기존법인”)이 다른 기존법인과 합병하는 경우에는 합병으로 취득하는 대도시 내 부동산을 중과세대상으로 보지 아니하며, 기존법인이 대도시에서 설립 후 5년이 경과되지 아니한 법인과 합병하여 기존법인 외의 법인이 합병 후 존속하는 법인이 되거나 새로운 법인을 신설하는 경우에는 합병 당시 기존법인에 대한 자산비율에 해당하는 부분을 중과세대 상으로 보지 않는다.":{},
                    "기존법인간의 합병":{
                        "신설합병 : 중과제외":{},
                        "흡수합병": {
                            "기존법인이 합병후 존속 : 중과제외":{},
                            "신설법인이 합병후 존속 : 중과제외":{},
                        },
                    },
                    "기존법인과 신설법인간의 합병":{
                        "신설합병 : 중과대상임.단,기존버인에 대한 자산비율(*)만큼 중과제외": {
                                "(*) 자산비율은 자산을 평가하는 때에는 평가액을 기준으로 계산한 비율로 하고, 자산을 평가하지 아니하는 때 에는 합병 당시의 장부가액을 기준으로 계산한 비율로 함":{},
                            },
                        "흡수합병": {
                            "기존법인이 합병후 존속 : 중과제외": {},
                            "신설법인이 합병후 존속 : 중과대상임.단,기존버인에 대한 자산비율(*)만큼 중과제외": {
                                "(*) 자산비율은 자산을 평가하는 때에는 평가액을 기준으로 계산한 비율로 하고, 자산을 평가하지 아니하는 때 에는 합병 당시의 장부가액을 기준으로 계산한 비율로 함":{},
                            },
                        },
                    },
                    "신설법인간의 합병":{
                        "신설합병 : 중과대상임. 중과제외 해당 없음.": {},
                        "흡수합병": {
                            "기존법인이 합병후 존속 : 중과대상임. 중과제외 해당 없음.": {},
                            "신설법인이 합병후 존속 : 중과대상임. 중과제외 해당 없음.": {},
                        },
                    },
                    "또한 합병당시에 취득하는 부동산뿐만이 아니라, 기존법인이 다른 기존법인과 ‘합병하는 과정’에 서 피합병법인이 임차하여 사용하던 종전 대도시 내 본점소재지에 합병법인의 지점을 설치하고 그 이후 5년 이내에 임차하던 해당 지점용 대도시 내 부동산을 취득하는 경우도 지방세법 시행령 제27 조 제5항에 따라 중과세대상으로 보지 않는다(대법원2011두12726, 2013.07.11.; 지방세운영-36, 2015.01.06.).":{},
                    "그러나, 흡수합병으로 피합병법인의 대도시 내 본점･지점을 소속만 합병법인의 지점으로 바꾸어 유지･존속하는 것이 아니라, ‘합병이전’에 합병법인이 피합병법인 소유 대도시 소재 부동산을 임차하 여 지점을 설치하였다가 해당 지점설치일 이후 5년 이내 합병법인이 흡수합병으로 해당 피합병법인 소유 대도시 소재 부동산을 취득하는 경우에는 지점설치 이후 5년 이내에 취득한 일체의 부동산에 해당하여 그 지점에 관계된 부동산은 취득세 중과대상에 해당된다(서울세제-300, 2017.01.05.). ":{
                        " 특 수관계 있는 계열회사 간의 합병 시 합병전에 상호 임대차관계가 있는 경우가 빈번한바, 실무적으로 주의를 요한다.":{},
                    },
                },
                "나. 법인 또는 사무소등이 대도시에서 법인의 지점 또는 분사무소를 설치하기 이전 5년 이내에 하는 법인의 지점･분사무소의 용도로 직접 사용하기 위한 대도시의 부동산 취득중과에 해당하는 경우":{
                    "대도시 외에 본점이 소재한 합병법인이 흡수합병으로 피합병법인의 대도시 내 임대용부동산을 승 계취득 하였다가 합병일(피합병법인의 임대용부동산 취득일 아님)로부터 5년 이내에 해당 부동산을 합병법인의 본점･지점의 용도로 직접 사용하는 경우에는 법인의 합병으로 대도시 내 부동산을 취득 하고 그 이후 5년 이내에 대도시 내로 본점을 이전한 경우 또는 대도시 내에 지점을 설치한 경우에 해당하여 합병법인의 본점 또는 지점의 용도로 ‘직접’ 사용하는 부분만큼 지방세법 제13조 제2항 제 1호에 따라 취득세가 중과된다(지방세운영-1554, 2016.06.17.취지)":{},
                    "그리고, 이 경우에는 대도시에 서 설립 후 5년이 경과한 ‘기존법인’이 다른 ‘기존법인’과 합병한 것에 해당하더라도 ｢지방세법 시행령｣ 제27조 제5항이 적용되지 않는다. ":{},
                    "한편, 대도시 소재 합병법인이 합병 전부터 소유하던 대도시 내 임대용 부동산에 합병후 피합병 법인의 조직이 이전하여 해당 합병법인의 부동산 취득일로부터 5년 이내 본점･지점의 용도로 직접 사용하는 경우 본점 또는 지점의 용도로 ‘직접’ 사용하는 부분만큼 취득세가 중과된다. ":{},
                    "그리고, 합병법인이 합병 전부터 소유하던 대도시 내 임대용 부동산은 합병과 무관한 것이므로 지방세법 제 15조 세율의 특례적용 없이 지방세법 제11조의 세율이 적용되고, 취득세 감면대상이 아니다":{},
                    "또한, 이 경우에도 대도시에서 설립 후 5년이 경과한 ‘기존법인’이 다른 ‘기존법인’과 합병한 것에 해당하 더라도 ｢지방세법 시행령｣ 제27조 제5항이 적용되지 않는다.":{},
                    "행정자치부 지방세운영과-1554, 2016. 6. 17. ":{
                        "(질의) 합병으로 합병법인 甲이 피합병법인 乙의 부동산을 취득하는 경우 중과세를 판단함에 있어 그 5년 이내의 기산일 ":{},
                        "(회신내용) 법인의 합병으로 인하여 소멸 법인소유 부동산을 존속법인 명의로 소유권을 이전할 때에는 합병일이 취득시기 (행자부 세정13470-1399, 1997.11.06. 참조)가 되며, 종전의 회사를 흡수합병하면서 그 지점을 소속만 합병회사의 지점으로 바꾸어 유지･존속한 것은 ｢지방세법｣ 제13조제2 항제1호에서 규정하는 대도시 내에서의 지점 설치로 볼 수 있다고 판단하였던 점(대법원 2004. 9. 3. 선고 2003두6566 판결 참조) 등을 고려해 볼 때, 피합병법인(乙)이 합병 전에 취득한 대도시내 부동산의 경우 합병일에 합병법인(甲)이 취득한 것으로 보아, 그 합병일을 중과적용 기산시점으로 보는 것이 타당하다고 할 것이므로, 합병일로부터 5년 이내에 해당 부동산을 법인의 본점 또는 지점의 용도로 직접 사용하는 경우에는 중과대상에 해당하게 됩니다.":{},
                    },
                },
                "다. 과밀억제권역 내에서 법인의 본점 또는 주사무소의 사업용 부동산을 신축 또는 증축하여 취득하는 경우의 중과":{
                    "합병으로 피합병법인의 과밀억제권역 내 토지를 취득하였다가 합병일 이후 5년 이내에 해당 토지 에 건축물을 신축하여 본점용도로 사용하는 경우 해당 건축물 및 부속토지는 법인의 합병으로 인하 여 취득한 과세물건이 합병등기일로부터 5년 이내에 지방세법 제13조 제1항의 과세물건에 해당하여 취득세가 중과된다.":{},
                },
                "라. 법인의 합병으로 인하여 취득한 과세물건이 합병전부터 지방세법 제13조 제5항 의 과세물건(사치성 재산)에 해당하는 경우 ":{
                    "합병 전 지방세법 제13조 제5항에 따른 취득세 중과세율을 적용 받았던 소멸법인의 과세물건을 적격합병으로 존속법인이 취득하는 경우라면, 지방세법 제15조 제1항에 따른 세율의 특례 적용대상이 된다(지방세운영-3603, 2015.11.16.취지). ":{},
                   "세율의 특례가 적용되는 경우 (구)취득세가 비과세 되 므로 지방세법 제13조 제5항에 따른 취득세 중과가 적용되지 않는다. ":{},
                    "한편, 골프장은 그 시설을 갖추어 ｢체육시설의 설치･이용에 관한 법률｣에 따라 체육시설업의 등록 (시설을 증설하여 변경등록하는 경우를 포함)을 하는 경우 및 등록을 하지 아니하더라도 사실상 골프 장으로 사용하는 경우에 한하여 취득세를 중과세 하므로, 합병으로 인하여 취득한 골프장은 일반적 으로 합병으로 취득하는 시점에 제13조 제5항의 과세물건에 해당하지 않는다. ":{},
                    "결국, 법인의 합병으로 인하여 취득한 과세물건이 합병전부터 제13조 제5항의 과세물건에 해당하 는 경우에는 취득세가 중과되지 않는다. ":{},
                },
                "마. 법인의 합병으로 인하여 취득한 과세물건이 합병일로부터 5년 이내에 지방세법 제13조 제5항의 과세물건에 해당하는 경우 ":{
                    "합병으로 피합병법인의 과밀억제권역 외 토지를 취득하였다가 합병일 이후 5년 이내에 해당 토지 에 건축물을 신축하여 해당 부동산이 지방세법 제13조 제5항의 과세물건에 해당되는 경우 취득세가 중과된다.":{},
                },
            },
            '합병으로 인하여 취득한 과세물건에 대한 취득세 감면': {
                "합병으로 인하여 취득한 과세물건이 다음의 요건을 모두 충족하는 경우에는 지방세법 제15조 제1 항에 따라 세율의 특례를 적용하여 산출한 취득세를 면제한다.":{},
                "지방세법 제15조 【세율의 특례】1항": 지방세법.제15조,
                "지방세특례제한법 제57조의 2 【기업합병･분할 등에 대한 감면】": 지방세특례제한법.제57_02조,
                "지방세특례제한법 제177조 【감면 제외대상": 지방세특례제한법.제177조,
                "지방세특례제한법 시행령 제28조의 2 【법인 합병의 범위 등】 ": 지방세특례제한법시행령.제28_02조,
                "다만, 법인의 합병으로 인하여 취득한 과세물건이 ‘합병 후’에 지방세법 제13조 제1항 및 제5항에 따른 취득세 중과세 과세물건에 해당하는 경우에는 (구)취득세 중과세 상당액을 감면대상에서 제외하고, (구)등록세 상당액만 감면한다. ":{
                    "그리고, 합병등기일부터 3년 이내에 ｢법인세법｣ 제44조의 3 제 3항 각 호의 어느 하나에 해당하는 사유(적격합병의 사후관리요건 위배 사유)가 발생하는 경우(단, 법 인세법 시행령 제80조의4 제7항의 부득이한 사유가 있는 경우 제외)에는 경감된 취득세를 추징한다":{},
                    "지방세법 제13조 제1항의 과세물건":{
                        "감면전 취득세 : 표준세율+2%*2":{},
                        "감면제외 대상 :(구)취득세 : 2%*3":{},
                        "감면 대상 :(구)등록세 : 표준세율+2%*2 -2%*3 =표준세율-2%":{},
                    },
                    "지방세법 제13조 제5항의 과세물건":{
                        "감면전 취득세 : 표준세율+2%*4": {},
                        "감면제외 대상 :(구)취득세 : 2%*5": {},
                        "감면 대상 :(구)등록세 : 표준세율+2%*4 -2%*5 =표준세율-2%": {},
                    },
                },
                "한편, 합병으로 피합병법인의 과밀억제권역 외 토지를 취득하였다가 합병일 이후 5년 이내에 해당 토 지에 건축물을 신축하여 해당 부동산이 지방세법 제13조 제5항의 과세물건에 해당되는 경우 취득세가 중 과되고, 합병으로 취득한 해당 토지는 방세특례제한법 제177조에 따라 취득세 감면대상에서 제외한다. ":{},
                "그리고, 지방세특례제한법 제57조의 2 제1항에 따라 법인 합병에 따른 취득세가 100% 면제되는 경우에도 2016.1.1.부터 최소납부세제가 적용되어 85%의 감면율(｢지방세법｣ 제13조 제1항부터 제 4항까지의 세율은 적용하지 아니한 감면율을 말함)이 적용된다. ":{},
                "지방세법 제15조【세율의 특례】제1항 제3호, 지방세특례제한법 제57조의 2【기업합병･분할 등에 대한 감면】, 지방세특례제한법 제177조【감면 제외대상】, 지방세특례제한법 제177조의 2【지방세 감 면 특례의 제한】을 종합적으로 적용한 결과는 다음과 같다. ":{},
            },
            '합병으로 인하여 취득한 과세물건에 대한 (구)지방세법과 현행지방세법의 과세내용 비교': {
                "법인의 합병으로 인하여 취득한 과세물건에 대한 (구)지방세법과 현행 지방세법의 과세내용을 비 교하면 다음과 같다":{},
                "첫째, (구)지방세법(2010.3.31 지방세법 전부개정 이전)에서는 법인의 합병으로 인하여 소멸법인 의 부동산 등을 존속하는 법인이 취득하는 경우 (구)지방세법 제110조 제4호의 규정에 의거 취득세 를 비과세하였고, 현행 지방세법 제15조 제1항 제3호에서는 ｢법인세법｣ 제44조 제2항 또는 제3항 에 해당하는 법인의 합병으로 인한 취득하는 경우에 한하여 중과기준세율(2%)을 차감한 특례세율을 적용하고 있다. ":{},
                "둘째, (구)지방세법에서는 법인합병으로 인하여 부동산 등기를 하는 경우에 종전의 회사를 흡수합 병하면서 그 지점을 소속만 합병회사의 지점으로 바꾸어 유지･존속한 것은 (구)지방세법 제138조 제 1항 제3호 후단에서 규정하는 대도시 내에서의 지점 설치에 해당하여 등록세를 중과(대법2008두 969, 2008.03.27)하였고, 현행 지방세법 제15조 제1항 단서에서는 지방세법 제15조 제1항 각 호 외의 부분 본문의 계산방법으로 산출한 세율의 100분의 300을 적용하여 (구)등록세 상당액을 중과 하고 있다.":{},
                "셋째, (구)지방세법 제110조 제4호에서는 법인의 합병에 의하여 취득하는 때에는 형식적인 취득으 로 보아 그 취득세를 비과세 하였지만, 이 경우에도 지방세법상 사치성 재산인 별장, 고급오락장, 고급주택 등에 대하여는 비과세하지 않았다. ":{
                    "그러나, 합병으로 인하여 존속하는 법인이 취득하는 소멸 법인소유의 과세물건 중 사치성재산으로서 합병 전부터 중과세대상에 해당하는 물건인 경우에는 취득세는 중과되지 않는 것으로 해석하였다":{},
                },
            },
            '일반기업 합병시 취득세와 관련된 지방교육세 검토': {},
            '일반기업 합병시 취득세와 관련된 농어촌특별세 검토': {},
            '합병에 따른 취득세 감면 적용시 지방세특례제한법 보칙 검토사항': {},
            '합병이 종전에 감면받은 취득세에 미치는 영향에 대한 검토': {},
            '합병로 취득한 재산에 대한 취득세 검토사례': {},
        }
적격분할취득세감면={
            '법인의 분할로 인하여 취득하는 재산의 과세표준': {},
            '법인의 분할로 인하여 취득한 과세물건에 적용하는 취득세율': {},
            '법인의 분할로 인하여 취득한 괴세물건에 대한 취득세 중과여부 판단': {},
            '법인의 분할로 인하여 취득하는 재산에 대한 취득세 감면 검토': {},
            '법인 분할시 취득세와 관련된 지방교육세 검토': {},
            '법인 분할시 취득세와 관련된 농어촌특별세 검토': {},
            '법인 분할에 따른 취득세 감면 적용시 지방세특례제한법 보칙 검토사항': {},
            '법인 분할이 종전에 감면받은 취득세에 미치는 영향에 대한 검토': {},
            '법인 분할로 취득한 재산에 대한 취득세 검토사례': {},
        }
취득세감면개별사항={
        '법인전환으로 취득한 사업용고정자산에 대한 취득세 감면 검토(지특법 57조의2제4항)':법인전환취득세감면,
        '사업시행자외의 자가 산업단지 등에서 취득하는 부동산에 대한 감면검토(지특법 78조4항)':사업시행자외의자산업단지감면 ,
        '물류단지에서 취득하는 물류사업용부동산 취득세 감면검토(지특법 71조 2항)':물류사업용부동산취득세감면 ,
        '기업부설연구소용 부동산 취득에 대한 취득세감면검토(지특법46조)': 기업부설연구소용부동산취득세감면,
        '창업중소기업 및 창업중소벤처기업의 부동산취득에 대한 취득세 감면검토(지특법58조의 제1항)':창업중소기업부동산취득세감면 ,
        '적격합병으로 취득하는 재산에 대한 취득세감면검토(지특법57조의2제1항)': 적격합병취득세감면,
        '적격분할로   취득하는 재산에 대한 취득세감면검토(지특법57조의2제3항2호)': 적격분할취득세감면,
    }
_= {
    '취득세 감면 실무 가이드':{},
    '지방세 감면 일반':지방세감면일반 ,
    '취득세 감면 공통사항 검토': 취득세감면공통사항,
    '취득세 감면 개별 검토': 취득세감면개별사항,
}
#___________________________________________________
제목='취득세감면'
tax=_
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=제목)
        self.SetSize(420,320*2)
        self.mainPanel=wx.Panel(self)
        self.expandButton=wx.Button(self.mainPanel,label='펼침')
        self.tree=wx.TreeCtrl(self.mainPanel)
        root=self.tree.AddRoot(제목)
        for i in tax:
            ii=self.tree.AppendItem(root,i)
            for j in tax[i]:
                jj=self.tree.AppendItem(ii,j)
                for k in tax[i][j]:
                    kk=self.tree.AppendItem(jj,k)
                    for m in tax[i][j][k]:
                        mm=self.tree.AppendItem(kk,m)
                        for n in tax[i][j][k][m]:
                            nn=self.tree.AppendItem(mm,n)
                            for p in tax[i][j][k][m][n]:
                                pp=self.tree.AppendItem(nn,p)
                                for q in tax[i][j][k][m][n][p]:
                                    qq=self.tree.AppendItem(pp,q)
                                    for r in tax[i][j][k][m][n][p][q]:
                                        rr=self.tree.AppendItem(qq,r)

        self.staticText =wx.TextCtrl(self.mainPanel,style=wx.TE_MULTILINE)


        self.vtBoxSizer=wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton,0,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.tree        ,5,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.staticText  ,0,wx.EXPAND|wx.ALL,5)


        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON          ,self.OnExpandButton,self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnNodeSelected,self.tree)
    def OnExpandButton(self,e):
        self.tree.ExpandAll()
    def OnNodeSelected(self,e):
        selected=self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________