# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
법인세={ # To 결정세액
    "개요":{},
    "법인세법상 세액공제":{
        '외국납부세액공제':{},
        '재해손실세액공제':{},
        '사실과 다른 회계처리 관련 세액공제':{},
    },
    "조세특례제한법상 세액공제":{
        "투자세액공제대사이 되는 투자":{},
        "사업부문의 분할 및 포괄양도의 경우":{},
        "수정신고 또는 경정청구에 의한 세애공제의 적용":{},
        "종류 및 내용":{
            '연구인력개발비 세액공제':{},
        },
        "투자세액공제의 시기 및 투자금액의 계산":{},
        "미공제세액의 이월공제 및 승계":{},
        "수도권과밀억제권역 투자에 대한 세액공제 배제":{},
    },
}
증여세={}
#___________________________________________________
제목='세액공제'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
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

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________