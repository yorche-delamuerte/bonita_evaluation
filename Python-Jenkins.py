import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='can.bin.hog-jenkins')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


# get all jobs from the specific view
jobs = server.get_jobs()
print(jobs)


print("Hello, World!")
