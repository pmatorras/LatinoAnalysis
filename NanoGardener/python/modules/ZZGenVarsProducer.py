import ROOT
import os
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from LatinoAnalysis.NanoGardener.framework.samples.susyCrossSections import SUSYCrossSections
ELECTRON_MASS = 0.000511 #[GeV]
MUON_MASS     = 0.106    #[GeV]
TAU_MASS      = 1.777    #[GeV]
Z_MASS        = 91.188   #[GeV]

class ZZGenVarsProducer(Module):

    ###
    def __init__(self):
        self.cmssw_base = os.getenv('CMSSW_BASE')
        pass

    ###
    def beginJob(self):
        pass

    ###
    def endJob(self):
        pass

    ###
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):

        self.out = wrappedOutputTree
        
        self.out.branch("ZZ_mass",  "F")
        self.out.branch("ZZ_dphi",  "F")
        self.out.branch("ZZ_pt"  ,  "F")

        if 'gg' in inputFile.GetName() or 'GluGlu' in inputFile.GetName():
            self.ZZproduction = 'gg'
            self.ReadGluGluHZZkfactors()
            for sys in range(len(self.strSystTitle)):
                self.out.branch("kZZ_gg_"+self.strSystTitle[sys],  "F")
                
        else:
            self.ZZproduction = 'qq'
            self.out.branch("kZZ_mass",  "F")
            self.out.branch("kZZ_dphi",  "F")
            self.out.branch("kZZ_pt"  ,  "F")

    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        del self.ggZZ_kf
        pass


    def kfactor_qqZZ_qcd_dPhi(self,GendPhiZZ, finalState):

        # finalState=1 : 4e/4mu/4tau
        # finalState=2 : 2e2mu/2mutau/2e2tau
        k       = 0  
        absdphi = abs(GendPhiZZ)
        if (finalState==1):
            if (absdphi > 0.0 and absdphi <= 0.1): k+=1.515838921760
            if (absdphi > 0.1 and absdphi <= 0.2): k+=1.496256665410 
            if (absdphi > 0.2 and absdphi <= 0.3): k+=1.495522061910
            if (absdphi > 0.3 and absdphi <= 0.4): k+=1.483273154250
            if (absdphi > 0.4 and absdphi <= 0.5): k+=1.465589701130
            if (absdphi > 0.5 and absdphi <= 0.6): k+=1.491500887510
            if (absdphi > 0.6 and absdphi <= 0.7): k+=1.441183580450
            if (absdphi > 0.7 and absdphi <= 0.8): k+=1.440830603990
            if (absdphi > 0.8 and absdphi <= 0.9): k+=1.414339019120
            if (absdphi > 0.9 and absdphi <= 1.0): k+=1.422534218560
            if (absdphi > 1.0 and absdphi <= 1.1): k+=1.401037066000
            if (absdphi > 1.1 and absdphi <= 1.2): k+=1.408539428810
            if (absdphi > 1.2 and absdphi <= 1.3): k+=1.381247744080
            if (absdphi > 1.3 and absdphi <= 1.4): k+=1.370553357430
            if (absdphi > 1.4 and absdphi <= 1.5): k+=1.347323316000
            if (absdphi > 1.5 and absdphi <= 1.6): k+=1.340113437450
            if (absdphi > 1.6 and absdphi <= 1.7): k+=1.312661036510
            if (absdphi > 1.7 and absdphi <= 1.8): k+=1.290055062010
            if (absdphi > 1.8 and absdphi <= 1.9): k+=1.255322614790
            if (absdphi > 1.9 and absdphi <= 2.0): k+=1.254455642450
            if (absdphi > 2.0 and absdphi <= 2.1): k+=1.224047664420
            if (absdphi > 2.1 and absdphi <= 2.2): k+=1.178816782670
            if (absdphi > 2.2 and absdphi <= 2.3): k+=1.162624827140
            if (absdphi > 2.3 and absdphi <= 2.4): k+=1.105401140940
            if (absdphi > 2.4 and absdphi <= 2.5): k+=1.074749265690
            if (absdphi > 2.5 and absdphi <= 2.6): k+=1.021864599380
            if (absdphi > 2.6 and absdphi <= 2.7): k+=0.946334793286
            if (absdphi > 2.7 and absdphi <= 2.8): k+=0.857458082628
            if (absdphi > 2.8 and absdphi <= 2.9): k+=0.716607670482
            if (absdphi > 2.9 and absdphi <= 3.1416): k+=1.132841784840
            
        if (finalState==2):
            if (absdphi > 0.0 and absdphi <= 0.1): k+=1.513834489150
            if (absdphi > 0.1 and absdphi <= 0.2): k+=1.541738780180
            if (absdphi > 0.2 and absdphi <= 0.3): k+=1.497829632510
            if (absdphi > 0.3 and absdphi <= 0.4): k+=1.534956782920
            if (absdphi > 0.4 and absdphi <= 0.5): k+=1.478217033060
            if (absdphi > 0.5 and absdphi <= 0.6): k+=1.504330859290
            if (absdphi > 0.6 and absdphi <= 0.7): k+=1.520626246850
            if (absdphi > 0.7 and absdphi <= 0.8): k+=1.507013090030
            if (absdphi > 0.8 and absdphi <= 0.9): k+=1.494243156250
            if (absdphi > 0.9 and absdphi <= 1.0): k+=1.450536096150
            if (absdphi > 1.0 and absdphi <= 1.1): k+=1.460812521660
            if (absdphi > 1.1 and absdphi <= 1.2): k+=1.471603622200
            if (absdphi > 1.2 and absdphi <= 1.3): k+=1.467700038200
            if (absdphi > 1.3 and absdphi <= 1.4): k+=1.422408690640
            if (absdphi > 1.4 and absdphi <= 1.5): k+=1.397184022730
            if (absdphi > 1.5 and absdphi <= 1.6): k+=1.375593447520
            if (absdphi > 1.6 and absdphi <= 1.7): k+=1.391901318370
            if (absdphi > 1.7 and absdphi <= 1.8): k+=1.368564350560
            if (absdphi > 1.8 and absdphi <= 1.9): k+=1.317884804290
            if (absdphi > 1.9 and absdphi <= 2.0): k+=1.314019950800
            if (absdphi > 2.0 and absdphi <= 2.1): k+=1.274641749910
            if (absdphi > 2.1 and absdphi <= 2.2): k+=1.242346606820
            if (absdphi > 2.2 and absdphi <= 2.3): k+=1.244727403840
            if (absdphi > 2.3 and absdphi <= 2.4): k+=1.146259351670
            if (absdphi > 2.4 and absdphi <= 2.5): k+=1.107804993520
            if (absdphi > 2.5 and absdphi <= 2.6): k+=1.042053646740
            if (absdphi > 2.6 and absdphi <= 2.7): k+=0.973608545141
            if (absdphi > 2.7 and absdphi <= 2.8): k+=0.872169942668
            if (absdphi > 2.8 and absdphi <= 2.9): k+=0.734505279177
            if (absdphi > 2.9 and absdphi <= 3.1416): k+=1.163152837230       
        
        if (k==0.0): return 1.1 #if something goes wrong return inclusive k-factor
        else: return k

    #---------------------------------------------
    def kfactor_qqZZ_qcd_M(self, GENmassZZ, finalState):

        # finalState=1 : 4e/4mu/4tau
        # finalState=2 : 2e2mu/2mutau/2e2tau

        k         = 0.0
        absZZmass = abs(GENmassZZ)
        if (finalState==1):
            if absZZmass >   0.0 and absZZmass <=  25.0: k+=1.23613311013
            if absZZmass >  25.0 and absZZmass <=  50.0: k+=1.17550314639
            if absZZmass >  50.0 and absZZmass <=  75.0: k+=1.17044565911
            if absZZmass >  75.0 and absZZmass <= 100.0: k+=1.03141209689
            if absZZmass > 100.0 and absZZmass <= 125.0: k+=1.05285574912
            if absZZmass > 125.0 and absZZmass <= 150.0: k+=1.11287217794
            if absZZmass > 150.0 and absZZmass <= 175.0: k+=1.13361441158
            if absZZmass > 175.0 and absZZmass <= 200.0: k+=1.10355603327
            if absZZmass > 200.0 and absZZmass <= 225.0: k+=1.10053981637
            if absZZmass > 225.0 and absZZmass <= 250.0: k+=1.10972676811
            if absZZmass > 250.0 and absZZmass <= 275.0: k+=1.12069120525
            if absZZmass > 275.0 and absZZmass <= 300.0: k+=1.11589101635
            if absZZmass > 300.0 and absZZmass <= 325.0: k+=1.13906170314
            if absZZmass > 325.0 and absZZmass <= 350.0: k+=1.14854594271
            if absZZmass > 350.0 and absZZmass <= 375.0: k+=1.14616229031
            if absZZmass > 375.0 and absZZmass <= 400.0: k+=1.14573157789
            if absZZmass > 400.0 and absZZmass <= 425.0: k+=1.13829430515
            if absZZmass > 425.0 and absZZmass <= 450.0: k+=1.15521193686
            if absZZmass > 450.0 and absZZmass <= 475.0: k+=1.13679822698
            if absZZmass > 475.0: k+=1.13223956942

        if (finalState==2) :
            if absZZmass >   0.0 and absZZmass <=  25.0: k+=1.25094466582
            if absZZmass >  25.0 and absZZmass <=  50.0: k+=1.22459455362
            if absZZmass >  50.0 and absZZmass <=  75.0: k+=1.19287368979
            if absZZmass >  75.0 and absZZmass <= 100.0: k+=1.04597506451
            if absZZmass > 100.0 and absZZmass <= 125.0: k+=1.08323413771
            if absZZmass > 125.0 and absZZmass <= 150.0: k+=1.09994968030
            if absZZmass > 150.0 and absZZmass <= 175.0: k+=1.16698455800
            if absZZmass > 175.0 and absZZmass <= 200.0: k+=1.10399053155
            if absZZmass > 200.0 and absZZmass <= 225.0: k+=1.10592664340
            if absZZmass > 225.0 and absZZmass <= 250.0: k+=1.10690381480
            if absZZmass > 250.0 and absZZmass <= 275.0: k+=1.11194928918
            if absZZmass > 275.0 and absZZmass <= 300.0: k+=1.13522586553
            if absZZmass > 300.0 and absZZmass <= 325.0: k+=1.11895090244
            if absZZmass > 325.0 and absZZmass <= 350.0: k+=1.13898508615
            if absZZmass > 350.0 and absZZmass <= 375.0: k+=1.15463977506
            if absZZmass > 375.0 and absZZmass <= 400.0: k+=1.17341664594
            if absZZmass > 400.0 and absZZmass <= 425.0: k+=1.20093349763
            if absZZmass > 425.0 and absZZmass <= 450.0: k+=1.18915554919
            if absZZmass > 450.0 and absZZmass <= 475.0: k+=1.18546007375
            if absZZmass > 475.0 : k+=1.12864505708

        if (k==0.0): return 1.1
        else: return k #if something goes wrong return inclusive k-factor

    #------------------------------------------------------------------------------
    #  kfactor_qqZZ_qcd_Pt  (GENpTZZ,   finalState);
    #------------------------------------------------------------------------------
    def kfactor_qqZZ_qcd_Pt(self, GENpTZZ, finalState):

        #finalState=1 : 4e/4mu/4tau
        # finalState=2 : 2e2mu/2mutau/2e2tau
        
        k       = 0.0
        absZZpt = abs(GENpTZZ)
        if (finalState==1):
            if absZZpt >   0.0 and absZZpt <=  5.0:  k+=0.64155491983
            if absZZpt >   5.0 and absZZpt <=  10.0: k+=1.09985240531
            if absZZpt >  10.0 and absZZpt <=  15.0: k+=1.29390628654
            if absZZpt >  15.0 and absZZpt <=  20.0: k+=1.37859998571
            if absZZpt >  20.0 and absZZpt <=  25.0: k+=1.42430263312
            if absZZpt >  25.0 and absZZpt <=  30.0: k+=1.45038493266
            if absZZpt >  30.0 and absZZpt <=  35.0: k+=1.47015377651
            if absZZpt >  35.0 and absZZpt <=  40.0: k+=1.48828685748
            if absZZpt >  40.0 and absZZpt <=  45.0: k+=1.50573440448
            if absZZpt >  45.0 and absZZpt <=  50.0: k+=1.50211655928
            if absZZpt >  50.0 and absZZpt <=  55.0: k+=1.50918720827
            if absZZpt >  55.0 and absZZpt <=  60.0: k+=1.52463089491
            if absZZpt >  60.0 and absZZpt <=  65.0: k+=1.52400838378
            if absZZpt >  65.0 and absZZpt <=  70.0: k+=1.52418067701
            if absZZpt >  70.0 and absZZpt <=  75.0: k+=1.55424382578
            if absZZpt >  75.0 and absZZpt <=  80.0: k+=1.52544284222
            if absZZpt >  80.0 and absZZpt <=  85.0: k+=1.57896384602
            if absZZpt >  85.0 and absZZpt <=  90.0: k+=1.53034682567
            if absZZpt >  90.0 and absZZpt <=  95.0: k+=1.56147329708
            if absZZpt >  95.0 and absZZpt <= 100.0: k+=1.54468169268
            if absZZpt >  100.0: k+=1.57222952415

        if (finalState==2) :
            if absZZpt >   0.0 and absZZpt <=   5.0: k+=0.743602533303
            if absZZpt >   5.0 and absZZpt <=  10.0: k+=1.14789453219
            if absZZpt >  10.0 and absZZpt <=  15.0: k+=1.33815867892
            if absZZpt >  15.0 and absZZpt <=  20.0: k+=1.41420044104
            if absZZpt >  20.0 and absZZpt <=  25.0: k+=1.45511318916
            if absZZpt >  25.0 and absZZpt <=  30.0: k+=1.47569225244
            if absZZpt >  30.0 and absZZpt <=  35.0: k+=1.49053003693
            if absZZpt >  35.0 and absZZpt <=  40.0: k+=1.50622827695
            if absZZpt >  40.0 and absZZpt <=  45.0: k+=1.50328889799
            if absZZpt >  45.0 and absZZpt <=  50.0: k+=1.52186945281
            if absZZpt >  50.0 and absZZpt <=  55.0: k+=1.52043468754
            if absZZpt >  55.0 and absZZpt <=  60.0: k+=1.53977869986
            if absZZpt >  60.0 and absZZpt <=  65.0: k+=1.53491994434
            if absZZpt >  65.0 and absZZpt <=  70.0: k+=1.51772882172
            if absZZpt >  70.0 and absZZpt <=  75.0: k+=1.54494489131
            if absZZpt >  75.0 and absZZpt <=  80.0: k+=1.57762411697
            if absZZpt >  80.0 and absZZpt <=  85.0: k+=1.55078339014
            if absZZpt >  85.0 and absZZpt <=  90.0: k+=1.57078191891
            if absZZpt >  90.0 and absZZpt <=  95.0: k+=1.56162666568
            if absZZpt >  95.0 and absZZpt <= 100.0: k+=1.54183774627
            if absZZpt > 100.0: k+=1.58485762205

        if (k==0.0): return 1.1
        else: return k #if something goes wrong return inclusive k-factor
    
    #------------------------------------------------------------------------------
    #  ReadGluGluHZZkfactors()
    #------------------------------------------------------------------------------
    def ReadGluGluHZZkfactors(self):

        self.strSystTitle = [ 'Nominal', 'PDFScaleDn', 'PDFScaleUp', 'QCDScaleDn', 'QCDScaleUp', 'AsDn', 'AsUp', 'PDFReplicaDn', 'PDFReplicaUp' ] 
        kfRoot = ROOT.TFile.Open(self.cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/kfactors/Kfactor_Collected_ggHZZ_2l2l_NNLO_NNPDF_NarrowWidth_13TeV.root')

        self.ggZZ_kf = [ ] 

        for sys in range(len(self.strSystTitle)):
            self.ggZZ_kf.append(kfRoot.Get('sp_kfactor_'+self.strSystTitle[sys]))

        kfRoot.Close()

    #------------------------------------------------------------------------------
    #  kfactor_ggHZZ_qcd(float GENmassZZ, TString SystTitle)
    #------------------------------------------------------------------------------
    def kfactor_ggHZZ_qcd(self, GENmassZZ, sys):
        if GENmassZZ>0.:
            return self.ggZZ_kf[sys].Eval(GENmassZZ)
        else:
            return self.ggZZ_kf[sys].GetMinimum(100., 2000.)
                    
    #---------------------------------------------

    def analyze(self, event):

        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")
        # Gen                                                                                    
        
        _ZZpt     =  0.
        _ZZdphi   =  0.
        _ZZmass   =  0.
        nZZleps   =  0
        ZZlep     =  []
        ZZlepID   =  []
        neupdgID  =  [ 12, 14, 16]
        lep_ch    =  []
        motherIdx =  []
        for idx, genpart in enumerate(genParticles):
            if genpart.genPartIdxMother < 0 : continue
            abspdgID  = abs(genpart.pdgId)
            abspdgMum = abs(genParticles[genpart.genPartIdxMother].pdgId)
            lepmass = -1
            isEle   = False
            isMu    = False
            isTau   = False
            isNeu   = False
            _lep_ch = genpart.pdgId/abspdgID
            if abspdgID is 11: 
                isEle   = True
                lepmass = ELECTRON_MASS
            elif abspdgID is 13:
                isMu    = True
                lepmass = MUON_MASS
            elif abspdgID is 15:
                isTau   = True
                lepmass = TAU_MASS
            elif abspdgID in neupdgID: 
                isNeu   = True
                lepmass = 0.
                _lep_ch = 0

            if (( isEle or isMu or isTau or isNeu ) and (abspdgMum == 23) and 
                (( genpart.statusFlags >> 0 & 1 )  or  ( genpart.statusFlags >> 2 & 1 )   or  
                 (genpart.statusFlags >> 3 & 1 )   or  ( genpart.statusFlags >> 4 & 1 ) ) ) :
                nZZleps += 1
                _ZZlep   = ROOT.TLorentzVector()
                _ZZlep.SetPtEtaPhiM(genpart.pt, genpart.eta, genpart.phi, lepmass)
                ZZlep.append(_ZZlep)
                ZZlepID.append(genpart.pdgId)
                lep_ch.append(_lep_ch) 
                motherIdx.append(genpart.genPartIdxMother)

        if nZZleps is not 4: print " ZZGenVarsProducer warning:", nZZleps, "leptons found"
        if nZZleps>=4: 

            nele = 0
            nmu  = 0
            ntau = 0
            nnu  = 0
            for lep in ZZlepID:
                if   abs(lep) in neupdgID: nnu  += 1
                elif abs(lep) == 11:       nele += 1
                elif abs(lep) == 13:       nmu  += 1
                elif abs(lep) == 15:       ntau += 1

            finalstate = 2
            if nele == 4 or nmu == 4 or ntau == 4 : finalstate = 1
        
            for l1 in range(0, nZZleps):
                for l2 in range(l1+1, nZZleps):
                    if (ZZlepID[l1]+ZZlepID[l2] is not 0) or (motherIdx[l1]!=motherIdx[l2]): continue
                    Z1 = ZZlep[l1]+ZZlep[l2]
                    for l3 in range(0, nZZleps):
                        if l3 in [l1,l2] : continue
                        for l4 in range(l3+1, nZZleps):
                            if (l4 in [l1,l2]) or (ZZlepID[l3]+ZZlepID[l4] is not 0) or (motherIdx[l3]!=motherIdx[l4]): continue
                            Z2 = ZZlep[l3]+ZZlep[l4]
                            ZZCand  = Z1 + Z2
                            _ZZmass = ZZCand.M()
                            _ZZpt   = ZZCand.Pt()
                            _ZZdphi = Z2.DeltaPhi(Z1)

        self.out.fillBranch("ZZ_dphi", _ZZdphi )
        self.out.fillBranch("ZZ_mass", _ZZmass )
        self.out.fillBranch("ZZ_pt"  , _ZZpt )

        if self.ZZproduction=='gg':
            
            for sys in range(len(self.strSystTitle)):
                k_gg = self.kfactor_ggHZZ_qcd(_ZZmass, sys)
                self.out.fillBranch('kZZ_gg_'+self.strSystTitle[sys], k_gg )

        elif self.ZZproduction=='qq':

            k_dphi = self.kfactor_qqZZ_qcd_dPhi(_ZZdphi,finalstate)
            k_mass = self.kfactor_qqZZ_qcd_M   (_ZZmass,finalstate)
            k_pt   = self.kfactor_qqZZ_qcd_Pt  (_ZZpt  ,finalstate)

            self.out.fillBranch("kZZ_dphi", k_dphi )
            self.out.fillBranch("kZZ_mass", k_mass )
            self.out.fillBranch("kZZ_pt"  , k_pt )

        return True
