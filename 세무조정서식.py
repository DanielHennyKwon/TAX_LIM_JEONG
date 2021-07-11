# -*- coding: utf-8 -*-
# 2018-12-24 권달현

법인세={
    "소득금액조정합계표":{

        "  계정과목별로 세무조정이 끝나면 조정사항을 합계하기 위해 소득조정합계표를 작성해야 합니다.": {},
        "  다음 자료의 의거 소득금액조정합계표를 작성하여 봅시다. ": {},
        "자 료 ": {

            "① 익금산입 및 손금불산입 해당액 내역 ": {},
            "Ⅲ ": {},
            "3,000,000": {},
            "770,000": {},
            "840,000": {},
            "134,000": {},
            "560,000": {},
            "130,000": {},
            "654,000": {},
            "75,000": {},
            "2,340,000": {},
            "2,000,000 ": {},
            "수입계상 누락분 재고자산 과소평가액 한도초과액 한도초과액 한도초과액 대표자 가지급금 인정이자 토지매입에 다른 취득세 벌과금 건설자금이자 과소계상액(토지) 중간예납 등 ": {},
            "과 목 금 액 내 용": {},
            "수 입 배 당 금 재 고 자 산 평 가 감 퇴 직 급 여 충 당 금 대 손 충 당 금 연 구 및 인 력 개 발 준 비 금 인 정 이 자 세 금 공 과 잡 비 건 설 자 금 이 자 법 인 세 등 ": {},
            "② 손금산입 및 익금불산입 해당액 내역 ": {},
            "과 목 금 액 내 용 ": {},
            "재 고 자 산 평 가 감 감 가 상 각 비 수 입 이 자 ": {},
            "380,000": {},
            "1,340,000": {},
            "22,000 ": {},
            "전기 손금불산입 유보분 중 당기사용분 전기 부인누계액 중 당기 용인액 국세환급금 이자 ": {},
            "Ⅲ. 주요 세무조정명세서의 작성 407 ": {},
            "사 업 연 도 ": {},
            "소득금액조정합계표 ": {},
            "①과 목 ②금 액 ": {},
            "130 000 상여 100 ": {},
            "500 ": {},
            "[별지 제15호 서식] (2013.3.23개정) ": {},
            "2017. 1. 1. ": {},
            "법인명 (주) 가 나 ~ 사업자등록번호 101－81－12345 2017.12.31 ": {},
            "익금산입 및 손금불산입 손금산입 및 익금불산입 ": {},
            "③소득처분": {},
            "④과 목 ⑤금 액 ": {},
            "⑥소득처분 처분 코드 처분 코드수 입 배 당 금 3 000 000 유보 400 재 고 자 산 평 가 감 380 000 유보 100": {},
            "재 고 자 산 평 가 감 770 000 〃 400 감 가 상 각 비 1 340 000 〃 100": {},
            "퇴 직 급 여 충 당 금 840 000 〃 400 수 입 이 자 22 000 기타 200": {},
            "대 손 충 당 금 134 000 〃 400": {},
            "연구및인력개발준비금 560 000 〃 400": {},
            "가 지 급 금 인 정 이 자 ": {},
            "세 금 과 공 과 654 000 유보 400": {},
            "잡 비 75 000 ": {},
            "기타 사외유출 ": {},
            "500": {},
            "건 설 자 금 이 자 2 340 000 유보 400": {},
            "법 인 세 등 2 000 000 ": {},
            "기타 사외유출 ": {},
            "합 계 10 503 000 합 계 1 742 000 ": {},
            "210mm×297mm[백상지 80g/㎡ 또는 중질지 80g/㎡] ": {},
        },

    },
}
농어촌특별세={
	'...':{},
}

#___________________________________________________
제목='세무조정서식'

_={
    "법인세":법인세,
    "농어촌특별세":농어촌특별세,
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