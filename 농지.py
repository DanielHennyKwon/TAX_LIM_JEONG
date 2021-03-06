# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현

양도소득세_비과세={ # 양도소득세
    '개요:농지 등에 대한 비과세':{ },
    '농지의 교환 분합시 비과세(소법 89조)':{
        '교환 또는 분합의 정의': {},
        '교환 또는 분합의 비과세 범위': {},
        '농지소재지의 범위': {},
        '편입농지(비과세 제외)': {},
        '새로운 농지 취득 후 3년 내 수용된 경우': {},
        '농지 교환,분합 및 대토 후 수용시의 경작기간 통산 여부': {},
        '사업소득자 등의 경작기간 계산': {},
        '새로운 농지 취득 후 3년 내 사망한 경우': {},
        '미등기양도 제외 농지': {},
    },
}
양도소득세_감면한도={}
양도소득세_감면={ # 양도소득세
    '개요:농지 등에 대한 감면':{ },
    '자경농지에 대한 양도소득세 등의 감면(조특법69조)':{
        '자경농지의 감면요건': {
            '감면 요건': {},
            '거주 및 경작의 범위': {},
            '주거지역 등에 편입된 농지(감면 제외)': {},
            '주거지역 등에 편입된 농지의 감면소득': {},
            '양도일 현재의 농지 판정기준': {},
            '농지의 범위': {},
            '자경농지의 확인서류': {},
            '감면신청 및 제출기한': {},
            '미등기양도 제외 농지': {},
        },
        '자경기간의 계산': {
            '일반적인 농지': {},
            '상속받은 농지': {},
            '사업소득 등의 자경기간 계산': {},
            '증여받은 농지': {},
            '환지된 농지': {},
            '교환된 농지': {},
            '농지 교환,분합 및 대토 후 수용시의 경작기간 통산 여부': {},
            '농지를 점유 취득한 경우': {},
            '재산분할청구로 소유권이전된 농지의 경작기간': {},
            '이혼시 취득한 농지에 대한 자경기간': {},
        },
        '요약': {
            '8년 자경 농지 요약': {},
            '농지의 비과세 및 감면 요약': {},
            '기타 농지 등의 감면 요약': {},
        },
        "8년 자경의 감면한도":{},
    },
    '농지의 대토의 감면(조특법70조)':{
        '감면 요건':{},
        '거주자의 범위': {},
        '자경의 범위': {},
        '대토 요건': {},
        '새로운 농지 취득후 4년내 수용되는 경우': {},
        '농지 교환,분합 및 대토 후 수용시의 경작기간 통산 여부': {},
        '사업소득자 등의 경작기간 계산': {},
        '종전농지와 새로운 농지의 경작기간 계산': {},
        '새로운 농지 취득 후 합산하여 8년이 지나기 전에 사망한 경우의 통산 여부': {},
        '주거지역 등에 편입된 농지(감면 제외)': {},
        '주거지역 등에 편입된 농지의 감면소득': {},
        '농지의 범위': {},
        '자경농지 확인 서류': {},
        '세액감면신청 및 신고기한': {},
        '경작기간의 의미': {},
        '재산분할청구로 소유권이전된 대토농지의 경작기간': {},
        '농지대토의 추징': {},
        '미등기양도제외 농지': {},
        "농지대토의 감면 한도":{},
    },
    '경영회생지원을 위한 농지매매 등에 대한 과세특례(조특법70조의2)':{
        '환급 요건': {},
        '재양도시 취득가액 및 취득시기': {},
        '환급신청 등': {},
        '재양도시 임차기간 내 경작한 기간의 감면 적요방법 등': {},
    },
    '축사용지에 대한 양도소득세 감면(조특법69조의2)':{
        '감면요건':{},
        '거주자의 범위': {},
        '축산의 범위': {},
        '편입축사(감면 제외)': {},
        '양도일 현재의 축사용지 판정기준': {},
        '축산에 사용한 기간의 계산': {},
        '사업소득자 등의 축산기간 계산': {},
        '폐업의 확인 방법': {},
        '감면세액의 산출': {},
        '주거지역 등에 편입된 축사용지의 감면소득': {},
        '감면세액의 추징': {},
        '세액감면신청 및 신고기한': {},
    },
    '어업용 토지에 대한 양도소득세 감면(조특법69조의3)':{
        '감면요건': {},
        '어업인의 범위': {},
        '어업용 토지 등의 범위': {},
        '주거지역 등에 편입된 어업용 토지 등(감면 제외)': {},
        '양도일 현재의 어업용 토지 등 판정기준': {},
        '양식 등 사용한 기간의 계산': {},
        '주거지역 등에 편입된 어업용 토지 등의 감면소득': {},
        '어업용 토지 등의 확인서류':{},
        '감면세액 신청': {},
        '양식 등에 사용한 기간의 계산': {},
    },
    '자경산지에 대한 양도소득세 감면(조특법69조의4)':{
        '감면요건': {},
        '임업인의 범위': {},
        '임업용 산지의 범위': {},
        '주거지역 등에 편입된 임업용 토지 등(감면 제외)': {},
        '자경산지의 범위': {},
        '양도일 현재 산지의 판정기준':{},
        '임업에 사용한 기간의 계산': {},
        '주거지역 등에 편입된 산지 등의 감면소득': {},
        '자경산지의 확인서류': {},
        '감면세액 신청': {},
        '산지에 사용한 기간의 계산': {},
    },
    '기타 농지 등에 대한 양도소득세 면제': {
        '영농조합법인에 농지 등을 현물출자 함에 따른 양도소득세의 감면': {
            '적용요건': {},
            '추징': {},
            '이자상당액': {},
            '세액감면신청': {},
        },
        '영농조합법인에 농작물생산업 등에 직접 사용되는 부동산을 현물출자시 이월과세': {
            '적용요건': {},
            '추징': {},
            '이자상당액': {},
            '이월과세 적용신청': {},
        },
        '영어조합법인 등에 어업용 토지 등을 현물출자 함에 따른 양도소득세의 감면': {
            '적용요건': {},
            '추징': {},
            '이자상당액': {},
            '세액감면신청': {},
        },
        '농업회사법인에 농지 등을 현물출자함에 따른 양도소득세의 감면': {
            '적용요건': {},
            '추징 등 준용': {},
        },
        '농업회사법인에 농작물생산업 등에 직접 사용되는 부동산을 현물출자시 이월과세': {
            '적용요건': {},
        },
    },
}
증여세_감면한도={
    '영농자녀의 증여세 감면한도':{},
}
증여세_감면={
    '영농자녀 등이 증여받는 농지 등에 대한 증여세의 감면':{
        '감면 요건': {},
        '5년 내 양도시 증여세 추징 등': {},
        '영농기간의 계산': {},
        '증여받은 농지를 제3자에게 양도한 경우의 양도차익': {},
        '상속세 과세가액 합산 배제': {},
        '증여세 과세가액 합산 배제': {},
        '감면신청기한': {},
        '감면소득 구분계산': {},
        '동시에 2필지 이상 증여받은 경우의 순위 신청': {},
    },
}
농지={
    '농지_양도소득세_비과세':양도소득세_비과세,
    '농지_양도소득세_감면':양도소득세_감면,
    '농지_양도소득세_감면한도':양도소득세_감면한도,
    '농지_증여세_감면':증여세_감면,
    '농지_증여세_감면한도':증여세_감면한도,
}
