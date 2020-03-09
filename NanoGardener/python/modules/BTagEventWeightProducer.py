import ROOT
import os
import copy
ROOT.PyConfig.IgnoreCommandLineOptions = True

import math

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class BTagEventWeightProducer(Module):
    def __init__(self, collection="Lepton", bTagAlgo="", bTagWP="", dataType='mc', bTagMethod = '1d', bTagPtCut = '20', bTagEff_path=''):
        self.collection = collection
        self.bTagAlgo = bTagAlgo
        self.random = ROOT.TRandom3(0)
        self.dataType = dataType
        self.bTagMethod = bTagMethod
        self.bTagPtCut = bTagPtCut
        self.bTagEff_path = bTagEff_path
        self.bTagEtaMax = 2.4 if ('2016' in bTagWP) else 2.5
        self.bTagFlag = ''
        if bTagMethod!='1d':
            self.bTagFlag = '_' + bTagAlgo + bTagWP[-1] + '_' + bTagMethod
            if bTagPtCut!='20': self.bTagFlag += '_Pt' + bTagPtCut
        print self.bTagFlag
        self.bTagWP = bTagWP
        if bTagAlgo=='btagDeepB':
            if '2016' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.2217
                if bTagWP[-1]=='M': self.bTagCut = 0.6321
                if bTagWP[-1]=='T': self.bTagCut = 0.8953
            elif '2017' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.1522
                if bTagWP[-1]=='M': self.bTagCut = 0.4941
                if bTagWP[-1]=='T': self.bTagCut = 0.8001
            elif '2018' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.1241
                if bTagWP[-1]=='M': self.bTagCut = 0.4184
                if bTagWP[-1]=='T': self.bTagCut = 0.7527
        elif bTagAlgo=="btagDeepFlavB": 
            if '2016' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.0614
                if bTagWP[-1]=='M': self.bTagCut = 0.3093
                if bTagWP[-1]=='T': self.bTagCut = 0.7221
            elif '2017' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.0521
                if bTagWP[-1]=='M': self.bTagCut = 0.3033
                if bTagWP[-1]=='T': self.bTagCut = 0.7489
            elif '2018' in bTagWP: 
                if bTagWP[-1]=='L': self.bTagCut = 0.0494
                if bTagWP[-1]=='M': self.bTagCut = 0.2770
                if bTagWP[-1]=='T': self.bTagCut = 0.7264
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        if self.bTagMethod!='1d' :

            self.out.branch('leadingPtTagged'+self.bTagFlag,'F')      
            self.out.branch('trailingPtTagged'+self.bTagFlag,'F')

        btagVar = 'btagWeight'+self.bTagFlag if (self.bTagMethod[0]=='1') else 'leadingPtTagged'+self.bTagFlag

        if self.bTagMethod=='1c':
            btagVar = btagVar.replace("Weight", "Weight_1tag")
            self.out.branch(btagVar,'F') 
            self.out.branch(btagVar.replace("_1tag", "_2tag"),'F')

        self.central_and_systs_shape_corr = [ "central" ]

        if self.dataType=='data':
            return True

        self.systs_shape_corr = []
        if self.bTagMethod=='1d' :
            for syst in [ 'jes',
                          'lf', 'hf',
                          'hfstats1', 'hfstats2',
                          'lfstats1', 'lfstats2',
                          'cferr1', 'cferr2' ]:
                self.systs_shape_corr.append("up_%s" % syst)
                self.systs_shape_corr.append("down_%s" % syst)
        else :
            self.systs_shape_corr.append("b_up")
            self.systs_shape_corr.append("b_down")
            self.systs_shape_corr.append("l_up")
            self.systs_shape_corr.append("l_down")
            if self.dataType=='fastsim':
                self.systs_shape_corr.append("b_up_fastsim")
                self.systs_shape_corr.append("b_down_fastsim")
                self.systs_shape_corr.append("c_up_fastsim")
                self.systs_shape_corr.append("c_down_fastsim")
                self.systs_shape_corr.append("l_up_fastsim")
                self.systs_shape_corr.append("l_down_fastsim")
        self.central_and_systs_shape_corr.extend(self.systs_shape_corr)
        self.branchNames_central_and_systs_shape_corr={}
        for central_or_syst in self.central_and_systs_shape_corr:
            if central_or_syst == "central":
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = btagVar
            else:
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = "%s_%s" % (btagVar, central_or_syst)
            if central_or_syst!="central" or (self.bTagMethod!='1c' and self.bTagMethod!='2a'):
                self.out.branch(self.branchNames_central_and_systs_shape_corr[central_or_syst],'F') 
                
        if self.dataType!='data':
            if self.bTagMethod=='1a' or self.bTagMethod=='2a':
                self.bTagEfficiencies = {}
                cmssw_base = os.getenv('CMSSW_BASE')
                btageff_file = self.open_root(cmssw_base + '/src/' + self.bTagEff_path)
                sample_flag = 'ttbar' if (self.dataType=='mc') else 'T2tt'
                # These two is because histograms from mkShapes are unrolled
                self.bTagEfficiencies['jetptbins']  = self.get_root_obj(btageff_file, 'taggablejets_b/jetpt/histo_'+sample_flag)
                self.bTagEfficiencies['jetetabins'] = self.get_root_obj(btageff_file, 'taggablejets_b/jeteta/histo_'+sample_flag)
                self.bTagEfficiencies['taggable_b'] = self.get_root_obj(btageff_file, 'taggablejets_b/jetpteta/histo_'+sample_flag)
                self.bTagEfficiencies['taggable_c'] = self.get_root_obj(btageff_file, 'taggablejets_c/jetpteta/histo_'+sample_flag)
                self.bTagEfficiencies['taggable_l'] = self.get_root_obj(btageff_file, 'taggablejets_l/jetpteta/histo_'+sample_flag)
                self.bTagEfficiencies['tagged_b'] = self.get_root_obj(btageff_file, self.bTagAlgo+'_'+self.bTagWP+'_b/jetpteta/histo_'+sample_flag)
                self.bTagEfficiencies['tagged_c'] = self.get_root_obj(btageff_file, self.bTagAlgo+'_'+self.bTagWP+'_c/jetpteta/histo_'+sample_flag)
                self.bTagEfficiencies['tagged_l'] = self.get_root_obj(btageff_file, self.bTagAlgo+'_'+self.bTagWP+'_l/jetpteta/histo_'+sample_flag)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def open_root(self, path, option=''):
        r_file = ROOT.TFile.Open(path, option)
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file

    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return copy.deepcopy(r_obj)

    def bTagEfficiency(self, jet_pt, jet_eta, jet_flv): 

        if abs(jet_flv)==5:
            flavour_flag = '_b'
        elif abs(jet_flv)==4 :
            flavour_flag = '_c'
        else :
            flavour_flag = '_l'

        """ This does not work because histograms from mkShapes are unrolled
        globalBin = self.bTagEfficiencies['taggable'+flavour_flag].FindBin(jet_pt, abs(jet_eta))
        
        binx, biny, binz = ROOT.Long(), ROOT.Long(), ROOT.Long()
        self.bTagEfficiencies['taggable'].GetBinXYZ(globalBin, binx, biny, binz)
        
        if binx==0: 
            binx = 1
        elif binx>self.bTagEfficiencies['taggable'+flavour_flag].GetNbinsX():
            binx = self.bTagEfficiencies['taggable'+flavour_flag].GetNbinsX()
        if biny==0:
            biny = 1
        elif biny>self.bTagEfficiencies['taggable'+flavour_flag].GetNbinsY():
            biny = self.bTagEfficiencies['taggable'+flavour_flag].GetNbinsY()
                
        njets_taggable = self.bTagEfficiencies['taggable'+flavour_flag].GetBinContent(binx, biny)
        """

        ptbin  = self.bTagEfficiencies['jetptbins'].FindBin(jet_pt)
        etabin = self.bTagEfficiencies['jetetabins'].FindBin(abs(jet_eta))
        nEtaBins = self.bTagEfficiencies['jetetabins'].GetNbinsX()
        globalBin = nEtaBins*(ptbin - 1) + etabin
       
        njets_taggable = self.bTagEfficiencies['taggable'+flavour_flag].GetBinContent(globalBin)

        if njets_taggable<=0:
            return 0.
        
        #njets_tagged = self.bTagEfficiencies['tagged'+flavour_flag].GetBinContent(binx, biny)
        njets_tagged = self.bTagEfficiencies['tagged'+flavour_flag].GetBinContent(globalBin)

        return njets_tagged/njets_taggable

    def getbTagSF(self, event, idx, jfl, central_or_syst):

        central_or_syst_flag = ""
        if (central_or_syst=="b_up" or central_or_syst=="b_down") and (abs(jfl)==5 or abs(jfl)==4):
            central_or_syst_flag = central_or_syst.replace("b", "")
        if (central_or_syst=="l_up" or central_or_syst=="l_down") and abs(jfl)<4:
            central_or_syst_flag = central_or_syst.replace("l", "")
        jet_weight = getattr(event, "Jet_btagSF%s" % central_or_syst_flag)[idx]
        if self.dataType=="fastsim":
            central_or_syst_fastsim_flag = ""
            if "fastsim" in central_or_syst:
                central_or_syst_temp = central_or_syst.replace('_fastsim', '')
                if "b" in central_or_syst_temp and abs(jfl)==5:	
                    central_or_syst_fastsim_flag = central_or_syst_temp.replace("b", "")
                if "c" in central_or_syst_temp and abs(jfl)==4:
                    central_or_syst_fastsim_flag = central_or_syst_temp.replace("c", "")
                if "l" in central_or_syst_temp and abs(jfl)<4:
                    central_or_syst_fastsim_flag = central_or_syst_temp.replace("l", "") 
            jet_weight *= getattr(event, "Jet_btagFastSimSF%s" % central_or_syst_fastsim_flag)[idx]

        return jet_weight


    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        leadingPtTaggedValue = { }
        trailingPtTaggedValue = { }

        for central_or_syst in self.central_and_systs_shape_corr:
            if central_or_syst=='central' or self.bTagMethod=='2a':
                            
                leadingPtTaggedValue[central_or_syst] = -1.     
                trailingPtTaggedValue[central_or_syst] = -1.

        for i in range(event.nCleanJet):
            if abs(event.CleanJet_eta[i])<self.bTagEtaMax and event.CleanJet_pt[i]>=float(self.bTagPtCut):

                idx = event.CleanJet_jetIdx[i]
                jet_discriminant = getattr(event, "Jet_%s" % self.bTagAlgo)[idx]

                bTagPass = jet_discriminant>=self.bTagCut

                if self.dataType!='data' and self.bTagMethod=='2a':
                    bTagDice = self.random.Rndm()
                    jfl = event.Jet_hadronFlavour[idx]
                    jet_bTagEff = self.bTagEfficiency(event.CleanJet_pt[i], 
                                                      event.CleanJet_eta[i], 
                                                      jfl)

                for central_or_syst in self.central_and_systs_shape_corr:
                    if central_or_syst=='central' or self.bTagMethod=='2a':

                        bTagConfirm = bTagPass
                    
                        if self.dataType!='data' and self.bTagMethod=='2a':

                            jet_weight = self.getbTagSF(event, idx, jfl, central_or_syst)

                            if jet_weight<1. and bTagPass==True:
                                if bTagDice<(1.-jet_weight):
                                    bTagConfirm = False
                            elif jet_weight>1. and bTagPass==False:
                                if bTagDice<((1.-jet_weight)/(1.-(1./jet_bTagEff))):
                                    bTagConfirm = True

                        if bTagConfirm==True:
                            
                            if event.CleanJet_pt[i]>leadingPtTaggedValue[central_or_syst] :
                                trailingPtTaggedValue[central_or_syst] = leadingPtTaggedValue[central_or_syst]
                                leadingPtTaggedValue[central_or_syst] = event.CleanJet_pt[i]
                            elif event.CleanJet_pt[i]>trailingPtTaggedValue[central_or_syst] :
                                trailingPtTaggedValue[central_or_syst] = event.CleanJet_pt[i]

        for central_or_syst in self.central_and_systs_shape_corr:
            if central_or_syst=='central':
                self.out.fillBranch('leadingPtTagged'+self.bTagFlag,  leadingPtTaggedValue[central_or_syst])   
            elif self.bTagMethod=='2a': 
                self.out.fillBranch(branchNames_central_and_systs_shape_corr[central_or_syst],  leadingPtTaggedValue[central_or_syst]) 

        self.out.fillBranch('trailingPtTagged'+self.bTagFlag, trailingPtTaggedValue['central'])

        if self.dataType=='data':
            if self.bTagMethod=='1c':
                self.out.fillBranch('btagWeight_1tag'+self.bTagFlag, (leadingPtTaggedValue['central']>=float(self.bTagPtCut)))
                self.out.fillBranch('btagWeight_2tag'+self.bTagFlag, (trailingPtTaggedValue['central']>=float(self.bTagPtCut)))
            return True

        if self.bTagMethod[0]!='1':
            return True

        for central_or_syst in self.central_and_systs_shape_corr:
            weight = 1.
            if self.bTagMethod=='1d' :
                if central_or_syst == "central":
                    weight = 1.
                    for i in range(event.nCleanJet):
                        #print event.nCleanJet , event.nJet , i , event.CleanJet_jetIdx[i]
                        #weight = weight*event.Jet_btagSF_shape[event.CleanJet_jetIdx[i]]
                        idx = event.CleanJet_jetIdx[i]
                        weight *= event.Jet_btagSF_shape[idx]
                else:
                    weight=1.
                    for i in range(event.nCleanJet):
                        weight = weight*getattr(event, "Jet_btagSF_shape_%s" % central_or_syst)[event.CleanJet_jetIdx[i]]
            else :
                if central_or_syst=='central':
                    weight1idx = [ ]
                    weight1jet = [ ]
		    weightjjet = [ ]
                    for j in range(event.nCleanJet):	
                        if event.CleanJet_pt[j]>=float(self.bTagPtCut) and abs(event.CleanJet_eta[j])<self.bTagEtaMax:
                            if getattr(event, "Jet_%s" % self.bTagAlgo)[event.CleanJet_jetIdx[j]]>=self.bTagCut:
                                weight1idx.append(j)
                                weight1jet.append(1.)
                                weightjjet.append(self.getbTagSF(event, event.CleanJet_jetIdx[j], event.Jet_hadronFlavour[j], central_or_syst))
                for i in range(event.nCleanJet):
                    if event.CleanJet_pt[i]>=float(self.bTagPtCut) and abs(event.CleanJet_eta[i])<self.bTagEtaMax:
                        idx = event.CleanJet_jetIdx[i]
                        jfl = event.Jet_hadronFlavour[idx]
                        jet_discriminant = getattr(event, "Jet_%s" % self.bTagAlgo)[idx]
                        jet_weight = self.getbTagSF(event, idx, jfl, central_or_syst)
                        if self.bTagMethod=='1a':
                            if jet_discriminant>=self.bTagCut:
                                weight *= jet_weight
                            else :
                                jet_bTagEff = self.bTagEfficiency(event.CleanJet_pt[i], 
                                                                  event.CleanJet_eta[i], 
                                                                  jfl)
                                weight *= (1. - jet_weight*jet_bTagEff)/(1. - jet_bTagEff)
                        elif self.bTagMethod=='1c':
                            if jet_discriminant>=self.bTagCut:
                                weight *= (1. - jet_weight)
                                if central_or_syst=='central':       
                                    for j in range(len(weight1jet)):
                                        if weight1idx[j]==i:
                                            weight1jet[j] *= jet_weight
                                        else:
                                            weight1jet[j] *= (1. - weightjjet[j])
                if self.bTagMethod=='1c':
                    weight = 1. - weight
                    if central_or_syst=='central':   
                        weight2tag = weight
                        for j in range(len(weight1jet)):
                            weight2tag -= weight1jet[j]
                        self.out.fillBranch(self.branchNames_central_and_systs_shape_corr[central_or_syst].replace("Weight_1tag", "Weight_2tag"), weight2tag)  
            self.out.fillBranch(self.branchNames_central_and_systs_shape_corr[central_or_syst], weight)   
            

        return True

