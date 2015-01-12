#!/usr/bin/env python
import os
import sys
from xml.dom.minidom import parse, parseString

import pyAMI.client

def getContainerContents(containerName):
  amiclient = pyAMI.client.Client('atlas')

  query = containerName.rstrip('/')
  data = "'%"+query+"%'"
  
  #print 'data', data

  argument = 'SearchQuery -glite="select dataset.logicalDatasetName, dataset.identifier where dataset.logicalDatasetName like %s" -processingStep=real_data -project=dataSuper_001' % data
  #print 'argument', argument

  maxTries = 3

  #print argument
  failures = 0
  for i in range(maxTries):
      try:
          results = amiclient.execute(argument, format='xml')
      except:
          failures += 1

  if failures == maxTries:
      print ''
      print logger.FAIL + 'is your voms proxy okay?' + logger.ENDC
      print 'Try voms-proxy-init -voms atlas'
      sys.exit(1)

  #print 'made it'

  #print results
  #txt = results.output('xml')
  #print txt
  dom = parseString(results)
  rows = dom.getElementsByTagName('row')

  #final = {}
  datasets = []
  #print 'found', len(rows)
  for row in rows:
      #print 'here', row
      fields = row.getElementsByTagName('field')
      for field in fields:
        #print field.attributes['name'].value
        if field.attributes['name'].value == 'logicalDatasetName':
          retName=field.firstChild.nodeValue
          #print retName
#
        if field.attributes['name'].value == 'identifier':
          identifier = field.firstChild.nodeValue

          #print identifier
          #Now search for all datasets that match that
          #print 'PART 2'
          #argument.append("entity=contained_dataset")
          argument = 'SearchQuery -glite="SELECT contained_dataset.contained_datasetName WHERE dataset.identifier=%s" -processingStep=real_data -project=dataSuper_001' % identifier

          results = amiclient.execute(argument, format='xml')
          #print results
          #txt = results.output('xml')
          #print txt
          dom = parseString(results)
          container = dom.getElementsByTagName('row')

          #print len(container)
          for dataset in container:
               fields = dataset.getElementsByTagName('field')
               for field in fields:
                 if field.attributes['name'].value == 'contained_datasetName':
                   #print 'hello'
                   #print field.firstChild.nodeValue
                   datasets.append(field.firstChild.nodeValue.encode('ascii','ignore') + '/')
  
  return sorted(datasets)

def askAmi(query):
  amiclient = pyAMI.client.Client('atlas')

  #swap * for % - databases
  query = query.replace('*', '%%')

  data = "'"+query+"'"

  #argument.append("entity=dataset")
  argument = 'SearchQuery -glite="SELECT dataset.logicalDatasetName, dataset.totalEvents WHERE dataset.logicalDatasetName LIKE %s"' % data

  if data.find('data') > -1:
        if data.find('data12') > -1:
            argument += ' -processingStep=real_data'
            argument += ' -project=data12_001'
        elif data.find('data11') > -1:
            argument += ' -processingStep=real_data'
            argument += ' -project=data11_001'
        else:
            argument += ' -processingStep=real_data'
            argument += ' -project=data10_001'
  else:
        argument += ' -processingStep=production'
        if data.find('mc09') > -1:
          argument += ' -project=mc09'
        if data.find('mc10') > -1:
          argument += ' -project=mc10'
        if data.find('mc11') > -1:
          argument += ' -project=mc11_001'
        if data.find('mc12') > -1:
          argument += ' -project=mc12_001'
        if data.find('mc14') > -1:
          argument += ' -project=mc14_001'

  maxTries = 3

  #print argument
  failures = 0
  for i in range(maxTries):
      try:
          results = amiclient.execute(argument, format='xml')
      except:
          failures += 1

  if failures == maxTries:
      print ''
      print logger.FAIL + 'is your voms proxy okay?' + logger.ENDC
      print 'Try voms-proxy-init -voms atlas'
      sys.exit(1)

  # print result
  #txt = results.output('xml')
  #print txt
  dom = parseString(results)
  rows = dom.getElementsByTagName('row')

  final = {}
  for row in rows:
      #print 'here', row
      fields = row.getElementsByTagName('field')
      for field in fields:
        #print field.attributes['name'].value
        if field.attributes['name'].value == 'logicalDatasetName':
          retName=field.firstChild.nodeValue

        if field.attributes['name'].value == 'totalEvents':
          retNEv = field.firstChild.nodeValue

      final[retName] = retNEv

  #unicode -> normalcode
  results = {}
  for k in final.keys():
    results[str(k)] = int(final[k])

  return results

