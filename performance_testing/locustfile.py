from locust import task, HttpUser
import random

class MemeUser(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post('/authorize', json={'name': 'Eugeny'})
        self.token = response.json()['token']

    @task(1) # indicates how often in comparison to other tasks it will run
    def get_all_memes(self):
        self.client.get('/meme', headers={'Authorization': self.token})

    # indicates how often in comparison to other tasks it will run.
    # @task(3) is 3x times mre likely to run than @ task(1)
    @task(3)
    def get_one_meme(self):
        self.client.get(f'/meme/{random.choice([21, 29, 276, 239])}', headers={'Authorization': self.token})