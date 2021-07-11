# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
양도소득세={
    '양도소득의 범위(과세대상)':{},
    '양도가액': {
        '실가 확인된 경우': {},
        '실가 확인 안된 경우': {},
    },
    '양도소득의 필요경비': {
        '취득가액': {},
        '자본적 지출액': {},
        '양도비': {},
        '필요경비 공제 안되는 경우': {},
    },
    '양도차익의 외화환산': {
        '원화로 환산한 양도차익': {},
        '장기할부조건의 양도차익': {},
    },
    '양도소득기본공제': {
        '공제대상': {},
        '공제방법': {},
    },
    '세율': {
        '일반세율': {},
        '탄력세율': {},
    },
    '외국납부세액의 공제': {
        '공제방법': {},
        '외국납부세액의 범위': {},
        '공제신청서 제출기한': {},
    },
    '준용규정': {},
    '해외부동산을 취득한 경우': {
        '자료제출의무': {},
        '자료제출의무 불이행에 따른 과태료': {},
    },
}

#___________________________________________________
제목='국외자산'
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