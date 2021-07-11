# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 신고납부절차, 각사업연도소득의계산,세무조정서식,과세표준,세액계산_구조,과세특례,추가납부세액,농어촌특별세
import 이전가격세제,과소자본세제
import 취득세중과세 , 취득세감면, 기업구조조정, 양도소득세 , 증여세
_={
    '법인세의 신고납부':신고납부절차.법인세,
    '각 사업연도 소득의 계산':각사업연도소득의계산.법인세,
    '주요 세무조정명세서의 작성':세무조정서식.법인세,
    '법인세 과세표준과 납부세액의 계산':{
        '과세표준의 계산':과세표준.법인세,
        '납부세액의 계산':세액계산_구조.법인세_각사업연도소득,
        },
    '토지 등 양도소득에 대한 과세특례':과세특례.법인토지등양도소득,
    '기업의 미환류소득에 대한 법인세 추가납부':추가납부세액.법인세,
    '비영리법인에 대한 과세특례':과세특례.비영리내국법인자산양도,
    '법인세에 대한 농어촌특별세':농어촌특별세.법인세,
    '이전가격세제':이전가격세제.법인세,
    '특정외국법인의 유보소득에 대한 합산과세제도':{
        '제도의 의의':{},
        '제도의 개요':{
            '적용대상자':{},
            '경과세국의 개념':{},
            '특수관계인의 범위':{},
            '경과세국 합산과세의 적용범위':{},
            '배당간주금액의 산출':{
                '배당간주금액':{},
                '배당가능 유보소득의 산출':{},
                '배당간주금액의 적용범위':{},
                '이익잉여금 처분시 공제순서':{},
                '배당간주금액의 귀속시기 및 실제배당금액의 익금불산입':{},
                '배당금액의 외국납부세액공제':{},
                },
            '과세자료 제출':{},
            '미제출 및 부실제출자에 대한 가산세 적용':{},
            },
        },
    '과소자본세제':과소자본세제.법인세,
    '특수관계법인과 거래를 통한 이익의 증여의제':{
        '배 경':{},
        '과세개요':{},
        '수혜법인 법인세 신고서 작성시 유의사항':{},
        },
    '특수관계법인으로부터 제공받은 사업기회로 발생한 이익의 증여의제':{
        '"일감떼어주기"에 대한 증여세 과세 개요':{},
        '"일감떼어주기"사례 ':{},
        },
    '법인세신고 관련 자료의 작성·제출':{
        '법인세 과세표준 및 세액신고서 작성·제출':{},
        '주식등변동상황명세서의 작성·제출':{
            '제출대상 법인':{},
            '제출기한 및 제출관서':{},
            '제출방법':{},
            '주식등변동상황명세서 제출의무 면제':{},
            '제출불성실에 대한 가산세':{},
            '기타 유의사항':{},
            },
        '전환사채 등 발행 및 인수자 내역 명세서 제출 안내':{
            '제출의무자':{},
            '제출자료':{},
            '제출시기 및 방법':{},
            },
        '주식·출자지분을 양도한 주주등에 대한 양도소득세 신고·납부안내 협조':{
            '협조요청 배경':{},
            '안내방법':{},
            '안내대상(양도소득세 과세대상)':{},
            '주식 양도시 양도소득세 신고·납부 방법':{},
            },
        '해외현지법인 명세서 등 제출 ':{
            '해외현지법인 등에 대한 자료제출 의무':{},
            '해외현지법인 명세서등의 자료제출 범위의 구분':{},
            '해외현지법인 등에 대한 자료제출 및 보완요구':{},
            '해외현지법인 등에 대한 자료제출 의무 불이행자 과태료 부과':{},
            '근거규정 및 제출서식':{},
            '과태료 부과기준':{},
            '서식제공':{},
            },
        '전산조직운용명세서 작성 및 제출':{
            '제출대상 법인':{},
            '제출기한 및 제출관서':{},
            '제출방법':{},
            '근거규정':{},
            },
        '전자기록의 보전방법 등에 관한 고시 개정 안내':{
            '개정 사유':{},
            '주요 개정 사항':{},
            },
        },
}
#___________________________________________________
제목='법인세_국세청'
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
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        제목 = '2018년 법인세'
        wx.Frame.__init__(self, parent=None, title=제목)

        self.SetSize(420, 320)
        self.mainPanel = wx.Panel(self)

        self.expandButton = wx.Button(self.mainPanel, label='펼침')
        self.tree = wx.TreeCtrl(self.mainPanel)

        root = self.tree.AddRoot(제목)
        tax = {
            제목:법인세2018,
            '취득세감면': 취득세감면._,
            '취득세중과세': 취득세중과세._,
            '증여세': 증여세._,
            '양도소득세': 양도소득세._,
        }

        for i in tax:
            ii = self.tree.AppendItem(root, i)
            for j in tax[i]:
                jj = self.tree.AppendItem(ii, j)
                for k in tax[i][j]:
                    kk = self.tree.AppendItem(jj, k)
                    for m in tax[i][j][k]:
                        mm = self.tree.AppendItem(kk, m)
                        for n in tax[i][j][k][m]:
                            nn = self.tree.AppendItem(mm, n)

        self.staticText = wx.TextCtrl(self.mainPanel, style=wx.TE_MULTILINE)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton, 0, wx.EXPAND | wx.ALL, 5)
        self.vtBoxSizer.Add(self.tree, 5, wx.EXPAND | wx.ALL, 5)
        self.vtBoxSizer.Add(self.staticText, 0, wx.EXPAND | wx.ALL, 5)

        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON, self.OnExpandButton, self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnNodeSelected, self.tree)

    def OnExpandButton(self, e):
        self.tree.ExpandAll()

    def OnNodeSelected(self, e):
        selected = self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))

        self.mainPanel.Layout()
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()