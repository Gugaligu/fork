from DB.json_DB import JSON


class TasksCRUD:
    @staticmethod
    def get_tasks():
        data=JSON()
        return data.get_all_task()

    @staticmethod
    def create_new_task(task_name,status):
        data = JSON()
        return data.create_task(task_name,status)

    @staticmethod
    def update_task(task_id,new_name_task,new_status):
        data = JSON()
        task_id=str(task_id)
        if task_id in data.get_all_task():
            if new_name_task is not None:
                data.update_name_task(task_id,new_name_task)
            if new_status is not None:
                data.update_status(task_id,new_status)
        return data.get_all_task()

    @staticmethod
    def delete_task(task_id):
        task_id=str(task_id)
        data = JSON()
        data.delete_task(task_id)
        return data.get_all_task()
