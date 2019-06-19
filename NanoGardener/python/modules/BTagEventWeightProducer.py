import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import math

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class BTagEventWeightProducer(Module):
    def __init__(self, collection="Lepton", bTagAlgo = "", bTagWP = "", isData = False):
        self.collection = collection
        self.bTagAlgo = bTagAlgo
        if bTagAlgo!="":
            self.bTagWP = bTagWP
            if bTagAlgo=="btagDeepB":
                if bTagWP=="2016M": 
                    self.bTagCut = 0.6321
                elif bTagWP=="2017M": 
                    self.bTagCut = 0.4941
                elif bTagWP=="2018M": 
                    self.bTagCut = 0.4184
            elif bTagAlgo=="btagDeepFlavB": 
                if bTagWP=="2016M": 
                    self.bTagCut = 0.3093
                elif bTagWP=="2017M": 
                    self.bTagCut = 0.3033
                elif bTagWP=="2018M": 
                    self.bTagCut = 0.2770
        self.isData = isData
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        if self.bTagAlgo!="" :
            self.out.branch('leadingPtTagged','F')      
            self.out.branch('trailingPtTagged','F')  

        if self.isData==True:
            return

        self.systs_shape_corr = []
        if self.bTagAlgo=="" :
            for syst in [ 'jes',
                          'lf', 'hf',
                          'hfstats1', 'hfstats2',
                          'lfstats1', 'lfstats2',
                          'cferr1', 'cferr2' ]:
                self.systs_shape_corr.append("up_%s" % syst)
                self.systs_shape_corr.append("down_%s" % syst)
        else :
            self.systs_shape_corr.append("up")
            self.systs_shape_corr.append("down")
        self.central_and_systs_shape_corr = [ "central" ]
        self.central_and_systs_shape_corr.extend(self.systs_shape_corr)
        self.branchNames_central_and_systs_shape_corr={}
        for central_or_syst in self.central_and_systs_shape_corr:
            if central_or_syst == "central":
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = "btagWeight"
            else:
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = "btagWeight_%s" % central_or_syst
            self.out.branch(self.branchNames_central_and_systs_shape_corr[central_or_syst],'F') 
                
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def bTagEfficiency(self, jet_pt, jet_eta, jet_flv): # This should be filled properly ...

        if "M" in self.bTagWP :
            if abs(jet_flv)==5 :
                return 0.7
            elif abs(jet_flv)==4 :
                return 0.2
            else :
                return 0.01

        return 0.

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        leadingPtTaggedValue = -999.     
        trailingPtTaggedValue = -999.
        for i in range(event.nCleanJet):
            idx = event.CleanJet_jetIdx[i]
            jet_discriminant = getattr(event, "Jet_%s" % self.bTagAlgo)[idx]
            if jet_discriminant>=self.bTagCut :
                if event.CleanJet_pt[i]>leadingPtTaggedValue :
                    trailingPtTaggedValue = leadingPtTaggedValue 
                    leadingPtTaggedValue = event.CleanJet_pt[i]
                elif event.CleanJet_pt[i]>trailingPtTaggedValue :
                    trailingPtTaggedValue = event.CleanJet_pt[i]
        self.out.fillBranch('leadingPtTagged',  leadingPtTaggedValue)  
        self.out.fillBranch('trailingPtTagged', trailingPtTaggedValue)  

        if self.isData==True:
            return True
                            
        for central_or_syst in self.central_and_systs_shape_corr:
            weight = 1.
            if self.bTagAlgo=="" :
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
                for i in range(event.nCleanJet):
                    if event.CleanJet_pt[i]>=20.:
                        central_or_syst_flag = ""
                        if central_or_syst != "central":
                            central_or_syst_flag = "_" + central_or_syst
                        idx = event.CleanJet_jetIdx[i]
                        jet_weight = getattr(event, "Jet_btagSF%s" % central_or_syst_flag)[idx]
                        jet_discriminant = getattr(event, "Jet_%s" % self.bTagAlgo)[idx]
                        if jet_discriminant>=self.bTagCut :
                            weight *= jet_weight
                        else :
                            jet_bTagEff = self.bTagEfficiency(event.CleanJet_pt[i], 
                                                              event.CleanJet_eta[i], 
                                                              event.Jet_hadronFlavour[idx])
                            weight *= (1. - jet_weight*jet_bTagEff)/(1. - jet_bTagEff)
                    
            self.out.fillBranch(self.branchNames_central_and_systs_shape_corr[central_or_syst], weight)   

        return True

