#!/usr/bin/env python
import os
import subprocess
import math
from optparse import OptionParser
import optparse
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM

mcm = McM(dev=True)
testcolor='95m'
if 'pmatorra' in os.environ.get('USER'):
    cmssw_directory= '/afs/cern.ch/work/p/pmatorra/private/CMSSW_10_6_19/'
    errorcolor = '93m'
    warningcolor = '96m'
    okcolor = '92m'
else:
    cmssw_directory = '/afs/cern.ch/work/s/scodella/SUSY/CMSSW_10_6_19_patch2/'
    errorcolor = '93m'
    warningcolor = '96m'
    okcolor = '92m'

gardening_directory = 'src/LatinoAnalysis/NanoGardener/python/framework/samples/'
production_directory = 'src/LatinoAnalysis/NanoProducer/python/samples/'

campaigns = { 'UL16APV' : { 'MC'   : { 'AODSIM' : 'RunIISummer20UL16RECOAPV', 'MINIAODSIM' : 'RunIISummer20UL16MiniAODAPV', 'NANOAODSIM' : 'RunIISummer20UL16NanoAODAPVv2', 'GEN' : 'RunIISummer*UL16*GENAPV-' },
                            'FS'   : { 'AODSIM' : '',                         'MINIAODSIM' : '',                            'NANOAODSIM' : ''                             , 'GEN' : ''                         }, },
              'UL16'  : { 'Data' : { 'AOD'    : '21Feb2020_UL2016-',      'MINIAOD'    : '21Feb2020_UL2016-',         'NANOAOD'    : 'UL2016_MiniAODv1_NanoAODv2'                                  },
                          'MC'   : { 'AODSIM' : 'RunIISummer20UL16RECO-', 'MINIAODSIM' : 'RunIISummer20UL16MiniAOD-', 'NANOAODSIM' : 'RunIISummer20UL16NanoAODv2', 'GEN' : 'RunIISummer*UL16*GEN-' },    
                          'FS'   : { 'AODSIM' : '',                       'MINIAODSIM' : '',                          'NANOAODSIM' : ''                          , 'GEN' : ''                      }, },
              'UL17'  : { 'Data' : { 'AOD'    : '09Aug2019_UL2017-',      'MINIAOD'    : '09Aug2019_UL2017-',         'NANOAOD'    : 'UL2017_MiniAODv1_NanoAODv2'                                  },             
                          'MC'   : { 'AODSIM' : 'RunIISummer*UL17RECO',   'MINIAODSIM' : 'RunIISummer*UL17MiniAOD',   'NANOAODSIM' : 'RunIISummer*UL17NanoAODv2',  'GEN' : 'RunIISummer*UL17*GEN'  },
                          'FS'   : { 'AODSIM' : '',                       'MINIAODSIM' : '',                          'NANOAODSIM' : ''                          , 'GEN' : ''                      }, }, 
              'UL18'  : { 'Data' : { 'AOD'    : '12Nov2019_UL2018-',      'MINIAOD'    : '12Nov2019_UL2018-',         'NANOAOD'    : 'UL2018_MiniAODv1_NanoAODv2'                                  },             
                          'MC'   : { 'AODSIM' : 'RunIISummer20UL18RECO',  'MINIAODSIM' : 'RunIISummer20UL18MiniAOD',  'NANOAODSIM' : 'RunIISummer20UL18NanoAODv2', 'GEN' : 'RunIISummer*UL18*GEN'  },
                          'FS'   : { 'AODSIM' : '',                       'MINIAODSIM' : '',                          'NANOAODSIM' : ''                          , 'GEN' : ''                      }, }, 
            }

# Main
def readSampleFile(filename):
    samhere=[]
    with open("Summer20ULPlanning.csv") as f:
        for row in f:
            samhere.append(row.split(",")[0])
    return samhere

def substringinlist(sample_list,substring):
    inlist=set() #defined so that duplicates are removed
    #loop to find samples with the substring
    for item in sample_list:
        if (substring in item) : 
            inlist.add(item)
            #print "satisfies", substring, item
    return list(inlist)

if __name__ == '__main__':

    csvsamples = readSampleFile("Summer20ULPlanning.csv")
    # Input parameters
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('-d', '--directory' , dest='directory' , help='CMSSW directory', default=cmssw_directory)
    parser.add_option('-s', '--samplefile', dest='samplefile', help='Sample file'    , default='Run2016_102X_nAODv6')
    parser.add_option('-c', '--campaign'  , dest='campaign',   help='Campaign'       , default='UL16')
    parser.add_option('-t', '--tier'      , dest='tier',       help='Tier'           , default='nanoAOD')
    parser.add_option('-o', '--outputfile', dest='outputfile', help='Output file'    , default='test')
    parser.add_option('-m', '--mute'      , dest='mute'      , help='mute'           , default=False, action='store_true')
    parser.add_option('-l', '--list'      , dest='list'      , help='List in csv'    , default=False, action='store_true')
    (opt, args) = parser.parse_args()

    csvsamples = readSampleFile("Summer20ULPlanning.csv")

    if opt.samplefile==opt.outputfile:
        print 'Error: overwriting input file', opt.samplefile
        exit()
    else:
        opt.outputfile = opt.outputfile.replace('.py', '')
    run2Samples=False
    isData=False

    verbose = not opt.mute

    if 'run2' in opt.campaign:
        campaign_years=campaigns.keys()
        run2Samples=True
        if 'data' in opt.campaign: isData=True
    elif opt.campaign in campaigns:
        campaign_years=[opt.campaign]
    else:
        print 'Error: missing information for campaign', opt.campaign
        exit()
    
    for campaign_year in campaign_years:
        if run2Samples:
            if   '16' in campaign_year: 
                if isData: opt.samplefile='Run2016_102X_nAODv6'
                else:      opt.samplefile='Summer16_susy_102X_nAODv6'
            elif '17' in campaign_year: 
                if isData: opt.samplefile='Run2017_102X_nAODv6'
                else:      opt.samplefile='fall17_susy_102X_nAODv6'
            elif '18' in campaign_year:
                if isData: opt.samplefile='Run2018_102X_nAODv6'
                else :     opt.samplefile='Autumn18_susy_102X_nAODv6'
            print campaign_year
        if 'Run' in opt.samplefile:
            Sim = '' 
            campaign = campaigns[campaign_year]['Data']
            isData=True
        else:      
            isData=False
            Sim  = 'SIM'
            if 'FS_' in opt.samplefile:
                campaign = campaigns[campaign_year]['FS']
            else:
                campaign = campaigns[campaign_year]['MC'] 
        
        tiers = [ ]
        for tier in [ 'NANOAOD', 'MINIAOD', 'AOD' ]:
            if opt.tier!='miniAOD' or tier!='NANOAOD': 
                tiers.append(tier+Sim)

        sample_directory = production_directory if opt.tier=='miniAOD' else gardening_directory 

        exec(open(opt.directory+sample_directory+opt.samplefile.replace('.py', '')+'.py').read())

        if opt.outputfile=='test' and ('UL' in opt.campaign or 'run2' in opt.campaign):
            opt.outputfile = opt.samplefile.replace('102X_nAODv6', '106X_nAODv8').replace('.py', '')
            if 'APV' in opt.campaign:
                opt.outputfile = opt.outputfile.replace('16', '16APV')
            print opt.samplefile
        OutputSamples = { }
        print opt.outputfile
        if opt.list:
            outList = open(opt.outputfile+'.csv' , 'w')

        print opt.tier, campaign_year
        thistier=opt.tier.upper()+Sim
        print "CAMPAIGN:", campaign[thistier].upper(), thistier
        for sample in Samples:
            #print sample
            #if ("WWTo2L" not in sample): continue
            process = Samples[sample][opt.tier].split('/')[1]
            period = '' if Sim=='SIM' else Samples[sample][opt.tier].split('/')[2].split('-')[0].split('_')[0]

            status = 'Missing'

            if not isData:
                process = process.replace('_PSweights', '')
                if 'Tune' not in process: process = process.replace('13TeV', '*13TeV')
                process = process.replace('pythia8_TuneCP5', 'pythia8*')
                process = process.replace('13TeV_powheg_pythia', '13TeV*powheg*pythia')
                process = process.replace('TuneCUETP8M1', 'TuneCP5')
                process = process.replace('TuneCUETP8M2', 'TuneCP5')         
                process = process.replace('_ttHtranche3', '')
                process = process.replace('DYJetsToLL_M-5to50', 'DYJetsToLL_M-4to50')
                process = process.replace('_ext1', '')
 
            if verbose: print '\n', process, period

            datasetsFound = [ ] 
            parentsFound = [ ]

            for tier in tiers:

                if campaign[tier]=='':
                    print 'Error: missing information for campaign', campaign, 'tier', tier
                    exit()

                query = '\"instance=prod/global dataset=/'+process+'/'+period+'*'+campaign[tier]+'*/'+tier+'\"'
                query_output = subprocess.check_output('dasgoclient -query='+query, shell=True)
                #print query
                for line in query_output.split('\n'):
                    if opt.tier.upper() in line:
                        datasetsFound.append(line)
                    elif '/' in line:
                        parentsFound.append(line)

            datasetFound = ''
            datasetFlag = '_'+Samples[sample][opt.tier].split('/')[2]

            if period!='': period = '_'+period 
            if len(datasetsFound)==1:
                datasetFound = datasetsFound[0]
                status = 'NanoAODv2 ready:, ' + datasetFound
                if verbose:
                    print '\033['+okcolor + 'Dataset found for sample', process+period, 'in campaign', campaign[thistier], '-->', datasetFound + '\033[0m'

            elif len(datasetsFound)>1:
                if verbose: 
                    print '\033['+okcolor + 'Warning: multiple datasets found for sample', process+period, 'in campaign', campaign[thistier], '-->', datasetsFound + '\033[0m'
                version = 0
                saveset = ''
                for dataset in datasetsFound:  
                    if len(dataset.split('-v'))>1: 

                        if (version < int(dataset.split('-v')[1].split('/')[0])):
                            #print "new sample", dataset, version
                            saveset=dataset
                        elif (version == int(dataset.split('-v')[1].split('/')[0])):
                            print "WARNING: "+ dataset+" and "+saveset+" have the same version" 
                    else: print "TRY DIFFERENT CODING"
                if verbose: print 'Dataset picked for sample', process+period, 'in campaign', campaign[thistier], '-->', saveset
                
                status = 'NanoAODv2 ready:, ' + saveset
            else:   
                if verbose: 
                    print 'Warning: no dataset found for sample', process+period, 'in tier', opt.tier, 'for campaign', campaign[thistier] 
                if len(parentsFound)>0:
                    for parent in parentsFound:
                        if 'MINIAOD' in parent: 
                            status = 'MiniAOD ready:, ' + parent
                        elif 'MINIAOD' not in status:
                            status = 'AOD ready:, ' + parent
                    if verbose:
                        print '\033['+okcolor + '        available parents are', parentsFound, '' + '\033[0m'

                elif not isData:
                    
                    mcm_status = 0

                    mcm_query = 'dataset_name='+process+'&prepid=*'+campaign['GEN']+'*'
                    #print mcm_query
                    requests = mcm.get('requests', None, mcm_query)
                    #print requests
                    if len(requests)>0:
                        status = 'McM:, '
                        for request in requests:

                            if request['status']=='new': mcm_status = 1
                            elif request['status']=='validation': mcm_status = 2
                            elif request['status']=='defined': mcm_status = 3
		            elif request['status']=='approved': mcm_status = 4
                            elif request['status']=='submitted': mcm_status = 5                         

                            status += request['prepid'] + ' in status ' + request['status'] + ' - '

                            if verbose:   
                                textcolor = okcolor if mcm_status==5 else warningcolor
                                print '\033['+textcolor + 'Request', request['prepid'], 'for sample', process, 'in status', request['status'] + '\033[0m'

                    if mcm_status<1:

                        if verbose:
                            print 'Warning: no request found for sample', process, 'in McM campaign', campaign['GEN'], 'check PC planning'

                        incsv=substringinlist(csvsamples,process)
                        if   (len(incsv)==0) :
                            incsvsample = substringinlist(csvsamples,sample)
                            print "---------->", process, sample, "\n", incsvsample
                            
                            if len(incsvsample)==0: 
                                print '\033['+errorcolor + 'Warning: sample', process, 'not in the planned production campaign' + '\033[0m'
                            else:
                                status = 'Planned alternative: '
                                sample_options = ['-powheg','-pythia8', '_TuneCP5']
                                skim_process = process
                                in_skim_proc = []
                                best_altern  = ''
                                notincommon  = 2*len(sample_options)
                                print "sample and process", sample, process
                                
                                #Cover from cases from TTSemilepton->Semileptonic or incorrectly read *
                                if sample not in process or "*" in process: 
                                    maxopts = 0
                                    if len(incsvsample)==1: bestcandidate=incsvsample[0]
                                    else: bestcandidate=''
                                    for alt_sample in incsvsample:
                                        #print sample, alt_sample, process, bool(sample in alt_sample), bool(process in alt_sample)

                                        if sample  not in alt_sample: continue
                                        nopts = 0
                                        for sample_option in sample_options:
                                            #print sample_option, incsvbool(sample_option in incsvsample)
                                            if sample_option in alt_sample: nopts+=1
                                        if nopts> maxopts:
                                            maxopts       = nopts
                                            bestcandidate = alt_sample
                                    print alt_sample, maxopts, len(sample_options)

                                    print '\033['+warningcolor + 'Warning: sample', process, 'not in the planned production campaign,',
                                    if maxopts==len(sample_options): print '\033['+testcolor +"but the sample ", bestcandidate, "should be equivalent"
                                    else: print "with the sample being the closest", bestcandidate
                                    print "\033[0m"
                                
                                #If many, check which one resembles closer to the input parametre
                                else:
                                    for sample_option in sample_options:
                                        if(sample_option in skim_process): 
                                            skim_process = skim_process.replace(sample_option,'')
                                            in_skim_proc.append(sample_option)
                                    for alt_sample in incsvsample:
                                        status     += alt_sample + ' - '
                                        skim_alt    = alt_sample
                                        in_skim_alt = []
                                        for sample_option in sample_options:
                                            if sample_option in skim_alt:
                                                skim_alt = skim_alt.replace(sample_option,'')
                                                in_skim_alt.append(sample_option)
                                        not_inproc=[x for x in in_skim_proc+in_skim_alt if x not in in_skim_proc]
                                        not_inalt =[x for x in in_skim_proc+in_skim_alt if x not in in_skim_alt] #Both could be combined

                                        if skim_process in skim_alt:
                                            if notincommon> len(not_inproc)+len(not_inalt):
                                                notincommon = len(not_inproc)+len(not_inalt)
                                                best_altern = alt_sample
                                            elif notincommon == len(not_inproc)+len(not_inalt): best_altern+= alt_sample

                                    print '\033['+warningcolor + 'Warning: sample', process, 'not in the planned production campaign,',
                                    if notincommon<2*len(sample_options):
                                        if notincommon==0: print '\033['+testcolor +"but the sample "+ best_altern+ " should be equivalent"
                                        else: print"should be similar with the exception of "+ not_inproc+ "not in the process name, and "+ not_inalt+ " not in the CSV"
                                    else: print 'but alternative samples are there:', incsvsample
                                    print '\033[0m',
                                    #if len(incsvsample)>1:exit()
                        elif (len(incsv)>1)  : 
                            status = 'Planned'
                            if verbose: print '\033['+testcolor+"MULTIPLE OPTIONS AVAILABLE FOR THE CSV FILE", ' \033[0m', incsv, set(incsv), len(set(incsv))
                            exit()
                        elif verbose: 
                            status = 'Planned'
                            print '\033['+warningcolor + 'SAMPLES IN CSV:', process, incsv, ' \033[0m'
                            #exit()
 
            if opt.list:
                outList.write(process + ',' + status + '\n')

            sampleName = process if Sim=='' else sample.replace('_newpmx','').split('_ext')[0]
            sampleName += datasetFlag # -> to be refined

            OutputSamples[sampleName] = { }
            OutputSamples[sampleName][opt.tier] = datasetFound

