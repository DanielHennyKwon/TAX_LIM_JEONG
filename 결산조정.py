# -*- coding: utf-8 -*-
# 2018-12-26 권달현
import 법인세법,법인세법시행령
법인세={
        "의의":{
                "세무조정에는 결산조정과 신고조정이 있다.":{},
                "결산조정이란 기업이 스스로 기말의 결산정리를 통하여 장부에 반영하여야 하는 사항을 통하여 세무조정을 하는 절차를 이른다.":{},
                "결산조정항목을 설명 하면, 세법상 특정한 손비에 대하여 법인의 내부적 의사결정, 즉 결산확정에 의하여 손금으로 계상하여야만 손금으로 인정하는 항목이 있는데,이를 결산조정항목이라 한다.":{},
        },
        "결산조정항목은 다음과 같다.":{},
        "내국법인":{
                '감가상각비': {
                        "법인세법 제23조(감가상각비의 손금불산입) 제1항": 법인세법.제23조,
                        "고정자산에 대한 감가상각비는 내국법인이 각 사업연도에 손금으로 계상한 경우에만....이를 손금에 산입하고,...": {},
                        "단,IFRS적용기업은 일정 조건하에서 신고 조정 허용: 법인세법 제23조(감가상각비의 손금불산입) 제2항": {},
                },
                '퇴직급여충당금': {
                        "법인세법 제33조(퇴직급여충당금의 손금산입) 제1항": 법인세법.제33조,
                        "...퇴직급여충당금을 손금으로 계상한 경우에는... 이를 손금에 산입한다.": {},
                },
                '대손충당금': {
                        "법인세법 제34조(대손충당금의 손금산입) 제1항": 법인세법.제34조,
                        "...대손충당금을 손금으로 계상한 경우에는... 이를 손금에 산입한다.": {},
                },
                '일정대손금': {
                        "법인세법 제19조의2(대손금의 손금불산입)제1항 ": 법인세법.제19_02조,
                        "법인세법시행령 제19조의2(대손금의 손금불산입)제1항 ": 법인세법시행령.제19_02조,
                        "... '대손금'이라 한다)은 해당 사업연도의 소득금액을 계산할 때 손금에 산입한다.": {},
                        "결산미반영 소멸시효완성채권은 소멸시효 완성 사업연도에 신고조정 가능":{},
                },
                '재고자산평가손': {
                        "법인세법 제42조(자산·부채의 평가) 제3항1호": 법인세법.제42조,
                        "... 장부가액을 감액할 수 있다....재고자산으로서 파손·부패 등의 사유로 정상가격으로 판매할 수 없는 것": {},
                        "법인세법시행령 제78조(재고자산 등의 평가차손) 제3항:....감액한 금액을 당해 사업연도의 손금으로 계상하는 방법을 말한다":법인세법시행령.제78조,
                },
                '고정자산평가손': {
                        "법인세법 제42조(자산·부채의 평가) 제3항2호": 법인세법.제42조,
                        "... 장부가액을 감액할 수 있다....고정자산으로서 천재지변·화재 등 대통령령으로 정하는 사유로 파손되거나 멸실된 것": {},
                        "법인세법시행령 제78조(재고자산 등의 평가차손) 제1항": 법인세법시행령.제78조,
                        "법인세법시행령 제78조(재고자산 등의 평가차손) 제3항:....감액한 금액을 당해 사업연도의 손금으로 계상하는 방법을 말한다":{},
                },
                '부도 등 발생한 주식': {
                        "법인세법 제42조(자산·부채의 평가) 제3항3호": 법인세법.제42조,
                        "... 장부가액을 감액할 수 있다....부도가 발생한 경우 또는 「채무자 회생 및 파산에 관한 법률」에 따른 회생계획인가의 결정을 받았거나 「기업구조조정 촉진법」에 따른 부실징후기업이 된 경우의 해당 주식등": {},
                        "법인세법시행령 제78조(재고자산 등의 평가차손) 제2항": 법인세법시행령.제78조,
"법인세법시행령 제78조(재고자산 등의 평가차손) 제3항:....감액한 금액을 당해 사업연도의 손금으로 계상하는 방법을 말한다":{},
                },
                '파산한 주식': {
                        "법인세법 제42조(자산·부채의 평가) 제3항4호": 법인세법.제42조,
                        "... 장부가액을 감액할 수 있다....부도가 발생한 경우 또는 「채무자 회생 및 파산에 관한 법률」에 따른 회생계획인가의 결정을 받았거나 「기업구조조정 촉진법」에 따른 부실징후기업이 된 경우의 해당 주식등": {},
                        "법인세법시행령 제78조(재고자산 등의 평가차손) 제3항:....감액한 금액을 당해 사업연도의 손금으로 계상하는 방법을 말한다":법인세법시행령.제78조,
                },
        },
        "비영리내국법인":{
                "고유목적사업준비금":{
                        "법인세법 제29조(고유목적사업준비금의 손금산입) 제1항": 법인세법.제29조,
                        "...고유목적사업준비금을 손금으로 계상한 경우에는 ... 이를 손금에 산입한다.": {},
                        "단,외부감사를 받는 비영리내국법인은 신고조정 가능:법인세법제61조(준비금의 손금 계상 특례)":법인세법.제61조,
                },
        },
        "특수목적 법인":{
                '구상채권상각충당금': {
                        "법인세법 제35조(구상채권상각충당금의 손금산입) 제1항": 법인세법.제35조,
                        "...구상채권상각충당금(求償債權償却充當金)을 손금으로 계상한 경우에는... 이를 손금에 산입한다.": {},
                        "법인세법 제35조(구상채권상각충당금의 손금산입) 제2항 : IFRS시 신고조정 가능": {},
                },
                '책임준비금 등': {
                        "법인세법 제30조(책임준비금 등의 손금산입) 제1항": 법인세법.제30조,
                        "...책임준비금과 비상위험준비금을 손금으로 계상한 경우에는... 이를 손금에 산입한다.": {},
                        "제30조(책임준비금 등의 손금산입) 제2항 : IFRS시 신고조정 가능": {},

                },
        },
}
#___________________________________________________
제목='결산조정'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
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

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________