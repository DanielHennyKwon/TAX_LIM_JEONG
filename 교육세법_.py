# -*- coding: utf-8 -*-
#Created on 2019년 @author: 권달현
from 교육세법 import *
import 교육세법시행령

제3조1항1호["교육세법시행령 "+교육세법시행령.제1조_]=교육세법시행령.제1조
제5조["교육세법시행령 "+교육세법시행령.제2조_]=교육세법시행령.제2조
제5조1항["교육세법시행령 "+교육세법시행령.제3조_]=교육세법시행령.제3조
제5조3항["교육세법시행령 "+교육세법시행령.제4조_]=교육세법시행령.제4조
제5조3항["교육세법시행령 "+교육세법시행령.제5조_]=교육세법시행령.제5조
제6조1항["교육세법시행령 "+교육세법시행령.제6조_]=교육세법시행령.제6조
제8_02조["교육세법시행령 "+교육세법시행령.제6_02조_]=교육세법시행령.제6_02조
제8_02조["교육세법시행령 "+교육세법시행령.제6_03조_]=교육세법시행령.제6_03조
제9조["교육세법시행령 "+교육세법시행령.제7조_]=교육세법시행령.제7조
제10조["교육세법시행령 "+교육세법시행령.제8조_]=교육세법시행령.제8조



import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title=bubname)
        self.SetSize(620, 520)
        self.mainPanel = wx.Panel(self)
        self.expandButton = wx.Button(self.mainPanel, label=bubname)
        self.tree = wx.TreeCtrl(self.mainPanel)
        root = self.tree.AddRoot(bubname)
        for i in bub:
            ii = self.tree.AppendItem(root, i)
            for j in bub[i]:
                jj = self.tree.AppendItem(ii, j)
                for k in bub[i][j]:
                    kk = self.tree.AppendItem(jj, k)
                    for m in bub[i][j][k]:
                        mm = self.tree.AppendItem(kk, m)
                        for n in bub[i][j][k][m]:
                            nn = self.tree.AppendItem(mm, n)
                            for p in bub[i][j][k][m][n]:
                                pp = self.tree.AppendItem(nn, p)
                                for q in bub[i][j][k][m][n][p]:
                                    qq = self.tree.AppendItem(pp, q)
                                    for r in bub[i][j][k][m][n][p][q]:
                                        rr = self.tree.AppendItem(qq, r)
                                        for s in bub[i][j][k][m][n][p][q][r]:
                                            ss = self.tree.AppendItem(rr, s)
                                            for t in bub[i][j][k][m][n][p][q][r][s]:
                                                tt = self.tree.AppendItem(ss, t)
                                                for u in bub[i][j][k][m][n][p][q][r][s][t]:
                                                    uu = self.tree.AppendItem(tt, u)
                                                    for v in bub[i][j][k][m][n][p][q][r][s][t][u]:
                                                        vv = self.tree.AppendItem(uu, v)
        self.staticText = wx.TextCtrl(self.mainPanel, style=wx.TE_MULTILINE)
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton, 0, wx.EXPAND | wx.ALL, 5)
        self.vtBoxSizer.Add(self.tree, 5, wx.EXPAND | wx.ALL, 5)
        self.vtBoxSizer.Add(self.staticText, 0, wx.EXPAND | wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)
        self.Bind(wx.EVT_BUTTON, self.OnExpandButton, self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnNodeSelected, self.tree)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnExpandButton(self, e):
        self.tree.ExpandAll()

    def __del__(self):
        print('소멸합니다.')

    def OnClose(self, event):
        frame.Destroy()

    def OnNodeSelected(self, e):
        selected = self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))
        self.mainPanel.Layout()
if __name__ == '__main__':
    app = wx.App(redirect=True)
    frame = MyFrame()
    wnd = wx.Frame(None, wx.ID_ANY, "")
    wnd.CenterOnScreen()
    app.SetTopWindow(wnd)
    frame.Show()
    app.MainLoop()