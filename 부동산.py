# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
import 토지, 주택, 농지, 건물, 부동산에관한권리
양도소득세_비과세={
    '주택': 주택.양도소득세_비과세,
    '농지': 농지.양도소득세_비과세,
}
양도소득세_감면={
    '주택': 주택.양도소득세_감면,
    '농지': 농지.양도소득세_감면,
    '공익사업 지원을 위한 조세특례':{
        '공익사업용 토지 등에 대한 양도소득세감면(조특법77조)': {
            '적용대상': {},
            '연도별 감면율': {},
            '지정전 사업시행자에게 양도하는 경우': {},
            '상속 또는 배우자 등 이월과세의 취득시기': {},
            '채권의 범위': {},
            '토지수용의 범위': {},
            '공익사업의 범위': {},
            '공익사업 등의 적용 사례': {},
            '감면신청자 및 기한 등': {},
            '감면세액의 추징 등': {},
            '위반사실의 국세청 통보방법 등': {},
        },
        '대토보상에대한 양도소득세 과세특례(조특법 77조의2)': {
            '적용대상': {},
            '적용방법': {},
            '감면 또는 과세이연받은 세액의 추징 등': {},
            '감면 또는 과세이연 신청': {},
            '고가주택 수용시 대토보상 과세이연방법': {},
        },
        '개발제한구역지정에따른 매수대상 토지등에대한 양도소득세의 감면(조특법77조의3)': {
            '적용대상': {},
            '상속받은 토지 등의 취득시기': {},
            '감면신청 등': {},
        },
        '박물관 등의 이전에 대한 양도소득세 과세특례(조특법83조)': {
            '감면요건': {},
        },
        '행정중심복합도시,혁신도시 개발예정지구 내 공장의 지방이전에 대한 과세특례': {},
        '어린이집용 토지 등의 양도차익에 대한 과세특례': {},
        '공익사업을 위한 수용 등에 따른 공장이전에대한 과세특례(조특법85조의7)': {},
        '중소기업의 공장이전에 대한 과세특례(조특법85조의8)': {},
        '공익사업을 위한 수용등에 따른 물류시설이전에대한 과세특례(조특법85조의9)': {},
        '국가에 양도하는 산지에 대한 양도소득세의 감면(조특법85조의10)': {},
        '산업단지 개발사업 시행에 다른 양도소득세 과세특례': {},
        '공익사업 지원을 위한 조세특례 요약': {},
    },
    '기업구조조정지원을 위한 조세특례 등': {
        '중소기업간의 통합에 대한 양도소득세의 이월과세(조특법31조)': {
            '적용대상': {},
            '중소기업간 통합의 범위': {},
            '사업용 고정자산의 범위': {},
            '이월과세 적용신청': {},
            '이월과세 적용대상 자산의 취득가액 산정': {},
            '잔존가액의 기간 승계': {},
            '미공제세액의 승계': {},
            '이월된 양도소득세 추징': {},
        },
        '법인전환에대한 양도소득세의 이월과세(조특법32조)': {
            '적용대상': {},
            '사업양수도방법': {},
            '신설법인의 자본금의 범위': {},
            '이월과세 적용신청': {},
            '이월과세 적용대상 자산의 취득가액 산정': {},
            '남은 감면기간의 승계 및 미공제세액의 승계': {},
            '이월된 양도소득세 추징': {},
        },
        '구조조정대상 부동산 취득자에 대한 양도소득세의 감면 등(조특법43조)': {},
    },
}
양도소득세={
    '부동산_양도소득세_비과세':양도소득세_비과세,
    '부동산_양도소득세_감면':양도소득세_감면,
}
부동산={
    '부동산_양도소득세':양도소득세,
}