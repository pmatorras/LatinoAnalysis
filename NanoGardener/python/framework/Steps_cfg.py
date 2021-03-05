#!/usr/bin/env python

import os
from pprint import pprint

## --------------------------------- Some predefined sequence Chains -----------------------------------------

# Import samples and cuts configuration for VBSjjlnu analysis
exec(open(os.getenv("CMSSW_BASE") + "/src/LatinoAnalysis/NanoGardener/python/framework/samples/VBSjjlnu_samples.py"))
# ... and samples for HM (2l2nu + jjlnu) analysis
exec(open(os.getenv("CMSSW_BASE") + "/src/LatinoAnalysis/NanoGardener/python/framework/samples/HMjjlnu_samples.py"))
# List of DY samples
allDY = ['DYJetsToLL_M-5to50-LO', 'DYJetsToLL_M-10to50-LO', 'DYJetsToLL_M-10to50-LO_ext1', 'DYJetsToLL_M-10to50-LO_ext2', 'DYJetsToLL_M-10to50-LO_newpmx', 'DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1', 'DYJetsToLL_M-50-LO', 'DYJetsToLL_M-50-LO_ext1', 'DYJetsToLL_M-50-LO_ext2', 'DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext1', 'DYJetsToLL_M-50_ext2', 'DYJetsToLL_M-50_newpmx', 'DYJetsToLL_M-50-UEup', 'DYJetsToLL_M-50-UEdo', 'DYJetsToLL_M-50-PSup', 'DYJetsToLL_M-50-PSdo', 'DYJetsToLL_M-4to50_HT-100to200', 'DYJetsToLL_M-4to50_HT-100to200_ext1', 'DYJetsToLL_M-4to50_HT-100to200_newpmx', 'DYJetsToLL_M-4to50_HT-200to400', 'DYJetsToLL_M-4to50_HT-200to400_ext1', 'DYJetsToLL_M-4to50_HT-200to400_newpmx', 'DYJetsToLL_M-4to50_HT-400to600', 'DYJetsToLL_M-4to50_HT-400to600_ext1', 'DYJetsToLL_M-4to50_HT-600toInf', 'DYJetsToLL_M-4to50_HT-600toInf_ext1', 'DYJetsToLL_M-5to50_HT-70to100', 'DYJetsToLL_M-5to50_HT-100to200', 'DYJetsToLL_M-5to50_HT-100to200_ext1', 'DYJetsToLL_M-5to50_HT-200to400', 'DYJetsToLL_M-5to50_HT-200to400_ext1', 'DYJetsToLL_M-5to50_HT-400to600', 'DYJetsToLL_M-5to50_HT-400to600_ext1', 'DYJetsToLL_M-5to50_HT-600toinf_ext1', 'DYJetsToLL_M-5to50_HT-600toinf', 'DYJetsToLL_M-50_HT-70to100', 'DYJetsToLL_M-50_HT-100to200', 'DYJetsToLL_M-50_HT-100to200_ext1', 'DYJetsToLL_M-50_HT-100to200_newpmx', 'DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1', 'DYJetsToLL_M-50_HT-400to600', 'DYJetsToLL_M-50_HT-400to600_ext1', 'DYJetsToLL_M-50_HT-400to600_ext2', 'DYJetsToLL_M-50_HT-400to600_newpmx', 'DYJetsToLL_M-50_HT-600to800', 'DYJetsToLL_M-50_HT-800to1200', 'DYJetsToLL_M-50_HT-1200to2500', 'DYJetsToLL_M-50_HT-2500toinf', 'DYJetsToLL_M-50_HT-2500toInf']
# ... and samples and for MonoHjjlnu analysis
exec(open(os.getenv("CMSSW_BASE") + "/src/LatinoAnalysis/NanoGardener/python/framework/samples/MonoHjjlnu_samples.py"))

# -------------------------------------------- HERE WE GO ----------------------------------------------------

def createJESvariation(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  dictionary = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
                  'declare'    : 'JES%s%s = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncert%s", kind="%s", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JES%s%s")' %(typeShort, kind.lower(), type, kind, typeShort, kind.lower()),
                  'module'     : 'JES%s%s()' %(typeShort, kind.lower())
               }
  return dictionary 

def copyJERvariation(type="", kind="Up"):
  dictionary = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
                  'declare'    : 'JER%s%s = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="", kind="%s", doMET=False, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JER%s%s")' %(type, kind.lower(),kind,type, kind.lower()),
                  'module'     : 'JER%s%s()' %(type, kind.lower())
               }
  return dictionary

def createFatjetJESvariation(type_, kind="Up"):
  if kind == "Up":
    input_suffix_fatjet = type_ + "Up"
  elif kind == "Do":
    input_suffix_fatjet = type_ + "Down"
  if type_=="Total":
    type_ = ""
  dictionary = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
          # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
          'declare'    : 'fatjetMaker_jes{0}{1} = lambda : FatJetMaker( input_branch_suffix="jes{2}", output_branch_map="fatjetJES{0}{1}", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)' .format(type_, kind.lower(),input_suffix_fatjet),
          'module'     : 'fatjetMaker_jes{0}{1}()'.format(type_, kind.lower())
  }
  return dictionary

def createFatjetJESvariation_Wtagging(type_, kind="Up"):
  if kind == "Up":
    input_suffix_fatjet = type_ + "Up"
  elif kind == "Do":
    input_suffix_fatjet = type_ + "Down"
  if type_=="Total":
    type_ = ""
  dictionary = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
          'declare'    : 'boostedWtagsf_jes{0}{1} = lambda : BoostedWtagSF(input_branch_suffix="jes{2}", output_branch_map="fatjetJES{0}{1}", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)'.format(type_, kind.lower(), input_suffix_fatjet),
          'module'     : 'boostedWtagsf_jes{0}{1}()'.format(type_, kind.lower()),
   }
  return dictionary


def createJESchain(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  toreplace = typeShort+kind.lower()  
  chainTemplate = ['do_JESVAR_suffix','l2Kin_JESVAR', 'l3Kin_JESVAR', 'l4Kin_JESVAR','DYMVA_JESVAR','MonoHiggsMVA_JESVAR','formulasMC_JESVAR','JJHEFT_JESVAR'] 
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain  

def createJERchain(type="", kind="Up"):
  toreplace = type+kind.lower()
  chainTemplate = ['do_JERVAR_suffix','l2Kin_JERVAR', 'l3Kin_JERVAR', 'l4Kin_JERVAR','DYMVA_JERVAR','MonoHiggsMVA_JERVAR','formulasMC_JERVAR','JJHEFT_JERVAR']
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain

def createJESchain_CombJJLNu(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  toreplace = typeShort+kind.lower()  
  chainTemplate = ['do_JESVAR_suffix', 'l2Kin_JESVAR', 'VBSjjlnu_pairing_JESVAR', 'VBSjjlnu_kin_JESVAR',
                  'whadJetSel_JESVAR', 'wlepMaker_JESVAR', 'HMlnjjVars_JESVAR', 'HMDNNProdSemi_JESVAR' , 'HMDNNNeutSemi_JESVAR',
                  'MHSemiLepVars_JESVAR', 'MHSemiLepMVA_JESVAR']
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain  


def createfatjetJESchain_CombJJLNu(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  toreplace = typeShort+kind.lower()  
  chainTemplate = ['CleanFatJet_fatjetJESVAR', 'BoostedWtagSF_fatjetJESVAR', 'VBSjjlnu_pairing_fatjetJESVAR', 'VBSjjlnu_kin_fatjetJESVAR',
                  'whadJetSel_fatjetJESVAR', 'wlepMaker_fatjetJESVAR', 'HMlnjjVars_fatjetJESVAR', 'HMDNNProdSemi_fatjetJESVAR' , 'HMDNNNeutSemi_fatjetJESVAR']
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain  
    
    
def addJESchainMembers():
  dictionary = {}
  for type in ["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"]:
    for kind in ["Up", "Do"]:
      typeShort = type
      if type == "Total":
        typeShort = ""  
      mapname = "JES"+typeShort+kind.lower()
      #print 'l2Kin_'+mapname
      dictionary['l2Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l3Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l4Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['formulasMC_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="%s")' %mapname ,
                 }
      dictionary['DYMVA_'+mapname] = {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MAPNAME = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="MAPNAME")'.replace("MAPNAME", mapname) ,
                  'module'     : 'DYMVA_MAPNAME()'.replace("MAPNAME", mapname),
            } 
      dictionary['MonoHiggsMVA_'+mapname] = {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MAPNAME = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                  'module'   : 'MonoHiggsMVA_MAPNAME()'.replace("MAPNAME", mapname),
               }
      dictionary['JJHEFT_'+mapname] = {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_MAPNAME = lambda : JJH_EFTVars(branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                    'module'     : 'JJHEFT_MAPNAME()'.replace("MAPNAME", mapname),
                 } 

  return dictionary 


def addMETchainMembers():
  dictionary = {}
  for type in ["Response", "Resolution"]:
    for kind in ["Up", "Do"]:
      typeShort = type
      if type == "Total":
        typeShort = ""  
      mapname = "MET"+typeShort+kind.lower()
      #print 'l2Kin_'+mapname
      dictionary['l2Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="%s")' %mapname ,
                  'onlySample' : allDY,
               }
      dictionary['l3Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="%s")' %mapname ,
                  'onlySample' : allDY,
               }
      dictionary['l4Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="%s")' %mapname ,
                  'onlySample' : allDY,
               }
      dictionary['formulasMC_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="%s")' %mapname ,
                  'onlySample' : allDY,
                 }
      dictionary['DYMVA_'+mapname] = {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MAPNAME = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="MAPNAME")'.replace("MAPNAME", mapname) ,
                  'module'     : 'DYMVA_MAPNAME()'.replace("MAPNAME", mapname),
                  'onlySample' : allDY,
            } 
      dictionary['MonoHiggsMVA_'+mapname] = {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MAPNAME = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                  'module'   : 'MonoHiggsMVA_MAPNAME()'.replace("MAPNAME", mapname),
                  'onlySample' : allDY,
               }
      dictionary['JJHEFT_'+mapname] = {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_MAPNAME = lambda : JJH_EFTVars(branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                    'module'     : 'JJHEFT_MAPNAME()'.replace("MAPNAME", mapname),
                    'onlySample' : allDY,
                 } 

  return dictionary 

def addJERchainMembers():
  dictionary = {}
  type=""
  for kind in ["Up", "Do"]:
      mapname = "JER"+type+kind.lower()
 
      dictionary['l2Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l3Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l4Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['formulasMC_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="%s")' %mapname ,
                 }
      dictionary['DYMVA_'+mapname] = {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MAPNAME = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="MAPNAME")'.replace("MAPNAME", mapname) ,
                  'module'     : 'DYMVA_MAPNAME()'.replace("MAPNAME", mapname),
            }
      dictionary['MonoHiggsMVA_'+mapname] = {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MAPNAME = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                  'module'   : 'MonoHiggsMVA_MAPNAME()'.replace("MAPNAME", mapname),
               }
      dictionary['JJHEFT_'+mapname] = {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_MAPNAME = lambda : JJH_EFTVars(branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                    'module'     : 'JJHEFT_MAPNAME()'.replace("MAPNAME", mapname),
                 }
  return dictionary

def addSystChainMembers_CombJJLNu():
  dictionary = {}
  for jetType in ["AK4", "AK8"]:
    for typ in ["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"]:
      for kind in ["Up", "Do"]:
        typeShort = typ
        if typ == "Total":
          typeShort = ""  

        if jetType == "AK4":
          mapname = "JES"+typeShort+kind.lower()
        elif jetType == "AK8":
          mapname = "fatjetJES"+typeShort+kind.lower()

        dictionary['VBSjjlnu_pairing_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_JetPairing',
          'declare'    : 'vbs_pairing_{0} = lambda : VBSjjlnu_JetPairing(year="RPLME_YEAR", mode="ALL", branch_map="{0}", debug=False)'.format(mapname),
          'module'     : 'vbs_pairing_{0}()'.format(mapname),
          'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
        }

        dictionary['VBSjjlnu_kin_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_kin',
          'declare'    : 'vbs_vars_maker_{0} = lambda : VBSjjlnu_kin(mode=["maxmjj","maxmjj_massWZ"], met="PuppiMET", branch_map="{0}", debug=False)'.format(mapname),
          'module'     : 'vbs_vars_maker_{0}()'.format(mapname),
          'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
        }

        dictionary['whadJetSel_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'    : 'LatinoAnalysis.NanoGardener.modules.WhadJetSel',
          'declare'   : 'whadJetSel_{0} = lambda : WhadJetSel(2,"custom",30.0,4.7,"CleanJet" , branch_map="{0}")'.format(mapname),
          'module'    : 'whadJetSel_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc +  vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        dictionary['wlepMaker_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'    : 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
          'declare'   : 'wlepMkr_{0} = lambda : WlepMaker(branch_map="{0}")'.format(mapname),
          'module'    : 'wlepMkr_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc +  vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        dictionary['HMlnjjVars_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars' ,
          'declare'    : 'HMlnjjVars_{0} = lambda : HMlnjjVarsClass(RPLME_YEAR, branch_map="{0}")'.format(mapname),
          'module'     : 'HMlnjjVars_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc +  vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        dictionary['HMDNNProdSemi_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_prod_semi' ,
          'declare'    : 'HMDNNPrSem_{0} = lambda : ApplyDNN_Production_Semi(branch_map="{0}")'.format(mapname),
          'module'     : 'HMDNNPrSem_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        dictionary['HMDNNNeutSemi_'+mapname] = {
          'isChain'    : False ,
          'do4MC'      : True  ,
          'do4Data'    : True  ,
          'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_neut_semi' ,
          'declare'    : 'HMDNNNeSem_{0} = lambda : ApplyDNN_Neutrino_Semi(branch_map="{0}")'.format(mapname),
          'module'     : 'HMDNNNeSem_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        # MonoHiggs Steps, we only need AK4 JES
        if jetType == "AK4": 
            dictionary['MHSemiLepVars_'+mapname] = {
                'isChain'  : False ,
                'do4MC'    : True  ,
                'do4Data'  : True ,
                'import'   : 'LatinoAnalysis.NanoGardener.modules.MHSemiLepVars' ,
                'declare'  : 'MHSemiLepVars_{0} = lambda : MHSemiLepVars(branch_map="{0}")'.format(mapname),
                'module'   : 'MHSemiLepVars_{0}()'.format(mapname),
                'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
            }
            dictionary['MHSemiLepMVA_'+mapname] = {
                'isChain'  : False ,
                'do4MC'    : True  ,
                'do4Data'  : True ,
                'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                'declare'  : 'MHSemiLepMVA_{0} = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/SemiLep_cfg.py", branch_map="{0}")'.format(mapname),
                #'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/2HDMa/2HDMaBDT_cfg.py")',
                'module'   : 'MHSemiLepMVA_{0}()'.format(mapname),
                'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
            }

  for typ in ["JER", "ElepT", "MupT", "MET", "fatjetJMS", "fatjetJMR", "fatjetJER",]:
    for kind in ["Up", "Do"]:
      mapname = typ+kind.lower()
      dictionary['VBSjjlnu_pairing_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_JetPairing',
        'declare'    : 'vbs_pairing_{0} = lambda : VBSjjlnu_JetPairing(year="RPLME_YEAR", mode="ALL", branch_map="{0}", debug=False)'.format(mapname),
        'module'     : 'vbs_pairing_{0}()'.format(mapname),
        'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
       }

      dictionary['VBSjjlnu_kin_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_kin',
        'declare'    : 'vbs_vars_maker_{0} = lambda : VBSjjlnu_kin(mode=["maxmjj","maxmjj_massWZ"], met="PuppiMET", branch_map="{0}", debug=False)'.format(mapname),
        'module'     : 'vbs_vars_maker_{0}()'.format(mapname),
        'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
      }

      dictionary['whadJetSel_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'    : 'LatinoAnalysis.NanoGardener.modules.WhadJetSel',
        'declare'   : 'whadJetSel_{0} = lambda : WhadJetSel(2,"custom",30.0,4.7,"CleanJet" , branch_map="{0}")'.format(mapname),
        'module'    : 'whadJetSel_{0}()'.format(mapname),
        'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

      dictionary['wlepMaker_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'    : 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
        'declare'   : 'wlepMkr_{0} = lambda : WlepMaker(branch_map="{0}")'.format(mapname),
        'module'    : 'wlepMkr_{0}()'.format(mapname),
        'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

      dictionary['HMlnjjVars_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars' ,
        'declare'    : 'HMlnjjVars_{0} = lambda : HMlnjjVarsClass(RPLME_YEAR, branch_map="{0}")'.format(mapname),
        'module'     : 'HMlnjjVars_{0}()'.format(mapname),
        'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

      dictionary['HMDNNProdSemi_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_prod_semi' ,
        'declare'    : 'HMDNNPrSem_{0} = lambda : ApplyDNN_Production_Semi(branch_map="{0}")'.format(mapname),
        'module'     : 'HMDNNPrSem_{0}()'.format(mapname),
        'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

      dictionary['HMDNNNeutSemi_'+mapname] = {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : True  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_neut_semi' ,
        'declare'    : 'HMDNNNeSem_{0} = lambda : ApplyDNN_Neutrino_Semi(branch_map="{0}")'.format(mapname),
        'module'     : 'HMDNNNeSem_{0}()'.format(mapname),
        'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

      # MonoHiggs Steps
      dictionary['MHSemiLepVars_'+mapname] = {
          'isChain'  : False ,
          'do4MC'    : True  ,
          'do4Data'  : True ,
          'import'   : 'LatinoAnalysis.NanoGardener.modules.MHSemiLepVars' ,
          'declare'  : 'MHSemiLepVars_{0} = lambda : MHSemiLepVars(branch_map="{0}")'.format(mapname),
          'module'   : 'MHSemiLepVars_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }
      dictionary['MHSemiLepMVA_'+mapname] = {
          'isChain'  : False ,
          'do4MC'    : True  ,
          'do4Data'  : True ,
          'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
          'declare'  : 'MHSemiLepMVA_{0} = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/SemiLep_cfg.py", branch_map="{0}")'.format(mapname),
          #'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/2HDMa/2HDMaBDT_cfg.py")',
          'module'   : 'MHSemiLepMVA_{0}()'.format(mapname),
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018 + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
      }

  return dictionary 


def prepare_CombJJLNu_syst(basename, selection):
  dictionary = {}
  for syst in ["JES", "JER", "MupT", "ElepT", "MET", "fatjetJES", "fatjetJMS", "fatjetJMR", "fatjetJER"]:
    for kind in ['Up', 'Do']:
      torep = syst + kind.lower()
      if syst == "JES":
        dictionary[basename +"_"+ syst+kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets' : ['JESBase', 
                        ] +
                          createJESchain_CombJJLNu("Total", kind) +
                          createJESchain_CombJJLNu("Absolute", kind) +
                          createJESchain_CombJJLNu("Absolute_RPLME_YEAR", kind) +
                          createJESchain_CombJJLNu("BBEC1", kind) +
                          createJESchain_CombJJLNu("BBEC1_RPLME_YEAR", kind) +
                          createJESchain_CombJJLNu("EC2", kind) +
                          createJESchain_CombJJLNu("EC2_RPLME_YEAR", kind) +
                          createJESchain_CombJJLNu("FlavorQCD", kind) +
                          createJESchain_CombJJLNu("HF", kind) +
                          createJESchain_CombJJLNu("HF_RPLME_YEAR", kind) +
                          createJESchain_CombJJLNu("RelativeBal", kind) +
                          createJESchain_CombJJLNu("RelativeSample_RPLME_YEAR", kind),   
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
            'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

      elif syst == "JER":
        dictionary[basename+"_"+ syst + kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets': ['do_{0}_suffix'.format(torep), 
                        'VBSjjlnu_pairing_{0}'.format(torep), 'VBSjjlnu_kin_{0}'.format(torep), 
                        'whadJetSel_{0}'.format(torep), 'wlepMaker_{0}'.format(torep), 'HMlnjjVars_{0}'.format(torep), 'HMDNNProdSemi_{0}'.format(torep), 'HMDNNNeutSemi_{0}'.format(torep),
                        'l2Kin_{0}'.format(torep), 'MHSemiLepVars_{0}'.format(torep), 'MHSemiLepMVA_{0}'.format(torep),
                        ],
          'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

        # other systematics
      elif syst in ["ElepT", "MupT"]:
        dictionary[basename+"_"+ syst + kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets': ['do_{0}_suffix'.format(torep), 
                        'trigMCKeepRun_{0}'.format(torep), 
                        'LeptonSF_{0}'.format(torep),
                        'VBSjjlnu_pairing_{0}'.format(torep), 'VBSjjlnu_kin_{0}'.format(torep), 
                        'whadJetSel_{0}'.format(torep), 'wlepMaker_{0}'.format(torep), 'HMlnjjVars_{0}'.format(torep), 'HMDNNProdSemi_{0}'.format(torep), 'HMDNNNeutSemi_{0}'.format(torep),
                        'l2Kin_{0}'.format(torep), 'MHSemiLepVars_{0}'.format(torep), 'MHSemiLepMVA_{0}'.format(torep),
                        ],
          'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }
      elif syst == "MET":
        dictionary[basename+"_"+ syst + kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets': ['do_{0}_suffix'.format(torep), 
                        'VBSjjlnu_pairing_{0}'.format(torep), 'VBSjjlnu_kin_{0}'.format(torep), 
                        'whadJetSel_{0}'.format(torep), 'wlepMaker_{0}'.format(torep), 'HMlnjjVars_{0}'.format(torep), 'HMDNNProdSemi_{0}'.format(torep), 'HMDNNNeutSemi_{0}'.format(torep),
                        'l2Kin_{0}'.format(torep), 'MHSemiLepVars_{0}'.format(torep), 'MHSemiLepMVA_{0}'.format(torep),
                        ],
          'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }
      elif syst  in ["fatjetJMS", "fatjetJMR", "fatjetJER"]:
        dictionary[basename+"_"+ syst + kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets': ['CorrFatJetMC', 'CleanFatJet_{0}'.format(torep), 'BoostedWtagSF_{0}'.format(torep),
                        'VBSjjlnu_pairing_{0}'.format(torep), 'VBSjjlnu_kin_{0}'.format(torep),  
                        'whadJetSel_{0}'.format(torep), 'wlepMaker_{0}'.format(torep), 'HMlnjjVars_{0}'.format(torep), 'HMDNNProdSemi_{0}'.format(torep), 'HMDNNNeutSemi_{0}'.format(torep)
                        ],
          'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }
      elif syst == "fatjetJES":
        dictionary[basename +"_"+ syst+kind.lower()] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'selection'  : selection,
          'subTargets' : ['CorrFatJetMC_fatjetJESBase'] +
                          createfatjetJESchain_CombJJLNu("Total", kind) +
                          createfatjetJESchain_CombJJLNu("Absolute", kind) +
                          createfatjetJESchain_CombJJLNu("Absolute_RPLME_YEAR", kind) +
                          createfatjetJESchain_CombJJLNu("BBEC1", kind) +
                          createfatjetJESchain_CombJJLNu("BBEC1_RPLME_YEAR", kind) +
                          createfatjetJESchain_CombJJLNu("EC2", kind) +
                          createfatjetJESchain_CombJJLNu("EC2_RPLME_YEAR", kind) +
                          createfatjetJESchain_CombJJLNu("FlavorQCD", kind) +
                          createfatjetJESchain_CombJJLNu("HF", kind) +
                          createfatjetJESchain_CombJJLNu("HF_RPLME_YEAR", kind) +
                          createfatjetJESchain_CombJJLNu("RelativeBal", kind) +
                          createfatjetJESchain_CombJJLNu("RelativeSample_RPLME_YEAR", kind), 
          'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt',
          'onlySample' : SemiLepHighMassSamples_2016 + SemiLepHighMassSamples_2017 + SemiLepHighMassSamples_2018 + vbsjjlnu_samples_mc + MonoHjjlnu_samples_2016 + MonoHjjlnu_samples_2017 + MonoHjjlnu_samples_2018
        }

  #pprint(dictionary)
  return dictionary



Steps = {

# ------------------------------------------------ CHAINS ----------------------------------------------------

  'MCnofilter' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['leptonMaker'],
                 },

## ------- MC:

# 'MCl1loose2016': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
#                 'subTargets' : ['baseW', 'leptonMaker','lepSel', 'puW2016', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2016', 'btagPerEvent'],
#               },

# 'MCl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent'],
#               },


  'MCl1loose2016' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL', 'ggHTheoryUncertainty', 'DressedLeptons'],
                                 # 'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2016v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

                               #   'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
  'MCl2loose2016_hmumu' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel_hmumu_2016','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TriggerObjectMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2016v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },

  'MCl1loose2016v7' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'DressedLeptons','EFTGen'],
                  },

  'MCSusy2016' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2016v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','JMEUncertMC2016',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2016FS' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  #'leptonMaker','lepSelSusy','JECupdate2016FS','jetSel',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'FSSusy2016v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','JMEUncertFS2016',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'SFSusy2016v6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'subTargets' : ['leptonMaker','lepSelSusySF','PromptParticlesGenVars','GenLeptonMatch'],
                },

  'SFSusy2016DYv6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'selection'  : '"((nElectron>1) || (nMuon>1))"' ,
                 'subTargets' : ['leptonMaker','lepSelSusySF'],
                },

  'MCl1loose2016v7_jetIDtest' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom_looseJetID_noPUID', 'CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'DressedLeptons','EFTGen'],
},

  # FIXME: check btagPerJet2016, btagPerEvent
  # FIXME: Cfg 'trigMC','LeptonSF','puW'
  'MCCorr2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  # copied but still missing the MonoH triggers -> will be patched later
  'MCCorr2016v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2016v5mh' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  'MCCorr2016v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  # JERsMC2016 removed due to bugs in the jet eta "horn" region 
  'MCCorr2016v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016','JetPUID_SF_16',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars','qqHTheoryUncertainty',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ],
                },

  'MCCorr2016Susy' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016','btagPerEvent2016',
                                     'rochesterMC','trigMC','LeptonSFSusy','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2016SusyFS' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2016','btagPerJet2016FS','btagPerEvent2016FS',#'EmbeddingVeto',  
                                     'rochesterMC','trigFS','LeptonSFSusyFS','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2016Susyv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016',
                                     'btagPerJet2016','btagPerEvent2016','btagPerEvent2016Pt25','btagPerEvent2016Pt30',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK'
                                   ],
                },

  'MCCorr2016SusyFSv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2016',
                                     'btagPerJet2016FS','btagPerEvent2016FS','btagPerEvent2016FSPt25','btagPerEvent2016FSPt30',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK'],
                },

  'MCSusyCorr2016v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','ZZGen' ],
                },

  'MCSusySyst2016v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2016','btagPerEvent2016Pt25','btagPerEvent2016Pt30'
                                   ],
                },

  'FSSusyCorr2016v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2016','btagPerJet2016FS',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK'],
                },

  'FSSusySyst2016v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2016FS','btagPerEvent2016FSPt25','btagPerEvent2016FSPt30'
                                   ],
                },

  'MCTRGFixv7' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['trigMCKeepRun', 'formulasMC' , 'EFTGen' , 'JJHEFT' ] ,
					 } ,  

  'MCCorr2016_hmumu' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'formulasMC','EmbeddingVeto'],
                },

  'MCCorr2016tmp'  : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','puW','rochesterMC','l2Kin','formulasMC16tmp'],
                     'onlySample' : ['DYJetsToLL_M-50_ext2'],
                 },

  'MCMonoH2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['MHTrigMC','MHSwitch','MonoHiggsMVA','l3Kin','formulasMCMH'],
                 },

  'MCMonoH' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['MHTrigMC','MHSwitch','MonoHiggsMVA','l3Kin','formulasMCMH'],
                 },

  'DATAMonoH' : {
                     'isChain'    : True  ,
                     'do4MC'      : False  ,
                     'do4Data'    : True ,
                     'subTargets' : ['MHTrigData','MHSwitch','MonoHiggsMVA','l3Kin'],
                 },


### OLD Stuff begin

  'MCl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent','PrefCorr2017'],
                },

  'MCCorr2017OLD' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut', 'btagPerJet2017', 'btagPerEvent' ,
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 'WGammaStar',
                                  'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

  'MCCorr2017_SemiLep' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['jetSel','CleanJetCut', 
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 
                                  'rochesterMC','trigMC'],
                    },

### OLD stuff End

  'MCl1loose2017' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2017v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2017v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },

  'MCl1loose2017v7' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty','DressedLeptons','EFTGen'],
                  },

  'MCSusy2017' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','METFixEEMC2017','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2017v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','METFixEEMC2017',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2017v8' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker', 'lepSelSusy',  'JMEUncertMC' ,
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2017FS' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','METFixEEFS2017','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  #'leptonMaker','lepSelSusy','JECupdate2017FS','jetSel',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'FSSusy2017v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','METFixEEFS2017',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'SFSusy2017v6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'subTargets' : ['leptonMaker','lepSelSusySF','PromptParticlesGenVars','GenLeptonMatch'],
                },

  'SFSusy2017DYv6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'selection'  : '"((nElectron>1) || (nMuon>1))"' ,
                 'subTargets' : ['leptonMaker','lepSelSusySF'],
                },
 
  'MCCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2017v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','MHTrigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','MHSwitch','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2017v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars',  
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  'MCCorr2017v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,

                     'subTargets' : ['baseW','JERsMC2017','PrefCorr2017','btagPerJet2017','JetPUID_SF_17',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars','qqHTheoryUncertainty',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ]
                },

  'MCCorr2017Susy' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017','btagPerEvent2017',#'EmbeddingVeto', 
                                     'rochesterMC','trigMC','LeptonSFSusy','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2017SusyFS' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2017','btagPerJet2017FS','btagPerEvent2017FS',#'EmbeddingVeto',  
                                     'rochesterMC','trigFS','LeptonSFSusyFS','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2017Susyv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017',
                                     'btagPerJet2017','btagPerEvent2017','btagPerEvent2017Pt25','btagPerEvent2017Pt30',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK' ],
                },

  'MCCorr2017SusyFSv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2017',
                                     'btagPerJet2017FS','btagPerEvent2017FS','btagPerEvent2017FSPt25','btagPerEvent2017FSPt30',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK' ],
                },


  'MCSusyCorr2017v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','ZZGen' ],
                },

  'MCSusySyst2017v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2017','btagPerEvent2017Pt25','btagPerEvent2017Pt30'
                                   ],
                },

  'MCSusyCorr2017v8' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorrUL17','btagPerJetCSVWPs',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','ZZGen' ],
                },


  'FSSusyCorr2017v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PrefCorr2017','btagPerJet2017FS',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK' ],
                },

  'FSSusySyst2017v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2017FS','btagPerEvent2017FSPt25','btagPerEvent2017FSPt30'
                                   ],
                },


  'MCCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19','EmbeddingVeto'],
                },


  'PUFIXLP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['puW','formulasMCLP19'],
  },               

  'MVAFix' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : [ 'DYMVA','MonoHiggsMVA' ] ,
             }, 

  'MCl1loose2018' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2018v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2018v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },

  'MCl1loose2018v7' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'DressedLeptons','EFTGen'],
                  },

  'test2018v7' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet','l2Kin','baseW','l2tightOR2018v7','JJHEFT'],
                  },

  'MCSusy2018' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2018v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','JMEUncertMC2018',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'MCSusy2018FS' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy',#'CleanJetCut',
                                  #'leptonMaker','lepSelSusy','JECupdate2018FS','jetSel',#'CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'FSSusy2018v6loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','JMEUncertFS2018',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TopGenVars'
                                  ],
                },

  'SFSusy2018v6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'subTargets' : ['leptonMaker','lepSelSusySF','PromptParticlesGenVars','GenLeptonMatch'],
                },

  'SFSusy2018DYv6loose' : {
                 'isChain'    : True  ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'selection'  : '"((nElectron>1) || (nMuon>1))"' ,
                 'subTargets' : ['leptonMaker','lepSelSusySF'],
                },

  'MCCorr2018' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  # copied but still missing the MonoH triggers -> will be patched later
  'MCCorr2018v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2018v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  'MCCorr2018v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','JERsMC2018','btagPerJet2018','JetPUID_SF_18',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK','qqHTheoryUncertainty',  
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ]
                },

  'MCCorr2018Susy' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018','btagPerEvent2018',#'EmbeddingVeto', 
                                     'rochesterMC','trigMC','LeptonSFSusy','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2018SusyFS' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['btagPerJet2018FS','btagPerEvent2018FS',#'EmbeddingVeto',  
                                     'rochesterMC','trigFS','LeptonSFSusyFS','puW',#'l2Kin', 'l3Kin', 'l4Kin','formulasMC'
                                     ],
                },

  'MCCorr2018Susyv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018','btagPerEvent2018','btagPerEvent2018Pt25','btagPerEvent2018Pt30',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK' ],
                },

  'MCCorr2018SusyFSv6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['btagPerJet2018FS','btagPerEvent2018FS','btagPerEvent2018FSPt25','btagPerEvent2018FSPt30',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK' ],
                },

  'MCSusyCorr2018v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSFSusy','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','ZZGen' ],
                },

  'MCSusySyst2018v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2018','btagPerEvent2018Pt25','btagPerEvent2018Pt30'
                                   ],
                },

  'FSSusyCorr2018v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['btagPerJet2018FS',
                                     'rochesterMC','trigFS','trigFS_Cut','LeptonSFSusyFS','puW','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK' ],
                },

  'FSSusySyst2018v6loose' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['PtCorrReader','jetSelSusy','btagPerEvent2018FS','btagPerEvent2018FSPt25','btagPerEvent2018FSPt30'
                                   ],
                },


  'MCCorr2018v7fixJER' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','JERsMC2018','btagPerJet2018','JetPUID_SF_18',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK','qqHTheoryUncertainty',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ]
                },


  'MCGenOnly': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['PromptParticlesGenVars','GenVar', 'HiggsGenVars', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'DressedLeptons',
                                  'baseW'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/MCGenOnly_outputbranches.txt'
               },

  'l23Kin': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'subTargets' : ['l2Kin', 'l3Kin'],
            },

## ------- T&P Skims

 'MCTandP' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"(nElectron>=2 || nMuon>=2) && (Sum$(Muon_pt > 10 && abs(Muon_eta)<2.4) >1 || Sum$(Electron_pt > 10 && abs(Electron_eta)<2.5) >1)"' , 
                  'subTargets' : ['RunPeriodMC','puW','baseW'] ,
                  'onlySample' : [ 
                                  'DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2','DYJetsToLL_M-50-LO',
                                 ] ,
              }, 

  'DataTandP' : {
                  'isChain'    : True  ,
                  'do4MC'      : False  ,
                  'do4Data'    : True ,
                  'selection'  : '"(nElectron>=2 || nMuon>=2) && (Sum$(Muon_pt > 10 && abs(Muon_eta)<2.4) >1 || Sum$(Electron_pt > 10 && abs(Electron_eta)<2.5) >1)"' ,
                  'subTargets' : ['RunPeriodDATA'] ,
                  'onlySample' : [
                                  # Run2016 v6
                                  'SingleElectron_Run2016B-Nano25Oct2019_ver2-v1',
                                  'SingleElectron_Run2016C-Nano25Oct2019-v1',      
                                  'SingleElectron_Run2016D-Nano25Oct2019-v1',      
                                  'SingleElectron_Run2016E-Nano25Oct2019-v1',      
                                  'SingleElectron_Run2016F-Nano25Oct2019-v1',      
                                  'SingleElectron_Run2016G-Nano25Oct2019-v1',      
                                  'SingleElectron_Run2016H-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016B-Nano25Oct2019_ver2-v1',
                                  'SingleMuon_Run2016C-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016D-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016E-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016F-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016G-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2016H-Nano25Oct2019-v1',      
                                  # Run2017 v6
                                  'SingleElectron_Run2017B-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017C-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017D-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017E-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017F-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017B-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017C-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017D-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017E-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017F-Nano25Oct2019-v1',
                                  # Run2018 v6
                                  'EGamma_Run2018A-Nano25Oct2019-v1',      
                                  'EGamma_Run2018B-Nano25Oct2019-v1',      
                                  'EGamma_Run2018C-Nano25Oct2019-v1',      
                                  'EGamma_Run2018D-Nano25Oct2019_ver2-v1',
                                  'SingleMuon_Run2018A-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2018B-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2018C-Nano25Oct2019-v1',      
                                  'SingleMuon_Run2018D-Nano25Oct2019_ver2-v1'
                                 ] ,

              }, 

  'addTnPMuon' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.addTnpTree' ,
                  'declare'  : 'TnPMu = lambda : addTnpTree(int("RPLME_YEAR"),"Muon")', 
                  'module'   : 'TnPMu()', 
                  'onlySample' : ['DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2','DYJetsToLL_M-50-LO',
                                  # Run2016 v6
                                  'SingleMuon_Run2016B-Nano25Oct2019_ver2-v1',
                                  'SingleMuon_Run2016C-Nano25Oct2019-v1',
                                  'SingleMuon_Run2016D-Nano25Oct2019-v1',
                                  'SingleMuon_Run2016E-Nano25Oct2019-v1',
                                  'SingleMuon_Run2016F-Nano25Oct2019-v1',
                                  'SingleMuon_Run2016G-Nano25Oct2019-v1',
                                  'SingleMuon_Run2016H-Nano25Oct2019-v1',
                                  # Run2017 v6
                                  'SingleMuon_Run2017B-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017C-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017D-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017E-Nano25Oct2019-v1',
                                  'SingleMuon_Run2017F-Nano25Oct2019-v1',
                                  # Run2018 v6
                                  'SingleMuon_Run2018A-Nano25Oct2019-v1',
                                  'SingleMuon_Run2018B-Nano25Oct2019-v1',
                                  'SingleMuon_Run2018C-Nano25Oct2019-v1',
                                  'SingleMuon_Run2018D-Nano25Oct2019_ver2-v1'
                                 ] ,

                 },

  'addTnPEle' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.addTnpTree' ,
                  'declare'  : 'TnPEle = lambda : addTnpTree(int("RPLME_YEAR"),"Electron")',
                  'module'   : 'TnPEle()', 
                  'onlySample' : ['DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2','DYJetsToLL_M-50-LO',
                                  # Run2016 v6
                                  'SingleElectron_Run2016B-Nano25Oct2019_ver2-v1',
                                  'SingleElectron_Run2016C-Nano25Oct2019-v1',
                                  'SingleElectron_Run2016D-Nano25Oct2019-v1',
                                  'SingleElectron_Run2016E-Nano25Oct2019-v1',
                                  'SingleElectron_Run2016F-Nano25Oct2019-v1',
                                  'SingleElectron_Run2016G-Nano25Oct2019-v1',
                                  'SingleElectron_Run2016H-Nano25Oct2019-v1',
                                  # Run2017 v6
                                  'SingleElectron_Run2017B-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017C-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017D-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017E-Nano25Oct2019-v1',
                                  'SingleElectron_Run2017F-Nano25Oct2019-v1',
                                  # Run2018 v6
                                  'EGamma_Run2018A-Nano25Oct2019-v1',
                                  'EGamma_Run2018B-Nano25Oct2019-v1',
                                  'EGamma_Run2018C-Nano25Oct2019-v1',
                                  'EGamma_Run2018D-Nano25Oct2019_ver2-v1',
                                 ] ,

                 },

## ------- WgStar MC:

  'MCWgStar2017' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel', 
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar'],
                     'onlySample' : [
                                   'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50', 'DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                   'DYJetsToLL_M-5to50-LO','DYJetsToLL_M-50-LO-ext1',
                                   'TTTo2L2Nu', 'ST_tW_antitop', 'ST_tW_top', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ZZTo2L2Nu',
                                   'ZZTo4L', 'ZZTo2L2Q', 
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','WZTo3LNu_mllmin01','WZTo3LNu', 'Zg', 
                                 ]
                   },

  'MCWgStarCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

   'MCWgStarCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
                    }, 

#   ---> v5

 'MCWgStar201Xv5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel','jetSelCustom',
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar','ggHTheoryUncertainty', 'DressedLeptons'],
                     'onlySample' : [
                                   'Wg500',
                                   'Wg_AMCNLOFXFX','Wg_AMCNLOFXFX_ext2','Wg_AMCNLOFXFX_ext3',
                                   'WZTo3LNu','WZTo3LNu_ext1',
                                   'WZTo3LNu_mllmin01',
                                   'WZTo3LNu_powheg',
                                   'Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50','DYJetsToLL_M-10to50_ext1',
                                   'DYJetsToLL_M-50','DYJetsToLL_M-50_ext','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2', 
                                   'DYJetsToLL_M-5to50-LO',
                                   'DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2',
                                   'TTTo2L2Nu', 
                                   'ST_tW_antitop','ST_tW_antitop_ext1','ST_tW_antitop_noHad','ST_tW_antitop_noHad_ext1', 
                                   'ST_tW_top','ST_tW_top_ext1','ST_tW_top_noHad','ST_tW_top_noHad_ext1', 
                                   'ST_s-channel','ST_s-channel_ext1', 
                                   'ST_t-channel_antitop', 
                                   'ST_t-channel_top', 
                                   'ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2',
                                   'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2', 
                                   'ZZTo2L2Q',
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','Zg',
                                 ]
                   },

  'MCWgStarCorr2016v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   },

  'MCWgStarCorr2017v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   },

  'MCWgStarCorr2018v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   }, 

#   ---> v7

 'MCWgStar201Xv7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar','ggHTheoryUncertainty', 'qqHTheoryUncertainty' , 'DressedLeptons','EFTGen'],
                     'onlySample' : [
                                   'Wg500',
                                   'Wg_AMCNLOFXFX','Wg_AMCNLOFXFX_ext2','Wg_AMCNLOFXFX_ext3',
                                   'WZTo3LNu','WZTo3LNu_ext1',
                                   'WZTo3LNu_mllmin01',
                                   'WZTo3LNu_powheg',
                                   'Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50','DYJetsToLL_M-10to50_ext1',
                                   'DYJetsToLL_M-50','DYJetsToLL_M-50_ext','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2',
                                   'DYJetsToLL_M-5to50-LO',
                                   'DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2',
                                   'TTTo2L2Nu',
                                   'ST_tW_antitop','ST_tW_antitop_ext1','ST_tW_antitop_noHad','ST_tW_antitop_noHad_ext1',
                                   'ST_tW_top','ST_tW_top_ext1','ST_tW_top_noHad','ST_tW_top_noHad_ext1',
                                   'ST_s-channel','ST_s-channel_ext1',
                                   'ST_t-channel_antitop',
                                   'ST_t-channel_top',
                                   'ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2',
                                   'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2',
                                   'ZZTo2L2Q',
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','Zg',
                                 ]
                   },

  'MCWgStarCorr2016v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016','JetPUID_SF_16',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ], 
                   },

  'MCWgStarCorr2017v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','JERsMC2017','PrefCorr2017','btagPerJet2017','JetPUID_SF_17',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ],
                   },

  'MCWgStarCorr2018v7' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','baseW','JERsMC2018','btagPerJet2018','JetPUID_SF_18',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',                                     'wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                                     'CorrFatJetMC', 'CleanFatJet', 'BoostedWtagSF' ],
                   },

## ------- DATA:
    
  'DATAl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData', 'formulasDATA'
                                  ],
                },

  'DATAl1loose2016v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  #'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                 },

  'DATAl1loose2016v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet','rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                 },
    
  'DATASusy2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2016Data' ###,'formulasDATA'
                                  ],
                },
    
  'DATASusy2016v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2016Data','btagPerEvent2016DataPt25','btagPerEvent2016DataPt30' ###,'formulasDATA'
                                  ],
                },

  'DATALatino2016v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelLatino','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2016Data','btagPerEvent2016DataPt25','btagPerEvent2016DataPt30' ###,'formulasDATA'
                                  ],
                },

  'DATAl1loose2016v7': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet','rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                 },

  'DATAl1loose2017': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },

  'DATAl1loose2017v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },

  'DATAl1loose2017v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },

  'DATAl1loose2017v7': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },
    
  'DATASusy2017': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData', 'btagPerEvent2017Data' ###,'formulasDATA'
                                  ],
                },
    
  'DATASusy2017v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2017Data','btagPerEvent2017DataPt25','btagPerEvent2017DataPt30' ###,'formulasDATA'
                                  ],
                },

  'DATALatino2017v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelLatino','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2017Data','btagPerEvent2017DataPt25','btagPerEvent2017DataPt30' ###,'formulasDATA'
                                  ], 
                },

  'DATASusy2017v8': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData', 'btagPerEventDeepCSVWPsData'
                                  ],
                },


# 'DATAl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : False ,
#                 'do4Data'    : True  ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
#               }, 

  'DATAl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                },

  'DATACorr2017' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['rochesterDATA','jetSel','CleanJetCut','l2Kin', 'l3Kin', 'l4Kin','formulasDATA'],
                },

  'DATAl1loose2018': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },


  'DATAl1loose2018v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },


  'DATAl1loose2018v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },

  'DATAl1loose2018v7': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },
                                
  'DATASusy2018': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData', 'btagPerEvent2018Data' ###,'formulasDATA'
                                  ],
                },
                                
  'DATASusy2018v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelSusy','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2018Data','btagPerEvent2018DataPt25','btagPerEvent2018DataPt30' ###,'formulasDATA'
                                  ],
                },

  'DATALatino2018v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSelLatino','jetSelSusy','rochesterDATA' , ###'l2Kin', 'l3Kin', 'l4Kin',
                                  'trigData','btagPerEvent2018Data','btagPerEvent2018DataPt25','btagPerEvent2018DataPt30' ###,'formulasDATA'
                                  ],
                },


  'jetSelfix': {
                  'isChain'    : True  ,
                  'do4MC'      : True ,
                  'do4Data'    : True  , 
                  'subTargets' : ['jetSel','l2Kin', 'l3Kin', 'l4Kin']
               },

## ------- WgStar DATA:

    'DATAWgStar2017v2' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSel','CleanJetCut' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

   'DATAWgStar2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','WgSSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },


##     --> v5

    'DATAWgStar2016v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },


    'DATAWgStar2017v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

    'DATAWgStar2018v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],

                   },

##     --> v7

    'DATAWgStar201Xv7' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'jetSelCustom','CorrFatJetData','CleanFatJet','rochesterDATA' , 
                                  'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                   },


## ------- EMBEDDING:

    'Embedding' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

## ------- HIGH MASS:

    'Semilep2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  :'"( Alt$( Lepton_pt[1],0) < 10 )"',
                  'subTargets' : ['l1tightOR2016v5','PreselFatJet','whadJetSel','wlepMaker','HMlnjjVars','HMDNNProdSemi','HMDNNNeutSemi'],
                  #'onlySample' : LNuQQSamples,
                   },

    'Semilep2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  :'"( Alt$( Lepton_pt[1],0) < 10 )"',
                  'subTargets' : ['l1tightOR2017v5','PreselFatJet','whadJetSel','wlepMaker','HMlnjjVars','HMDNNProdSemi','HMDNNNeutSemi'],
                  #'onlySample' : LNuQQSamples,
                   },

    'Semilep2018' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  :'"( Alt$( Lepton_pt[1],0) < 10 )"',
                  'subTargets' : ['l1tightOR2018v5','PreselFatJet','whadJetSel','wlepMaker','HMlnjjVars','HMDNNProdSemi','HMDNNNeutSemi'],
                  #'onlySample' : LNuQQSamples,
                   },

    'HighMass' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['HMvars','HMDNNProd','HMDNNCateg','HMDNNNeut'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },
   

    'HMlnjjSel'  : {
                  'isChain'    : True,
                  'do4MC'      : True,
                  'do4Data'    : True,
                  'selection'  : '"(Lepton_pt[0] > 30 && (Alt$(Lepton_pt[1], 0) < 10))"',
                  'subTargets' : ['HMlnjjVars'],
		  },

    'HMlnjjSelBWRew_Dev'  : {
                  'isChain'    : True ,
		  'do4MC'	: True ,
		  'do4Data'	: True,
                  'subTargets' : ['HMlnjjLepSel','BWReweight'],
		  },
                  #'selection'  : '"(Lepton_pt[0] > 30 && (Alt$(Lepton_pt[1], 0) < 10))"',
                  #'subTargets' : ['BWReweight'],

    'HMlnjjFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=1, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=1.0, over_jetR=0.8)',
                  'module'     : 'fatjetMaker()'
    },

    'HMlnjjLepSel': {
    	          'isChain'	: False	,
		  'do4MC'	: True	,
		  'do4Data'	: True	,
                  'selection'  :'"(  Lepton_pt[0]>30 \
		  	&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
		  	||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
		  	&& ( ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
		  	||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
		  		)"',
		  },
		  #	|| Alt$( !Lepton_isLoose[1],1 ) )


## ------- HIGH MASS & VBS COMBINATION CHAINS:

    'MCCombJJLNu2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : CombJJLNu_preselections["2016"]["MC"],
                  'subTargets' : ['VBSjjlnu_pairing', 'VBSjjlnu_kin' ,
                                  'whadJetSel', 'wlepMaker', 'wwNLL', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi',
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],
                  'onlySample' : vbsjjlnu_samples_mc  + SemiLepHighMassSamples_2016 + MonoHjjlnu_samples_2016,
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

    'DATACombJJLNu2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : CombJJLNu_preselections["2016"]["DATA"],
                  'subTargets' : ['fakeWstep1l', 'VBSjjlnu_pairing', 'VBSjjlnu_kin', 
                                  'whadJetSel', 'wlepMaker', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi', 
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],
                  'onlySample' : vbsjjlnu_samples_data2016,
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

    'MCCombJJLNu2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : CombJJLNu_preselections["2017"]["MC"],
                  'subTargets' : ['VBSjjlnu_pairing', 'VBSjjlnu_kin',
                                  'whadJetSel', 'wlepMaker', 'wwNLL', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi',
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],

                  'onlySample' : vbsjjlnu_samples_mc  + SemiLepHighMassSamples_2017 + MonoHjjlnu_samples_2017,#vbsjjlnu_samples_signal
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

    'DATACombJJLNu2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : CombJJLNu_preselections["2017"]["DATA"],
                  'subTargets' : ['fakeWstep1l', 'VBSjjlnu_pairing', 'VBSjjlnu_kin', 
                                  'whadJetSel', 'wlepMaker', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi',
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],
                  'onlySample' : vbsjjlnu_samples_data2017,
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

    'MCCombJJLNu2018' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection'  : CombJJLNu_preselections["2018"]["MC"],
                  'subTargets' :  ['VBSjjlnu_pairing', 'VBSjjlnu_kin', 
                                  'whadJetSel', 'wlepMaker', 'wwNLL', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi',
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],
                  'onlySample' : vbsjjlnu_samples_mc + SemiLepHighMassSamples_2018 + MonoHjjlnu_samples_2018,#vbsjjlnu_samples_signal
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

    'DATACombJJLNu2018' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : CombJJLNu_preselections["2018"]["DATA"],
                  'subTargets' : ['fakeWstep1l','VBSjjlnu_pairing','VBSjjlnu_kin', 
                                  'whadJetSel', 'wlepMaker', 'HMlnjjVars', 'HMDNNProdSemi', 'HMDNNNeutSemi',
                                  'l2Kin', 'MHSemiLepVars', 'MHSemiLepMVA'],
                  'onlySample' : vbsjjlnu_samples_data2018,
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/removeHLT.txt'
                   },

# mnonoH dileptonic skims

  'monoHSkim2016' : { 
                  'isChain'  : True ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'selection': '"(nLepton >= 2 && \
                               LepCut2l__ele_mva_90p_Iso2016__mu_cut_Tight80x == 1 && \
                               Alt$(Lepton_pt[2],0) < 10. && \
                               Lepton_pdgId[0]*Lepton_pdgId[1] < 0 && \
                               Lepton_pt[0] > 25. && \
                               Lepton_pt[1] > 20. && \
                               mll > 12. && \
                               PuppiMET_pt > 20. && \
                               ptll > 30.)"',
                  'subTargets' : ['mT2Davis', 'MHDileptonMVAsplit','MHGetParametrizedMass_darkHiggs','MHGetParametrizedMass_2HDMa', 'MHDiLepVars2016'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/monoHskim.txt'
               },

  'monoHSkim2017' : { 
                  'isChain'  : True ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'selection': '"(nLepton >= 2 && \
                               LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW == 1 && \
                               Alt$(Lepton_pt[2],0) < 10. && \
                               Lepton_pdgId[0]*Lepton_pdgId[1] < 0 && \
                               Lepton_pt[0] > 25. && \
                               Lepton_pt[1] > 20. && \
                               mll > 12. && \
                               PuppiMET_pt > 20. && \
                               ptll > 30.)"',
                  'subTargets' : ['mT2Davis', 'MHDileptonMVAsplit','MHGetParametrizedMass_darkHiggs','MHGetParametrizedMass_2HDMa', 'MHDiLepVars2017'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/monoHskim.txt'
               },

  'monoHSkim2018' : { 
                  'isChain'  : True ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'selection': '"(nLepton >= 2 && \
                               LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW == 1 && \
                               Alt$(Lepton_pt[2],0) < 10. && \
                               Lepton_pdgId[0]*Lepton_pdgId[1] < 0 && \
                               Lepton_pt[0] > 25. && \
                               Lepton_pt[1] > 20. && \
                               mll > 12. && \
                               PuppiMET_pt > 20. && \
                               ptll > 30.)"',
                  'subTargets' : ['mT2Davis', 'MHDileptonMVAsplit','MHGetParametrizedMass_darkHiggs','MHGetParametrizedMass_2HDMa', 'MHDiLepVars2018'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/monoHskim.txt'
               },



# ------------------------------------------------ MODULES ---------------------------------------------------

## ------- MODULES: Exo analyses                                                                                                                                    
    'TopPlusDMRunIILegacy': {
                   'isChain'    : True ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                   'subTargets' : ['mT2Davis'],
    },

    'mT2Davis': {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                   'module'     : 'mt2Producer()' ,
    },

## ------- MODULES: MonoHiggs

#### MHTrigs step only works for 2016 and 2017 for now !!!!!!
  'MHTrigData' : { 
                  'isChain'  : False ,
                  'do4MC'    : False ,
                  'do4Data'  : True  ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigData = lambda : TrigMaker("RPLME_CMSSW",True,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigData()',
               },

  'MHTrigMC'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },
####

  'MHDiLepVars2016' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHDiLepVars2016' ,
                  'module'   : 'MHDiLepVars2016()',
               },
  'MHDiLepVars2017' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHDiLepVars2017' ,
                  'module'   : 'MHDiLepVars2017()',
               },
  'MHDiLepVars2018' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHDiLepVars2018' ,
                  'module'   : 'MHDiLepVars2018()',
               },

  'MHDileptonMVAsplit' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MVAsplitter' ,
                  'module'   : 'MVAsplitter("RPLME_SAMPLE", "LatinoAnalysis/NanoGardener/python/data/MH2HDMaBDTsplitter_cfg.py", "EventSplit")',
               },

  'MHGetParametrizedMass_darkHiggs' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHParametrizedMasses' ,
                  'module'   : 'MHParametrizedMasses("RPLME_SAMPLE", "LatinoAnalysis/NanoGardener/python/data/MHParametrizedMasses_cfg.py", "darkHiggs")',
               },

  'MHGetParametrizedMass_2HDMa' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHParametrizedMasses' ,
                  'module'   : 'MHParametrizedMasses("RPLME_SAMPLE", "LatinoAnalysis/NanoGardener/python/data/MHParametrizedMasses_cfg.py", "2HDMa")',
               },

  'MH2HDMaBDTsplit' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MVAsplitter' ,
                  'module'   : 'MVAsplitter("RPLME_SAMPLE", "LatinoAnalysis/NanoGardener/python/data/MH2HDMaBDTsplitter_cfg.py", "MH2HDMaBDT")',
               },
  'MHSemiLepVars' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MHSemiLepVars' ,
                  'module'   : 'MHSemiLepVars()',
               },
  'MHSemiLepMVA' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MHSemiLepMVA = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/SemiLep_cfg.py")',
                  #'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MVA/monoHiggs/SemiLep/2HDMa/2HDMaBDT_cfg.py")',
                  'module'   : 'MHSemiLepMVA()',
               },

  'MHskim4BDT' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/MHskim4BDT_branches.txt',
                  #'selection': '"MH2HDMaBDT_isTrainingEvent && idx_j1 > -0.5 && Whad_mass > 65. && Whad_mass < 105."',
                  'selection': '"(nLepton >= 1 && \
                               Alt$(Lepton_pt[1],0) < 10. && \
                               (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5) && \
                               PuppiMET_pt > 50. && \
                               Lepton_pt[0] > 30 && \
                               Sum$(CleanJet_pt>30.)>=2 && \
                               idx_j1 > -0.5 && \
                               MH2HDMaBDT_isTrainingEvent && \
                               Whad_mass > 65. && Whad_mass < 105.)"',
               },

  'MHSwitch' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.Switch' ,
                  'declare'  : 'MHSwitch = lambda : Switch(cmssw="RPLME_CMSSW", cfg_path="LatinoAnalysis/NanoGardener/python/data/switch/MH_triggerSwitch_cfg.py")',
                  'module'   : 'MHSwitch()',
               },

  'MonoHiggsMVA' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py")',
                  'module'   : 'MonoHiggsMVA()',
               },

               
  'MonoHiggsMVA_ElepTup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_ElepTup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="ElepTup")',
                  'module'   : 'MonoHiggsMVA_ElepTup()',
               },

               
  'MonoHiggsMVA_ElepTdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_ElepTdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="ElepTdo")',
                  'module'   : 'MonoHiggsMVA_ElepTdo()',
               },

  'MonoHiggsMVA_MupTup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MupTup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MupTup")',
                  'module'   : 'MonoHiggsMVA_MupTup()',
               },

               
  'MonoHiggsMVA_MupTdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MupTdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MupTdo")',
                  'module'   : 'MonoHiggsMVA_MupTdo()',
               },
  'MonoHiggsMVA_METup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_METup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="METup")',
                  'module'   : 'MonoHiggsMVA_METup()',
               },

               
  'MonoHiggsMVA_METdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_METdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="METdo")',
                  'module'   : 'MonoHiggsMVA_METdo()',
               },
  'MonoHiggsMVA_JESup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JESup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JESup")',
                  'module'   : 'MonoHiggsMVA_JESup()',
               },

               
  'MonoHiggsMVA_JESdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JESdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JESdo")',
                  'module'   : 'MonoHiggsMVA_JESdo()',
               },

  'MonoHiggsMVA_JERup' : {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JERup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JERup")',
                  'module'   : 'MonoHiggsMVA_JERup()',
               },


  'MonoHiggsMVA_JERdo' : {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JERdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JERdo")',
                  'module'   : 'MonoHiggsMVA_JERdo()',
               },

## ------------------------MODULES : EFT analysis -----------------------------------

  'EFTaBDTsplit' : {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.MVAsplitter' ,
                  'module'   : 'MVAsplitter("RPLME_SAMPLE", "LatinoAnalysis/NanoGardener/python/data/EFTaBDTsplitter_cfg.py", "EFTaBDT")',
                  'onlySample' : ['H0PM_ToWWTo2L2Nu','H0PH_ToWWTo2L2Nu','H0L1_ToWWTo2L2Nu','H0M_ToWWTo2L2Nu','H0PHf05_ToWWTo2L2Nu','H0Mf05_ToWWTo2L2Nu','VBF_H0PM_ToWWTo2L2Nu','VBF_H0PH_ToWWTo2L2Nu','VBF_H0L1_ToWWTo2L2Nu','VBF_H0M_ToWWTo2L2Nu','VBF_H0PHf05_ToWWTo2L2Nu','VBF_H0Mf05_ToWWTo2L2Nu','WH_H0PM_ToWWTo2L2Nu','WH_H0PH_ToWWTo2L2Nu','WH_H0L1_ToWWTo2L2Nu','WH_H0M_ToWWTo2L2Nu','WH_H0PHf05_ToWWTo2L2Nu','WH_H0Mf05_ToWWTo2L2Nu','ZH_H0PM_ToWWTo2L2Nu','ZH_H0PH_ToWWTo2L2Nu','ZH_H0L1_ToWWTo2L2Nu','ZH_H0M_ToWWTo2L2Nu','ZH_H0PHf05_ToWWTo2L2Nu','ZH_H0Mf05_ToWWTo2L2Nu','H0L1f05_ToWWTo2L2Nu','VBF_H0L1f05_ToWWTo2L2Nu','ZH_H0L1f05_ToWWTo2L2Nu','WH_H0L1f05_ToWWTo2L2Nu'],
               },

  'EFTskim4analysis' : {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'selection': '"EFTaBDT_isAnalysisEvent"',
               },

  'EFTskim4BDT' : {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'selection': '"EFTaBDT_isTrainingEvent"',
                 # 'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/EFTskim4BDT_branches.txt',
                 # 'selection': '"PuppiMET_pt > 30 \
                  #              && WH3l_mOSll > 12 \
                  #              && EFTaBDT_isTrainingEvent \
                  #              && Lepton_pt[0] > 25 \
                  #              && Lepton_pt[1] > 20 \
                  #              && Lepton_pt[2] > 15 \
                  #              && Alt$(Lepton_pt[3],0)<10 \
                  #              && abs(WH3l_chlll) == 1 "',
                              },
                 #'selection': '"PuppiMET_pt > 20 \
                 #              && Lepton_pt[0] > 25 \
                 #              && Lepton_pt[1] > 15 \
                 #              && Lepton_pt[2] > 10 \
                 #              && Lepton_pt[3] > 10 \
                 #              && chllll_zh4l == 0 \
                 #              && Alt$(Lepton_pt[4],0)<10 \
                 #              && abs(z0Mass_zh4l-91.1876)< 15 \
                 #              && mll > 12"',
                 #             },

## ------- MODULES: MC Kinematic
  
  'PromptParticlesGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PromptParticlesGenVarsProducer' ,
                  'declare'    : 'PromptParticlesGenVars = lambda : PromptParticlesGenVarsProducer()',
                  'module'     : 'PromptParticlesGenVars()',
                  } , 


  'GenVar'       : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenVarProducer' ,
                  'declare'    : 'GenVar = lambda : GenVarProducer()',
                  'module'     : 'GenVar()' ,
                   },

  'GenLeptonMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenLeptonMatchProducer' ,
                  'declare'    : 'GenLeptonMatch = lambda : GenLeptonMatchProducer()',
                  'module'     : 'GenLeptonMatch()' ,
                   },

  'TriggerObjectMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TriggerObjectMatchProducer' ,
                  'declare'    : 'TriggerObjectMatch = lambda : TriggerObjectMatchProducer()',
                  'module'     : 'TriggerObjectMatch()' ,
                   },

   'HiggsGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HiggsGenVarsProducer' ,
                  'declare'    : 'HiggsGenVars = lambda : HiggsGenVarsProducer()',
                  'module'     : 'HiggsGenVars()',
                  } ,                 

   'DressedLeptons': {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.DressedLeptonProducer' ,
                   'declare'    : 'dressedLeptons = lambda : DressedLeptonProducer(0.3)',
                   'module'     : 'dressedLeptons()' 
                  },

   'ggHTheoryUncertainty':  {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.GGHUncertaintyProducer' ,
                   'declare'    : 'ggHUncertaintyProducer = lambda : GGHUncertaintyProducer()',
                   'module'     : 'ggHUncertaintyProducer()',
                   'onlySample' : [
                                  'GluGluHToWWTo2L2NuPowheg_M125_PrivateNano',
                                  'GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2NuPowhegNNLOPS_M125_private',
                                  'GluGluHToWWTo2L2NuPowhegNNLOPS_M125',
                                  'GGHjjToWWTo2L2Nu_minloHJJ_M125'
                                  ]
                  },    
   'qqHTheoryUncertainty':  {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.QQHUncertaintyProducer' ,
                   'declare'    : 'qqHUncertaintyProducer = lambda : QQHUncertaintyProducer()',
                   'module'     : 'qqHUncertaintyProducer()',
                   'onlySample' : [
                                  'VBFHToWWTo2L2NuPowheg_M125',
                                  'VBFHToWWTo2L2Nu_M125',
                                  'VBFHToWWTo2L2NuPowheg_M125_CP5Up',
                                  'VBFHToWWTo2L2Nu_M125_CP5Up',
                                  'VBFHToWWTo2L2NuPowheg_M125_CP5Down',
                                  'VBFHToWWTo2L2Nu_M125_CP5Down',
                                  'HWminusJ_HToWW_LNu_M125',
                                  'HWplusJ_HToWW_LNu_M125',
                                  'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToWW_M125',
                                  'HZJ_HToWWTo2L2Nu_M125',
                                  'HZJ_HToWWTo2L2Nu_ZTo2L_M125',
                                  'HZJ_HToWW_M125'
                                  ]
                  },    

   'TopGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TopGenVarsProducer' ,
                  'declare'    : 'TopGenVars = lambda : TopGenVarsProducer()',
                  'module'     : 'TopGenVars()',
                  'onlySample' : [
                                  'TTTo2L2Nu',
                                  'TTTo2L2Nu_PSWeights_CP5Down',
                                  'TTTo2L2Nu_PSWeights_CP5Up',
                                  'TTTo2L2Nu_PSWeights',
                                  'TTToSemiLeptonic',
                                  'TTWjets',
                                  'TTWjets_ext1'
                                  'TTZjets',
                                  'TTZjets_ext1',
                                  'ST_s-channel',
                                  'ST_s-channel_ext1',
                                  'ST_t-channel_antitop',
                                  'ST_t-channel_top',
                                  'ST_tW_antitop',
                                  'ST_tW_antitop_ext1',
                                  'ST_tW_top',
                                  'ST_tW_top_ext1',
                                 ]
                  } ,

    'wwNLL' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.wwNLLcorrectionWeightProducer' ,
                  'declare'    : 'wwNLL = lambda : wwNLLcorrectionWeightProducer()',
                  'module'     : 'wwNLL()',
                  'onlySample' : ['WW-LO', 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down', 'WWToLNuQQ', 'WWToLNuQQ_ext1', 'WWToLNuQQ_AMCNLOFXFX']
                  } ,

    'wwNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wwNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("ww")',
                  'module'     : 'wwNLOEWK()',
                  'onlySample' : [ 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down',
                                  'WWToLNuQQ', 'WWToLNuQQ_ext1', 'WWToLNuQQ_AMCNLOFXFX'
                                  ]
                  } ,
    'wwNLOEWK2' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vv2lnujjEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wwNLOEWK2 = lambda : qq2vv2lnujjEWKcorrectionsWeightProducer()',
                  'module'     : 'wwNLOEWK2()',
                  'onlySample' : [ 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down',
                                  'WmToLNu_WmTo2J_QCD', 'WpToLNu_WpTo2J_QCD', 'WpToLNu_WmTo2J_QCD', 'WpTo2J_WmToLNu_QCD',
                                  'WWToLNuQQ', 'WWToLNuQQ_ext1', 'WWToLNuQQ_AMCNLOFXFX'
                                  ]
                  } ,


    'wzNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("wz")',
                  'module'     : 'wzNLOEWK()',
                  'onlySample' : ['WZTo3LNu', 'WZTo3LNu_ext1', 'WZTo2L2Q', 'WZTo3LNu_mllmin01', 'WZTo3LNu_powheg',
                                  'WmTo2J_ZTo2L_QCD', 'WmToLNu_ZTo2J_QCD', 'WpTo2J_ZTo2L_QCD', 'WpToLNu_ZTo2J_QCD'
                                  ]
                  } ,

    'zzNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'zzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("zz")',
                  'module'     : 'zzNLOEWK()',
                  'onlySample' : ['ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2', 'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2', 'ZZTo2L2Q',
                                  'ZTo2L_ZTo2J_QCD'
                                  ]
                  } ,

    'wNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("w")',
                  'module'     : 'wNLOEWK()',
                  'onlySample' : [
                                  ####
                                  'WJetsToLNu-LO','WJetsToLNu-LO_ext1'
                                  'WJetsToLNu',
                                  'WJetsToLNu_HT70_100','WJetsToLNu_HT100_200',
                                  'WJetsToLNu_HT200_400','WJetsToLNu_HT400_600',
                                  'WJetsToLNu_HT600_800','WJetsToLNu_HT800_1200',
                                  'WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  'WJetsToLNu_Pt50to100',
                                  'WJetsToLNu_Pt100to250',
                                  'WJetsToLNu_Pt250to400',
                                  'WJetsToLNu_Pt400to600',
                                  'WJetsToLNu_Pt600toInf', 
                                  'WJetsToLNu_Pt100To250_ext4', 'WJetsToLNu_Pt250To400_ext4', 
                                  'WJetsToLNu_Pt400To600_ext4', 'WJetsToLNu_Pt600ToInf_ext4',
                                  'WJetsToLNu_Wpt100t0200_ext1','WJetsToLNu_Wpt200toInf_ext1', 
                                  'WJetsToLNu-LO', 'WJetsToLNu-LO_ext1',
                                  'WJetsToLNu_0J','WJetsToLNu_1J','WJetsToLNu_2J',
                                  'WJetsToLNu-0J','WJetsToLNu-1J','WJetsToLNu-2J',
                                  'WJetsToLNu-LO_1J', 'WJetsToLNu-LO_2J','WJetsToLNu-LO_3J', 'WJetsToLNu-LO_4J',
                                  ]
                  } ,

    'zNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
                  'declare'    : 'zNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("z")',
                  'module'     : 'zNLOEWK()',
                  'onlySample' : [ 
                                   #### DY
                                  'DYJetsToLL_M-5to50-LO',
                                  'DYJetsToLL_M-10to50',
                                  'DYJetsToLL_M-50','DYJetsToLL_M-50_ext1',
                                  'DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2',
                                  'DYJetsToLL_M-10to50-LO-ext1',
                                  'DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-70to100',
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-100to200_ext1',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-200to400_ext1',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-400to600_ext1',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toinf',

                                  'DYJetsToLL_M-5to50_HT-70to100', 
                                  'DYJetsToLL_M-5to50_HT-100to200',
                                  'DYJetsToLL_M-5to50_HT-100to200_ext1',
                                  'DYJetsToLL_M-5to50_HT-200to400',
                                  'DYJetsToLL_M-5to50_HT-200to400_ext1',
                                  'DYJetsToLL_M-5to50_HT-400to600',
                                  'DYJetsToLL_M-5to50_HT-400to600_ext1',
                                  'DYJetsToLL_M-5to50_HT-600toinf_ext1',
                                  'DYJetsToLL_M-5to50_HT-600toinf',
                                                        
                                  ]
                  } ,


#
#  This woudl be for Z>nunu sample, but we currently don't use it
#
#    'zvvNLOEWK' : {
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
#                  'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("zvv")',
#                  'module'     : 'wNLOEWK()',
#                  'onlySample' : [''
#                                  ]
#                  } ,


    'WGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStarV2()',
                  'module'     : 'wGS()',
                  } ,

    'redoWGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStar()',
                  'module'     : 'wGS()',
                  'onlySample' : ['WZTo3LNu','Wg_MADGRAPHMLM','WZ','WZTo2L2Q'],
                  } ,

    'BWReweight' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BWEwkSingletReweighter' ,
                  'declare'    : 'BWEwkSingRew = lambda : BWEwkSingletReweighter(year=RPLME_YEAR)',
                  'module'     : 'BWEwkSingRew()',
                  'onlySample' : TwoL2NuSamples + LNuQQSamples,
               },

    'MelaDisc' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MelaDiscriminator' ,
                  'declare'    : 'MelaDisc = lambda : MelaDiscClass(year=RPLME_YEAR)',
                  'module'     : 'MelaDisc()',
               },

    'HMvars' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMvariables' ,
                  'declare'    : 'HMvars = lambda : HighMassVariables()',
                  'module'     : 'HMvars()',
               },

    'HMDNNCateg' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_categ' ,
                  'declare'    : 'HMDNNCa = lambda : ApplyDNN_Category()',
                  'module'     : 'HMDNNCa()',
               },

    'HMDNNNeut' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_neut' ,
                  'declare'    : 'HMDNNNe = lambda : ApplyDNN_Neutrino()',
                  'module'     : 'HMDNNNe()',
               },

    'HMDNNNeutSemi' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_neut_semi' ,
                  'declare'    : 'HMDNNNeSem = lambda : ApplyDNN_Neutrino_Semi()',
                  'module'     : 'HMDNNNeSem()',
               },

    'HMDNNProd' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_prod' ,
                  'declare'    : 'HMDNNPr = lambda : ApplyDNN_Production()',
                  'module'     : 'HMDNNPr()',
               },

    'HMDNNProdSemi' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMDNN_prod_semi' ,
                  'declare'    : 'HMDNNPrSem = lambda : ApplyDNN_Production_Semi()',
                  'module'     : 'HMDNNPrSem()',
               },

    'HMlnjjVarsGen' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVarsGen' ,
                  'declare'    : 'HMlnjjVarsGen = lambda : HMlnjjVarsGenClass("MC")',
                  'module'     : 'HMlnjjVarsGen()',
               },

    'HMlnjjVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars' ,
                  'declare'    : 'HMlnjjVars = lambda : HMlnjjVarsClass(RPLME_YEAR)',
                  'module'     : 'HMlnjjVars()',
               },

    'HMlnjjVars_Dev' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev' ,
                  'declare'    : 'HMlnjjVars_Dev = lambda : HMlnjjVarsClass_Dev(RPLME_YEAR)',
                  'module'     : 'HMlnjjVars_Dev()',
               },


    'assignRun': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RunAssigner' ,
                  'declare'    : 'assignRun = lambda: RunAssigner("RPLME_CMSSW")',
                  'module'     : 'assignRun()',
            },

## ------- MODULES: Object Handling

  'Dummy' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Dummy' ,
                  'module'     : 'Dummy()',
            },

  'leptonMaker': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonMaker' ,
                  'declare'    : 'leptonMaker = lambda : LeptonMaker()' ,
                  'module'     : 'leptonMaker()' ,
               }, 

   'lepSel': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 1)' ,
                  'module'     : 'leptonSel()' ,
               },

   'lepSelLatino': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 2)' ,
                  'module'     : 'leptonSel()' ,
               },

   'lepSelSusy': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 2, "LatinoAnalysis/NanoGardener/python/data/LeptonSelSUSY_cfg.py")' ,
                  'module'     : 'leptonSel()' ,
               },

   'lepSelSusySF': {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                    'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 0, "LatinoAnalysis/NanoGardener/python/data/LeptonSelSUSY_cfg.py")' ,
                    'module'     : 'leptonSel()' ,
               },

   'WgSSel' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "WgStar", 2)' ,
                  'module'     : 'leptonSel()' ,
               },             

   'jetSel'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"medium",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },         

   'jetSelSusy'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  'declare'    : 'jetSelSusy = lambda : JetSel(2,"loose",20.0,2.5,"CleanJet")' ,
                  'module'     : 'jetSelSusy()' ,
               },

   'jetSelCustom' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"custom",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },

   'jetSelCustom_looseJetID_noPUID' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(1,"none",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },


   'CleanJetCut' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.CopyCleanJet',
                  'declare'    : 'cleanJetCut = lambda : CopyCleanJet(newcollectionname="CleanJetCut", cuts=["eta>2.65","eta<3.139"])',
                  'module'     : 'cleanJetCut()',
               }, 


    'CorrFatJetData' :  {
                'isChain': False,
                'do4MC': False,
                'do4Data': True,
                'import': 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2',
                'declare': 'corr_fatjet_data = createJMECorrector(isMC=False,dataYear=RPLME_YEAR, runPeriod="RPLME_RUNPERIOD", jesUncert="Total", redojec=True, jetType="AK8PFPuppi")',
                'module':  'corr_fatjet_data()'
    },

    'CorrFatJetMC' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'LatinoAnalysis.NanoGardener.modules.FatJetCorrHelper',
                'declare': 'corr_fatjet_mc = createFatjetCorrector( globalTag="Regrouped_RPLME_JESGT", dataYear="RPLME_YEAR", jetType="AK8PFPuppi", isMC=True, redojec=True, applySmearing=True)',
                'module':  'corr_fatjet_mc()'
    },


    'CleanFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker()'
    },

    'BoostedWtagSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                  'declare'    : 'boostedWtagsf = lambda : BoostedWtagSF(year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                  'module'     : 'boostedWtagsf()'
    },

    # 'CorrFatJetMass' : {
    #               'isChain'    : False ,
    #               'do4MC'      : True  ,
    #               'do4Data'    : False  ,
    #               'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMassScaler',
    #               'declare'    : 'fatjetmass_scaler = lambda : FatJetMassScaler(year=RPLME_YEAR, type="scale_smear", kind="Central",collection="CleanFatJet")',
    #               'module'     : 'fatjetmass_scaler()'
    # },


   'susyGen': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyGenVarsProducer' ,
                  'module'     : 'SusyGenVarsProducer()' ,
               },  

   'susyMT2recoNomin': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                  'module'     : 'mt2Producer(analysisRegion="",  metKind="reco", metSystematic="nom", filterRegion="region")' ,
               },  

   'susyMT2fastNomin': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                  'module'     : 'mt2Producer(analysisRegion="",  metKind="fast", metSystematic="nom", filterRegion="region")' ,
               }, 

   'susyMT2genmNomin': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                  'module'     : 'mt2Producer(analysisRegion="",  metKind="gen",  metSystematic="nom", filterRegion="region")' ,
               },

   'susyMT2puppi': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                  'module'     : 'mt2Producer(metType="puppi")' ,
               },

## EFT JJH->WW->2l2nu

    'JJHl2EFT' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['JJHEFT','EFTGen'],
                  },

    'JJHEFT' : {
                   'isChain'    : False ,
                   'do4MC'      : True ,
                   'do4Data'    : True ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                   'declare'    : 'JJHEFT = lambda : JJH_EFTVars()',
                   'module'     : 'JJHEFT()',
                 },

    'JJHEFT_ElepTup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                 },
    
  'DATAl1loose2018v7': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],                'declare'    : 'JJHEFT_ElepTup = lambda : JJH_EFTVars(branch_map="ElepTup")',
                    'module'     : 'JJHEFT_ElepTup()',
                 },
  
    'JJHEFT_ElepTdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_ElepTdo = lambda : JJH_EFTVars(branch_map="ElepTdo")',
                    'module'     : 'JJHEFT_ElepTdo()',
                 },
  
    'JJHEFT_MupTup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_MupTup = lambda : JJH_EFTVars(branch_map="MupTup")',
                    'module'     : 'JJHEFT_MupTup()',
                 },
  
    'JJHEFT_MupTdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_MupTdo = lambda : JJH_EFTVars(branch_map="MupTdo")',
                    'module'     : 'JJHEFT_MupTdo()',
                 },

    'JJHEFT_METup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_METup = lambda : JJH_EFTVars(branch_map="METup")',
                    'module'     : 'JJHEFT_METup()',
                 },
  
    'JJHEFT_METdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
                    'declare'    : 'JJHEFT_METdo = lambda : JJH_EFTVars(branch_map="METdo")',
                    'module'     : 'JJHEFT_METdo()',
                 },

#   'JJHEFT_JESup' : {
#                   'isChain'    : False ,
#                   'do4MC'      : True  ,
#                   'do4Data'    : True  ,
#                   'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
#                   'declare'    : 'JJHEFT_JESup = lambda : JJH_EFTVars(branch_map="JESup")',
#                   'module'     : 'JJHEFT_JESup()',
#                },

#   'JJHEFT_JESdo' : {
#                   'isChain'    : False ,
#                   'do4MC'      : True  ,
#                   'do4Data'    : True  ,
#                   'import'     : 'LatinoAnalysis.NanoGardener.modules.JJH_EFTVars' ,
#                   'declare'    : 'JJHEFT_JESdo = lambda : JJH_EFTVars(branch_map="JESdo")',
#                   'module'     : 'JJHEFT_JESdo()',
#                },


    'EFTGen' : {
                     'isChain'    : False ,
                     'do4MC'      : True ,
                     'do4Data'    : False ,
                     'import'     : 'LatinoAnalysis.NanoGardener.modules.EFTReweighter' ,
                     'declare'    : 'EFTGen = lambda : EFTReweighter("RPLME_SAMPLE")',
                     'module'     : 'EFTGen()',
                     'onlySample' : ['H0PM_ToWWTo2L2Nu','H0PH_ToWWTo2L2Nu','H0L1_ToWWTo2L2Nu','H0M_ToWWTo2L2Nu','H0PHf05_ToWWTo2L2Nu','H0Mf05_ToWWTo2L2Nu','VBF_H0PM_ToWWTo2L2Nu','VBF_H0PH_ToWWTo2L2Nu','VBF_H0L1_ToWWTo2L2Nu','VBF_H0M_ToWWTo2L2Nu','VBF_H0PHf05_ToWWTo2L2Nu','VBF_H0Mf05_ToWWTo2L2Nu','WH_H0PM_ToWWTo2L2Nu','WH_H0PH_ToWWTo2L2Nu','WH_H0L1_ToWWTo2L2Nu','WH_H0M_ToWWTo2L2Nu','WH_H0PHf05_ToWWTo2L2Nu','WH_H0Mf05_ToWWTo2L2Nu','ZH_H0PM_ToWWTo2L2Nu','ZH_H0PH_ToWWTo2L2Nu','ZH_H0L1_ToWWTo2L2Nu','ZH_H0M_ToWWTo2L2Nu','ZH_H0PHf05_ToWWTo2L2Nu','ZH_H0Mf05_ToWWTo2L2Nu','H0L1f05_ToWWTo2L2Nu','VBF_H0L1f05_ToWWTo2L2Nu','ZH_H0L1f05_ToWWTo2L2Nu','WH_H0L1f05_ToWWTo2L2Nu','GGHjj_H0PM_ToWWTo2L2Nu','GGHjj_H0M_ToWWTo2L2Nu','GGHjj_H0Mf05_ToWWTo2L2Nu'],
                    },

    
    ##--High Mass SemiLeptonic channel
  'wlepMaker' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
                  'declare'   : 'wlepMkr = lambda : WlepMaker()',
                  'module'    : 'wlepMkr()',
     },
    'whadJetSel' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WhadJetSel',
                  'declare'   : 'whadJetSel = lambda : WhadJetSel(2,"custom",30.0,4.7,"CleanJet")',
                  'module'    : 'whadJetSel()',
    },
    'PreselFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=1, minpt=200, maxeta=2.4, max_tau21=9999., mass_range=[40, 13000], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker()'
    },


## ------- MODULES: Trigger

  'PrefCorr2016' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2016BtoH.root", jetmapname="L1prefiring_jetpt_2016BtoH", photonroot="L1prefiring_photonpt_2016BtoH.root", photonmapname="L1prefiring_photonpt_2016BtoH", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'PrefCorr2017' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2017BtoF.root", jetmapname="L1prefiring_jetpt_2017BtoF", photonroot="L1prefiring_photonpt_2017BtoF.root", photonmapname="L1prefiring_photonpt_2017BtoF", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'PrefCorrUL16' : {
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorrUL16 = lambda : PrefCorr(jetroot="L1PrefiringMaps_WithUL17.root", jetmapname="L1prefiring_jetptvseta_2016BtoH", photonroot="L1PrefiringMaps_WithUL17.root", photonmapname="L1prefiring_photonptvseta_2016BtoH", UseEMpT=0)',
                 'module'     : 'prefCorrUL16()',
               },

  'PrefCorrUL17' : {
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorrUL17 = lambda : PrefCorr(jetroot="L1PrefiringMaps_WithUL17.root", jetmapname="L1prefiring_jetptvseta_UL2017BtoF", photonroot="L1PrefiringMaps_WithUL17.root", photonmapname="L1prefiring_photonptvseta_UL2017BtoF", UseEMpT=0)',
                 'module'     : 'prefCorrUL17()',
               },

  'trigData' : { 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigData = lambda : TrigMaker("RPLME_CMSSW",isData=True,keepRunP=False)',
                 'module'     : 'trigData()',
               },

 
  'trigMC'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=False)',
                 'module'     : 'trigMC()',
               },

  'trigMC_Cut'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'CBtrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_CutBased_cfg.py")',
                 'module'     : 'CBtrigMC()',
               },
 
  'trigFS'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=False,isFastSim=True)',
                 'module'     : 'trigMC()',
             },

  'trigFS_Cut'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'CBtrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_CutBased_cfg.py",isFastSim=True)',
                 'module'     : 'CBtrigMC()',
               },

 'TrigMC_hmumu'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_hmumu_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },

  'trigMCKeepRun' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True)',
                 'module'     : 'trigMCKR()',
               },

  # TODO: We shouldn't be instantiating almost exactly identical modules for each variation
  # Perhaps create a global "static" instance which the variations can refer to?
  'trigMCKeepRun_ElepTup' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_ElepTup = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="ElepTup")',
                 'module'     : 'trigMCKR_ElepTup()',
               },

  'trigMCKeepRun_ElepTdo' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_ElepTdo = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="ElepTdo")',
                 'module'     : 'trigMCKR_ElepTdo()',
               },
               
  'trigMCKeepRun_MupTup' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_MupTup = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="MupTup")',
                 'module'     : 'trigMCKR_MupTup()',
               },

  'trigMCKeepRun_MupTdo' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_MupTdo = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="MupTdo")',
                 'module'     : 'trigMCKR_MupTdo()',
               },

## ------- MODULES: JEC

  'JECupdateMC2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'declare'    : 'jetRecalib2017MC = lambda : jetRecalib(globalTag="Fall17_17Nov2017_V32_MC", jetCollections=["CleanJet"], metCollections=["MET"])',
                  'module'     : 'jetRecalib2017MC()',
                 }, 
 
  # Old style, to be deleted when UL is fully done

  'JMEUncertMC2016' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorMC2016 = createJMECorrector(isMC=True, dataYear=2016, jesUncert="Total", redojec=True)',
                  'module'     : 'jetmetCorrectorMC2016()',
                 },   
 
  'JMEUncertFS2016' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorFS2016 = createJMECorrector(isMC=True, dataYear=2016, jesUncert="Total", redojec=True, isFastSim=True)',
                  'module'     : 'jetmetCorrectorFS2016()',
                 }, 

  'METFixEEMC2017' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEMC2017 = createJMECorrector(isMC=True, dataYear=2017, runPeriod="", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEMC2017()',
                 }, 

  'METFixEEFS2017' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEFS2017 = createJMECorrector(isMC=True, dataYear=2017, runPeriod="", metBranchName="METFixEE2017", isFastSim=True)',
                  'module'     : 'jetmetCorrectorEEFS2017()',
                 },  
 
  'JMEUncertMC2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorMC2018 = createJMECorrector(isMC=True, dataYear=2018, jesUncert="Total", redojec=True)',
                  'module'     : 'jetmetCorrectorMC2018()',
                 },   
 
  'JMEUncertFS2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorFS2018 = createJMECorrector(isMC=True, dataYear=2018, jesUncert="Total", redojec=True, isFastSim=True)',
                  'module'     : 'jetmetCorrectorFS2018()',
                 }, 

  # End old style

  'JMEUncertMC' : {
                   'isChain'    : False ,
                   'do4MC'      : True ,
                   'do4Data'    : False ,
                   'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                   'declare'    : 'jetmetCorrectorMC = createJMECorrector(isMC=True, dataYear="RPLME_YEAR", jesUncert="Total", isFastSim=False)',
                   'module'     : 'jetmetCorrectorMC()',
                 },

  'JMEUncertFS' : {
                   'isChain'    : False , 
                   'do4MC'      : True ,
                   'do4Data'    : False ,
                   'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                   'declare'    : 'jetmetCorrectorFS = createJMECorrector(isMC=True, dataYear="RPLME_YEAR", jesUncert="Total", redojec=True, isFastSim=True)',
                   'module'     : 'jetmetCorrectorFS()',
                  },

  'PtCorrReader' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrReader', 
                  'declare'    : 'ptcorr_SYSTVAR = lambda : PtCorrReader(Coll="CleanJet", CorrSrc="SYSTVAR")', 
                  'module'     : 'ptcorr_SYSTVAR()',
                 }, 

  # Old style, to be deleted when UL is fully done

  #'METFixEEDATA2017' : {
  #                'isChain'    : False ,
  #                'do4MC'      : False ,
  #                'do4Data'    : True ,
  #                'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
  #                'declare'    : 'jetmetCorrectorEEDATA2017 = createJMECorrector(isMC=False, dataYear=2017, runPeriod="RPLME_PERIOD", metBranchName="METFixEE2017")',
  #                'module'     : 'jetmetCorrectorEEDATA2017()',
  #               }, 

  'METFixEEDATA2017B' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEDATA2017B = createJMECorrector(isMC=False, dataYear=2017, runPeriod="B", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEDATA2017B()',
                 }, 

  'METFixEEDATA2017C' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEDATA2017C = createJMECorrector(isMC=False, dataYear=2017, runPeriod="C", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEDATA2017C()',
                 }, 

  'METFixEEDATA2017D' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEDATA2017D = createJMECorrector(isMC=False, dataYear=2017, runPeriod="D", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEDATA2017D()',
                 }, 

  'METFixEEDATA2017E' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEDATA2017E = createJMECorrector(isMC=False, dataYear=2017, runPeriod="E", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEDATA2017E()',
                 }, 

  'METFixEEDATA2017F' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2' ,
                  'declare'    : 'jetmetCorrectorEEDATA2017F = createJMECorrector(isMC=False, dataYear=2017, runPeriod="F", metBranchName="METFixEE2017")',
                  'module'     : 'jetmetCorrectorEEDATA2017F()',
                 },  

  # End old style

  'JECupdateDATA2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'module'     : 'jetRecalib2017RPLME_RUN()', ### <--- TODO
                 },   

# Check HEM15/16 ISSUE for 2018

  'JECupdateMC2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection': '"(nLepton>=2 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && \
                               Alt$(Lepton_pt[2],0) < 10. && \
                               Lepton_pt[0] > 25. && \
                               Lepton_pt[1] > 20. && \
                               mpmet > 20. && \
                               PuppiMET_pt > 20. && \
                               drll < 2.5 && \
                               mll > 12. && \
                               ptll > 30.)"',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'declare'    : 'jetRecalib2018MC = lambda : jetRecalib(globalTag="Autumn18_V19_MC", jetCollections=["CleanJet"], metCollections=["PuppiMET"], jetType = "AK4PFchs")',
                  'module'     : 'jetRecalib2018MC()',
                 },    

  'JECupdateDATA2018': {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'selection': '"(nLepton>=2 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && \
                               Alt$(Lepton_pt[2],0) < 10. && \
                               Lepton_pt[0] > 25. && \
                               Lepton_pt[1] > 20. && \
                               mpmet > 20. && \
                               PuppiMET_pt > 20. && \
                               drll < 2.5 && \
                               mll > 12. && \
                               ptll > 30.)"',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'module'     : 'jetRecalib2018RPLME_RUN()', ### <--- TODO
                 }, 

## ------- MODULES: JER
    'JERsMC2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JERMaker' ,
                  'declare'    : 'JERMakerMC16 = lambda : JERMaker("2016","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Summer16_25nsV1_MC",jmr_vals=[1.0, 1.2, 0.8])',
                  'module'     : 'JERMakerMC16()',
                 },  
    'JERsMC2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JERMaker' ,
                  'declare'    : 'JERMakerMC17 = lambda : JERMaker("2017","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Fall17_V3_MC",jmr_vals=[1.09, 1.14, 1.04])',
                  'module'     : 'JERMakerMC17()',
                 },
    'JERsMC2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JERMaker' ,
                  'declare'    : 'JERMakerMC18 = lambda : JERMaker("2018","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Autumn18_V7b_MC",jmr_vals=[1.24, 1.20, 1.28])',
                  'module'     : 'JERMakerMC18()',
                 },
    #jerTag for 2018 is missing on purpose, 2017 JERs are used instead (for a moment)

   'JERup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : createJERchain("", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },
    'JERdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : createJERchain("", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

## ------- MODULES: MC PU ID SF, EFF and (stat/syst) uncertainty creator 
    'JetPUID_SF_16': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSFMaker' ,
                  'declare'    : 'JetPUID_SFMaker16 = lambda : JetSFMaker("Full2016v7")',
                  'module'     : 'JetPUID_SFMaker16()',
                 },
    'JetPUID_SF_17': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSFMaker' ,
                  'declare'    : 'JetPUID_SFMaker17 = lambda : JetSFMaker("Full2017v7")',
                  'module'     : 'JetPUID_SFMaker17()',
                 },
    'JetPUID_SF_18': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSFMaker' ,
                  'declare'    : 'JetPUID_SFMaker18 = lambda : JetSFMaker("Full2018v7")',
                  'module'     : 'JetPUID_SFMaker18()',
                 },

## ------- MODULES: MC Weights

  'baseW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Grafter' ,
                  'module'     : 'Grafter(["baseW/F=RPLME_baseW","Xsec/F=RPLME_XSection"])',
               },  

  'btagPerJet2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2016 = lambda : btagSFProducer(era="Legacy2016", algo="deepcsv")',
                  'module'     : 'btagSFProducer2016()',
                 },  

  'btagPerJet2016FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2016 = lambda : btagSFProducer(era="Legacy2016", algo="deepcsv", doFastSim=True)',
                  'module'     : 'btagSFProducer2016()',
                 },

  'btagPerJet2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2017 = lambda : btagSFProducer(era="2017", algo="deepcsv")',
                  'module'     : 'btagSFProducer2017()',
                 }, 

  'btagPerJet2017FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2017 = lambda : btagSFProducer(era="2017", algo="deepcsv", doFastSim=True)',
                  'module'     : 'btagSFProducer2017()',
                 },               

  'btagPerJet2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2018 = lambda : btagSFProducer(era="2018", algo="deepcsv")',
                  'module'     : 'btagSFProducer2018()',
                 },               

  'btagPerJet2018FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2018 = lambda : btagSFProducer(era="2018", algo="deepcsv", doFastSim=True)',
                  'module'     : 'btagSFProducer2018()',
                 },

  'btagPerJetDeepCSVWPs': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducerWPs = lambda : btagSFProducer(era="RPLME_YEAR", algo="deepcsv", doFastSim=False, selectedWPs=["L", "M", "T"])',
                  'module'     : 'btagSFProducerWPs()',
                 },

  ### Old style, to be removed after transition to UL complete
  'btagPerEvent2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2016M", bTagMethod="1c", bTagPtCut="20")',
                },

  'btagPerEvent2016FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2016M", bTagMethod="1c", bTagPtCut="20", dataType="fastsim")',
                },

  'btagPerEvent2016Data': {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2016M", bTagMethod="1c", bTagPtCut="20", dataType="data")',
                },

  'btagPerEvent2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2017M", bTagMethod="1c", bTagPtCut="20")',
                },

  'btagPerEvent2017FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2017M", bTagMethod="1c", bTagPtCut="20", dataType="fastsim")',
                },

  'btagPerEvent2017Data': {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2017M", bTagMethod="1c", bTagPtCut="20", dataType="data")',
        
                },

  'btagPerEvent2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2018M", bTagMethod="1c", bTagPtCut="20")',
                },

  'btagPerEvent2018FS': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2018M", bTagMethod="1c", bTagPtCut="20", dataType="fastsim")',
                },

  'btagPerEvent2018Data': {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagWP="2018M", bTagMethod="1c", bTagPtCut="20", dataType="data")',
                },
  # End old style

  'btagPerEventDeepCSVWPs': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer(bTagAlgo="btagDeepB", bTagEra="RPLME_YEAR", bTagWPs=["L", "M", "T"], bTagMethod="1c", bTagPtCuts=["20", "25", "30"], dataType="mc")',
                },

  'LeptonSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW")',
                  'module'     : 'LeptonSF()',
                },
  'LeptonSF_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_ElepTup = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="ElepTup")',
                  'module'     : 'LeptonSF_ElepTup()',
                },
  'LeptonSF_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_ElepTdo = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="ElepTdo")',
                  'module'     : 'LeptonSF_ElepTdo()',
                },
  'LeptonSF_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_MupTup = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="MupTup")',
                  'module'     : 'LeptonSF_MupTup()',
                },
  'LeptonSF_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_MupTdo = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="MupTdo")',
                  'module'     : 'LeptonSF_MupTdo()',
                },

  'LeptonSFSusy' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW", "LatinoAnalysis/NanoGardener/python/data/LeptonSelSUSY_cfg.py")',
                  'module'     : 'LeptonSF()',
                },

  'LeptonSFSusyFS' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW", "LatinoAnalysis/NanoGardener/python/data/LeptonSelSUSY_cfg.py", "", True)',
                  'module'     : 'LeptonSF()',
                },

  'JetSF': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSFMaker' ,
                  'declare'    : 'JetSF = lambda : JetSFMaker("RPLME_CMSSW")',
                  'module'     : 'JetSF()',
                },

## ------ Charge Flip

  'ChargeFlip' : {
                 'isChain'     : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['ChargeFlipDY','ChargeFlipWW','ChargeFlipTop'],
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50','WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' , 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                 },

  'ChargeFlipDY' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipDY = lambda : ChargeFlipWeight("RPLME_CMSSW","DY")',
                  'module'     : 'ChargeFlipDY()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

   'ChargeFlipWW' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipWW = lambda : ChargeFlipWeight("RPLME_CMSSW","WW")',
                  'module'     : 'ChargeFlipWW()',
                  'onlySample' : ['WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' ]
                 },

   'ChargeFlipTop' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipTop = lambda : ChargeFlipWeight("RPLME_CMSSW","Top")',
                  'module'     : 'ChargeFlipTop()',
                  'onlySample' : [ 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                    },

   'ChargeFlipClosure' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipClosusre = lambda : ChargeFlipWeight("RPLME_CMSSW","DY",False)',
                  'module'     : 'ChargeFlipClosusre()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

## ------- Pile-Up weights

  'RunPeriodMC' : {
                     'isChain'    : False ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'import'     : 'LatinoAnalysis.NanoGardener.modules.RunPeriod',
                     'declare'    : 'RunPeriodMC = lambda : RunPeriod("RPLME_CMSSW",False)',
                     'module'     : 'RunPeriodMC()'
                  },

  'RunPeriodDATA' : {
                     'isChain'    : False ,
                     'do4MC'      : False  ,
                     'do4Data'    : True ,
                     'import'     : 'LatinoAnalysis.NanoGardener.modules.RunPeriod',
                     'declare'    : 'RunPeriodDATA = lambda : RunPeriod("RPLME_CMSSW",True)',
                     'module'     : 'RunPeriodDATA()'
                  },
 

  'puW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.runDependentPuW' ,
                  'declare'    : 'puWeight = lambda : runDependentPuW("RPLME_CMSSW")',
                  'module'     : 'puWeight()', 
             } , 




  'puW2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_mc2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_profile_Summer16.root" % os.environ["CMSSW_BASE"]; pufile_data2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupData_GoldenJSON_Full2016.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer(pufile_mc2016,pufile_data2016,"pu_mc","pileup",verbose=False)',

                },
              
  'puW2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_data2017="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer("auto",pufile_data2017,"pu_mc","pileup",verbose=False)',
  },

  'susyW': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyWeightsProducer' ,
                  'module'     : 'SusyWeightsProducer("RPLME_CMSSW", "RPLME_SOURCEDIR")' ,
                },

  'ZZGen': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ZZGenVarsProducer' ,
                  'module'     : 'ZZGenVarsProducer()' ,
                  #'onlySample' : ['ggZZ4e', 'ggZZ4m', 'ggZZ4t', 'ggZZ2e2m', 'ggZZ2e2t', 'ggZZ2m2t', 'ggZZ2e2n', 'ggZZ2m2n', 'ZZTo4L_ext1', 'ZZTo4L_ext2', 'ZZTo4L_newpmx', 'ZZTo2L2Nu', 'ZZTo2L2Nu_ext1', 'ZZTo2L2Nu_ext2', 'GluGluHToZZTo4L_M125'],
                  'onlySample' : ['ZZTo4L_ext1', 'ZZTo4L_ext2', 'ZZTo4L_newpmx', 'ZZTo2L2Nu', 'ZZTo2L2Nu_ext1', 'ZZTo2L2Nu_ext2'],
               },
  

## ------- MODULES: Embedding

  'EmbeddingWeights' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="hww_scalefactors_XXX.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingVeto' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedVeto' ,
                 'declare'    : 'embedveto = lambda : EmbedVeto()',
                 'module'     : 'embedveto()',
               },

## ------- MODULES: Fakes

  'fakeWMC' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                  'onlySample' : [ 'Zg', 'WZTo3LNu_mllmin01', 'Wg_MADGRAPHMLM', 'WZTo3LNu' ] , 
                   }, 

  'fakeWp2NB'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },
  'fakeWelewithiso'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },

  'fakeW_CutBasedTest'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },



  'fakeW'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },
    
  'fakeW1l'  : {
                'isChain'    : True ,
                'do4MC'      : False ,
                'do4Data'    : True ,
                'selection'  : '"Alt$(Lepton_pt[1],0)<=10"',
                'subTargets' : ['fakeWstep1l','formulasFAKE1l'],
                  },


  'fakeWPUFIXLP19'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },


  'fakeWstep'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW")',
              },

  'fakeWstep1l'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW", min_nlep=1)',
              },

## ------- MODULES: Rochester corrections

  'rochesterMC'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR)',
                  'module'     : 'rochesterMC()',
              },

  'rochesterDATA'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR)',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterDATALP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterMCLP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterMC()',
              },


## ------- MODULES: Recoil corrections

  'recoilCorr'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RecoilCorr',
                  'declare'    : 'Recoil = lambda : RecoilCorr(RPLME_YEAR)',
                  'module'     : 'Recoil()',
                  'onlySample' : allDY,
              },

  'do_METResponseup_suffix'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RecoilCorr',
                  'declare'    : 'RecoilRespUp = lambda : RecoilCorr(RPLME_YEAR, variation=1, variationType=0, suffix="_METResponseup")',
                  'module'     : 'RecoilRespUp()',
                  'onlySample' : allDY,
              },

  'do_METResponsedo_suffix'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RecoilCorr',
                  'declare'    : 'RecoilRespDo = lambda : RecoilCorr(RPLME_YEAR, variation=-1, variationType=0, suffix="_METResponsedo")',
                  'module'     : 'RecoilRespDo()',
                  'onlySample' : allDY,
              },

  'do_METResolutionup_suffix'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RecoilCorr',
                  'declare'    : 'RecoilResoUp = lambda : RecoilCorr(RPLME_YEAR, variation=1, variationType=1, suffix="_METResolutionup")',
                  'module'     : 'RecoilResoUp()',
                  'onlySample' : allDY,
              },

  'do_METResolutiondo_suffix'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RecoilCorr',
                  'declare'    : 'RecoilResoDo = lambda : RecoilCorr(RPLME_YEAR, variation=-1, variationType=1, suffix="_METResolutiondo")',
                  'module'     : 'RecoilResoDo()',
                  'onlySample' : allDY,
              },

   'recoilDY' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection'  : '"(nLepton>=2)"' ,
                  'subTargets' : ['recoilCorr','l2Kin','l3Kin','l4Kin','formulasMC','DYMVA','MonoHiggsMVA','JJHEFT'],
                  'onlySample' : allDY,
              },


## ------- MODULES: Kinematic

  'l2Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer()' ,
               },  

  'l2Kin_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="ElepTup")' ,
               },

  'l2Kin_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="ElepTdo")' ,
               },

  'l2Kin_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="MupTup")' ,
               },

  'l2Kin_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="MupTdo")' ,
               },
  'l2Kin_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="METup")' ,
               },

  'l2Kin_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="METdo")' ,
               },
  'l2Kin_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JESup")' ,
               },

  'l2Kin_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JESdo")' ,
               },

  'l2Kin_JERup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JERup")' ,
               },

  'l2Kin_JERdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JERdo")' ,
               },

  'l3Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer()' ,
               },
  

  'l3Kin_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="ElepTdo")' ,
               },

  'l3Kin_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="ElepTup")' ,
               },
  'l3Kin_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="MupTdo")' ,
               },

  'l3Kin_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="MupTup")' ,
               },
  'l3Kin_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="METdo")' ,
               },

  'l3Kin_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="METup")' ,
               },
  'l3Kin_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JESdo")' ,
               },

  'l3Kin_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JESup")' ,
               },

  'l3Kin_JERdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JERdo")' ,
               },

  'l3Kin_JERup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JERup")' ,
               },
  
  'l4Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer()' ,
               }, 

  'l4Kin_ElepTup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="ElepTup")' ,
               }, 
               

  'l4Kin_ElepTdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="ElepTdo")' ,
               },

  'l4Kin_MupTup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="MupTup")' ,
               }, 
               

  'l4Kin_MupTdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="MupTdo")' ,
               },
  'l4Kin_METup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="METup")' ,
               }, 
               

  'l4Kin_METdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="METdo")' ,
               },
  'l4Kin_JESup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JESup")' ,
               }, 
               

  'l4Kin_JESdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JESdo")' ,
               },

  'l4Kin_JERup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JERup")' ,
               },


  'l4Kin_JERdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JERdo")' ,
               },
## ------- MODULES: Adding Formulas

# .... 2016/2017/... : switch in the code RPLME_YEAR

  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\')' ,
                 },
   

  'formulasMC_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="ElepTup")' ,
                 },

  'formulasMC_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="ElepTdo")' ,
                 },
  'formulasMC_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="MupTup")' ,
                 },

  'formulasMC_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="MupTdo")' ,
                 },
  'formulasMC_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="METup")' ,
                 },

  'formulasMC_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="METdo")' ,
                 },
  'formulasMC_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="JESup")' ,
                 },

  'formulasMC_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="JESdo")' ,
                 },

  'formulasMC_JERup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="JERup")' ,
                 },

  'formulasMC_JERdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_CMSSW.py\', branch_map="JERdo")' ,
                 },
  
  'formulasMCLP19' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_2017LP19.py\')' ,
                 },

  'formulasMCnoSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MCnoSF_RPLME_YEAR.py\')' ,
                 },
   
  'formulasMC16tmp' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_16tmp.py\')' ,
                 },

  'formulasMCMH' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_MonoH.py\')' ,
                 },


  'formulasDATA' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_RPLME_CMSSW.py\')' ,
                 },
  'formulasDATALP19' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_2017LP19.py\')' ,
                 },



  'formulasFAKE' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE_RPLME_CMSSW.py\')' ,
                 },

  # 'formulasFAKE1l' : {
  #                 'isChain'    : False ,
  #                 'do4MC'      : True  ,
  #                 'do4Data'    : True  ,
  #                 'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
  #                 'declare'    : '',
  #                 'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE1l_RPLME_YEAR.py\')' ,
  #                },

  'formulasEMBED' : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_CMSSW.py\')' ,
                 },

  'formulasEMBED_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_CMSSW.py\', branch_map="ElepTup")' ,
                 },

  'formulasEMBED_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_CMSSW.py\', branch_map="ElepTdo")' ,
                 },

  'formulasEMBED_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_CMSSW.py\', branch_map="MupTup")' ,
                 },

  'formulasEMBED_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_CMSSW.py\', branch_map="MupTdo")' ,
                 },

## -------- DYMVA

  'DYMVA' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\')' ,
                  'module'     : 'DYMVA()',
            } ,

  'DYMVA_ElepTup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_ElepTup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="ElepTup")' ,
                  'module'     : 'DYMVA_ElepTup()',
            } ,

  'DYMVA_ElepTdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_ElepTdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="ElepTdo")' ,
                  'module'     : 'DYMVA_ElepTdo()',
            } ,
  'DYMVA_MupTup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MupTup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="MupTup")' ,
                  'module'     : 'DYMVA_MupTup()',
            } ,

  'DYMVA_MupTdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MupTdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="MupTdo")' ,
                  'module'     : 'DYMVA_MupTdo()',
            } ,
  'DYMVA_METup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_METup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="METup")' ,
                  'module'     : 'DYMVA_METup()',
            } ,

  'DYMVA_METdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_METdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="METdo")' ,
                  'module'     : 'DYMVA_METdo()',
            } ,
  'DYMVA_JESup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JESup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="JESup")' ,
                  'module'     : 'DYMVA_JESup()',
            } ,

  'DYMVA_JESdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JESdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="JESdo")' ,
                  'module'     : 'DYMVA_JESdo()',
            } ,

  'DYMVA_JERup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JERup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="JERup")' ,
                  'module'     : 'DYMVA_JERup()',
            } ,

  'DYMVA_JERdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JERdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\', branch_map="JERdo")' ,
                  'module'     : 'DYMVA_JERdo()',
            } ,

# 'DYMVA_v5' : {
#           #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
#                 'isChain'    : False ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : True  ,
#                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
#                 'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\')' ,
#                 'module'     : 'DYMVA()',
#           } ,

  'DYMVA_alt' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_alt_cfg.py\')' ,
                  'module'     : 'DYMVA()',
            } ,



# ------------------------------------ SYSTEMATICS ----------------------------------------------------------------

## ------- JES

  'JESBaseTestV8' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="Fall17_17Nov2017_V8_MC", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
                  'onlySample' : [ 'WWTo2L2Nu' ] ,
               },

  'JESBase' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="Regrouped_RPLME_JESGT", types=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
               },

  'JESBaseTotal' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="RPLME_JESGT", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
               },

  'do_JESup' : {  
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESUp = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESUp()' 
               },

  'do_JESdo' : {  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESDo = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Do", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESDo()' 
               },
  'do_JESup_suffix' : createJESvariation("Total", "Up"),
#{  
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
#                  'declare'    : 'JESUp = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JESup")', 
#                  'module'     : 'JESUp()' 
#               },

  'do_JESdo_suffix' : createJESvariation("Total", "Do"),
#{  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
#                  'declare'    : 'JESDo = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Do", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JESdo")', 
#                  'module'     : 'JESDo()' 
#               },
    
   'do_JESAbsoluteup_suffix' : createJESvariation("Absolute", "Up"), 
   'do_JESAbsolutedo_suffix' : createJESvariation("Absolute", "Do"), 
   'do_JESAbsolute_RPLME_YEARup_suffix' : createJESvariation("Absolute_RPLME_YEAR", "Up"), 
   'do_JESAbsolute_RPLME_YEARdo_suffix' : createJESvariation("Absolute_RPLME_YEAR", "Do"), 
   'do_JESBBEC1up_suffix' : createJESvariation("BBEC1", "Up"), 
   'do_JESBBEC1do_suffix' : createJESvariation("BBEC1", "Do"), 
   'do_JESBBEC1_RPLME_YEARup_suffix' : createJESvariation("BBEC1_RPLME_YEAR", "Up"), 
   'do_JESBBEC1_RPLME_YEARdo_suffix' : createJESvariation("BBEC1_RPLME_YEAR", "Do"), 
   'do_JESEC2up_suffix' : createJESvariation("EC2", "Up"), 
   'do_JESEC2do_suffix' : createJESvariation("EC2", "Do"), 
   'do_JESEC2_RPLME_YEARup_suffix' : createJESvariation("EC2_RPLME_YEAR", "Up"), 
   'do_JESEC2_RPLME_YEARdo_suffix' : createJESvariation("EC2_RPLME_YEAR", "Do"), 
   'do_JESFlavorQCDup_suffix' : createJESvariation("FlavorQCD", "Up"), 
   'do_JESFlavorQCDdo_suffix' : createJESvariation("FlavorQCD", "Do"), 
   'do_JESHFup_suffix' : createJESvariation("HF", "Up"), 
   'do_JESHFdo_suffix' : createJESvariation("HF", "Do"), 
   'do_JESHF_RPLME_YEARup_suffix' : createJESvariation("HF_RPLME_YEAR", "Up"), 
   'do_JESHF_RPLME_YEARdo_suffix' : createJESvariation("HF_RPLME_YEAR", "Do"), 
   'do_JESRelativeBalup_suffix' : createJESvariation("RelativeBal", "Up"), 
   'do_JESRelativeBaldo_suffix' : createJESvariation("RelativeBal", "Do"), 
   'do_JESRelativeSample_RPLME_YEARup_suffix' : createJESvariation("RelativeSample_RPLME_YEAR", "Up"), 
   'do_JESRelativeSample_RPLME_YEARdo_suffix' : createJESvariation("RelativeSample_RPLME_YEAR", "Do"), 

   'do_JERup_suffix' : copyJERvariation("", "Up"),
   'do_JERdo_suffix' : copyJERvariation("", "Do"),



   # What about B-Tag weights ? They are done on top of the Jet Collection, not the CleanJet, so they don't catch th jet pT update !!!!

   'JESup' :   {  
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'JESup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Up") +
                                  createJESchain("Absolute", "Up") +
                                  createJESchain("Absolute_RPLME_YEAR", "Up") +
                                  createJESchain("BBEC1", "Up") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Up") +
                                  createJESchain("EC2", "Up") +
                                  createJESchain("EC2_RPLME_YEAR", "Up") +
                                  createJESchain("FlavorQCD", "Up") +
                                  createJESchain("HF", "Up") +
                                  createJESchain("HF_RPLME_YEAR", "Up") +
                                  createJESchain("RelativeBal", "Up") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESup_suffix','l2Kin_JESup', 'l3Kin_JESup', 'l4Kin_JESup','DYMVA_JESup','MonoHiggsMVA_JESup','formulasMC_JESup',
                  #               'do_JESAbsoluteup_suffix','do_JESAbsolutedo_suffix','do_JESAbsolute_RPLME_YEARup_suffix','do_JESAbsolute_RPLME_YEARdo_suffix','do_JESBBEC1up_suffix','do_JESBBEC1do_suffix','do_JESBBEC1_RPLME_YEARup_suffix','do_JESBBEC1_RPLME_YEARdo_suffix','do_JESEC2up_suffix','do_JESEC2do_suffix','do_JESEC2_RPLME_YEARup_suffix','do_JESEC2_RPLME_YEARdo_suffix','do_JESFlavorQCDup_suffix','do_JESFlavorQCDdo_suffix','do_JESHFup_suffix','do_JESHFdo_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBal_RPLME_YEARup_suffix','do_JESRelativeBal_RPLME_YEARdo_suffix'],
               },

## Split JES steps to have faster jobs
   'JESTotalup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESAbsoluteup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Absolute", "Up") +
                                  createJESchain("Absolute_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESBBEC1up_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("BBEC1", "Up") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESEC2up_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("EC2", "Up") +
                                  createJESchain("EC2_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESFlavorQCDup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("FlavorQCD", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESHFup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("HF", "Up") +
                                  createJESchain("HF_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESRelativeup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("RelativeBal", "Up") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },



   'JESTotaldo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESAbsolutedo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Absolute", "Do") +
                                  createJESchain("Absolute_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESBBEC1do_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("BBEC1", "Do") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESEC2do_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("EC2", "Do") +
                                  createJESchain("EC2_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESFlavorQCDdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("FlavorQCD", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESHFdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("HF", "Do") +
                                  createJESchain("HF_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'JESRelativedo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("RelativeBal", "Do") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },


   'JESup_suffix_redoMVA' :   {  
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] + 
                                  createJESchain("Total", "Up") +
                                  createJESchain("Absolute", "Up") +
                                  createJESchain("Absolute_RPLME_YEAR", "Up") +
                                  createJESchain("BBEC1", "Up") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Up") +
                                  createJESchain("EC2", "Up") +
                                  createJESchain("EC2_RPLME_YEAR", "Up") +
                                  createJESchain("FlavorQCD", "Up") +
                                  createJESchain("HF", "Up") +
                                  createJESchain("HF_RPLME_YEAR", "Up") +
                                  createJESchain("RelativeBal", "Up") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'                
                  #'subTargets' : ['JESBase','do_JESup_suffix','l2Kin_JESup', 'l3Kin_JESup', 'l4Kin_JESup','DYMVA_JESup','MonoHiggsMVA_JESup','formulasMC_JESup',
                  #               'do_JESAbsoluteup_suffix','do_JESAbsolutedo_suffix','do_JESAbsolute_RPLME_YEARup_suffix','do_JESAbsolute_RPLME_YEARdo_suffix','do_JESBBEC1up_suffix','do_JESBBEC1do_suffix','do_JESBBEC1_RPLME_YEARup_suffix','do_JESBBEC1_RPLME_YEARdo_suffix','do_JESEC2up_suffix','do_JESEC2do_suffix','do_JESEC2_RPLME_YEARup_suffix','do_JESEC2_RPLME_YEARdo_suffix','do_JESFlavorQCDup_suffix','do_JESFlavorQCDdo_suffix','do_JESHFup_suffix','do_JESHFdo_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBal_RPLME_YEARup_suffix','do_JESRelativeBal_RPLME_YEARdo_suffix'],
               },

   'JESdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'JESdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Do") +
                                  createJESchain("Absolute", "Do") +
                                  createJESchain("Absolute_RPLME_YEAR", "Do") +
                                  createJESchain("BBEC1", "Do") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Do") +
                                  createJESchain("EC2", "Do") +
                                  createJESchain("EC2_RPLME_YEAR", "Do") +
                                  createJESchain("FlavorQCD", "Do") +
                                  createJESchain("HF", "Do") +
                                  createJESchain("HF_RPLME_YEAR", "Do") +
                                  createJESchain("RelativeBal", "Do") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },

   'JESdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Do") +
                                  createJESchain("Absolute", "Do") +
                                  createJESchain("Absolute_RPLME_YEAR", "Do") +
                                  createJESchain("BBEC1", "Do") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Do") +
                                  createJESchain("EC2", "Do") +
                                  createJESchain("EC2_RPLME_YEAR", "Do") +
                                  createJESchain("FlavorQCD", "Do") +
                                  createJESchain("HF", "Do") +
                                  createJESchain("HF_RPLME_YEAR", "Do") +
                                  createJESchain("RelativeBal", "Do") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'                
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },


   'JESupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'JESdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


## ------- MET

  'do_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METup()',
                },

  'do_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METDo()',
                },
  'do_METup_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"], suffix="_METup")',
                  'module'     : 'METup()',
                },

  'do_METdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"], suffix="_METdo")',
                  'module'     : 'METDo()',
                },

   'METup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'METup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup_suffix','l2Kin_METup', 'l3Kin_METup', 'l4Kin_METup','DYMVA_METup','MonoHiggsMVA_METup','formulasMC_METup','JJHEFT_METup'] + 
                                 [item.replace("JES", "MET") for item in createJESchain("Response", "Up")] + 
                                 [item.replace("JES", "MET") for item in createJESchain("Resolution", "Up")],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },


   'METup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup_suffix','l2Kin_METup', 'l3Kin_METup', 'l4Kin_METup','DYMVA_METup','MonoHiggsMVA_METup','formulasMC_METup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'METdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo_suffix','l2Kin_METdo', 'l3Kin_METdo', 'l4Kin_METdo','DYMVA_METdo','MonoHiggsMVA_METdo','formulasMC_METdo','JJHEFT_METdo'] + 
                                 [item.replace("JES", "MET") for item in createJESchain("Response", "Do")] + 
                                 [item.replace("JES", "MET") for item in createJESchain("Resolution", "Do")],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo_suffix','l2Kin_METdo', 'l3Kin_METdo', 'l4Kin_METdo','DYMVA_METdo','MonoHiggsMVA_METdo','formulasMC_METdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'METdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

## ------- e-Scale

  'do_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTup()',
                },

  'do_ElepTup_suffix': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_ElepTup")',
                  'module'     : 'ElepTup()',
                },

  'do_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTdo()',
                },

  'do_ElepTdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_ElepTdo")',
                  'module'     : 'ElepTdo()',
                },

  'ElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'ElepTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup_suffix', 'trigMCKeepRun_ElepTup', 'LeptonSF_ElepTup', 'l2Kin_ElepTup', 'l3Kin_ElepTup', 'l4Kin_ElepTup', 'DYMVA_ElepTup', 'MonoHiggsMVA_ElepTup', 'formulasMC_ElepTup', 'JJHEFT_ElepTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup_suffix', 'trigMCKeepRun_ElepTup', 'LeptonSF_ElepTup', 'l2Kin_ElepTup', 'l3Kin_ElepTup', 'l4Kin_ElepTup', 'DYMVA_ElepTup', 'MonoHiggsMVA_ElepTup', 'formulasMC_ElepTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
                },
 
  'ElepTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo_suffix', 'trigMCKeepRun_ElepTdo', 'LeptonSF_ElepTdo', 'l2Kin_ElepTdo', 'l3Kin_ElepTdo', 'l4Kin_ElepTdo', 'DYMVA_ElepTdo', 'MonoHiggsMVA_ElepTdo', 'formulasMC_ElepTdo', 'JJHEFT_ElepTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },
 
  'ElepTdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo_suffix', 'trigMCKeepRun_ElepTdo', 'LeptonSF_ElepTdo', 'l2Kin_ElepTdo', 'l3Kin_ElepTdo', 'l4Kin_ElepTdo', 'DYMVA_ElepTdo', 'MonoHiggsMVA_ElepTdo', 'formulasMC_ElepTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'ElepTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'EmbElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbElepTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTup_suffix','trigMCKeepRun_ElepTup','LeptonSF_ElepTup','l2Kin_ElepTup', 'l3Kin_ElepTup', 'l4Kin_ElepTup','DYMVA_ElepTup','MonoHiggsMVA_ElepTup','formulasEMBED_ElepTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'EmbElepTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTdo_suffix','trigMCKeepRun_ElepTdo','LeptonSF_ElepTdo','l2Kin_ElepTdo', 'l3Kin_ElepTdo', 'l4Kin_ElepTdo','DYMVA_ElepTdo','MonoHiggsMVA_ElepTdo','formulasEMBED_ElepTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

## ------- mu-Scale

  'do_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

                
  'do_MupTup_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_MupTup")',
                  'module'     : 'MupTup()',
                },

  'do_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

  'do_MupTdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_MupTdo")',
                  'module'     : 'MupTdo()',
                },
  
  'MupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'MupTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'DYMVA_MupTup', 'MonoHiggsMVA_MupTup', 'formulasMC_MupTup', 'JJHEFT_MupTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'DYMVA_MupTup', 'MonoHiggsMVA_MupTup', 'formulasMC_MupTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'MupTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'l2Kin_MupTdo', 'l3Kin_MupTdo', 'l4Kin_MupTdo', 'DYMVA_MupTdo', 'MonoHiggsMVA_MupTdo', 'formulasMC_MupTdo', 'JJHEFT_MupTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'l2Kin_MupTdo', 'l3Kin_MupTdo', 'l4Kin_MupTdo', 'DYMVA_MupTdo', 'MonoHiggsMVA_MupTdo', 'formulasMC_MupTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },
  
  'MupTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'MupTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


  'EmbMupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbMupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbMupTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'DYMVA_MupTup', 'MonoHiggsMVA_MupTup', 'formulasEMBED_MupTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'EmbMupTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'l2Kin_MupTdo', 'l3Kin_MupTdo', 'l4Kin_MupTdo', 'DYMVA_MupTdo', 'MonoHiggsMVA_MupTdo', 'formulasEMBED_MupTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

#-------------------------  Fatjet Systematics steps

  'CorrFatJetMC_fatjetJESBase' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'LatinoAnalysis.NanoGardener.modules.FatJetCorrHelper',
                'declare': 'corr_fatjet_mc_alljes = createFatjetCorrector( globalTag="Regrouped_RPLME_JESGT", dataYear="RPLME_YEAR", jetType="AK8PFPuppi", isMC=True, jesUncert=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], redojec=True, applySmearing=True)',
                'module':  'corr_fatjet_mc_alljes()'
    },

   'CleanFatJet_fatjetJESup' : createFatjetJESvariation("Total", "Up"), 
   'CleanFatJet_fatjetJESdo' : createFatjetJESvariation("Total", "Do"), 
   'CleanFatJet_fatjetJESAbsoluteup' : createFatjetJESvariation("Absolute", "Up"), 
   'CleanFatJet_fatjetJESAbsolutedo' : createFatjetJESvariation("Absolute", "Do"), 
   'CleanFatJet_fatjetJESAbsolute_RPLME_YEARup' : createFatjetJESvariation("Absolute_RPLME_YEAR", "Up"), 
   'CleanFatJet_fatjetJESAbsolute_RPLME_YEARdo' : createFatjetJESvariation("Absolute_RPLME_YEAR", "Do"), 
   'CleanFatJet_fatjetJESBBEC1up' : createFatjetJESvariation("BBEC1", "Up"), 
   'CleanFatJet_fatjetJESBBEC1do' : createFatjetJESvariation("BBEC1", "Do"), 
   'CleanFatJet_fatjetJESBBEC1_RPLME_YEARup' : createFatjetJESvariation("BBEC1_RPLME_YEAR", "Up"), 
   'CleanFatJet_fatjetJESBBEC1_RPLME_YEARdo' : createFatjetJESvariation("BBEC1_RPLME_YEAR", "Do"), 
   'CleanFatJet_fatjetJESEC2up' : createFatjetJESvariation("EC2", "Up"), 
   'CleanFatJet_fatjetJESEC2do' : createFatjetJESvariation("EC2", "Do"), 
   'CleanFatJet_fatjetJESEC2_RPLME_YEARup' : createFatjetJESvariation("EC2_RPLME_YEAR", "Up"), 
   'CleanFatJet_fatjetJESEC2_RPLME_YEARdo' : createFatjetJESvariation("EC2_RPLME_YEAR", "Do"), 
   'CleanFatJet_fatjetJESFlavorQCDup' : createFatjetJESvariation("FlavorQCD", "Up"), 
   'CleanFatJet_fatjetJESFlavorQCDdo' : createFatjetJESvariation("FlavorQCD", "Do"), 
   'CleanFatJet_fatjetJESHFup' : createFatjetJESvariation("HF", "Up"), 
   'CleanFatJet_fatjetJESHFdo' : createFatjetJESvariation("HF", "Do"), 
   'CleanFatJet_fatjetJESHF_RPLME_YEARup' : createFatjetJESvariation("HF_RPLME_YEAR", "Up"), 
   'CleanFatJet_fatjetJESHF_RPLME_YEARdo' : createFatjetJESvariation("HF_RPLME_YEAR", "Do"), 
   'CleanFatJet_fatjetJESRelativeBalup' : createFatjetJESvariation("RelativeBal", "Up"), 
   'CleanFatJet_fatjetJESRelativeBaldo' : createFatjetJESvariation("RelativeBal", "Do"), 
   'CleanFatJet_fatjetJESRelativeSample_RPLME_YEARup' : createFatjetJESvariation("RelativeSample_RPLME_YEAR", "Up"), 
   'CleanFatJet_fatjetJESRelativeSample_RPLME_YEARdo' : createFatjetJESvariation("RelativeSample_RPLME_YEAR", "Do"), 

    'CleanFatJet_fatjetJMSup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmsup = lambda : FatJetMaker( input_branch_suffix="jmsUp",output_branch_map="fatjetJMSup", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmsup()'
    },

     'CleanFatJet_fatjetJMSdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmsdo = lambda : FatJetMaker( input_branch_suffix="jmsDown",output_branch_map="fatjetJMSdo", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmsdo()'
    },

    'CleanFatJet_fatjetJMRup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmrup = lambda : FatJetMaker( input_branch_suffix="jmrUp", output_branch_map="fatjetJMRup",jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmrup()'
    },

     'CleanFatJet_fatjetJMRdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmrdo = lambda : FatJetMaker( input_branch_suffix="jmrDown",output_branch_map="fatjetJMRdo", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmrdo()'
    },

     'CleanFatJet_fatjetJERup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jerup = lambda : FatJetMaker( input_branch_suffix="jerUp", output_branch_map="fatjetJERup",jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jerup()'
    },

     'CleanFatJet_fatjetJERdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jerdo = lambda : FatJetMaker( input_branch_suffix="jerDown",output_branch_map="fatjetJERdo", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jerdo()'
    },
 
  #########################
  ############  Boosted WtagSF for VBSjjlnu analysis
      'BoostedWtagSF_fatjetJMSup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jmsUp = lambda : BoostedWtagSF(input_branch_suffix="jmsUp",output_branch_map="fatjetJMSup", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jmsUp()'
      },

      'BoostedWtagSF_fatjetJMSdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jmsDo = lambda : BoostedWtagSF(input_branch_suffix="jmsDown",output_branch_map="fatjetJMSdo", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jmsDo()'
      },

      'BoostedWtagSF_fatjetJMRup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jmrUp = lambda : BoostedWtagSF(input_branch_suffix="jmrUp",output_branch_map="fatjetJMRup", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jmrUp()'
      },

      'BoostedWtagSF_fatjetJMRdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jmrDo = lambda : BoostedWtagSF(input_branch_suffix="jmrDown",output_branch_map="fatjetJMRdo", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jmrDo()'
      },

      'BoostedWtagSF_fatjetJERup' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jerUp = lambda : BoostedWtagSF(input_branch_suffix="jerUp",output_branch_map="fatjetJERup", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jerUp()'
      },

      'BoostedWtagSF_fatjetJERdo' : {
                    'isChain'    : False ,
                    'do4MC'      : True  ,
                    'do4Data'    : True  ,
                    'import'     : 'LatinoAnalysis.NanoGardener.modules.BoostedWtagSF',
                    'declare'    : 'boostedWtagsf_jerDo = lambda : BoostedWtagSF(input_branch_suffix="jerDown",output_branch_map="fatjetJERdo", year="RPLME_YEAR", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8)',
                    'module'     : 'boostedWtagsf_jerDo()'
      },

    'BoostedWtagSF_fatjetJESup' : createFatjetJESvariation_Wtagging("Total", "Up"), 
    'BoostedWtagSF_fatjetJESdo' : createFatjetJESvariation_Wtagging("Total", "Do"),
    'BoostedWtagSF_fatjetJESAbsoluteup' : createFatjetJESvariation_Wtagging("Absolute", "Up"), 
    'BoostedWtagSF_fatjetJESAbsolutedo' : createFatjetJESvariation_Wtagging("Absolute", "Do"), 
    'BoostedWtagSF_fatjetJESAbsolute_RPLME_YEARup' : createFatjetJESvariation_Wtagging("Absolute_RPLME_YEAR", "Up"), 
    'BoostedWtagSF_fatjetJESAbsolute_RPLME_YEARdo' : createFatjetJESvariation_Wtagging("Absolute_RPLME_YEAR", "Do"), 
    'BoostedWtagSF_fatjetJESBBEC1up' : createFatjetJESvariation_Wtagging("BBEC1", "Up"), 
    'BoostedWtagSF_fatjetJESBBEC1do' : createFatjetJESvariation_Wtagging("BBEC1", "Do"), 
    'BoostedWtagSF_fatjetJESBBEC1_RPLME_YEARup' : createFatjetJESvariation_Wtagging("BBEC1_RPLME_YEAR", "Up"), 
    'BoostedWtagSF_fatjetJESBBEC1_RPLME_YEARdo' : createFatjetJESvariation_Wtagging("BBEC1_RPLME_YEAR", "Do"), 
    'BoostedWtagSF_fatjetJESEC2up' : createFatjetJESvariation_Wtagging("EC2", "Up"), 
    'BoostedWtagSF_fatjetJESEC2do' : createFatjetJESvariation_Wtagging("EC2", "Do"), 
    'BoostedWtagSF_fatjetJESEC2_RPLME_YEARup' : createFatjetJESvariation_Wtagging("EC2_RPLME_YEAR", "Up"), 
    'BoostedWtagSF_fatjetJESEC2_RPLME_YEARdo' : createFatjetJESvariation_Wtagging("EC2_RPLME_YEAR", "Do"), 
    'BoostedWtagSF_fatjetJESFlavorQCDup' : createFatjetJESvariation_Wtagging("FlavorQCD", "Up"), 
    'BoostedWtagSF_fatjetJESFlavorQCDdo' : createFatjetJESvariation_Wtagging("FlavorQCD", "Do"), 
    'BoostedWtagSF_fatjetJESHFup' : createFatjetJESvariation_Wtagging("HF", "Up"), 
    'BoostedWtagSF_fatjetJESHFdo' : createFatjetJESvariation_Wtagging("HF", "Do"), 
    'BoostedWtagSF_fatjetJESHF_RPLME_YEARup' : createFatjetJESvariation_Wtagging("HF_RPLME_YEAR", "Up"), 
    'BoostedWtagSF_fatjetJESHF_RPLME_YEARdo' : createFatjetJESvariation_Wtagging("HF_RPLME_YEAR", "Do"), 
    'BoostedWtagSF_fatjetJESRelativeBalup' : createFatjetJESvariation_Wtagging("RelativeBal", "Up"), 
    'BoostedWtagSF_fatjetJESRelativeBaldo' : createFatjetJESvariation_Wtagging("RelativeBal", "Do"), 
    'BoostedWtagSF_fatjetJESRelativeSample_RPLME_YEARup' : createFatjetJESvariation_Wtagging("RelativeSample_RPLME_YEAR", "Up"), 
    'BoostedWtagSF_fatjetJESRelativeSample_RPLME_YEARdo' : createFatjetJESvariation_Wtagging("RelativeSample_RPLME_YEAR", "Do"),


    # chain of chains
    'systematics': {
        'isChain': True,
        'do4MC': True,
        'do4Data': False,
        'subTargets': ['JESup_suffix', 'JESdo_suffix', 'JERup_suffix', 'JERdo_suffix', 'METup_suffix', 'METdo_suffix', 'ElepTup_suffix', 'ElepTdo_suffix', 'MupTup_suffix', 'MupTdo_suffix'],
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
    },

# ------------------------------------ SKIMS : CUTS ONLY ----------------------------------------------------------

  'TrgwSel'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection'  : '"((TriggerEffWeight_2l_u/TriggerEffWeight_2l)>10)"' ,
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

  'wwSel'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(mll>12 && ptll>30 && (MET_pt > 20 || PuppiMET_pt>20) && Alt$(Lepton_pt[0],0.)>20 && Alt$(Lepton_pt[1],0.)>10 && Alt$(Lepton_pt[2],0.)<10 && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13)"',
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

## ------- Fake Study:

  'fakeSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' ,
                 },


  'fakeSelKinMC'  : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"(MET_pt < 20 || PuppiMET_pt < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                  'DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2','DYJetsToLL_M-10to50-LO_ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu-LO',
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                 ] ,               
                    'subTargets' : ['baseW','rochesterMC','trigMC','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCnoSF'] ,
                 },



  'fakeSelMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                  'DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf', 'GJets_HT40To100', 'GJets_HT40To100-ext1',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                  ###
                                  'GJetsDR04_HT40To100', 'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf',
                                  'GJets_HT40To100-ext1',
                                 ] ,               
                 },

## ------- 2-Leptons: Loose / tightOR

#  'l2loose'   : {
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : True  , 
#                  'selection'  : '"(nLepton>=2)"' , 
#                 },

# Run MVA after 2 lepton selection !
   'l2loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(nLepton>=2)"' ,
                  'subTargets' : ['DYMVA','MonoHiggsMVA','JJHEFT'], 
                  'excludeSample' : LNuQQSamples
                },


#muWP='cut_Tight80x'
#eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016','mva_90p_Iso2016_SS']
  'l2tightOR2016' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v7' : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_tthmva_70[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS_tthmva_70[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5              \
                                         || Lepton_isTightMuon_cut_Tight80x_tthmva_80[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_tthmva_70[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS_tthmva_70[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5              \
                                         || Lepton_isTightMuon_cut_Tight80x_tthmva_80[1] > 0.5             ) \
                                  "' ,
                  'subTargets' : ['EFTaBDTsplit'],
                 },

  'l2tightOR2017' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' , 
                 },

  'l2tightOR2017v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v7' : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_tthmva_70[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS_tthmva_70[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             \
                                         || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_tthmva_70[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS_tthmva_70[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5              \
                                         || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[1] > 0.5             ) \
                                  "' ,
                  'subTargets' : ['EFTaBDTsplit'],
                 },

  'l2tightOR2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },


  'l2tightOR2018v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v7' : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_tthmva_70[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS_tthmva_70[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             \
                                         || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_tthmva_70[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS_tthmva_70[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5              \
                                         || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[1] > 0.5             ) \
                                  "' ,
                  'subTargets' : ['EFTaBDTsplit'],
                 },

## ------- 1-Lepton: tightOR (For LNuQQ samples)

  'l1tightOR2016v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>30) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2017v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>30) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2018v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>30) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },


## ------- Analysis Skims:

  'trainDYMVA'   : {
                 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : True  ,
                 'selection'  : '"(mll>12 && Lepton_pt[0]>20 && Lepton_pt[1]>10 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
                                   && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 && LepCut2l==1 \
                                   && ptll>30 && PuppiMET_pt > 20 && fabs(91.1876 - mll) > 15 \
                                   && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)))"' ,
                 'onlySample' : [
                                 #### DY
                                 'DYJetsToLL_M-10to50-LO',
                                 'DYJetsToLL_M-50-LO-ext1',
                                 #### Higgs
                                 'GluGluHToWWTo2L2NuPowheg_M125_private','VBFHToWWTo2L2NuPowheg_M125_private',
                                ] ,
                 },

  'trainDYMVA_0j'   : {
                 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : True  ,
                 'selection'  : '"(Alt$(CleanJet_pt[0], 0) < 30 \
                                   && mll>12 && Lepton_pt[0]>25 && Lepton_pt[1]>10 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
                                   && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
                                   && ptll>30 && PuppiMET_pt > 20 && fabs(91.1876 - mll) > 15 \
                                   && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)))"' ,
                 'onlySample' : [
                                 ##   2016   ###
                                 #### DY
                                 'DYJetsToLL_M-10to50','DYJetsToLL_M-10to50-LO','DYJetsToLL_M-10to50_ext1',
                                 'DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-50-LO_ext2',
                                 #### Higgs
                                 'GluGluHToWWTo2L2Nu_M125_CUETDown','GluGluHToWWTo2L2Nu_M125_CUETDown',
                                 'GluGluHToWWTo2L2NuAMCNLO_M125','GluGluHToWWTo2L2NuPowheg_M125'
                                ] ,
                 },


  ##################################################################
  ########### VBSjjlnu semileptonic analysis SKIM
  #################################################################

  'VBSjjlnu_pairing': {
      'isChain'    : False ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_JetPairing',
      'declare'    : 'vbs_pairing = lambda : VBSjjlnu_JetPairing(year="RPLME_YEAR", mode="ALL", debug=False)',
      'module'     : 'vbs_pairing()',
      'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
  },

  'VBSjjlnu_kin': {
      'isChain'    : False ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_kin',
      'declare'    : 'vbs_vars_maker = lambda : VBSjjlnu_kin(mode=["maxmjj","maxmjj_massWZ"], met="PuppiMET", debug=False)',
      'module'     : 'vbs_vars_maker()',
      'onlySample' : vbsjjlnu_samples_mc + vbsjjlnu_samples_data2016 + vbsjjlnu_samples_data2017 + vbsjjlnu_samples_data2018
  },


  ############ New VBSjjlnu v5 skim and systematics
  ### News: 
  ### - rerun the NLOEWk modules
  ### - rerun trigMC to fix the trig efficiency systematic for electrons
  ### - rerun FatJet correction and cleaning


  'VBSjjlnuSkim2016v5' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2016"]["MC"],
      'subTargets': ['wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_mc
  },

  'VBSjjlnuSkim2016v5_data' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2016"]["DATA"],  
      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2016
  },

  'VBSjjlnuSkim2017v5' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2017"]["MC"],
      'subTargets': ['wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_mc
  },

  'VBSjjlnuSkim2017v5_data' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2017"]["DATA"],  
      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2017
  },

  'VBSjjlnuSkim2018v5' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2018"]["MC"],
      'subTargets': ['wwNLOEWK','wwNLOEWK2','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_mc
  },

  'VBSjjlnuSkim2018v5_data' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : CombJJLNu_preselections["2018"]["DATA"],  
      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2018
  },

  #### Fatjet systematics are included at the bottom

# ------------------------------------ SPECIAL STEPS: HADD & UEPS -------------------------------------------------

## ------- HADD 

  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'SizeMax'    : 1e9 ,
                 #'bigSamples' : ['DYJetsToLL_M-50','DY2JetsToLL','ZZTo2L2Q','DYJetsToLL_M-50-LO',
                 #                'DYJetsToLL_M-50-LO-ext1',
                 #                'WZTo2L2Q','TTToSemiLepton','TTToSemiLeptonic','TTTo2L2Nu_ext1','TTJetsDiLep-LO-ext1','TTTo2L2Nu',
                 #                'DYJetsToEE_Pow',
                 #                'DY1JetsToLL',
                 #                #'TTJets',
                 #               ],
               },

## ------- UEPS 
## ------- UEPS 

  'UEPS'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'onlySample' : [
                                    'GluGluHToWWTo2L2NuPowheg_M125_CP5Up', 'VBFHToWWTo2L2NuPowheg_M125_CP5Up', 'VBFHToWWTo2L2Nu_M125_CP5Up', 'WWTo2L2Nu_CP5Up',
                                    'GluGluHToWWTo2L2NuPowheg_M125_CP5Down', 'VBFHToWWTo2L2NuPowheg_M125_CP5Down', 'VBFHToWWTo2L2Nu_M125_CP5Down', 'WWTo2L2Nu_CP5Down',
                                    'GluGluHToWWTo2L2Nu_M125_CUETDown' , 'VBFHToWWTo2L2Nu_M125_CUETDown' , 'WWTo2L2Nu_CUETDown' ,
                                    'GluGluHToWWTo2L2Nu_M125_CUETUp'   , 'VBFHToWWTo2L2Nu_M125_CUETUp'   , 'WWTo2L2Nu_CUETUp'   ,
                                    'GluGluHToWWTo2L2NuHerwigPS_M125'  , 'VBFHToWWTo2L2NuHerwigPS_M125'  , 'WWTo2L2NuHerwigPS'  ,
                                    'GluGluHToWWTo2L2Nu_M125_herwigpp' , 'VBFHToWWTo2L2Nu_M125_herwigpp',
                                 ] ,
                  'cpMap' : {
                              'UEdo' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Down' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Down'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'VBFHToWWTo2L2Nu_M125_CP5Down'    : ['VBFHToWWTo2L2Nu_M125']    ,
                                          'WWTo2L2Nu_CP5Down'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                          'GluGluHToWWTo2L2Nu_M125_CUETDown' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETDown'    : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETDown'               : ['WWTo2L2Nu'] ,
                                       },
                              'UEup' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Up' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Up'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'VBFHToWWTo2L2Nu_M125_CP5Up'    : ['VBFHToWWTo2L2Nu_M125']    ,
                                          'WWTo2L2Nu_CP5Up'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                          'GluGluHToWWTo2L2Nu_M125_CUETUp'   : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETUp'      : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETUp'                 : ['WWTo2L2Nu'] ,
                                       },
                              'PS'   : {
                                          'GluGluHToWWTo2L2NuHerwigPS_M125'  : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'GluGluHToWWTo2L2Nu_M125_herwigpp' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuHerwigPS_M125'     : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125'] ,
                                          'VBFHToWWTo2L2Nu_M125_herwigpp'    : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125'] ,
                                          'WWTo2L2NuHerwigPS'                : ['WWTo2L2Nu'] ,
                                       },
                            },
               },
}

# Copy versions
Steps['MCSusy2016v6']    = Steps['MCSusy2016']
Steps['MCSusy2016FSv6']  = Steps['MCSusy2016FS']
Steps['MCSusy2017v6']    = Steps['MCSusy2017']
Steps['MCSusy2017FSv6']  = Steps['MCSusy2017FS']
Steps['MCSusy2018v6']    = Steps['MCSusy2018']
Steps['MCSusy2018FSv6']  = Steps['MCSusy2018FS']

# METFixEEDATA2017
for dataperiod in [ 'B', 'C', 'D', 'E', 'F' ] :
    Steps['DATASusy2017'+dataperiod+'v6'] = { }
    for key in Steps['DATASusy2017v6']:
        if key!='subTargets':
            Steps['DATASusy2017'+dataperiod+'v6'][key] = Steps['DATASusy2017v6'][key]
        else:
            Steps['DATASusy2017'+dataperiod+'v6']['subTargets'] = [ ]
            for subtarget in Steps['DATASusy2017v6']['subTargets']:
                Steps['DATASusy2017'+dataperiod+'v6']['subTargets'].append(subtarget)
            Steps['DATASusy2017'+dataperiod+'v6']['subTargets'].insert(1, 'METFixEEDATA2017'+dataperiod)

for dataperiod in [ 'B', 'C', 'D', 'E', 'F' ] :
    Steps['DATALatino2017'+dataperiod+'v6'] = { }
    for key in Steps['DATALatino2017v6']:
        if key!='subTargets':
            Steps['DATALatino2017'+dataperiod+'v6'][key] = Steps['DATALatino2017v6'][key]
        else:
            Steps['DATALatino2017'+dataperiod+'v6']['subTargets'] = [ ]
            for subtarget in Steps['DATALatino2017v6']['subTargets']:
                Steps['DATALatino2017'+dataperiod+'v6']['subTargets'].append(subtarget)
            Steps['DATALatino2017'+dataperiod+'v6']['subTargets'].insert(1, 'METFixEEDATA2017'+dataperiod)

# btagPerEvent 

# Old style. To be removed after transition to UL
for datatype in [ '', 'FS', 'Data' ] :
    for year in [ '2016', '2017', '2018' ] : 
        for ptcut in [ '25', '30' ] :
	    Steps['btagPerEvent'+year+datatype+'Pt'+ptcut] = { }
            for key in Steps['btagPerEvent'+year+datatype]: 
                Steps['btagPerEvent'+year+datatype+'Pt'+ptcut][key] = Steps['btagPerEvent'+year+datatype][key]
            Steps['btagPerEvent'+year+datatype+'Pt'+ptcut]['module'] = Steps['btagPerEvent'+year+datatype]['module'].replace('bTagPtCut="20"', 'bTagPtCut="'+ptcut+'"') 
# end old style to be removed

for datatype in [ 'FS', 'Data' ] :
    
    Steps['btagPerEventDeepCSVWPs'+datatype] = { }
    for key in Steps['btagPerEventDeepCSVWPs']:
        Steps['btagPerEventDeepCSVWPs'+datatype][key] = Steps['btagPerEventDeepCSVWPs'][key]
    if datatype=='FS':
        Steps['btagPerEventDeepCSVWPs'+datatype]['module'] = Steps['btagPerEventDeepCSVWPs'+datatype]['module'].replace('dataType="mc"', 'dataType="fastsim"')
    elif datatype=='Data':
        Steps['btagPerEventDeepCSVWPs'+datatype]['do4MC'] = False
        Steps['btagPerEventDeepCSVWPs'+datatype]['do4Data'] = True
        Steps['btagPerEventDeepCSVWPs'+datatype]['module'] = Steps['btagPerEventDeepCSVWPs'+datatype]['module'].replace('dataType="mc"', 'dataType="data"')

    if datatype=='FS':

        Steps['btagPerJetDeepCSVWPs'+datatype] = { }
        for key in Steps['btagPerJetDeepCSVWPs']:
            Steps['btagPerJetDeepCSVWPs'+datatype][key] = Steps['btagPerJetDeepCSVWPs'][key]
        Steps['btagPerJetDeepCSVWPs'+datatype]['declare'] = Steps['btagPerJetDeepCSVWPs'+datatype]['declare'].replace('btagSFProducerWPs =', 'btagSFProducerWPs'+datatype+' =') 
        Steps['btagPerJetDeepCSVWPs'+datatype]['declare'] = Steps['btagPerJetDeepCSVWPs'+datatype]['declare'].replace('doFastSim=False', 'doFastSim=True')
        Steps['btagPerJetDeepCSVWPs'+datatype]['module'] = Steps['btagPerJetDeepCSVWPs'+datatype]['module'].replace('btagSFProducerWPs()', 'btagSFProducerWPs'+datatype+'()')

# mt2Producer regions

mt2CRs = [ 'SameSign', 'Fake', 'WZ', 'WZtoWW', 'ttZ', 'ZZ' ]

mt2regions = [ x for x in mt2CRs ]
mt2regions.extend([ 'ctrl'+x for x in mt2CRs ])
mt2regions.extend([ 'reco', 'fast' ])

for region in mt2CRs: 

    Steps['susyMT2'+region+'Nomin']     = { }
    Steps['susyMT2ctrl'+region+'Nomin'] = { }

    for key in Steps['susyMT2recoNomin']:
        Steps['susyMT2'+region+'Nomin'][key]     = Steps['susyMT2recoNomin'][key]  
        Steps['susyMT2ctrl'+region+'Nomin'][key] = Steps['susyMT2recoNomin'][key]

    Steps['susyMT2'+region+'Nomin']['module'] = Steps['susyMT2recoNomin']['module'].replace('analysisRegion=""', 'analysisRegion="'+region+'"')
    Steps['susyMT2ctrl'+region+'Nomin']['module'] = Steps['susyMT2'+region+'Nomin']['module'].replace('filterRegion="region"', 'filterRegion="control"')
   
# JES, JER, MET variations

for treesyst in [ 'nom', 'jer', 'jesTotalDown', 'jesTotalUp', 'unclustEnDown', 'unclustEnUp', 'jerDown', 'jerUp', 'jesTotalSmearDown', 'jesTotalSmearUp', 'unclustEnSmearDown', 'unclustEnSmearUp' ]:

  treesystname = treesyst.replace('Total', '').replace('unclustEn', 'MET').upper().replace('UP', 'Up').replace('DOWN', 'Do').replace('NOM', 'Nomin')
  treesystname = treesystname.replace('JESSMEAR', 'SJS').replace('METSMEAR', 'SMT')
  if treesystname=='JER': treesystname = 'Smear'
  
  if treesyst in [ 'nom', 'jesTotalDown', 'jesTotalUp', 'jerDown', 'jerUp' ]:

    Steps['PtCorr'+treesystname] = { } 
    for key in Steps['PtCorrReader']:
      Steps['PtCorr'+treesystname][key] = Steps['PtCorrReader'][key]
    Steps['PtCorr'+treesystname]['declare'] = Steps['PtCorrReader']['declare'].replace('SYSTVAR', treesyst)
    Steps['PtCorr'+treesystname]['module'] = Steps['PtCorrReader']['module'].replace('SYSTVAR', treesyst)

    for year in [ '2016', '2017', '2018' ]:
      for datatype in [ 'MC', 'FS' ]:
      
        Steps[datatype+'Susy'+treesystname+year+'v6loose'] = { } 
        for key in Steps[datatype+'SusySyst'+year+'v6loose']:
          if key!='subTargets':
            Steps[datatype+'Susy'+treesystname+year+'v6loose'][key] = Steps[datatype+'SusySyst'+year+'v6loose'][key]
          else: 
            Steps[datatype+'Susy'+treesystname+year+'v6loose'][key] = [ 'PtCorr'+treesystname if x=='PtCorrReader' else x for x in Steps[datatype+'SusySyst'+year+'v6loose'][key] ]
                  
  if treesyst!='nom': 

    for region in mt2regions: 

      addfilter = '' if (treesyst=='jer' or region not in [ 'reco', 'fast' ]) else 'syst'
    
      Steps['susyMT2'+region+treesystname] = { }
      for key in Steps['susyMT2'+region+'Nomin']:
        Steps['susyMT2'+region+treesystname][key] = Steps['susyMT2'+region+'Nomin'][key] 
      Steps['susyMT2'+region+treesystname]['module'] = Steps['susyMT2'+region+'Nomin']['module'].replace('metSystematic="nom", filterRegion="', 'metSystematic="'+treesyst+'", filterRegion="'+addfilter)   

  Steps['susyMT2ctrl'+treesystname] = {
      'isChain'    : True  ,
      'do4MC'      : True  ,
      'do4Data'    : False ,
      'subTargets' : [ 'susyMT2ctrl'+x+treesystname for x in mt2CRs ],
    }
  if treesyst=='nom': 
    Steps['susyMT2ctrl'+treesystname]['do4Data'] = True

#

Steps.update(addJESchainMembers())
Steps.update(addMETchainMembers())
Steps.update(addSystChainMembers_CombJJLNu())

# ## ADD systematics for VBSjjlnu & HMjjlnu analysis & MonoHiggsSemiLep
Steps.update(prepare_CombJJLNu_syst("MCCombJJLNu2016", CombJJLNu_preselections["2016"]["MC"]))
Steps.update(prepare_CombJJLNu_syst("MCCombJJLNu2017", CombJJLNu_preselections["2017"]["MC"]))
Steps.update(prepare_CombJJLNu_syst("MCCombJJLNu2018", CombJJLNu_preselections["2018"]["MC"]))
