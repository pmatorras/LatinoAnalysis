#!/usr/bin/env python
import os
import subprocess
import math
from optparse import OptionParser
import optparse
if 'pmatorra' in os.environ.get('USER'):
    cmssw_directory= '/afs/cern.ch/work/p/pmatorra/private/CMSSW_10_6_19/'
else:
    cmssw_directory = '/afs/cern.ch/work/s/scodella/SUSY/CMSSW_10_2_14/'
gardening_directory = 'src/LatinoAnalysis/NanoGardener/python/framework/samples/'
production_directory = 'src/LatinoAnalysis/NanoProducer/python/samples/'

campaigns = { 'UL16'  : { 'Data' : { 'AOD'    : '21Feb2020_UL2016-',     'MINIAOD'    : '21Feb2020_UL2016-',        'NANOAOD'    : 'UL2016_MiniAODv1_NanoAODv2' },
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL16RECO', 'MINIAODSIM' : 'RunIISummer19UL16MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL16NanoAODv2' },    
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                           }, },
              'UL17'  : { 'Data' : { 'AOD'    : '09Aug2019_UL2017-',     'MINIAOD'    : '09Aug2019_UL2017-',        'NANOAOD'    : 'UL2017_MiniAODv1_NanoAODv2' },             
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL17RECO', 'MINIAODSIM' : 'RunIISummer19UL17MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL17NanoAODv2' },
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                           }, }, 
              'UL18'  : { 'Data' : { 'AOD'    : '12Nov2019_UL2018-',     'MINIAOD'    : '12Nov2019_UL2018-',        'NANOAOD'    : 'UL2018_MiniAODv1_NanoAODv2' },             
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL18RECO', 'MINIAODSIM' : 'RunIISummer19UL18MiniAOD', 'NANOAODSIM' : 'RunIISummer20UL18NanoAODv2' },
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                           }, }, 
            }

# Main
if __name__ == '__main__':

    # Input parameters
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('-d', '--directory' , dest='directory' , help='CMSSW directory', default=cmssw_directory)
    parser.add_option('-s', '--samplefile', dest='samplefile', help='Sample file'    , default='Run2016_102X_nAODv6')
    parser.add_option('-c', '--campaign'  , dest='campaign',   help='Campaign'       , default='UL16')
    parser.add_option('-t', '--tier'      , dest='tier',       help='Tier'           , default='nanoAOD')
    parser.add_option('-o', '--outputfile', dest='outputfile', help='Output file'    , default='test')
    parser.add_option('-v', '--verbose'   , dest='verbose'   , help='Verbose'        , default=False, action='store_true')
    (opt, args) = parser.parse_args()

    if opt.samplefile==opt.outputfile:
        print 'Error: overwriting input file', opt.samplefile
        exit()
    else:
        opt.outputfile = opt.outputfile.replace('.py', '')
    run2Samples=False
    isData=False

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
        else:      
            Sim  = 'SIM'
            if 'FS_' in opt.samplefile:
                campaign = campaigns[campaign_year]['FS']
            else:
                campaign = campaigns[campaign_year]['MC'] 
        
        tiers = [ ]
        for tier in [ 'NANOAOD', 'MINIAOD', 'AOD' ]:
            if opt.tier!='miniAOD' or tier!='NANOAODSIM': 
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

            if opt.verbose: print period

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

            if len(datasetsFound)==1:
                datasetFound = datasetsFound[0]
                #print datasetFound
                if 1==1:#opt.verbose:
                    1<2
                    print 'Dataset found for sample', process+period, 'in campaign', campaign[thistier], '-->', datasetFound

            elif len(datasetsFound)>1:
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
                print 'Warning: no dataset found for sample', process+'_'+period, 'in campaign', campaign[thistier]
                if len(parentsFound)>0:
                    print '         available parents are', parentsFound

            sampleName = process if Sim=='' else sample.replace('_newpmx','').split('_ext')[0]
            sampleName += datasetFlag

            OutputSamples[sampleName] = { }
            OutputSamples[sampleName][opt.tier] = datasetFound


