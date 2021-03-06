# -*- coding: utf-8 -*-
#권달현 2019-1-1
import 일반기업회계기준제06장,일반기업회계기준제23장
import KIFRS_1021,KIFRS_1039
import 법인세법,법인세법시행령

기업회계_환율변동효과={
        "요약":{
                "화폐성 외화항목":{
                        "환산방법 : 마감환율로 환산" :{},
                        "외환차이(외화환산손익)의 회계처리 : 당기손익으로 인식": {},
                },
                "역사적원가로 측정하는 비회폐성 외화항목" :{
                        "환산방법 : 거래일의 환율로 환산" :{},
                        "외환차이(외화환산손익)의 회계처리 : 외환차이(외화환산손익)가 발생하지 않음": {},
                },
                "공정가치로   측정하는 비회폐성 외화항목": {
                        "환산방법 : 공정가치가 결정된 날의 환율로 환산": {},
                        "외환차이(외화환산손익)의 회계처리 : 공정가치평가손익을 당기손익(또는 기타포괄손익)으로 인식하면 외환차이도 당기손익(또는 기타포괄손익)으로 인식": {},
                },
        },
        "국제회계기준":KIFRS_1021.환율변동효과,
        "일반기업회계기준":일반기업회계기준제23장.환율변동효과,
        "기준간 비교":{},
        "외화환산방법":{},
        "해외사업장의 환산방법":{},
        }
기업회계_파생상품거래={
        "요약":{},
        "국제회계기준":KIFRS_1039.파생상품,
        "일반기업회계기준":일반기업회계기준제06장.금융자산금융부채,
        "기준간 비교":{},
        }
기업회계={
        "기업회계상 환율변동효과":기업회계_환율변동효과,
        "기업회계상 파생상품거래":기업회계_파생상품거래,
}
법인세={
        "외화자산 부채의 평가 및 상환차손익 ": {

                "종전 은행 등 금융회사가 보유하는 외화자산 부채 및 통화선도 통화스왑에 대하여만 평가손익을 인식하도록 규정하였으나,": {},
                "－ 2011.1.1.이후 최초로 개시하는 사업연도 분부터는 은행 등 금융회사의 경우 화폐성 외화자산 부채, 통화선도 통화스왑에 대하여 ": {},
                "☞ 2012.1.1. 이후 개시하는 사업연도 분부터는 일반형 환변동보험을 추가함 ": {},
                "－ 금융회사 이외의 법인은 화폐성 외화자산 부채, 화폐성 외화자산 부채의 환위험을 회피하기 위한 통화선도 통화스왑에 대하여 평가손익을 인식할 수 있도록 허용하였습니다(법령§73, 2010.12.30. 개정). ": {},

                "☞ 금융회사 이외 법인의 경우 회계상 헷지대상자산의 평가손익과 헷지거래손익이 상쇄되는 경우에도 세법상 평가손익이 부인되어 거래손익만 인식되므로 세부담이 발생하는 문제점 개선 ": {},
                "외화자산의 평가방법 ": {},
                "- 은행 등 금융회사：①, ② 중 선택 ": {},
                "구 분 화폐성 외화자산 부채 통화선도 스왑 ": {},
                "① 평가 ○ 평가 ×": {},
                "② 평가 ○ 평가 ○ ": {},
                "- 비은행 일반법인：①, ② 중 선택": {},
                "구 분 화폐성 외화자산 부채 헷지목적의 통화선도 스왑": {},
                "① 평가 × 평가 ×": {},
                "② 평가 ○ 평가 ○ ": {},

                "  평가차손익": {},
                "- 화폐성외화자산 부채, 통화선도 통화스왑 및 환위험회피용 통화선도  통화스왑을 평가함에 따라 발생하는 평가한 원화금액과 원화가장액의 차익 또는 차손은 해당 사업연도의 익금 또는 손금에 산입합니다(법령§76④).": {},
                "- 이 경우, 통화선도 통화스왑 및 환위험회피용 통화선도 통화스왑의 계약 당시 원화기장액은 계약의 내용 중 외화자산 및 부채의 가액에 계약체결일의 매매기준율 등을 곱한 금액을 말합니다.": {},
                "  금융기관 등이 보유하는 통화선도 통화스왑을 사업연도 종료일 현재의 매매기준율 등으로 평가하고자 하거나,": {},
                "- 금융회사 등 외의 법인이 보유하는 화폐성외화자산 부채와 환위험회피용 통화 선도 통화스왑을 사업연도 종료일 현재의 매매기준율 등으로 평가 하고자 할경우에는 - 최초로 동 평가방법을 적용하려는 사업연도의 법인세 신고와 함께 ‘화폐성 외화 자산등평가방법신고서’ 및 ‘외화자산등 평가차손익조정명세서’를 관할 세무서장 에게 제출하여야 하며(법령§76②,⑥,⑦)": {},
                "- 신고한 평가방법은 그 후의 사업연도에도 계속하여 적용하여야 하며, 신고한 평가방법을 적용한 사업연도를 포함하여 5개 사업연도가 지난 후에 다른 평가 방법으로 신고할 수 있습니다(법령§76③).": {},
                "  상환차손익": {},
                "- 법인이 상환 받거나 상환하는 외화채권 채무의 원화금액과 원화기장액의 차익 또는 차손은 당해 사업연도에 익금 또는 손금에 산입합니다(법령§76⑤).": {},
                "- 한국은행의 외화채권 채무 중 외화로 상환받거나 상환하는 금액의 환율변동 분은 한국은행이 정하는 방식에 따라 해당 외화금액을 매각하여 원화로 전환한 사업연도의 익금 또는 손금에 산입합니다. ": {},

                "참고：예규 ": {

                        " 내국법인이 외화예금을 원화로 인출함으로써 수취하는 원화금액과 해당 외화예금의 원화 기장액의 차익 또는 차손은 그 인출일이 속하는 사업연도의 익금 또는 손금에 산입하는 것이며, 이 경우 수차례에 걸쳐 입금한 외화예금의 일부를 인출한 때에는 먼저 입금된 분부터 인출하는 것으로 하는 것이나, 해당 법인이  법인세법 시행령  제74조제1항제1호 마목의 ‘이동평균법’을 준용한 평가방법을 계속적으로 적용하여 온 경우에는 그에 따른 평가방법을 적용할 수 있는 것임(법인세과-865, 2009.7.29.). ": {},
                        "참고 집행기준 42-76-1 외화자산 및 부채의 평가 ": {},
                        "① 은행업을 영위하는 금융회사가 보유하는 화폐성 외화자산 및 부채 등은 다음과 같이 평가한다. ": {},
                        "평가대상 자산 평가 방 법 ": {},
                        "화폐성 외화자산 및 부채 사업연도종료일 매매기준율 등 ": {},
                        "통화선도, 통화스왑, 환변동보험 ": {},
                        "다음의 방법 중 신고한 방법(신고한 평가방법은 그 후 사업연도에도 계속하여 적용) 1. 계약의 내용 중 외화자산 및 부채를 사업연도종료일 현재의 매매기준율 등으로 평가하는 방법 2. 계약의 내용 중 외화자산 및 부채를 계약체결일의 매매기준율 등으로 평가하는 방법 ": {},
                        "② 금융회사 등 외의 법인이 보유하는 화폐성 외화자산 부채와 환위험회피용 통화선도 등은 다음의 어느 하나에 해당하는 방법 중 신고한 방법에 따라 평가한다. ": {},
                        "평가대상 자산 평 가 방 법 ": {},
                        "화폐성외화자산 부채와 환위험회피용 통화선도 등 ": {},
                        "1. 취득일 또는 발생일(통화선도의 경우 계약체결일) 현재의 매매기준율 등 2. 사업연도 종료일 현재의 매매기준율 등(2호 적용 이전에는 1호를 적용함) ": {},

                        "1. 사업연도 중에 발생된 외화자산 부채 ": {},
                        "거래은행에서 실제 적용한 환율에 따른다. ": {},
                        "참고 집행기준 42-76-2 외화자산 부채의 기장환율 ": {},
                        "외화자산 부채는 다음의 방법에 따라 환산한 원화금액으로 기장한다. ": {},
                        "구 분 원화 환산 방법 ": {},
                        "발생일 현재 매매기준율 등에 따라 환산한다. 이경우 외화자산 부채의 발생일이 공휴일인 때에는그 직전일의 환율에 따른다.": {},
                        "2. 사업연도 중에 보유외환을 매각하거나 외환을 매입하는 경우 ": {},
                        "3. 사업연도 중에 보유외환으로 다른 외화 자산을 취득하거나 기존의 외화부채를 상환하는 경우 ": {},
                        "보유외환의 장부상 원화금액으로 회계처리한다. ": {},
                },

                "통 화(Currency)  주요통화별 환율 고 시 환 율 비 고 2016.12.31현재 2017.12.31현재 ": {

                        "미 국 달러 USD 1,208.50 1,071.40 일 본 엔 JPY 1,036,81 949.11 100엔당유 로 유로 EUR 1,267.60 1,279.25 (독 일) 마르크 DEM EUR통화 EUR통화 (프랑스) 프랑 FRF 〃 〃 (이태리) 리라 ITL 〃 〃 (벨기에) 프랑 BEF 〃 〃 (오스트리아) 실링 ATS 〃 〃 영 국 파운드 GBP 1,480.17 1,439.53 캐 나 다 달러 CAD 894.72 852.69 스 위 스 프랑 CHF 1,181.33 1,094.72 홍 콩 달러 HKD 155.83 137.07 스 웨 덴 크로네 SEK 132.40 129.90 호 주 달러 AUD 872.05 835.16 덴 마 크 크로네 DKK 170.52 171.82 싱 가 폴 달러 SGD 834.60 800.63 중 국 위안 CNH 173.26 163.65 인도네시아 루피아 IDR 8.98 7.90 100루피아당태 국 바트 THB 33.63 32.77 쿠 웨 이 트 디나르 KWD 3,948.70 3,547.92 말레이시아 링기트 MYR 269.48 263.47 노 르 웨 이 크로네 NOK 139.75 129.86 뉴 질 랜 드 달러 NZD 841.00 759.68 사우디아라비아 리알 SAR 322.20 285.68 아랍에미리트연합국 디르함 AED 329.02 291.70 바 레 인 디나르 BHD 3,207.02 2,842.74": {},
                        "※ 외화자산 부채평가 시 사업연도 종료일 현재의 기준환율 또는 재정환율은 사업연도 종료일 전일의 거래실적에 의하여 사업연도 종료일에 외국환중개회사가 고시한 환율을 말합니다.": {},
                },
                "☞ 사업연도 종료일이 공휴일 등으로 고시한 환율이 없는 경우에는 사업연도 종료일 전일에 고시한 기준환율 또는 재정환율을 적용합니다(법인46012-462, 2000.2.17.).": {},
                "→ 서울외국환중개주식회사(www.smbs.biz/'환율조회')에서 조회 가능(단, CNY는 2016년 1월 1일부터 고시하지 않습니다) ": {},

                "평가대상 자산 ": {},
                "□ 유가증권 - 일반회사 보유 ": {},
                "- 원가법중  개별법(채권에 한함)  총평균법  이동평균법 ": {},
                "- 원가법중 총평균법 ": {},
        },
        "법인세법시행령 제76조": 법인세법시행령.제76조,
        "금융회사 등": 법인세법시행령.제76조1항,
        "금융회사 등 외의 법인": 법인세법시행령.제76조2항,
        "평가방법의 계속적용": 법인세법시행령.제76조3항,
        "평가손익의 처리": 법인세법시행령.제76조4항,
        "최초 평가시 환산손익 인식방법": {},
        "와화자산부채의 상환차손익": 법인세법시행령.제76조5항,
        "구상무역에 있어서의 매매가액": {},
        "외화자산,부채의 차환: 법기통42-76...3, 법인세법집 행기준 42-76-3": {},
        "기능통화도입기업의 과세표준 계산 특례": {
                법인세법.제53_02조1항_: {
                        법인세법.제53_02조1항1호_: 법인세법시행령.제91_03조1항,
                        법인세법.제53_02조1항2호_: {},
                        법인세법.제53_02조1항3호_: {},
                },
                법인세법.제53_02조2항_: {},
        },
        "해외사업장의 과세표준 계산 특례": {
                # 법인세법.제53_3조1항,
                # 법인세법시행령.제91_4조,
                # 법인세법.제53_3조2항_ :{},
        },
}


#___________________________________________________
제목='외화자산부채'
_={
    #"지방소득세_법인세분 가산세": 지방소득세_법인세분,
    "기업회계":기업회계,
    "법인세":법인세,
    #"국제조세조정":국제조세조정,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"상속세":상속세,
    #"양도소득세":양도소득세,
    #"농어촌특별세":{},
}
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
        #self.
        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________