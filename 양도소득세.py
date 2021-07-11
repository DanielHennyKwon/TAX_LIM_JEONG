# -*- coding: utf-8 -*-
#Created on 2018-11-6 @author: 권달현
import wx
import 개정세법 ,계산흐름도,요약, 납세의무,과세원인 ,과세대상,양도차익,비과세감면,비과세,세액감면 ,필요경비 ,손익의귀속사업연도
import 기준시가 ,공제,세율,주택,비사업용,신고납부절차,국외자산,국외전출,비거주자,예정신고납부\
    ,업종별구분,계산사례,증빙서류
_={
    '양도소득세 개정세법':개정세법.양도소득세,
    "개요":계산흐름도.양도소득세,
    "양도소득세 요약" :요약.양도소득세,
    "양도소득세 납세의무"       :납세의무.양도소득세,
    "양도의 정의(양도소득세 과세원인)"       :과세원인.양도소득세,
    "양도소득의 범위(양도소득세 과세대상자산)"  :과세대상.양도소득세,
    '양도소득세 비과세 및 감면 제도':비과세감면.양도소득세,
    '양도소득세 비과세':비과세.양도소득세,
    '양도소득세 감면':세액감면.양도소득세,
    "양도 또는 취득의 시기" :손익의귀속사업연도.양도소득세,
    "양도차익의 산정"       :양도차익.양도소득세,
    "기준시가의 산정"       :기준시가.양도소득세,
    "필요경비"  :필요경비.양도소득세,
    "장기보유특별공제액" :공제.장기보유특별공제,
    "양도소득기본공제액":공제.양도소득기본공제,
    "세율":세율.양도소득세,
    "2주택․3주택 이상의 중과" :주택.양도소득세_다주택자중과,
    "비사업용 토지의 중과"       :비사업용.양도소득세,
    "신고와 결정"       :신고납부절차.양도소득세,
    "국외자산양도에 대한 양도소득세"  :국외자산.양도소득세,
    "거주자의 출국시(국외전출세) 국내주식 등에 대한 과세특례" :국외전출.양도소득세,
    "비거주자의 부동산 등 양도소득에 대한 원천징수 등":비거주자._,
    "토지 등 매매차익(매매업) 예정신고와 납부":업종별구분.양도소득세,
    "양도소득․주택신축판매업․부동산매매업의 소득구분" :예정신고납부.양도소득세,
    "계산사례"       :계산사례.양도소득세,
    '객관적 증빙서류 수취 및 제출방법':증빙서류.양도소득세,
}#___________________________________________________
제목='양도소득세'
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