import jenkins
import requests

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='can.bin.hog-jenkins')
user = server.get_whoami()
version = server.get_version()
info = server.get_info()
print('\n\nHello %s from Jenkins %s' % (user['fullName'], version))

# slists all running jobs on a Jenkins server
jobs = info['jobs']
totalBuildCount = 0
print ('\n\n lists all running jobs on a Jenkins server')
for job in jobs:
    jobName = job['name']
    jobinfo = server.get_job_info(jobName)
    jobconfig = server.get_job_config(jobName)
    print ('\n\n' + jobName + ' info : ' )
    print(jobinfo)
    #print(jobconfig)
    builds = jobinfo['builds']
    print (jobName + ' build count: ' + str(len(builds)))
    totalBuildCount += len(builds)

#server.reconfig_job('Job3_test','job_config.xml')

#curl --user admin:1126805b03f6b9f87ef99a77cbc6db8e30
#-X POST http://localhost:8080/job/Job2_test/config.xml
#-H 'Content-Type: application/xml' -H 'Jenkins-Crumb: 7f5216af792aa7ebd0af95ef4c3f6aa4b87fcae210ec16625dfdb6a66178ff07'
#--data-binary "@./job_config.xml"
print ('\n\n starts a job Job2_test at a given hour at 0 1 * * *')
url = 'http://localhost:8080/job/Job2_test/config.xml'
payload = open("job_config.xml")
headers = {'content-type': 'application/xml', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers, auth = ('admin', '1126805b03f6b9f87ef99a77cbc6db8e30'))
print(r.text)
