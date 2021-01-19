#!/usr/bin/env python
import os
import subprocess
import math
from optparse import OptionParser
import optparse
 
cmssw_directory = '/afs/cern.ch/work/s/scodella/SUSY/CMSSW_10_2_14/'
gardening_directory = 'src/LatinoAnalysis/NanoGardener/python/framework/samples/'
production_directory = 'src/LatinoAnalysis/NanoProducer/python/samples/'

campaigns = { 'UL16'  : { 'Data' : { 'AOD'    : '21Feb2020_UL2016-',     'MINIAOD'    : '21Feb2020_UL2016-',        'NANOAOD'    : 'UL2016_MiniAODv1_NanoAODv2' },
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL16RECO', 'MINIAODSIM' : 'RunIISummer19UL16MiniAOD', 'NANOAODSIM' : 'RunIISummer19UL16NanoAODv2' },    
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                           }, },
              'UL17'  : { 'Data' : { 'AOD'    : '09Aug2019_UL2017-',     'MINIAOD'    : '09Aug2019_UL2017-',        'NANOAOD'    : 'UL2017_MiniAODv1_NanoAODv2' },             
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL17RECO', 'MINIAODSIM' : 'RunIISummer19UL17MiniAOD', 'NANOAODSIM' : 'RunIISummer19UL17NanoAODv2' },
                          'FS'   : { 'AODSIM' : '',                      'MINIAODSIM' : '',                         'NANOAODSIM' : ''                           }, }, 
              'UL18'  : { 'Data' : { 'AOD'    : '12Nov2019_UL2018-',     'MINIAOD'    : '12Nov2019_UL2018-',        'NANOAOD'    : 'UL2018_MiniAODv1_NanoAODv2' },             
                          'MC'   : { 'AODSIM' : 'RunIISummer19UL18RECO', 'MINIAODSIM' : 'RunIISummer19UL18MiniAOD', 'NANOAODSIM' : 'RunIISummer19UL18NanoAODv2' },
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

    if opt.campaign not in campaigns:
        print 'Error: missing information for campaign', opt.campaign
        exit()
 
    if 'Run' in opt.samplefile:
        Sim = '' 
        campaign = campaigns[opt.campaign]['Data']   
    else:      
        Sim  = 'SIM'
        if 'FS_' in opt.samplefile:
            campaign = campaigns[opt.campaign]['FS']
        else:
            campaign = campaigns[opt.campaign]['MC'] 

    tiers = [ ]
    for tier in [ 'NANOAOD', 'MINIAOD', 'AOD' ]:
        if opt.tier!='miniAOD' or tier!='NANOAODSIM': 
            tiers.append(tier+Sim)

    sample_directory = production_directory if opt.tier=='miniAOD' else gardening_directory 

    exec(open(opt.directory+sample_directory+opt.samplefile.replace('.py', '')+'.py').read())

    OutputSamples = { }

    for sample in Samples:

        process = Samples[sample][opt.tier].split('/')[1]
        period = '' if Sim=='SIM' else Samples[sample][opt.tier].split('/')[2].split('-')[0].split('_')[0]

        if opt.verbose: print period

        datasetsFound = [ ] 
        parentsFound = [ ]

        for tier in tiers:
            
            if campaign[tier]=='':
                print 'Error: missing information for campaign', opt.campaign, 'tier', tier
                exit()

            query = '\"instance=prod/global dataset=/'+process+'/'+period+'*'+campaign[tier]+'*/'+tier+'\"'
            query_output = subprocess.check_output('dasgoclient -query='+query, shell=True)

            for line in query_output.split('\n'):
                if opt.tier.upper() in line:
                    datasetsFound.append(line)
                elif '/' in line:
                    parentsFound.append(line)

        datasetFound = ''
        datasetFlag = '_'+Samples[sample][opt.tier].split('/')[2]

        if len(datasetsFound)==1:
            datasetFound = datasetsFound[0]
            if opt.verbose: 
                print 'Dataset found for sample', process+period, 'in campaign', opt.campaign, '-->', datasetFound

        elif len(datasetsFound)>1:
            print 'Warning: multiple datasets found for sample', process+period, 'in campaign', opt.campaign, '-->', datasetsFound
            # Insert code to select the right one
            #for datasetCandidate in datasetsFound:
            #    query = '\"instance=prod/global summary dataset='+datasetCandidate+'\"'
            #    query_output = subprocess.check_output('dasgoclient -query='+query, shell=True)

        else:   
            print 'Warning: no dataset found for sample', process+'_'+period, 'in campaign', opt.campaign
            if len(parentsFound)>0:
                print '         available parents are', parentsFound

        sampleName = process if Sim=='' else sample.replace('_newpmx','').split('_ext')[0]
        sampleName += datasetFlag

        OutputSamples[sampleName] = { }
        OutputSamples[sampleName][opt.tier] = datasetFound


