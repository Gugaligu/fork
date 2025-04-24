from types import new_class

from DB.json_DB import JSON
from integrate_cloudflare.api_cloudflare import CloudflareAISolver
from online_json.mockapi import MockAPIClient


class TasksCRUD:
    @staticmethod
    def get_tasks():
        data_obj = JSON()
        return data_obj.get_all_task()

    @staticmethod
    def create_new_task(task_name, status):
        task_name = task_name + CloudflareAISolver().get_solution(task_name)

        data_obj = JSON()
        new_data = data_obj.create_task(task_name, status)
        print(new_data)
        MockAPIClient().new_json(new_data)
        return new_data

    @staticmethod
    def update_task(task_id, new_name_task, new_status):
        data_obj = JSON()
        task_id = str(task_id)
        if task_id in data_obj.get_all_task():
            flag_new = False
            if new_name_task is not None:
                new_name_task = new_name_task + CloudflareAISolver().get_solution(new_name_task)
                data_obj.update_name_task(task_id, new_name_task)
                flag_new = True
            if new_status is not None:
                data_obj.update_status(task_id, new_status)
                flag_new = True

            if flag_new == True:
                MockAPIClient().new_json(data_obj.get_all_task())

        return data_obj.get_all_task()

    @staticmethod
    def delete_task(task_id):
        task_id = str(task_id)
        data_obj = JSON()
        data_obj.delete_task(task_id)

        MockAPIClient().new_json(data_obj.get_all_task())
        return data_obj.get_all_task()
