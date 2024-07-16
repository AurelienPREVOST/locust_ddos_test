from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about")

# to launch it :
# C:\Users\aurelien.PREVOST\Documents\code\fake_ddos> python -m locust -f locustfile.py --host=http://siteatester.com
# @task represent url + post / get ...whatever .. to path(s)