# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import  합병분할 , 현물출자, 자산교환, 감가상각비,부당행위계산부인, 가지급금,인정이자
법인세={
       "합병 및 기업분할 등에 관한 과세특례":{
           "합병분할 과세체계":합병분할.과세체계,
           "합병기업분할과세특례":{},
           "현물출자시 자산양도차익의 손금산입":현물출자.과세특례,
           "자산교환시 자산양도차익의 손금산입":자산교환.과세특례,
           "적격합병 등에 의해 취득한 자산의 감가상각":감가상각비.적격합병취득자산,
           "기업회계상 사업결합":합병분할.기업회계,
       },       
       "부당행위계산의 부인 등 소득금액계산특례":{
           "부당행위계산의 부인":부당행위계산부인.법인세,
           "가지급금의 인정이자 계산":인정이자.법인세,
           "국제조세조정에 관한 법률상의 부당행위계산 부인제도":부당행위계산부인.국제조세조정,
       },
       "기업구조조정 지원세제":{
           "중소기업간 통합 또는 개인기업 법인전환시 양도소득세의 이월과세":{
               "중소기업간의 통합":{},
               "개인기업의 법인전환":{},
           },
           "자산양도차익의 익금불산입":{
               "사업전환 무역조정지원기업의 전환전 사업용 고정자산 양도차익":{},
               "기업의 금융채무 상환을 위한 자산매각 양도차익":{},
               "내국법인의 외국자회사 주식 등의 현물출자에 따른 양도차익":{},
               "주주 등의 자산양도에 관한 법인 자산수증익의 익금불산입":{},
               "재무구조개선계획 등에 따른 채무면제익의 익금불산입":{},
               "감자에 따른 무상수증 주식가액의 익금불산입":{},
               "자가물류시설 양도차익":{},
               "합병에 따른 중복자산의 양도시 양도차익":{},
           },
           "자산양도차익의 손금산입(압축기장충당금)등":{
               "자산의 포괄적 양도에 대한 양도차익의 손금산입 등":{
                   "피인수법인의 압축기장충당금 설정에 의한 손금산입":{},
                   "인수법인의 자산조정계정 계상 등":{},
               },
               "주식의 포괄적 교환,이전에 대한 양도차익의 손금산입":{
                   "완전자회사의 압축기장충당금설정에 의한 손금산입":{},
                   "완전모회사의 자산조정계정 계상 등":{},
               },
           },
           "기타의 기업구조조정 지원세제":{  },
       },
       "지역간 균형발전 및 공익사업지원을 위한 과세특례":{
           "공장의 대도시 밖 이전에 대한 양도차익의 익금불산입(=분할과세)":{
               "적용요건":{},
               "분할과세금액(=익금불산입액)의 계산":{},
               "익금산입(=환입)":{},
           },
           "법인본사의 수도권 과밀억제권역 밖 이전시 양도차익의 익금불산입(=분할과세)":{
               "적용요건":{},
               "분할과세금액(=익금불산입액)의 계산":{},
               "익금산입(=환입)":{},
           },
           "중소기업 공장이전에 대한 양도차익의 익금불산입(=분할과세)":{
               "적용요건":{},
               "분할과세금액(=익금불산입액)의 계산":{},
               "익금산입(=환입)":{},
           },
           "지역간 균형발전 및 공익사업 지원을 위한 그밖의 지원세제":{},
       },
}
tax=법인세
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        제목='법인조정과세무조정실무'
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