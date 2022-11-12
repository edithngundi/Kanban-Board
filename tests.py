import unittest
import requests



class AppTest(unittest.TestCase):

    #test ids
    getId = 3
    delId = 1

    #app url
    APP_URL = 'http://127.0.0.1:5000/'
    def test_1_add_new_task_url(self):
        r = requests.get(self.APP_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 1 COMPLETE")

    #update url
    UPDATE_URL = ('{}/update/'+str(getId)).format(APP_URL)
    def test_2_update_url(self):
        r = requests.get(self.UPDATE_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 2 COMPLETE")

    #move_to_todo url
    MOVE_TO_TODO_URL = ('{}/move_to_todo/'+str(getId)).format(APP_URL)
    def test_3_move_to_todo_url(self):
        r = requests.get(self.MOVE_TO_TODO_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 3 COMPLETE")

    #move_to_doing url 
    MOVE_TO_DOING_URL = ('{}/move_to_doing/'+str(getId)).format(APP_URL)
    def test_4_move_to_doing_url(self):
        r = requests.get(self.MOVE_TO_DOING_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 4 COMPLETE")

    #move_to_done url
    MOVE_TO_DONE_URL = ('{}/move_to_done/'+str(getId)).format(APP_URL)
    def test_5_move_to_done_url(self):
        r = requests.get(self.MOVE_TO_DONE_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 5 COMPLETE")

    #delete url
    DELETE_URL = ('{}/delete/'+str(delId)).format(APP_URL)
    def test_6_delete_url(self):
        r = requests.get(self.DELETE_URL)
        self.assertEqual(r.status_code, 200)
        print("TEST 6 COMPLETE")

if __name__ == '__main__':
    unittest.main()
