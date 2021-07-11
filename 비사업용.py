# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
양도소득세={
    '비사업용 토지 총괄': {
        '비사업용 토지중과제도 개요': {},
        '비사업용토지 해당여부 총괄흐름도': {}
    },
    '지목별 비사업용 토지 해당여부 판단': {
        '농지(논밭 및 과수원)': {},
        '임야': {},
        '목장용지': {},
        '기타토지(농지,임야,목장용지 외의 토지로서 나대지 잡종지등)':{},
        '주택의 부속토지': {},
        '별장건물 및 그 부속토지': {},
        '기타 상당한 이유 있는 토지': {},
        '비사업용 토지의 기간 기준':{},
        '토지 지목의 판정': {},
        '다수의 필지가 하나의 용도로 사용되고 기준면적 초과하는 경우': {},
        '하나 이상의 건축물이 있고 여러 용도로 사용되는 경우의 부속토지면적 계산': {},
        '업종의 분류': {},
        '비사업업용토지의 판정요약': {},
    },
    '부득이한 사유가 있어 비사업용토지로 보지 아니하는 토지의 판정기준': {
        '법령 등 부득이한 사유가 있어 당해 기간을 사업에 사용한 것으로 간주한 경우': {},
        '경매 등 부득이한 사유가 있어 부득이한 사유가 발생하기 직전의 기간을 기준으로 사업용 여부를 판정하는 경우(양도일 의제)': {},
        '상속,20년,수용 등 부득이한 사유가 있는 경우 당해 토지를 사업용 토지로 구분하는 경우': {},
    },
}

#___________________________________________________
제목='비사업용'
_={
    #"기업회계":기업회계,
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
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