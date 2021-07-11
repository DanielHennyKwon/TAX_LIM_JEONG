# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 결산조정,신고조정 ,익금산입, 익금불산입, 손금산입, 손금불산입, 기부금, 이월결손금, 비과세, 소득공제, 과세표준, \
    세율, 세액공제, 세액감면,최저한세 , 가산세, 기납부세액
법인세={
    '결산서상 당기순손익':{},
    '○ 세무조정 : 결산조정:결산에 반영되어야 인정 예) 감가상각비, 퇴직급여충당금, 대손충당금, 일정대손금, 재고자산평가손, 고정자산평가손 등 ':결산조정.법인세,
    '○ 세무조정 : 신고조정：결산반영 없이 신고서 계상 가능 예) 국고보조금의 손금산입, 손익귀속시기 차이 등':신고조정.법인세,
    '+ 익금산입 - 수익의 범위 - 배당금 또는 분배금의 의제':익금산입.법인세,
    '- 익금불산입- 자본거래로 인한 수익의 익금불산입 - 평가이익 등의 익금불산입 - 지주회사 수입배당금액의 익금불산입 - 수입배당금액의 익금불산입 - 연구개발 관련 출연금 등의 과세특례 - 사업전환 무역조정지원기업에 대한 과세특례 - 기업의 금융채무 상환을 위한 자산매각에 대한 과세특례 등 ':익금불산입.법인세,
    '- 손금산입 - 손비의 범위 - 기타 특정 손금 책임준비금 등퇴직급여충당금 대손충당금 구상채권상각충당금':손금산입.법인세,
    '+ 손금불산입 - 자본거래 등으로 인한 손금불산입 등 - 지급이자의 손금불산입 - 감가상각비 한도초과액의 손금불산입 - 접대비의 손금불산입 - 업무용승용차 관련비용의 손금불산입 - 공동경비 분담초과액 손금불산입':손금불산입.법인세,
    '=차가감 소득금액':{},
    '± 기부금 한도초과 및이월액 손금산입 - 기부금한도 초과  ...':기부금.법인세,
    '◇ 각 사업연도 소득금액':{},
    '- 이월결손금 - 공제대상 결손금：당해 사업연도 개시일 전 10년이내에 개시한 사업연도에서 발생한 결손금 중 공제되지 아니한 금액(한도：당해 소득금액 등의 80% 또는 100%) ':이월결손금.법인세,
    '- 비과세소득 - 법인세법상 비과세 소득 - 조세특례제한법상 비과세소득':비과세.법인세,
    '- 소득공제 - 유동화전문회사 등에 대한 소득공제':소득공제.법인세,
    '◇ 과세표준':과세표준.법인세,
    "+ 선박표준이익 - 개별선박순톤수 × 톤당 1운항일 이익 * × 운항일수 × 사용률 * 1천톤이하 14원, 1천톤초과 1만톤이하 11원, 1만톤초과 2만5천톤 이하 7원, 2만5천톤 초과 4원 ":{},
    '× 세율 - 일반 법인세율 (과세표준 ,세율 /200억원 초과, 22% /2억원~200억원 이하, 20%/ 2억원 이하, 10% /* 2012. 1. 1. 이후 개시하는 사업연도부터 적용)':세율.법인세,
    '◇ 산출세액':{},
    '- 공제   감면세액 ':{
        '- 세액공제:외국납부세액공제 재해손실세액공제 사실과 다른 회계처리 관련 세액공제 조세특례제한법상 세액공제(연구인력개발비 세액공제 등) ':세액공제.법인세,
        '- 세액감면 창업중소기업에 대한 법인세 감면 등':세액감면.법인세,
    },
    '최저한세※ 최저한세의 계산 구 분 과세표준 2017년 중소기업 유예기간 4년 포함 7% /일반기업 유예기간 이후 1~3년차 8% 유예기간 이후 4~5년차 9% 100억원 이하 10% 1천억원 이하 12% 1천억원 초과 17% /':최저한세.법인세,
    '+ 가산세 - 국세기본법상 가산세 무신고   과소신고  납부불성실가산세 등 - 법인세법상 가산세 무기장   주주등의 명세서 제출불성실   지출증명 미수취가산세 등 ':가산세.법인세,
    '가감계':{},
    '기납부세액 : 기한내 납부세액 중간예납세액, 수시부과세액 등(가산세 제외) ':기납부세액.법인세,
    "신고납부전 가산세액 중간예납 미납부가산세 등 ": {},
    '감면분 추가납부세액':{},
    '◇ 차감납부할세액':{},
}
양도소득세={}
증여세={
    '증여세액 계산 구조':{},
    '과세표준의 계산':{}
}
#___________________________________________________
제목='세금계산흐름도'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    "양도소득세":양도소득세,
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

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________
