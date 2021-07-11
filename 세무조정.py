# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 익금항목의조정,손금항목의조정,손금불산입항목의조정
import 계산흐름도 , 결산조정 , 신고조정 , 익금산입 , 익금불산입 , 손금산입 , 손금불산입 , 순자산증가설_세무조정 , 수입금액의조정 , 소득처분 , 체크리스트,세무조정_흐름도
import 법인세법,법인세법시행령,법인세법시행규칙
외부={
    '법인세 외부조정 신고제도란?':{},
    "외부세무조정": {},
    "자기세무조정": {},
    "법인세법 제60조(과세표준 등의 신고) 9항 ": 법인세법.제60조,
    "법인세법시행령 제97조의2(외부세무조정 대상법인) ": 법인세법시행령.제97_02조,
    "법인세법시행령 제97조의3(조정반) ": 법인세법시행령.제97_03조,
    "법인세법시행규칙 제50조의3(조정반의 지정 절차 등) ": 법인세법시행규칙.제50_03조,
}
명세서={
        '익금항목의 조정':익금항목의조정.법인세,
        '손금항목의 조정':손금항목의조정.법인세,
        '손금불산입 항목의 조정':손금불산입항목의조정.법인세,
        '소득처분':소득처분.법인세,
        '소득금액조정합계표의 작성':{},
}
계산서={
    "법인세법 제60조(과세표준 등의 신고) 2항 2호 ":법인세법.제60조,
    "법인세법시행령 제97조(과세표준의 신고) 4항 ": 법인세법시행령.제97조,
    "법인세법시행규칙 제82조(서식) 3항 ": 법인세법시행규칙.제82조,
}
법인세_서식_공제감면={
    "[별지 제8호 부표1] 공제감면세액계산서(1)":{},
    "[별지 제8호 부표2] 공제감면세액계산서(2)": {},
    "[별지 제8호 부표3] 공제감면세액계산서(3)": {},
    "[별지 제8호 부표4] 공제감면세액계산서(4)": {},
    "[별지 제8호 부표5] 공제감면세액계산서(5)": {},
    "[별지 제8호 부표6] 추가납부세액계산서(6)": {},
}
법인세={
        '세무조정이란?':{
            "기업회계의 목적":{},
            "세무회계의 목적":{},
            "세법에 의한 정확한 과세소득의 계산을 위하여 기업이 작성한 재무제표상의 당기순손익을 기초로 하여 세법의 규정에 따라 손금과 익금을 조정하는 것을 세무조정이라고 한다.":{},
            "협의의 세무조정:세법규정에 의해 손금과 익금의 가감산을 하는 절차":{},
            "광의의 세무조정:과세소득과 과세표준의 산정은 물론 납부할 세액의 계산까지를 포함하는 일련의 절차":{},
            "세무조정은 그 절차상의 특색을 기준으로 결산조정과 신고조정으로 나뉜다.":{},
        },
        "순자산증가설과 세무조정":순자산증가설_세무조정._,
#        '세무조정 흐름도':세무조정_흐름도.법인세,
        '법인세 세무조정과 신고납부를 위한 체크리스트':체크리스트.법인세,
        '결산조정':결산조정.법인세,
        '신고조정':신고조정.법인세,
        '익금산입':익금산입.법인세,
        '익금불산입':익금불산입.법인세,
        '손금산입':손금산입.법인세,
        '손금불산입':손금불산입.법인세,
        "법인세_세무조정서식_공제감면":법인세_서식_공제감면,
        '외부조정 신고제도':외부,
        "세무조정명세서":명세서,
        "세무조정계산서":계산서,
}
#___________________________________________________
제목='세무조정'
_={
    "법인세":법인세,
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