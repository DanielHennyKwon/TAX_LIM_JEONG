# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import wx

import 농어촌특별세법
import 농어촌특별세법시행령
import 법인세법
import 법인세법시행령
import 부가가치세법
import 부가가치세법시행령
import 상법
import 상속세및증여세법
import 상속세및증여세법시행령
import 소득세법
import 소득세법시행령
import 조세특례제한법
import 조세특례제한법시행령
import 지방세법
import 지방세특례제한법
import 지방세특례제한법시행령
import 취득세감면
import 합병및분할등에관한특례

합병보고서={
    "주식회사 00 대표이사 귀하":{},
    "지성회계법인은 귀사의 의뢰에 의하여 합병에 대한 분석을 한 결과 다음과 같은 평가의견서를 제시 합니다.":{},
    "I. 구조조정의 의의 ":{
        "기업은 새로운 가치창출을 위해 존재하고 그 성장을 거듭한다.":{},
        "이러한 목적을 달성하기 위해 기업은 새로운 경영자원을 동원하고, 동원된 자원을 유기적으로 결합하여 새로운 가치 창출에 활용한다. ":{},
        "반면에 기업이 동원한 경영자원들이 더 이상의 새로운 가치를 창출하지 못한다면 그러한 자원의 결합관계는 지속될 수 없다. ":{},
        "이와 같이 기업안에 결합된 경영자원을 분해하고 재배치하는 과정을 구조조정이라고 한다.":{},
        "그러나, 과거 규제과잉 속에서 차입금 조달을 통해 기업규모를 확대하고 무분별한 중복투자 등을 통해서 외형극대화 전략을 추구하여 온 국내 기업은 비효율적인 자본투자와 높은 금융비용 부담 등으로 인해서 경쟁력이 아주 약화되어 있으므로 기업의 효율개선 (경쟁력 강화)을 위한 노력이 필요하다. ":{},
        "즉 과거의 외형성장목표에서 내실위주의 경영 패러다임으로 전환필요하며 기업가치의 극대화(주주 가치의 극대화)를 기업경영의 목표로 해야 한다. ":{},
        " 기업들은 구조조정을 통한 고질적인 문제인 고비용. 저효율 개선을 위해 노력하고 있으나 효율성 증대는 상당한 시간과 비용, 노력의 투여가 요구됨으로 해서 상대적으로 손쉬운 비용절감(임금삭감, 인원감축 등)에 역점을 두어 오고 있다. ":{},
        "그런, 효율성의 개선이 없이는 기업경쟁력의 향상은 있을 수 없으므로 차별적 핵심역량이 없는 사업분야에의 투자나 사업규모 확장을 그치고 남보다 확실히 잘할 수 있는 사업에 선별적으로 집중 투자 필요 (선택과 집중) 필요하다. ":{},
        " 이처럼 구조조정은 경제여건의 변화에 따라 경쟁력이 떨어지는 산업은 도태 시키고 고부가가치 산업을 중심으로 산업구조가 고도화되는 과정을 말하며 기업이 사업재편을 통해서 핵심역량을 집중하고 재무구조를 개선하거나 리엔지니어링 및 규모축소를 통해서 원가를 절감하여 기업의 경쟁력을 강화하려는 노력을 의미한다. ":{},
        "구조조정을 위해서 기업은 자산매각, 정리해고, 조직개편, 사업정리, 분사 등 다양한 의사결정을 내리게 되며 이중에서 기업은 자신의 현재 기업상황에 맞는 전략을 선택하게 된다. ":{},
    },
    "II. 구조조정의 방법":{
        "기업의 사업구조 개편은 방향으로는 합병.인수, 사업 맞교환, 퇴출전략, 자산매각, 벤처투자, 전략적 투자와 제휴 등 여러 가지가 있으며 이는 주변환경과 기업이 처한 특성과 상황에 따라 전략적으로 전개해야 한다. ":{
            "① 도입, 성장기에 있는 사업 또는 제품에 투자하여 기업의 연령을 낮추고 활력을 불어넣어 성장을 계속할 수 있는 기반을 확보 : 신규사업진출": {},
            "② 동종의 타기업이나 계열사를 합병하여 시너지 효과를 창출 : 합병전략": {},
            "③ 기업간 비교우위 사업부분을 교환하여 핵심역량을 갖춘 사업부문에 집중하거나 핵심업종을 전문화하고 육성 : 사업맞교환 (big deal) ": {},
            "④ 특정 사업부문을 매각하거나 기업전체를 매각 : 매각전략": {},
            "⑤ 기업을 몇 개로 분할하여 슬림화와 효율성 제고 : 기업 분할전략 ": {},
            "⑥ 타사와의 협력관계를 구축하여 자사능력의 한계를 극복하고 공동의 목표를 달성 : 전략적 제휴": {},
            "⑦ 기업을 몇 개로 분할하여 슬림화와 효율성 제고 : 기업 분할전략": {},
        },
        "일반적으로 기업구조조정은 기업의 지분보유율과 지분의 매각상대에 따라서 다음과 같이 분류할 수 있습니다.":{
            "① 기존의 회사내부에서 기업지배구조를 미세 조정 : 사내분사, 제한주식 발행":{},
            "② 기업의 주식 처분: Spin-off, Split-off, Split-up, Equity Carve-out 등":{},
            "③ 기업을 확장하거나 축소 : M&A, 합작투자 ":{},
        },
    },
    "III. 합병전략을 통한 구조조정 ":{
        "세계산업계는 구조조정을 통하여 끊임없이 재편되어 왔으며 업체간 결합.협력을 통하여 업계지도가 변화를 거듭하여 왔습니다.":{},
        "현재 국내외의 시장환경은 아주 빠르게 변화하고 있으며 극심한 글로벌 경쟁상황에 있다. 이러한 상황하에는 한 기업이 구매, 생산, 판매, 기술 등 모든 면에서 최고의 경쟁력을 갖추는 것은 불가능하므로 타기업의 강점을 흡수하여 자신의 약점을 보완하여야 합니다.":{},
        "M&A는 이러한 면에서 기업의 구조조정을 위한 강력한 도구로서 M&A를 통해서 기업의 핵심역량을 강화하고 기업을 강한 체질로 만들 수 있습니다. ":{},
        "수평적 M&A":{
            "형태":{"동종업종간 결합":{},},
            "목적":{
                "생산설비의 효율적 활용":{},
                "규모의 경제":{},
                "제품생산 적정화":{},
                "유통망 중복 회피":{},
                "중복.노후시설 폐쇄":{},
                "재고량 감축":{},
            },
        },
        "수직적 M&A":{
            "형태":{"생산공정의 전후 또는 원료.생산.판매 관계의 결합":{},},
            "목적":{
                "생산흐름개선":{},
                "유통경로단축":{},
                "재고관리비용 절감 ":{},
            },
        },
        "복합적 M&A":{
            "형태":{"수평적,수직적 관계가 없음":{},},
            "목적":{
                "사업다각화":{},
            },
        },
        "구조재편":{
            "형태":{
                "자산매각":{},
                "회사분할":{},
                " LBO":{},
            },
            "목적":{
                "회사구조의 축소.단순화":{},
                "경영개선":{},
            },
        },
    },
    "IV. 합병 준비 절차":{
        "1. 합병 준비 절차의 목적":{
            "재무구조개선과 세무위험을 감소시키는 목적으로 합병을 추진하며 합병에 따른 잠재적인 위험요소를 고려하여 합병을 추진하는데 그 목적이 있습니다.":{},
        },
        "2. 재무상태 분석 및 합병비율 추정치":{
            "지난 20XX년 12월 31일 현재의 각 기업의 재무상황과 합병비율 추정치는 다음과 같습니다. (단위:억원)(주의:합병시 주식평가 재계산해야함)":{},
            "회사별 자산/부채/자본/순장부가액/순공정시가액 추정치/주식가치액 추정치/합병비율 추정치":{},

        },
        "3. 합병전 요구사항":{
            "주주변경":{},
            "사업목적을 모회사와 일치화":{
                "법인등기부등본, 사업자등록증상 사업목적을 모회사와 일치시키고 변경일로부터 1년 경과되어야 함":{},
            },
        },
        "4. 합병후 사후관리 및 처분손실 공제제한":{
            "① 합병등기일 사업연도 종료일 기준 3년이내 승계사업을 중지하거나 처분시 세액추징":{},
            "② 합병등기일 이후 5년 이내의 사업연도에 발생한 처분손실은 승계소득 범위내에서 손금 산입":{},
        },
        "5. 합병후 증자나 자산재평가 필요":{},
    },
    "V. 합병 절차-일반적인 경우":{
        "사전준비-외부평가의뢰":{},
        "이사회결의 및 합병계약-기업결합신고(계약후 30일 이내)":{},
        "합병신고서 제출":{},
        "1일 - 주주 명부 폐쇄기간 공고":{},
        "2주 - 주주명부 폐쇄 개시":{},
        "15일 - 주주총회 소집통지 발송(공고)-합병 대차대조표 공시":{},
        "2주 - 합병주주총회-채권자 이의제출공고/최고,-주주제출공고/통지":{},
        "1개월 - 합병기일":{},
        "보고주총 갈음 이사회/공고-본점(2주내),지점(3주내),-합병종료보고서제출":{},
        "합병등기":{},
        "1개월 - 신주권 교부":{},
    },
    "VI. 합병 절차와 법률":{
        "합병절차에 따른 제반법률은 다음과 같습니다.":{},
        "사전준비":{
            "당사회사간 협의":{
                "해당주체 : 합병법인,피합병법인": {},
            },
            "자산재평가":{
                "해당주체 : 피합병법인":{},
                "대상 : 2곳 이상의 감정평가법인":{},
                "비고 : 필요시,토지건물등에 대해 감정":{},
            },
            "합병비율적정성 외부 평가 의뢰":{
                "해당주체 : 비상장 합병법인,비상장 피합병법인": {},
                "대상 : 외부평가기관": {},
                "기한 : 결산후":{},
                "목적 : 증여세,법인세 부당행위계산부인 회피용": {},
            },
        },
        "합병계약":{
            "합병이사회 결의":{
                "해당주체 : 합병법인,피합병법인": {},
            },
            "합병계약 체결":{
                "해당주체 : 합병법인,피합병법인": {},
                "근거규정 ": {
                    "상법 제523조(흡수합병의 합병계약서)":상법.제523조,
                    "상법 제524조(신설합병의 합병계약서)":상법.제524조,
                },
            },
        },
        "합병실행/합병보고주총":{
            "주주총회 소집 이사회결의":{
                "해당주체 : 합병법인": {},
                "근거규정 ": {
                    "상법 제526조(흡수합병의 보고총회)": 상법.제526조,
                    "상법 제527조(신설합병의 창립총회)": 상법.제527조,
                },
            },
            "주주명부 폐쇄공고":{
                "해당주체 : 합병법인": {},
                "기한 : 폐쇄기간2주전": {},
                "근거규정 ": {
                    "상법 제354조(주주명부의 폐쇄, 기준일)": 상법.제354조,
                },
            },
            "주주명부 폐쇄개시":{
                "해당주체 : 합병법인": {},
                "기한 : 3월 이내": {},
                "근거규정 ": {
                    "상법 제354조(주주명부의 폐쇄, 기준일)": 상법.제354조,
                },
            },
            "합병기일":{
                "해당주체 : 합병법인,피합병법인": {},
                "근거규정 ": {
                    "상법 제523조(흡수합병의 합병계약서) 6. 합병을 할 날":상법.제523조,
                    "상법 제524조(신설합병의 합병계약서) 5. 제523조제5호 및 제6호에 규정된 사항":상법.제524조,
                },
            },
            "주주총회 소집통지발송(주총소집공고)":{
                "해당주체 : 합병법인": {},
                "기한 : 주주총회 2주전": {},
                "근거규정 ": {
                    "상법 제363조(소집의 통지)": 상법.제363조,
                },
            },
            "주주총회 개최":{},
        },
        "합병등기":{
            "변경등기 (존속회사)":{
                "해당주체 : 합병법인": {},
                "대상 : 등기소": {},
            },
            "해산등기 (소멸회사)":{
                "해당주체 : 피합병법인": {},
                "대상 : 등기소": {},
            },
            "기한 : - 본점: 보고총회후2주간이내- 지점: 보고총회후3주간이내": {},
            "근거규정 ": {
                "상법 제528조(합병의 등기)": 상법.제528조,
            },
        },
        "합병승인주총":{
            "주총소집 이사회결의":{
                "해당주체 : 합병법인,피합병법인": {},
            },
            "주주명부 폐쇄기간공고":{
                "해당주체 : 합병법인,피합병법인": {},
                "기한 : 폐쇄기간2주전": {},
                "근거규정 ": {
                    "상법 제354조(주주명부의 폐쇄, 기준일)": 상법.제354조,
                },
            },
            "주주명부 폐쇄개시":{
                "해당주체 : 합병법인,피합병법인": {},
                "기한 : 3개월 이내": {},
                "근거규정 ": {
                    "상법 제354조(주주명부의 폐쇄, 기준일)": 상법.제354조,
                },
            },
            "주총소집통지발송(공고)":{
                "해당주체 : 합병법인,피합병법인": {},
                "기한 : 주총2주전": {},
                "근거규정 ": {
                    "상법 제363조(소집의 통지)": 상법.제363조,
                },
            },
            "합병대차대조표공시":{
                "해당주체 : 폐쇄합병법인,피합병법인": {},
                "기한 : 주총2주전부터 합병후6월까지": {},
                "근거규정 ": {
                    "상법 제522조의2(합병계약서 등의 공시)": 상법.제522_02조,
                },
            },
            "합병반대의사통지마감":{
                "해당주체 : 합병법인,피합병법인": {},
                "기한 : 주총전까지": {},
            },
            "주총개최(승인결의)":{
                "해당주체 : 합병법인,피합병법인": {},
                "근거규정 ": {
                    "상법 제436조(준용규정)": 상법.제436조,
                    "상법 제522조(합병계약서와 그 승인결의)": 상법.제522조,
                },
            },
        },
        "채권자보호 절차":{
            "이의제출 공고.최고":{
                "해당주체 : 폐쇄합병법인,피합병법인": {},
                "대상 : 채권자":{},
                "기한 : 주총2주간내": {},
            },
            "이의제출기간완료":{
                "해당주체 : 폐쇄합병법인,피합병법인": {},
                "기한 : 1개월 이상": {},
            },
            "근거규정 ": {
                "상법 상법 제232조(채권자의 이의)": 상법.제232조,
                "상법 상법 제530조②(준용규)": 상법.제530조,
            },
        },
    },
    "VII. 합병 세무에 대한 법률과 과세 대상 ":{
        "합병시 합병회사는 잘못 합병할 경우에는 대상기업의 세금을 떠 안거나 과도한 세금으로 불이익을 초래할 수 있기 때문에 세법상의 문제는 없는지를 검토하는 것이 중요합니다. ":{},
        "합병대상기업이 선정되면 합병회사는 실사단계에서 그 기업의 매출추세, 예상손익, 자금흐름, 자산상태 등의 중요한 재무자료 뿐만 아니라 세무상의 문제도 사전에 검토해야 합니다.":{},
        "합병시 세금문제는 합병내용에 따라 차이가 날 수 있으나 주요 과세대상은 합병법인, 합병회사의 주주, 피합병법인, 피합병법인의 주주 등 입니다. ":{},
        "합병기업":{
            "법인":{
                "합병후 최초사업년도 중간예납":{
                    "법인세법 제63조(중간예납)":법인세법.제63조,
                },
                "비적격합병시 합병매수손익 세무처리":{
                    "법인세법 제44조의2(비적격 합병 시 합병법인에 대한 과세)": 법인세법.제44_02조,
                    "법인세법시행령 제80조의3(비적격합병 시 양도가액과 순자산시가와의 차액 처리)": 법인세법시행령.제80_03조,
                },
                "적격합병시 세무처리":{
                    "1.자산조정계정":{},
                    "2.이월결손금 등 승계":{},
                    "3.세무조정사항 승계":{},
                    "4.세액감면 공제 등":{},
                    "법인세법 제44조의3(적격 합병 시 합병법인에 대한 과세특례) 제1,2항": 법인세법.제44_03조,
                    "법인세법시행령 제80조의4(적격합병 과세특례에 대한 사후관리) 제1,2항": 법인세법시행령.제80_04조,
                },
                "적격합병의 사후관리":{
                    "1.세무조정사항 승계 배제":{},
                    "2.자산조정계정의 익금산입":{},
                    "3.공제받은 이월결손금의 익금산입":{},
                    "4.세액감면 공제 등의 배제":{},
                    "5.합병매수차익 등의 세무조정":{},
                    "법인세법 제44조의3(적격 합병 시 합병법인에 대한 과세특례) 제3,4항": 법인세법.제44_03조,
                    "법인세법시행령 제80조의4(적격합병 과세특례에 대한 사후관리) 제3,4항": 법인세법시행령.제80_04조,
                },
                "완전자회사의 사후관리 예외":{
                    "법인세법 제44조의3(적격 합병 시 합병법인에 대한 과세특례) 제5항": 법인세법.제44_03조,
                },
                "자산의 승계":{
                    "1.피합병법인의 자산,부채":{},
                    "2.합병에 따라 취득한 주식":{},
                    "법인세법 제44조의3(적격 합병 시 합병법인에 대한 과세특례) 제1항": 법인세법.제44_03조,
                    "법인세법시행령 제72조(자산의 취득가액 등) 제2항 제5호": 법인세법시행령.제72조,
                },
                "중복자산 처분시 법인세 분할과세":{
                    "조세특례제한법 제47조의4(합병에 따른 중복자산의 양도에 대한 과세특례) ": 조세특례제한법.제47_04조,
                    "조세특례제한법시행령 제44조의4(합병에 따른 중복자산의 양도에 대한 과세특례)": 조세특례제한법시행령.제44_04조,
                },
                "이월결손금 승계":{
                    "1.합병법인 이월결손금":{},
                    "2.피합병법인 이월결손금":{},
                    "3.승계받은 자산 처분손실 공제제한":{},
                    "법인세법 제45조(합병 시 이월결손금 등 공제 제한) 제1,2,3항 ": 법인세법.제45조,
                    "법인세법시행령 제81조(합병에 따른 이월결손금 등의 승계) 제2항": 법인세법시행령.제81조,
                },
                "세액감면 세액공제 승계":{
                    "법인세법시행령 제81조(합병에 따른 이월결손금 등의 승계) 제3항": 법인세법시행령.제81조,
                },
                "피합병법인의 납세의무 승계":{
                    "법인세법시행령 제85조의2(합병·분할에 따른 양도손익 등에 대한 납세의무)": 법인세법시행령.제85_02조,
                },
                "증권거래세":{
                    "조세특례제한법 제117조(증권거래세의 면제) 1항14호 ": 조세특례제한법.제117조,
                },
                "취득세,농어촌특별세,지방교육세":{
                    "지방세특례제한법 제57조의2(기업합병ㆍ분할 등에 대한 감면) 1항 ": 지방세특례제한법.제57_02조,
                    "농어촌별세법시행령법 제4조(비과세) 6항1호 ": 농어촌특별세법시행령.제4조,
                },
            },
            "주주":{
                "불공정합병에 대한 증여세 과세":{
                    "상속세및증여세법 제38조(합병에 따른 이익의 증여)": 상속세및증여세법.제38조,
                    "상속세및증여세법시행령 제28조(합병에 따른 이익의 계산방법 등)": 상속세및증여세법시행령.제28조,
                },
                "자기주식소각이익의 자본전입":{
                    "소득세법 제17조(배당소득) 제2항 제5호": 소득세법.제17조,
                    "법인세법 제16조(배당금 또는 분배금의 의제) 제3호": 법인세법.제16조,
                },
                "부당행위계산부인":{
                    "법인세법시행령 제88조(부당행위계산의 유형 등) 1항8호 가목": 법인세법시행령.제88조,
                    "법인세법시행령 제89조(시가의 범위 등) 5,6항": 법인세법시행령.제89조,
                },
            },
        },
        "피합병기업":{
            "법인": {
                "의제사업년도에 대한 법인세":{
                    "법인세법 제8조(사업연도의 의제) 제2항 ": 법인세법.제8조,
                },
                "비적격합병시 양도손익 과세":{
                    "법인세법 제44조(합병 시 피합병법인에 대한 과세) 제1항 ": 법인세법.제44조,
                    "법인세법시행령 제80조(합병에 따른 양도손익의 계산) ": 법인세법시행령.제80조,
                },
                "적격합병시 양도손익 과세이연":{
                    "법인세법 제44조(합병 시 피합병법인에 대한 과세) 제2,3항 ": 법인세법.제44조,
                    "법인세법시행령 제80조의2(적격합병의 요건 등)": 법인세법시행령.제80_02조,
                },
                "완전자회사의 양도손익 예외":{
                    "법인세법 제44조(합병 시 피합병법인에 대한 과세) 제3항 ": 법인세법.제44조,
                },
                "기부금한도 계산시 양도손익 예외":{
                    "법인세법 제24조(기부금의 손금불산입) 제2항 1호 ": 법인세법.제24조,
                },
                "토지등 양도소득에 대한 법인세":{
                    "법인세법 제55조의2(토지등 양도소득에 대한 과세특례)": 법인세법.제55_02조,
                },
                "부가가치세 확정신고,폐업신고 등":{
                    "부가가치세법시행령 제7조(폐업일의 기준)": 부가가치세법시행령.제7조,
                },
            },
            "주주":{
                "불공정합병에 대한 증여세 과세":{
                    "상속세및증여세법 제38조(합병에 따른 이익의 증여)": 상속세및증여세법.제38조,
                    "상속세및증여세법시행령 제28조(합병에 따른 이익의 계산방법 등)": 상속세및증여세법시행령.제28조,
                },
                "의제배당 소득에 대한 과세":{
                    "소득세법 제17조(배당소득) 제2항 제4호": 소득세법.제17조,
                    "소득세법시행령 제27조(의제배당의 계산) 제4항": 소득세법시행령.제27조,
                    "법인세법 제16조(배당금 또는 분배금의 의제) 제1항 3호": 법인세법.제16조,
                    "법인세법시행령 제12조(자본전입 시 과세되지 아니하는 잉여금의 범위 등) 제1항": 법인세법시행령.제12조,
                },
                "부당행위계산부인":{
                    "법인세법시행령 제88조(부당행위계산의 유형 등) 1항8호 가목": 법인세법시행령.제88조,
                    "법인세법시행령 제89조(시가의 범위 등) 5,6항": 법인세법시행령.제89조,
                },
            },
        },
    },
    "VIII. 합병의 진행절차와 합병세무 적용":{
        "1. 합병 절차 ":{},
        "2. 합병 비율 ":{},
        "3. 피합병법인의 세무(20XX년12월31일 기준)":{
            "법인":{
                "의제사업년도에 대한 법인세 :((1.1~합병등기일까지의 과세표준)-이월결손금)X법인세율 ":{},
                "비적격합병시 양도손익 과세 : 양도가액-순자산장부가액":{},
                "적격합병시 양도손익 과세이연 :양도손익 과세이연":{},
                "완전자회사의 양도손익 예외 : 선택가능하며 양도손익은 이월결손금에서 전액공제가능":{},
                "기부금한도 계산시 양도손익 예외 : 일반적으로 세무상 영향없음":{},
                "토지등 양도소득에 대한 법인세 : 비사업용토지,주택 등이 없다면 해당없음":{},
                "부가가치세 확정신고,폐업신고 등 : 해산등기일까지 피합병법인 부가가치세 신고 필요함":{},
            },
            "주주":{
                "불공정합병에 대한 증여세 과세 : 기존주주간의 지분율변화가 없다면 적용되지 않음":{},
                "의제배당 소득에 대한 과세":{},
                "부당행위계산부인":{},
            },
        },
        "4. 합병법인의 세무(20XX년12월31일 기준)": {
            "법인":{
                "합병후 최초사업년도 중간예납 : 특이한 문제 없음":{},
                "비적격합병시 합병매수손익 세무처리 : 순자산시가-양도가,음수이면 합병매수차손":{},
                "적격합병시 세무처리":{
                    "1.자산조정계정 : 순자산시가-순자산장부가(상각,양도시 익금산입)":{},
                    "2.이월결손금 등 : 승계":{},
                    "3.세무조정사항  : 승계":{},
                    "4.세액감면 공제 등 : 승계":{},
                },
                "적격합병의 사후관리 : 3년이내에 승계사업 폐지시 추징됨":{
                    "1.세무조정사항 승계 배제":{},
                    "2.자산조정계정의 익금산입":{},
                    "3.공제받은 이월결손금의 익금산입":{},
                    "4.세액감면 공제 등의 배제":{},
                    "5.합병매수차익 등의 세무조정":{},
                },
                "완전자회사의 사후관리 예외 ":{
                    "제44조 제3항에 따라 양도손익이 없는 것으로 한 경우 제44조 제2항 각 호의 요건을 갖추지 아니하더라도 합병법인은 피합병법인의 자산을 장부가액으로 양도받은 것으로 하여 제1항과 제2항을 적용한다. 이 경우 제3항과 제4항은 적용하지 아니한다. ->양도손익없이 인수시 사후관리적용받지 아니함":{},
                },
                "자산의 승계":{
                    "1.피합병법인의 자산,부채":{},
                    "2.합병에 따라 취득한 주식":{},
                },
                "중복자산 처분시 법인세 분할과세":{},
                "이월결손금 승계":{
                    "1.합병법인 이월결손금 : 해당없음":{},
                    "2.피합병법인 이월결손금 : 장부가액대로 승계,사업승계시 결손금승계":{},
                    "3.승계받은 자산 처분손실 공제제한 : 승계사업소득에서 공제":{},
                },
                "세액감면 세액공제 승계:	장부가액대로 승계,사업승계시 결손금승계":{},
                "피합병법인의 납세의무 승계	: 승계함":{},
                "증권거래세	":{},
                "2018년12월31일 이전 : 1.575%~4.55%":{
                    "취득세+농특세+지방교육게:합병등기일부터 3년 이내에 「법인세법」 제44조의 3 제3항 각 호의 어느 하나에 해당하는 사유가 발생하는 경우 :토지건물의 과세표준의3.5%(1+10%+20%)":{},
                    "취득세":{
                        "상기 사유 없이 사업승계(합병사업유지의 경우)-->토지건물의 과세표준의 *3.5%*15%":{},
                    },
                    "농어촌특별세:감면분의20%":{
                        "양도손익이 없을시:비과세":{},
                        "양도손익이 있을시:토지건물의 과세표준*3.5%*85%*20%":{},
                    },
                    "농어촌특별세:취득세의10%":{},
                    "지방교육세:취득세의20%":{},
                    "요약":{
                        "감면":{
                            "양도손익이 없을시:(3.5%*15%)+0++(3.5%*10%)+(3.5%*20%)=3.5%(15%+0+10%+20%)=1.575%": {},
                            "양도손익이 있을시:(3.5%*15%)+(3.5%*85%*20%)+(3.5%*10%)+(3.5%*20%)=3.5%*(15%+85%*20%+10%+20%)=2.17%": {},
                        },
                        "과세 : 3.5%*(1+10%+20%) = 4.55%":{},
                    },
                },
                "2019년 1월 1일 이후 : 4.55%":{
                    "취득세 : 토지건물의 과세표준의3.5%" : {},
                    "농어촌특별세:취득세의10%": {},
                    "지방교육세:   취득세의20%": {},
                    "계산 : 3.5%*(1+10%+20%)":{},
                },
            },
            "주주":{
                "불공정합병에 대한 증여세 과세 :	기존주주간의 지분율변화가 없다면 적용되지 않음":{},
                "자기주식소각이익의 자본전입":{},
                "부당행위계산부인":{},
            },
        },
    },
    "IX. 합병검토에 대한 결론":{
        "1. 합병의 결과 관계회사간 대여금과 차입금,투자유가증권과 자본금의 상계로 인하여  불필요한 세무상불이익인 지급이자 손금불산입사유가 대부분 해소되는 긍정적인 효과가 있습니다.":{},
        "2. 금융기관 대출시 충분한 담보제공으로 인해 이자율 인하를 촉구할 수 있습니다.":{},
        "3. 합병으로 인해 부실자산을 인수하게 되어 자기자본이 줄어드는 부정적인 효과를 초래하게 됩니다. 향후 이익의 달성과 합병후 6개월초과되는 시점에서 자산재평가를 통하여 자기자본의 확충을 통하여 자기자본의 건실화를 추구하여야 합니다.":{},
        "4. 합병소멸회사의 사업을 계속 유지하는 조건으로 세무상 혜택을 부여하고 있지만 합병소멸회사의 사업이 XXX,YYY로서 ZZZ와 차이가 있고 이의 주장을 하는 것이 쉽지 않습니다. 사업의 계속성을 판단할 때에 한국표준산업분류의 세분류를 기준으로 하고 있고 입법취지를 놓고 판단 하면 주장하기가 쉽지 않은 상황입니다. 이에 세무상의 위험성을 판단하면 가산세를 제외한 취득세 추정금액은 A억원으로 판단됩니다.":{},
        "5. 상기4번사항에도 불구하고 세법상 1년이상 운영한 사업을 기준으로 3년이상유지한다면이라는 법문구를 유리하게 해석하고 1년정도 YYY을 유지하고 난 후에 합병한다면 주장의 약한 근거는 있다고 사료되나 확신할 수는 없습니다.":{},
        "6. 합병시 최우선적으로 판단하는 합병비율산정에 있어서 토지,건물을 2군데이상의 감정평가법인을 선정하여 평균하는 것이 맞으나 합병일 기준 6개월내에 감정평가액이 없으면 보충적 평가방법인 공시지가와 국세청기준시가에 의해 평가할 수 있습니다. ":{},
        "7. BB에 건물을 매각하는 방안은 보유 토지건물을 감정평가법인2군데이상 감정받아 매각하고 그 대금은 외상매입금과 상계약정을 하면 문제가 없을 것으로 판단됩니다. 관련 유형자산처분이익에 대한 법인세(10%,20%)와 취득세5.2%는 별도로 납부하여야 할 것으로 사료됩니다.":{},
        "8. 대표이사 가지급금은 관계회사의 증자대금으로 인해 발생된 것으로서 향후 급여,퇴직금 등 합리적인 방안으로 빠른 시일내에 해소하여야 합니다.":{},
        "9. YY의 이월결손금은 엄밀히 말하면 과거 ZZ업종에서 발생한 결손금이므로 합병시 소멸하는 것으로 판단됩니다.":{},
        "10. 합병관련 비용은 다음과 같습니다.":{
            "합병취득세,농특세,지방교육세 :7,500만원":{
                "소소리635번지 과표 16억원 기준시 4.55%: 7,500만원":{},
            },
            "회계법인'합병자문수수료   800만원 ": {},
            "감정평가법인'감정평가수수료 250만원":{},
            "법무사'상업등기수수료 250만원":{},
            "기타 200":{},

            "합계 : 9천만원":{},
        },
    },
    "X. 합병 관련 법률":{
        "1. 상법":{
            "상법 제522조(합병계약서와 그 승인결의)":상법.제522조,
            "상법 제522조의2(합병계약서 등의 공시)":상법.제522_02조,
            "상법 제523조(흡수합병의 합병계약서)":상법.제523조,
            "상법 제526조(흡수합병의 보고총회)":상법.제526조,
            "상법 제527조의2(간이합병)":상법.제527_02조,
            "상법 제527조의3(소규모합병) ":상법.제527_03조,
            "상법 제527조의5(채권자보호절차)":상법.제527_05조,
            "상법 제527조의6(합병에 관한 서류의 사후공시) ":상법.제527_06조,
            "상법 제528조(합병의 등기)":상법.제528조,
            "상법 제527조의4(이사ㆍ감사의 임기)":상법.제527_04조,
        },
        "2.세법":{
            "합병기업":{
                "법인": {
                    "합병후 최초사업년도 중간예납": 법인세법.제63조,
                    "비적격합병시 합병매수손익 세무처리": {
                        "법인세법44조의2": 법인세법.제44_02조,
                        "법령80조의3": 법인세법시행령.제80_03조,
                    },
                    "적격합병시 세무처리": {
                        "1.자산조정계정": {},
                        "2.이월결손금 등 승계": {},
                        "3.세무조정사항 승계": {},
                        "4.세액감면 공제 등": {},
                        "법인세법44조의3제1,2항": 법인세법.제44_03조,
                        "법령80조의4제1,2항": 법인세법시행령.제80_04조,
                    },
                    "적격합병의 사후관리": {
                        "1.세무조정사항 승계 배제": {},
                        "2.자산조정계정의 익금산입": {},
                        "3.공제받은 이월결손금의 익금산입": {},
                        "4.세액감면 공제 등의 배제": {},
                        "5.합병매수차익 등의 세무조정": {},
                        "법인세법44조의3제3,4항": 법인세법.제44_03조,
                        "법령80조의4제3,4,8항": 법인세법시행령.제80_04조,
                        "법인세법113조3항": 법인세법.제113조,
                        "법인세법시행령156조2항": 법인세법시행령.제156조,
                    },
                    "완전자회사의 사후관리 예외:법인세법,제44_03조5항": 법인세법.제44_03조,
                    "자산의 승계": {
                        "1.피합병법인 자산,부채": {},
                        "2.합병에따라취득한 주식": {},
                        "법인세법44조의3제1항": 법인세법.제44_03조,
                        "법령72조1항5호": 법인세법시행령.제72조,
                    },
                    "중복자산 처분시 법인세 분할과세": {
                        "조특법47조의4": 조세특례제한법.제47_04조,
                        "조령44조의4": 조세특례제한법시행령.제44_04조,
                    },
                    "이월결손금 승계": {
                        "1.합병법인 이월결손금": {},
                        "2.피합병법인 이월결손금": {},
                        "3.승계받은 자산 처분손실 공제제한": {},
                        "법인세법45조1,2,3항": 법인세법.제45조,
                        "법령81조2항": 법인세법시행령.제81조,
                    },
                    "세액감면 세액공제 승계": {
                        "법령81조3항": 법인세법시행령.제81조,
                    },
                    "피합병법인의 납세의무 승계": {
                        "법인세법시행령85조의2": 법인세법시행령.제85_02조,
                    },
                    "증권거래세": {
                        "조세특례제한법117조1항14호": 조세특례제한법.제117조,
                    },
                    "취득세": {
                        "지방세특례제한법57조의2제1항": 지방세특례제한법.제57_02조,
                        "지방세법15조1항3호": 지방세법.제15조,
                        "지방세법11조": 지방세법.제11조,
                        "지방세법12조": 지방세법.제12조,
                        "지방세특례제한법177조의2": 지방세특례제한법.제177_02조,
                        "지방세특례제한법시행령28조의2제1항": 지방세특례제한법시행령.제28_02조,
                        "조세특례제한법 시행령제29조3항": 지방세특례제한법시행령.제29조,
                        "【문서번호】 지방세특례제도-1534, 2016.07.05. : 「지방세특례제한법」제177조의2에서 최소납부세제 적용에 대하여 “이 법에 따라 취득세 또는 재산세가 면제되는 경우”라고 규정하고 있어, 합병의 경우 같은 법 제57의2에 의해 산출된 과세표준액에 취득세율(1.5%)을 적용하여 산출한 세액에 대해 100분의 85에 해당하는 감면율을 적용하는 것이 타당함.": {},
                        "지방세법기본통칙11-1의2호 : 11-1【부동산 취득의 세율】2. 법인의 흡수합병으로 인하여 피합병법인의 부동산을 합병법인의 명의로 하는 소유권이전은「지방세법」 제11조 제1항 제2호의 규정에 의거 1,000분의 35의 세율이 적용된다. (2011. 7. 1. 제정)": {},
                    },
                    "농어촌특별세": {
                        "농어촌특별세법제5조1항1호,6호": 농어촌특별세법.제5조,
                        "농어촌특별세법제4조12호": 농어촌특별세법.제4조,
                        "농어촌특별세법시행령4조6항5호": 농어촌특별세법시행령.제4조,
                    },
                    "지방교육세": {
                        "지방세법 151조1항1호": 지방세법.제151조,
                    },
                },
                "주주": {
                    "불공정합병에 대한 증여세 과세": {
                        "상속세및증여세법38조": 상속세및증여세법.제38조,
                        "상속세및증여세법시행령28조": 상속세및증여세법시행령.제28조,
                        "상속세및증여세법  38-28-2【합병에 따른 이익의 증여】": {},
                    },
                    "자기주식소각이익의 자본전입": {
                        "소득세법17조2항5호": 소득세법.제17조,
                        "법인세법16조1항3호": 법인세법.제16조,
                    },
                    "부당행위계산부인": {
                        "법인세법시행령88조1항8호 가목": 법인세법시행령.제88조,
                        "법인세법시행령89조5,6항": 법인세법시행령.제89조,
                    },
                },
            },
            "피합병기업": {
                "법인": {
                    "의제사업년도에 대한 법인세 : 법인세법8조 2항 ": 법인세법.제8조,
                    "비적격합병시 양도손익 과세": {
                        "법인세법44조1항": 법인세법.제44조,
                        "법령80조": 법인세법시행령.제80조,
                    },
                    "적격합병시 양도손익 과세이연": {
                        "법인세법44조2,3항": 법인세법.제44조,
                        "법령80조의2": 법인세법시행령.제80_02조,
                    },
                    "완전자회사의 양도손익 예외:법인세법,제44조3항": 법인세법.제44조,
                    "기부금한도 계산시 양도손익 예외 : 법인세법24조1항1호":법인세법.제24조,
                    "토지등 양도소득에 대한 법인세 : 법인세법55조의2":법인세법.제55_02조,
                    "부가가치세 확정신고,폐업신고 등":{
                        "부가가치세법5조3항": 부가가치세법.제5조,
                        "부가령7조1항1호": 부가가치세법시행령.제7조,
                    },
                },
                "주주": {
                    "불공정합병에 대한 증여세 과세": {
                        "상속세및증여세법38조": 상속세및증여세법.제38조,
                        "상속세및증여세법시행령28조": 상속세및증여세법시행령.제28조,
                        "상속세및증여세법  38-28-2【합병에 따른 이익의 증여】": {},
                    },
                    "자기주식소각이익의 자본전입": {
                        "소득세법17조2항5호": 소득세법.제17조,
                        "법인세법16조1항3호": 법인세법.제16조,
                    },
                    "부당행위계산부인": {
                        "법인세법시행령88조1항8호 가목": 법인세법시행령.제88조,
                        "법인세법시행령89조5,6항": 법인세법시행령.제89조,
                    },
                },
            },
        },
    },
}
기업회계={
    "의의":{},
    "사업결합의 식별":{},
    "적용배제":{},
    "사업결합의 방법":{},
    "사업결합의 회계처리":{},
    "취득법의 절차":{},
    "잠정금액의 추후 조정":{},
    "단계적으로 이루어지는 사업결합":{},    
    "적격합병시 자산조정계정 발생-KIFRS적용":{},
    "비적격합병시 합병매수차손익 발생-KIFRS적용":{},
    "특수한 경우 합병시 세무조정-KIFRS적용":{},
}
과세체계={
    "합병당사자별 과세체계의 비교":{},
    "분할":{},
}
법인세={
    "합병분할과세체계":과세체계,
    "합병":{
        '합병법인에 대한 과세_합병시':{
            "비적격합병의 경우-비적격합병 시 합병법인에 대한 과세":{
                "합병매수차익":{},
                "합병매수차손":{},
            },
            "적격합병의 경우  -적격합병 시 합병법인에 대한 과세특례":{
                "장부가액으로의 양수":{},
                "자산조정계정":{},
                '적격합병 과세특례에 대한 사후관리':{},
            },
            "결손금과 자산,부채 등 세무조정사항의 승계":{
                "합병법인의 이월결손금":{},
                "적격합병":{
                    "제목:적격합병시 결손금 및 세액감면 등의 공제제한":{},
                    "합병법인이 승계한 피합병법인의 이월결손금":{
                        "승계결손금의 범위액":{},
                        "사업의 계속,폐지와 이월결손금의 익금산입 등":{},
                    },
                    "합병전 보유하던 자산의 처분손실의 손금산입":{},
                    "합병법인이 승계한 피합병법인의 세액공제,감면":{},
                    "조세특례제한법에 따른 합병시 이월결손금의 승계":{
                        "물류법인의 합병시 이월결손금의 승계":{},
                        "벤처기업의 합병시 이월결손금의 승계":{},
                    },
                },
                "비적격합병":{},
            },
            "익금산입":{
                "익금산입 사유":{},
                "익금산입액 및 방법":{},
            },
        },
        '피합병법인에 대한 과세_합병시':{
            '피합병법인의 양도손익':{},
            '적격합병 시 피합병법인에 대한 과세-적격합병에 대한 과세이연':{},
            '적격합병 시 부득이한 사유가 있는 경우':{},
            },
        },
    "분할":{        
        '분할법인 등에 대한 과세_분할시':{
            "개요":{},
            '분할법인 등의 양도손익-분할에 따른 양도손익의 계산':{},
            '적격분할 시 분할법인 등에 대한 과세-적격분할에 대한 과세이연':{},
            '적격분할 시 부득이한 사유가 있는 경우':{},
            },
        '물적분할시 분할법인에 대한 과세특례':{
            "개요":{},
            '손금산입:분할법인의 자산양도차익상당액 손금산입-압축기장충당금에 의한 손금산입 등':{},
            '익금산입':{},
            "적격물적분할시 자산부채 등 세무조정사항의 승계":{},
            },
        '분할신설법인 등에 대한 과세_분할시':{
            '비적격분할':{
                "분할신설법인 등에 대한 과세":{},
            },
            '적격분할':{
                "분할신설법인 등에 대한 과세특례":{},
                '적격분할 과세특례에 대한 사후관리':{},
            },            
            '분할신설법인이 승계한 이월결손금 등 공제 제한':{},
            '분할신설법인이 승계한 세액감면 또는 세액공제액의 적용':{},            
            },
        '분할 후 분할법인이 존속하는 경우의 과세특례':{ 
            "개요":{},
            "분할에 따른 양도손익의 계산":{},
            "적격분할에 대한 과세이연":{},
            "기타":{},
        },
        "적격분할시 결손금 및 세액감면 등의 공제 제한":{
            "분할합병시 분할합병의 상대법인의 이월결손금":{},
            "분할신설법인 등이 승계한 분할법인 등의 이월결손금":{
                "승계결손금의 범위액":{},
                "사업의 계속,폐지와 이월결손금의 익금산입 등":{},
            },
            "분할합병전 보유하던 자산의 처분손실의 손금산입":{},
            "분할신설법인 등이 승계한 분할법인 등의 세액감면,공제":{},
        },
        '합병·분할에 따른 양도손익 등에 대한 납세의무':{},
    },
    "합병및분할등에관한특례":합병및분할등에관한특례._,
}
지방세={
    "취득세감면":취득세감면.적격합병취득세감면,
}

#___________________________________________________
제목='합병분할'
_={
    #"지방소득세_법인세분 가산세": 지방소득세_법인세분,
    "기업회계":기업회계,
    "법인세":법인세,
    "합병 검토 보고서": 합병보고서,
    "지방세":지방세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"상속세":상속세,
    #"양도소득세":양도소득세,
    #"농어촌특별세":{},
}
tax=_
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=제목)
        self.SetSize(500,500)
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
                                        for s in tax[i][j][k][m][n][p][q][r]:
                                            ss = self.tree.AppendItem(rr, s)
                                            for t in tax[i][j][k][m][n][p][q][r][s]:
                                                tt = self.tree.AppendItem(ss, t)
                                                for u in tax[i][j][k][m][n][p][q][r][s][t]:
                                                    uu = self.tree.AppendItem(tt, u)
                                                    for v in tax[i][j][k][m][n][p][q][r][s][t][u]:
                                                        vv = self.tree.AppendItem(uu, v)
        self.staticText =wx.TextCtrl(self.mainPanel,style= wx.TE_MULTILINE)
        self.staticText.SetDefaultStyle(wx.TextAttr(wx.RED))
        self.vtBoxSizer=wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton,0,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.tree        ,5,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.staticText  ,5,wx.EXPAND|wx.ALL,5)
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
