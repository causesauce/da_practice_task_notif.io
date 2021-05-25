import json

import pytest
import requests


# testing "/messages/{message_id} endpoint with nonexistent id
def test_get_by_id():
    url = "https://not-io-practice-task.herokuapp.com/messages/1000"
    response = requests.get(url=url)
    assert response.status_code == 404


# -----------------------------------------testing secure endpoints for actual security----------------------------
def test_post_message_with_no_access_token():
    url = "https://not-io-practice-task.herokuapp.com/messages"
    # message with id {message_obj.id_message} has been created
    message_data = """{"body": "message_trial"}"""
    response = requests.post(url, message_data)
    assert response.status_code == 401


def test_put_message_with_no_access_token():
    url = "https://not-io-practice-task.herokuapp.com/messages/1"
    # message with id {message_obj.id_message} has been created
    message_data = """{"body": "message_trial"}"""
    response = requests.put(url, message_data)
    assert response.status_code == 401


def test_delete_message_with_no_access_token():
    url = "https://not-io-practice-task.herokuapp.com/messages/1"

    response = requests.delete(url)
    assert response.status_code == 401


# -------------------------------testing C,U,D secure methods from CRUD with access token----------------------------
def test_post_put_delete_message():
    # post
    url = "https://not-io-practice-task.herokuapp.com/messages"
    headers = {'access_token': 'ed049313-16eb-4fc1-aa36-398d21255f76112d'}
    message_data = """{"body": "message_trial"}"""
    response = requests.post(url, message_data, headers=headers)
    assert response.status_code == 201

    # put
    # "message with id {message_obj.id_message} has been created"
    created_message_id = int(response.text.split(" ")[3])

    message_data = """{"body": "message_trial_changed"}"""
    url += '/'+str(created_message_id)
    response = requests.put(url, message_data, headers=headers)
    #assert response.status_code == 204
    assert json.loads(response.content) == 'dwqdqwdwqdqwdqwdqw'
    assert json.loads(response.text)["detail"] == f"message with the id {created_message_id} has been modified"

    # delete
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204

    # get
    response = requests.get(url=url)
    assert response.status_code == 404

