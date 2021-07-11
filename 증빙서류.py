# -*- coding: utf-8 -*-
#Created on 2018-11-8 @author: 권달현
양도소득세={
    '1세대1주택':{
        '실제 가주하였으나 주민등록이 되어 있지 아니한 경우':{
            '입주자 기록카드(아파트 관리사무소등': {},
            '이삿짐 영수증': {},
            '봉투 또는 택배 등 우편물 영수증': {},
            '신문구독료 및 생수 등 생필품 영수증': {},
            '도시가스 및 전기사용료 영수증': {},
            '신용카드 또는 교통카드 사용내역': {},
            '핸드폰,스마트폰,일반전화 영수증': {},
            '인근 병원 진료 영수증': {},
            '인근 은행 거래 내역': {},
            '노인정 회원명부': {},
            '재학증명서': {},
            '통반장 또는 인근 주민 확인서': {},
        },
        '실제 주택으로 사용하였으나 공부상 상가인 경우':{
            '본인이 거주한 경우: 본인 주민등록등본':{},
            '임대한 경우':{
                '임대차계약서':{},
                '세입자 주민등록등본':{},
            },
            '도면 및 사진(납세자 또는 세입자가 거실 등에 있는 상태에서 사진을 찍음)':{},
            '위 "실제 가주하였으나 주민등록이 되어 있지 아니한 경우"의 증빙서류':{},
        },
    },
    '8년자경농지':{
        '실제거주였으나 주민등록이 되어 있지 않은 경우 :상기"실제 가주하였으나 주민등록이 되어 있지 아니한 경우"의 증빙':{},
        '실제 경작하였으나 증빙서 불충분한 경우':{
            '종자,비료,농약,농기계 및 면세유 등 구입영수증':{},
            '농기계 임대 또는 사용료 영수증': {},
            '벼 수매실적 및 농작물 판매 영수증': {},
            '양도일 현재 농지 여부: 네이버,다음에서 지도검색,항공사진 등': {},
            '농지위원회 또는 인근주민의 확인서 ': {},
            '농지의 자경거리30키로미터 확인:지도검색': {
                '실제 거주하고 다른 직업이 없는 경우로서 농지규모가 사회통념상 소규모인 경우에는 특별항ㄴ 증빙이 없어도 자경으로 추정 가능':{},
            },
            '토지특성조사표(개별공시지가 조사 목적용)': {},
        },
    },
    '양도차익': {
        '일반적인 경우': {
            '취득 및 양도 계약서': {},
            '필요경비': {
                '취득세 등록세 영수증': {},
                '공인중개사 및 법무사 수수료': {},
                '자본적 지출액(수리비등)': {},
            },
            '토지,건물 등기부등본': {},
            '건축물대장:공동주택과 분양상가는 표제부 및 전유부분 각각 발급신청': {},
            '토지대장:1990.8.31이전 취득분은 취득시부터 등급이 나와야 하며,1985.1.1이전 취득자는 1984.7부터 토지등급나오도록 발급신청': {},
            '수용사실확인서': {},
            '환지예정지증명원': {},
            '잠정등급확인원': {},
            '실제 주택 사용여부:관련 증빙': {},
            '실제 자경 여부 : 관련 증빙': {},
            '': {},
        },
        '재개발,재건축': {
            '신축주택': {
                '취득 및 양도 계약서': {},
                '필요경비': {
                    '취득세 등록세 영수증': {},
                    '공인중개사 및 법무사 수수료': {},
                    '자본적 지출액(수리비등)': {},
                },
                '토지,건물 등기부등본': {},
                '건축물대장:공동주택과 분양상가는 표제부 및 전유부분 각각 발급신청': {},
                '토지대장:1990.8.31이전 취득분은 취득시부터 등급이 나와야 하며,1985.1.1이전 취득자는 1984.7부터 토지등급나오도록 발급신청': {},
            },
            '기존건물': {
                '등기부등본': {},
                '건축물대장:공동주택과 분양상가는 표제부 및 전유부분 각각 발급신청': {},
                '토지대장:1990.8.31이전 취득분은 취득시부터 등급이 나와야 하며,1985.1.1이전 취득자는 1984.7부터 토지등급나오도록 발급신청': {},
                '취득계약서': {},
                '필요경비': {},
            },
            '관리처분내역서': {
                '기존건물과 그 부수토지의 평가액':{},
                '납부한 청산금': {},
                '구청 등에서 확인 가능': {},
                '평가액 및 청산금 확인 불가능한 경우': {
                    '매매사례가액,감정가액,기준시가의 방법을 순차 적용함': {},
                },
            },
        },
    },
}
#___________________________________________________
제목='증빙서류'
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