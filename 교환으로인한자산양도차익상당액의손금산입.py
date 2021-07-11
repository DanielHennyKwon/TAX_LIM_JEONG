# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
법인세={
    "자산의 교환으로 인한 양도차익 상당액의 손금산입은 기업의 구조조정을 지원하기 위하여 다른 기업과 사업 또는 자산을 교환하는 경우에 발생하는 자산양도차익에 대한 일시적인 법인세 부담을 줄여주고, 교환 취득자산을 매각하거나 감가상각하는 시점에서 익금산입하여 법인세를 과세하는 과세이연제도입니다. ": {},
    "가. 손금산입 요건 ": {

        "   조세특례제한법시행령  제29조 제3항의 규정에 의한 소비성서비스업 및 같은 령제60조의2 제1항 제1호부터 제3호에 해당하는 부동산업(임대ㆍ중개ㆍ매매업) 이외의 사업을 영위하는 내국법인이": {},
        "- 2년 이상 그 사업에 직접 사용하던 고정자산으로서  법인세법시행령  제86조 제2항의 규정에 의한 사업용 고정자산을 특수관계인외의 다른 내국법인이 2년 이상그 사업에 직접 사용하던 동일한 종류의 사업용 고정자산(이하 “교환취득자산”이라 함)과 교환하는 경우": {},
        "- 그 교환취득자산의 가액 중 교환으로 발생한 사업용고정자산의 양도차익에 상당하는 금액은 해당 사업연도 소득금액을 계산할 때 손금에 산입할 수 있습니다 (법법§50①) ": {},

    },
    "나. 손금산입 한도 ": {

        "  손금에 산입하는 양도차익에 상당하는 금액은 다음의 ①과 ②중 적은 금액으로 합니다(법령§86④, 집행기준 50-0-2)": {},
        "① 양도자산 처분이익 = 교환취득자산의 가액 - 현금으로 대가의 일부를 지급한 경우 그 금액 및 사업용 고정자산의 장부가액": {},
        "② 양도자산 평가이익 = 교환양도자산의 시가 - 교환양도자산의 장부가액 ": {},
    },
    "다. 손금산입 및 익금산입 방법 ": {

        "  손금산입 방법 - 자산양도차익 상당액은 감가상각자산의 경우 일시상각충당금으로, 감가상각자산외 자산의 경우 압축기장충당금으로 하여 결산조정은 물론 신고조정에 의하여 손금에 산입할 수 있습니다(법령§86⑤, 법령§64③∼⑤).": {},
        "  익금산입 방법 - 손금에 산입한 자산양도차익 상당액의 익금산입은  법인세법시행령  제64조 제4항, 제5항의 규정을 준용합니다(법령§86⑤, 법령§64③∼⑤). ": {},

    },
}


#___________________________________________________
제목='교환으로인한자산양도차익상당액의손금산입'
_={
    #"지방소득세_법인세분 가산세": 지방소득세_법인세분,
    #"기업회계":기업회계,
    "법인세":법인세,
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