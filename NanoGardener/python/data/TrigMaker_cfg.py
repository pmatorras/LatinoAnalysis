Trigger = {

# --------------------------- Full2017 ---------------------------------

        'Full2017'  :  { 
                          1  :  { 'begin' : 294927 , 'end' : 299367 , 'lumi' : 4.793 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : '?' ,
                                                'DoubleEleLegLowPt' : '?' ,
                                                'SingleEle'         : '?' ,
                                                'DoubleMuLegHigPt'  : '?' ,
                                                'DoubleMuLegLowPt'  : '?' ,
                                                'SingleMu'          : '?' ,
                                                'MuEleLegHigPt'     : '?' ,
                                                'MuEleLegLowPt'     : '?' ,
                                                'EleMuLegHigPt'     : '?' ,
                                                'EleMuLegLowPt'     : '?' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 1.0 ,
                                                'DoubleMu'  : 0.993   ,
                                                'MuEle'     : 0.873   ,
                                                'EleMu'     : 0.860   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },
                          2  :  { 'begin' : 299368 , 'end' : 306463 , 'lumi' : 37.067 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : '?' ,
                                                'DoubleEleLegLowPt' : '?' ,
                                                'SingleEle'         : '?' ,
                                                'DoubleMuLegHigPt'  : '?' ,
                                                'DoubleMuLegLowPt'  : '?' ,
                                                'SingleMu'          : '?' ,
                                                'MuEleLegHigPt'     : '?' ,
                                                'MuEleLegLowPt'     : '?' ,
                                                'EleMuLegHigPt'     : '?' ,
                                                'EleMuLegLowPt'     : '?' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 1.0 ,
                                                'DoubleMu'  : 0.993   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 0.86   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf' , ''] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },
                       },   
# --------------------------- 2015 ---------------------------------

#        'Full2015'  :  { 1  :  { 'begin' : 1 , 'end' : 999999 , 'lumi' :  5.0 ,
#                                 'LegEff' :  { 'DoubleEleLegHigPt' : 'HLT_Ele17_12LegHigPt.txt' ,
#                                               'DoubleEleLegLowPt' : 'HLT_Ele17_12LegLowPt.txt' ,
#                                               'SingleEle'         : 'HLT_Ele23Single.txt'      ,
#                                               'DoubleMuLegHigPt'  : 'HLT_DoubleMuLegHigPt.txt' ,
#                                               'DoubleMuLegLowPt'  : 'HLT_DoubleMuLegLowPt.txt' ,
#                                               'SingleMu'          : 'HLT_MuSingle.txt' ,
#                                               'MuEleLegHigPt'     : 'HLT_MuEleLegHigPt.txt' ,
#                                               'MuEleLegLowPt'     : 'HLT_MuEleLegLowPt.txt' ,
#                                               'EleMuLegHigPt'     : 'HLT_EleMuLegHigPt.txt' ,
#                                               'EleMuLegLowPt'     : 'HLT_EleMuLegLowPt.txt' ,
#                                             } ,
#                                 'DZEff'  :  { 'DoubleEle' : 0.995 ,
#                                               'DoubleMu'  : 0.95  ,
#                                               'MuEle'     : 1.0   ,
#                                               'EleMu'     : 1.0   ,
#                                             } ,
#                                 'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
#                                 'EMTFBug':  False , 
#                               },
#                       },


# --------------------------- Full2016 ---------------------------------

#   ------------------------------
#     dataset | from run | to run
#   ----------+----------+--------
#    Run2016B |   272007 | 275376  -> 5.788 /fb                             f_BCDEF = 0.294
#    Run2016C |   275657 | 276283  -> 2.573 /fb                             f_BCDEF = 0.130
#    Run2016D |   276315 | 276811  -> 4.248 /fb                             f_BCDEF = 0.215
#    Run2016E |   276831 | 277420  -> 4.009 /fb                             f_BCDEF = 0.203
#    Run2016F |   277772 | 278808  -> 3.102 /fb -> B+C+D+E+F : 19.720 / fb  f_BCDEF = 0.157
#    Run2016G |   278820 | 280385  -> 7.540 /fb
#    Run2016H |   280919 |         -> 8.606 /fb --> G+H: 16.146 /fb
#    Total lumi: 35.867 /fb (brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt -u /fb)
#   ------------------------------

        'Full2016'  :  { 
                          # Lower Muon efficiency at begin of 2016 + L1 EMTF Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.616 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
                          # L1 EMFT Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          2  :  { 'begin' : 274095 , 'end' : 277165 , 'lumi' : 15.005  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=277166: L1 EMTF Bug fixed ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.059  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=278273: Switch to DZ version of E-Mu triggers
                          # OLD: 4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                          4  :  { 'begin' : 278273 , 'end' : 278808 , 'lumi' : 2.041  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 0.956 ,
                                                'EleMu'     : 0.956 ,
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # No change of trigger, same as period 4
                          # END of HIP problem -> Muon ID/ISO SF change
                          #    Run2016G |   278820 | 280385
                          #    Run2016H |   280919 |
                          5  :  { 'begin' : 278820 , 'end' : 281612 , 'lumi' : 7.540  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016GH_PTvsETA_HWW.txt',
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt',
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 0.956 ,
                                                'EleMu'     : 0.956 ,
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=281613: Switch to DZ version of Double Mu triggersA : Lumi 8.606 - 0.860 = 7.746 (to accomodate space for pseudo period 7)
                          6  :  { 'begin' : 281613 , 'end' : 284042 , 'lumi' : 7.746  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016GH_PTvsETA_HWW.txt',
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt',
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 0.979 , 
                                                'MuEle'     : 0.956 ,
                                                'EleMu'     : 0.956 ,
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                }, 
                          # Run>=281613: Switch to DZ version of Double Mu triggers ... Few LS where HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL is seeded by L1_Mu23_EG10 
                          # Attributed to last run as a trick to switch to the lower efficiency
                          7  :  { 'begin' : 284043 , 'end' : 284044 , 'lumi' : 0.860  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'SingleEle'         : 'Full2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_2016_cut_WP_Tight80X.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016/DoubleIsoMu17Mu8_IsoMu17leg_Run2016GH_PTvsETA_HWW.txt',
                                                'DoubleMuLegLowPt'  : 'Full2016/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt',
                                                'SingleMu'          : 'Full2016/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016/DoubleMu_IsoMu23_l1pt23_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016/HLT_DoubleEleLegLowPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016/HLT_DoubleEleLegHigPt_2016_cut_WP_Tight80X.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.991 ,
                                                'DoubleMu'  : 0.979 ,
                                                'MuEle'     : 0.956 ,
                                                'EleMu'     : 0.956 ,
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
        
                       }
}

NewVar_MC_dict = {
   'F': [
         'TriggerEffWeight_2l',
         'TriggerEffWeight_2l_u',
         'TriggerEffWeight_2l_d',
         'TriggerEffWeight_3l',
         'TriggerEffWeight_3l_u',
         'TriggerEffWeight_3l_d',
         'TriggerEffWeight_4l',
         'TriggerEffWeight_4l_u',
         'TriggerEffWeight_4l_d',
         'TriggerEffWeight_sngEl',
         'TriggerEffWeight_sngMu',
         'TriggerEffWeight_dblEl',
         'TriggerEffWeight_dblMu',
         'TriggerEffWeight_ElMu',
        ],
   'I': [
         'TriggerEmulator',
         'EMTFbug_veto',
         'run_period',
         'Trigger_sngEl',
         'Trigger_sngMu',
         'Trigger_dblEl',
         'Trigger_dblMu',
         'Trigger_ElMu'
         #'metFilter'
        ]        
}

NewVar_DATA_dict = {
   'F': [
        ],
   'I': [
         'EMTFbug_veto',
         'run_period',
         'Trigger_sngEl',
         'Trigger_sngMu',
         'Trigger_dblEl',
         'Trigger_dblMu',
         'Trigger_ElMu'
         #'metFilter'
        ]        
}



if __name__ == '__main__':
   for key in Trigger:
      print(Trigger[key])
   print(Trigger['Full2016'][6]['MC'])

