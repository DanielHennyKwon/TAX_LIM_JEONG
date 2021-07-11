# -*- coding: utf-8 -*-
#Created on 2018-11-6 @author: 권달현
import 토지, 건물 , 부동산에관한권리 , 주식 , 기타자산 , 파생상품 , 동업기업과세특례
증여세={#증여세'로
    '과세대상':{},
    '증여재산':{}
}
양도소득세={#양도소득세'로
    '과세대상자산(양도소득의 범위)':{},
    '토지':토지._,
    '건물':건물.양도소득세_과세대상,
    '부동산에 관한 권리':부동산에관한권리.양도소득세_과세대상,
    '주식 또는 출자지분':주식.양도소득세_과세대상,
    '기타자산':기타자산.양도소득세_과세대상,
    '파생상품(2016년부터 시행)':파생상품.양도소득세_과세대상,
    '동업기업에 대한 조세특례': 동업기업과세특례.양도소득세,
    '파산선고에 의한 처분의 비과세': {
        '비과세하는 경우':{},
        '과세되는 경우':{},
    },
    '창업자(벤처기업) 등에의 출자에 대한 과세특례': {
        '비과세대상':{},
        '일몰기한':{},
        '출자주식을 상속받은 경우':{},
        '벤처기업이 일반기업에 흡수합병된 이후 합병신주 양도시 과세특례 여부':{},
    },
    '벤처기업 주식매수선택권 행사이익에 대한 과세특례': {},
    '산업재산권 현물출자이익에 대한 과세특례': {},
    '우리사주조합원 등에 대한 과세특례': {},
}

_={
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    "양도소득세":양도소득세,
}
tax=_;제목='과세대상'
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