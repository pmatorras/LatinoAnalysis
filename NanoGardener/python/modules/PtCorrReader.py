import re
import math
import ROOT
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
import copy

class PtCorrReader(Module):
    '''
    Simplified version of PtCorrApplier, design to read the output from the standard jetmetHelperRun2
    '''
    def __init__(self, Coll='CleanJet', CorrSrc='nom', suffix=''):
        self.CollTC  = Coll
        self._suffix = suffix
        self.CorrSrc = CorrSrc

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.CollBr = {}
        # we clone it otherwise it changes as we add more branches
        oBrList = copy.deepcopy(self.out._tree.GetListOfBranches())
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            # GIULIO: we don't want to pick CleanJet_pt_JESup not CleanJet_jecUncert
            # KELLO: will exclude CleanJet_pt_JERup, CleanJet_corr_JER as well  
            if re.match('\A'+self.CollTC+'_', bname) and len(bname.split("_"))==2 and "jecUncert" not in bname and "corr_JER" not in bname:
                if btype not in self.CollBr: self.CollBr[btype] = []
                self.CollBr[btype].append(bname)
                self.out.branch(bname+self._suffix, btype, lenVar='n'+self.CollTC)
        
        #print inputFile, outputFile, inputTree
        if len(self.CollBr) < 1: raise IOError('PtCorrReader: no branches with ' + self.CollTC+'_' +  ' found in inputTree or outputTree.')
 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        coll = Collection(event, self.CollTC)
        jets = Collection(event, 'Jet')
        nColl = len(coll)

        # Create new pt
        new_pt = []
        for iObj in range(nColl):
            thisIdx = coll[iObj]['jetIdx']
            tmp_pt = jets[thisIdx]['pt_'+self.CorrSrc]
            new_pt.append(tmp_pt)

        # Reorder
        order = []
        for idx1, pt1 in enumerate(new_pt):
            pt_idx = 0
            for idx2, pt2 in enumerate(new_pt):
                if pt1 < pt2 or (pt1 == pt2 and idx1 > idx2): pt_idx += 1
            order.append(pt_idx)

        jet_order = range(len(order))
        for ij in range(len(order)):
            jet_order[order[ij]] = ij 

        # Fill branches
        for typ in self.CollBr:
            for bname in self.CollBr[typ]:
                if '_pt' in bname:
                    temp_v = [new_pt[idx] for idx in jet_order]
                    self.out.fillBranch(bname+self._suffix, temp_v)
                else:
                    temp_b = bname.replace(self.CollTC+'_', '')
                    temp_v = [coll[idx][temp_b] for idx in jet_order]
                    self.out.fillBranch(bname+self._suffix, temp_v)

        return True 

