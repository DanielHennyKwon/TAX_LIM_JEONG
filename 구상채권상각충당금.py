# -*- coding: utf-8 -*-
#Created on 2019-1-1 @author: 권달현
import 법인세법,법인세법시행령,법인세법시행규칙
import 부가가치세법,부가가치세법시행령,부가가치세법시행규칙
import 소득세법,소득세법시행령
import 조세특례제한법
기업회계={
}
법인세={
    "법법§35":법인세법.제35조,
    "신용보증사업을 영위하는 법인이 구상채권의 대손금과 상계하기 위하여 구상채권 상각충당금을 손금으로 계상한 때에는 일정금액의 범위안에서 손금에 산입합니다 (법법§35). ": {},
    "① 구상채권상각충당금 설정대상법인(법령§63①) ": {},
    "  「신용보증기금법」에 따른 신용보증기금   「기술신용보증기금법」에 따른 기술신용보증기금   「농림수산업자 신용보증법」에 따른 농림수산업자신용보증기금   「한국주택금융공사법」에 따른 주택금융신용보증기금   「무역보험법」에 따른 한국무역보험공사   「지역신용보증재단법」에 따른 신용보증재단   「산업재해보상법」에 따른 근로복지공단(근로자신용보증지원사업에서 발생한 구상 채권에 한함)   「주택도시기금법」에 따른 주택도시보증공사   「사회기반시설에 대한 민간투자법」에 따른 산업기반신용보증기금   「지역신용보증재단법」 제35조에 따른 신용보증재단중앙회   「서민의 금융생활 지원에 관한 법률」 제3조에 따른 서민금융진흥원 ": {},
    "* 2017.2.3. 이후 과세표준을 신고하는 분부터 적용합니다 ": {},
    "  「엔지니어링산업 진흥법」에 따른 엔지니어링공제조합   「소프트웨어산업진흥법」에 따른 소프트웨어공제조합   「방문판매 등에 관한 법률」에 따른 공제조합   「한국주택금융공사법」에 따른 한국주택금융공사   「건설산업기본법에 따른 공제조합, 「전기공사공제조합법」에 따른 전기공사공제조합, 「산업발전법」에 따른 자본재공제조합, 「소방산업진흥법」에 따른 소방산업공제조합,   「정보통신공사업법」에 따른 정보통신공제조합, 「건축사법」에 따른 건축사공제조합,   「건설기술 진흥법」에 따른 공제조합, 「콘텐츠산업 진흥법」에 따른 콘텐츠공제조합 ": {},
    "* 건설기술용역공제조합 및 콘텐츠공제조합은 2016년 1월 1일 이후 개시하는 사업 연도분부터 적용합니다. ": {},
    "② 손금산입 범위액：사업연도종료일 현재 신용보증사업과 관련된 신용보증 잔액에 1%와 구상채권발생률 중 낮은 비율을 곱하여 계산한 금액 ": {},
    "③ 충당금과 상계가능한 대손금 범위 ": {},
    "  법령§19의2 제1항 각호의 1에 해당하는 구상채권": {},
    "  당해 법인의 설립에 관한 법률에 의한 운영위원회가 기획재정부장관과 협의하여 정한 기준에 해당한다고 인정한 구상채권 ": {},
    "④ 익금산입 ": {},
    "  대손금과 상계하고 남은 잔액은 다음 사업연도에 일시 익금에 산입하며, 구상채권 상각충당금과 상계한 대손금 중 회수된 금액은 그 회수된 날이 속하는 사업연도에 익금에 산입합니다. ": {},
}
#___________________________________________________
제목='구상채권상각충당금'
_={
    #"지방소득세_법인세분 가산세": 지방소득세_법인세분,
    "기업회계":기업회계,
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