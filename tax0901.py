# -*- coding: utf-8 -*-
#Created on 2021-7-10 @author: 권달현
import 가산세,가업승계
#___________________________________________________
제목='9-1 상속세'
tax={
    "9-1-1 상속세 총설": {
        "9-1-1-1 부의 무상이전에 대한 과세체계":{
            "상속세와 증여세는 부의 무상이전에 대해 부과되는 조세이다.":{
                "상속과 증여의 형태를 취하는데, 그 개념은 다음과 같다.":{},
            },
            "가. 부의 무상이전의 개념":{
                "(1) 상속":{
                    "상속이란 민법 상 다음과 같은 것을 포함한다.(상증법 2조1항)":{},
                    "1. 상속":{},
                    "2. 유증":{},
                    "3. 사인증여":{},
                    "4. 특별연고자에 대한 상속재산의 분여":{},
                    "5. 유언대용신탁":{},
                    "6. 수익자연속신탁":{},
                },
                "(2) 증여":{
                    "증여란 그 행위 또는 거래의 명칭,형식,목적 등과 관계없이 직접 또는 간접적인 방법으로 타인에게 무상으로 유형,무형의 이익을 이전하거나 타인의 재산가치를 증가시키는 것을 말한다.":{},
                    "이에는 현저히 낮은 대가를 받고 이전하는 경우를 포함한다.":{},
                    "다만, 유증,사인증여,유언대용신탁 및 수익자 연속신탁은 제외한다.(상증법 2조6항)":{},
                },
            },
            "나. 부의 무상이전의 유형":{},
            "다. 무상취득자의 구분에 따른 과세체계":{},
        },
        "9-1-1-2 상속세의 과세유형":{
            "가. 유산과세형":{
                "과세방법":{
                    "피상속인의 유산총액에 과세":{},
                    "공동산속의 경우에도 분할 전의 유산총액에 누진세율로 과세":{},
                },
                "세율이 적용되는 대상":{
                    "피상속인의 유산총액":{},
                },
                "납세의무자":{
                    "피상속인의 인격대표자(유언집행자 또는 유산관리인)":{},
                },
                "대표적인 입법례 : 미국,영국":{},
            },
            "나. 취득과세형":{
                "과세방법":{
                    "상속인의 유산취득가액에 각각 과세":{},
                    "공동상속의 경우 분할된 각 상속인의 유산취득가액에 각각 누진세율로 과세":{},
                },
                "세율이 적용되는 대상":{
                    "각 상속인이 취득한 유산가액":{},
                },
                "납세의무자: 각 상속인":{},
                "대표적인 입법례 : 독일,일본":{},
            },
        },
        "9-1-1-3 상속세의 과세대상":{
            "상속개시일 현재 상속재산에 대하여 상속세를 부과한다.":{},
            "상속개시일은 피상속인이 사망한 날 또는 실종선고일을 말한다.":{},
            "과세대상 범위는 피상속인이 거주자인 경우와 비거주자인 경우로 구분한다(상증법3조)":{},
        },
        "9-1-1-4 상속세의 납세의무자":{
            "가. 납부의무자 및 그 부담비율":{
                "상속인 또는 수유자는 상속재산중 각자가 받았거나 받을 재산을 기준으로 부담비율에 따라 계산한 금액을 상속세로 납부할 의무가 있다.(상증법3조의2제1항)": {},
                "상속인별 상속세의 부담비율은 다음과 같이 계산한다.(상증령3조1항)": {},
                "개정사항: 위탁자,수익자 사망과 연계한 신탁의 과세기준 명확화": {
                    "1. 유언대용신탁의 경우":{},
                    "2. 수익자연속신탁의 경우":{},
                },
            },
            "나. 상속인,수유자의 연대납세의무":{
                "상속세는 상속인 또는 수유자가 각자가 받았거나 받을 재산을 한도로 하여 연대ㅏ여 납부할 의무를 가진다.(상증법33조의2)":{},
            },
            "다. 수유자가 영리법인 경우":{
                "수유자 또는 특별연고자가 영리법인인 경우에는 그 영리법인은 상속세 납부의무자에서 제외한다.":{},
                "제도취지 : 영리법인을 이용한 변칙상속에 대한 상속세 과세강화":{},
            },
        },
        "9-1-1-5 상속세의 과세관할":{},
        "9-1-1-6 상속세의 계산구조":{
            "총상속재산가액":{
                "(-) 공과금": {},
                "(-) 장례비용": {},
                "(-) 채무": {},
                "(+)  증여재산 가산액": {},
            },
            "(=) 상속세 과세가액":{
                "(-) 상속공제(=인적공제+물적공제)": {},
                "(-) 감정평가수수료공제": {},
            },
            "(=)상속세 과세표준 ":{
                "(X) 세율(10%~50%)의 5단계 초과누진세율": {},
            },
            "(=) 상속세 산출세액":{
                "(-) 징수유예세액":{},
                "(-) 세액공제액":{},
            },
            "(=) 신고납부세액":{
                "(-) 연부연납세액":{},
                "(-) 물납세액":{},
            },
            "(=) 자진납부세액":{},
        },
    },
    "9-1-2 상속세 과세가액의 계산": {
        "계산구조":{
            "총상속재산가액":{
                "(=) 상속재산가액":{},
                "(+) 유증한 재산가액":{},
                "(+) 사인증여한 재산가액":{},
                "(+) 의제(추정) 상속재산가액":{},
            },
            "(-) 비과세재산가액":{
                "(=) 국가 등에 유증한 재산":{},
                "(+) 분묘에 속한 금양임야":{},
                "(+) 묘토인 농지 등":{},
            },
            "(-) 과세가액 불산입":{
                "(=) 공익법인 등에게 출연한 재산 등":{},
                "(+) 기타":{},
            },
            "(-) 공과금,장례비용,채무":{
                "상속재산가액에서 빼는 공과금,장례비용,채무의 금액이 상속재산가액을 초과하는 경우 그 초과액은 없는 것으로 본다(상증법13조1항 후단)":{},
            },
            "(+) 증여재산 가산액 : 피상속인이 상속개시일 이전 일덩한 기간 이내에 증여한 재산가액":{},
            "(=) 상속세과세가액":{},
        },
        "9-1-2-1 총상속재산가액":{
            "가. 상속재산의 범위":{
                "(=) 상속재산가액":{},
                "(+) 유증한 재산가액":{},
                "(+) 사인증여한 재산가액":{},
                "(+) 의제(추정) 상속재산가액":{},
            },
            "나. 상속의 의제":{
                "상속재산으로 보는 보험금":{},
                "상속재산으로 보는 신탁재산":{},
                "상속재산으로 보는 퇴직금":{},
                "상속재산으로 보는 퇴직수당":{},
                "상속재산으로 보는 공로금":{},
                "상속재산으로 보는 연금":{},
                "상속재산으로 보는 기타":{},
            },
            "다. 상속의 추정":{
                "1. 개요":{
                    "상증법 15조":{},
                    "피상속인이 피상속인의 재산을 처분하였거나 채무를 부담한 경우로서 다음에 해당하는 경우에는 이를 상속받은 것으로 추정하여 상속세 과세가액에 산입한다.":{},
                    "(1) 재산처분의 경우":{},
                    "(2) 채무부담의 경우":{},
                    "재산종류별이란 ":{},
                    "용도가 객관적으로 명백하지 않은 경우란":{},
                },
                "2. 상속세 과세가액에 산입할 금액":{},
            },
        },
        "9-1-2-2 상속세의 비과세":{
            "가. 전사자 등에 대한 비과세(상증법11조)":{},
            "나. 비과세되는 상속재산(상증법12조,상증령8조)":{},
        },
        "9-1-2-3 상속세 과세가액 불산입":{
            "가. 공익법인 등의 출연재산에 대한 상속세 과세가액 불산입(상증법16조1항)":{},
            "나. 공익신탁재산에 대한 상속세 과세가액 불산입(상증법17조1항)":{},
        },
        "9-1-2-4 공과금(상증령9조1항,상증칙1조)":{},
        "9-1-2-5 장례비용(상증령9조2항)":{
            "장례비용은 증빙서류가 없어도 최저 500만원을 인정한다.":{},
            "장례비용에 관한 증빙이 있다고 하더라도 최고 1천만원(봉안시설 등인 경우 1500만원)까지만 인정된다.":{},
        },
        "9-1-2-6 채무(상증령10조1항)":{},
        "9-1-2-7 증여재산 가산액(상증법13조)":{},
    },
    "9-1-3 상속세 과세표준의 계산": {
        "계산구조":{
            "() 상속세 과세가액":{},
            "(-) 상속공제":{
                "인적공제":{
                    "기초공제":{},
                    "그 밖의 인적공제":{},
                    "일괄공제":{},
                    "배우자 상속공제":{},
                },
                "물적공제":{
                    "가업상속공제":{},
                    "영농상속공제":{},
                    "금융재산상속공제":{},
                    "재해손실공제":{},
                    "동거주택상속공제":{},
                },
            },
            "(-감정평가수수료공제) ":{},
            "(=) 과세표준":{
                "과세최저한 50만원 미만":{
                    "상속세 과세표준이 50만원 미만이면 상속세를 부과하지 않는다(상증법25조2항":{},
                },
            },
        },
        "9-1-3-1 인적공제":{
            "가. 기초공제(상증법18조1항):2억원":{},
            "나. 배우자상속공제(상증법19조)":{
                "1. 개요":{},
                "2. 배우자상속공제의 최저한:5억원(상증법19조4항)":{},
                "3. 배우자 상속재산의 분할과 신고(상증법19조2,3항)":{},
                "4. 배우자 상속재산분할기한 연장":{},
                "5. 예제배우자상속공제":{},
            },
            "다. 그밖의 인적공제(상증법 20조1항)":{
                "1. 자녀공제: 자녀1인당 5천만원":{},
                "2. 미성ㄴ녀자공제":{},
                "":{},
                "":{},
                "":{},
                "":{},
            },
            "라. 일괄공제(상증법 21조1항)":{},
        },
        "9-1-3-2 물적공제":{},
        "9-1-3-3 상속공제의 종합한도":{},
        "9-1-3-4 감정평가수수료공제":{},
    },
    "9-1-4 상속세액의 계산": {
        "9-1-4-1 상속세 산출세액":{},
        "9-1-4-2 문화재자료 등에 대한 징수유예":{},
        "9-1-4-3 증여세액공제":{},
        "9-1-4-4 외국납부세액공제":{},
        "9-1-4-5 단기 상속재산에 대한 세액공제":{},
        "9-1-4-6 신고세액공제":{},
    },
    "9-1-5 상속세의 납세절차": {
        "9-1-5-1 상속세의 신고":{},
        "9-1-5-2 상속세의 납부":{},
        "9-1-5-3 연부연납":{},
        "9-1-5-4 물납":{},
        "9-1-5-5 상속세의 결정":{},
        "9-1-5-6 상속세의 갱정":{},
        "9-1-5-7 가산세":가산세.tax,
    },
}


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