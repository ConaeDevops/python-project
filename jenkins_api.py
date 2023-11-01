import csv

def List_job(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins
    jen_server = jenkins.Jenkins(jenkins_url,username= jenkins_user, password=jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()

    job_stats=[]
    for i in jobs:
        jobs_name =i['name'] 
        job_url = i['url']
        job_status =i['color']
        job_stats.append([jobs_name,job_url,job_status])
    return job_stats

"""with open("example.txt", 'w') as f:
    content = "ajhvhjvjv\n"
    f.write(content)

with open("example.txt", 'r') as file:
    cont = file.read()
    print(cont)

c=List_job('http://45.33.11.12:8080', 'utrains', 'devops')
print(c)"""

data=List_job('http://45.33.11.12:8080', 'utrains', 'devops')
with open("jenkins_objective.csv", 'w') as j:
    write_row =csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])
    for item in data:
        write_row.writerow(item)
