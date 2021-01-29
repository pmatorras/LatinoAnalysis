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

if 'pmatorra' in os.environ.get('USER'):
    cmssw_directory= '/afs/cern.ch/work/p/pmatorra/private/CMSSW_10_6_19/'
    errorcolor = '96m'
    warningcolor = '92m'
else:
    cmssw_directory = '/afs/cern.ch/work/s/scodella/SUSY/CMSSW_10_6_19_patch2/'
    errorcolor = '96m'
    warningcolor = '92m'

gardening_directory = 'src/LatinoAnalysis/NanoGardener/python/framework/samples/'
production_directory = 'src/LatinoAnalysis/NanoProducer/python/samples/'

campaigns = { 'UL16'  : { 'Data' : { 'AOD'    : '21Feb2020_UL2016-',     'MINIAOD'    : '21Feb2020_UL2016-',        'NANOAOD'    : 'UL2016_MiniAODv1_NanoAODv2'                                     },
                          'MC'   : { 'AODSIM' : 'RunIISummer20UL16RECO', 'MINIAODSIM' : 'RunIISummer20UL16MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL16NanoAODv2', 'GEN' : 'RunIISummer20UL16*GEN' },    
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                          , 'GEN' : ''                         }, },
              'UL17'  : { 'Data' : { 'AOD'    : '09Aug2019_UL2017-',     'MINIAOD'    : '09Aug2019_UL2017-',        'NANOAOD'    : 'UL2017_MiniAODv1_NanoAODv2'                                     },             
                          'MC'   : { 'AODSIM' : 'RunIISummer20UL17RECO', 'MINIAODSIM' : 'RunIISummer20UL17MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL17NanoAODv2', 'GEN' : 'RunIISummer20UL17*GEN' },
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                          , 'GEN' : ''                         }, }, 
              'UL18'  : { 'Data' : { 'AOD'    : '12Nov2019_UL2018-',     'MINIAOD'    : '12Nov2019_UL2018-',        'NANOAOD'    : 'UL2018_MiniAODv1_NanoAODv2'                                     },             
                          'MC'   : { 'AODSIM' : 'RunIISummer20UL18RECO', 'MINIAODSIM' : 'RunIISummer20UL18MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL18NanoAODv2', 'GEN' : 'RunIISummer20UL18*GEN' },
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                          , 'GEN' : ''                         }, }, 
            }

# Main
def readSampleFile(filename):
    samhere=[]
    with open("Summer20ULPlanning.csv") as f:
        for row in f:
            samhere.append(row.split(",")[0])
    return samhere
def substringinlist(sample_list,substring):
    inlist=[]
    for item in sample_list:
        if (substring in item) : 
            inlist.append(item)
            #print "satisfies", substring, item
    return inlist

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
    elif opt.campaign not in campaigns:
        print 'Error: missing information for campaign', opt.campaign
        exit()
    else:
        if   '16' in opt.samplefile: campaign_years=['UL16']
        elif '17' in opt.samplefile: campaign_years=['UL17']
        elif '18' in opt.samplefile: campaign_years=['UL18']
        else:  campaign_years=[opt.campaign]
    
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

        OutputSamples = { }
        print opt.tier, campaign_year
        thistier=opt.tier.upper()+Sim
        print "CAMPAIGN:", campaign[thistier].upper(), thistier
        for sample in Samples:

            process = Samples[sample][opt.tier].split('/')[1]
            period = '' if Sim=='SIM' else Samples[sample][opt.tier].split('/')[2].split('-')[0].split('_')[0]

            if not isData:
                process = process.replace('_PSweights', '')
                if 'Tune' not in process: process = process.replace('13TeV', 'TuneCP5_13TeV')
                process = process.replace('TuneCUETP8M1', 'TuneCP5')
                process.replace('TuneCUETP8M2', 'TuneCP5')         
                process = process.replace('_ttHtranche3', '')
 
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
                if verbose:
                    print 'Dataset found for sample', process+period, 'in campaign', campaign[thistier], '-->', datasetFound

            elif len(datasetsFound)>1:
                if verbose: 
                    print 'Warning: multiple datasets found for sample', process+period, 'in campaign', campaign[thistier], '-->', datasetsFound
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
                print 'Dataset picked for sample', process+period, 'in campaign', campaign[thistier], '-->', saveset
                # Insert code to select the right one
                #for datasetCandidate in datasetsFound:
                #    query = '\"instance=prod/global summary dataset='+datasetCandidate+'\"'
                #    query_output = subprocess.check_output('dasgoclient -query='+query, shell=True)
                #exit()
            else:   
                if verbose: 
                    print 'Warning: no dataset found for sample', process+period, 'in tier', opt.tier, 'for campaign', campaign[thistier] 
                if len(parentsFound)>0:
                    if verbose:
                        print '         available parents are', parentsFound

                elif not isData:
                    
                    mcm_status = 0

                    mcm_query = 'dataset_name='+process+'&prepid=*'+campaign['GEN']+'*'
                    requests = mcm.get('requests', None, mcm_query)

                    if len(requests)>0:
                        for request in requests:
                            if verbose:
                                print 'Request', request['prepid'], 'in status', request['status']
                            if request['status']=='new': mcm_status = 1
                            elif request['status']=='validation': mcm_status = 2
                            elif request['status']=='defined': mcm_status = 3
		            elif request['status']=='approved': mcm_status = 4
                            elif request['status']=='submitted': mcm_status = 5                         
   
                    if mcm_status<1:

                        if verbose:
                            print 'Warning: no request found for sample', process, 'in McM campaign', campaign['GEN'], 'check PC planning'

                        incsv=substringinlist(csvsamples,process)
                        if   (len(incsv)==0) :
                            incsvsample = substringinlist(csvsamples,sample)
                            if len(incsvsample)==0: 
                                print '\033['+errorcolor + 'Warning: sample', process, 'not in the planned production campaign' + '\033[0m'
                            else:
                                print '\033['+warningcolor + 'Warning: sample', process, 'not in the planned production campaign' + '\033[0m'
                                print '         but alternative samples are there:', incsvsample
                        elif (len(incsv)>5)  : 
                            if verbose: print "MULTIPLE OPTIONS AVAILABLE FOR THE CSV FILE"
                        elif verbose:  print "SAMPLES IN CSV:",sample, incsv[:5]
 
            sampleName = process if Sim=='' else sample.replace('_newpmx','').split('_ext')[0]
            sampleName += datasetFlag # -> to be refined

            OutputSamples[sampleName] = { }
            OutputSamples[sampleName][opt.tier] = datasetFound


