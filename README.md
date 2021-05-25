# da_practice_task_notif.io


## description
 The API basically works on link: https://not-io-practice-task.herokuapp.com/
 
 To open visual interface based on SWAGGER and Open API you should add /docs 
 to the root url ( or click on this link https://not-io-practice-task.herokuapp.com/docs )
 
 The API is protected and uses API Key to authenticate those who have to have 
 access to number of features

 The key is provided here: ed049313-16eb-4fc1-aa36-398d21255f76112d
 ( in case you want to use it please make sure you paste it in the place specified bellow without 
  preceding and succeeding WHITESPACES ). 
 
 To access secured endpoints please provide the given key either within a header or specifying it in the
 url. Examples:

        - Header: add such a header to your http request <access_token : [YOUR API KEY]>
        where instead of [YOUR API KEY] provide your API Key ( the key from the upper section for example  )
        
        - Query Parameter / URL: add you key to the end of your URL in your HTTP request as show here
        https://not-io-practice-task.herokuapp.com/messages/[SOME PARAMETER]?access_token=[YOUR API KEY]
        where instead of [YOUR API KEY] provide your API Key ( the key from the upper section for example )

        I prefere and recommend to use 'the header' method not to reveal the key in the URL.

In total there are 6 endpoints related to the API.

1. GET /messages  -  returns list of all messages and status code 200 (body and counter for every message). 
The counter of all the messages increases by 1 every time the method is called.


2. GET /messages/with-id  -  returns list of all messages with their ids and status code 200 (id, body, counter for every message).
If message exists, its counter is increased by 1 every time this message is retrieved by this method.


3. GET /messages/{id_message}  -  returns a message with a specified id and status code 200 or 404 exception with details if message was not found
   (id, body for every message). If message exists, its counter is increased by 1 every time this message is retrieved by this method.
   

4. POST /messages  -  receives a message in JSON body; returns 201 or 400 message in case format is wrong


5. PUT /messages/{id_message}  -  receives a message in JSON body and id of the message to be modified; returns
   status code 204 and details with modified message body in case the message was modified successfully, otherwise returns status code 404


6. DELETE /messages/{id_message}  -  simply takes id of a message, returns status code 204 in case message was deleted successfully,
   otherwise returns status code 404


## Specification

##### All the following examples are done with using API Key in header
<br>
1. GET /messages [UNSECURED]
    <br><br>
    Link:  https://not-io-practice-task.herokuapp.com/messages


    METHOD: GET

    Returns: all messages without their IDs in JSON Format along with status code 200 (if there are no messages return an empty list)
   
    Example response: [{"body":"11","counter":4},{"body":"Hello world","counter":8}]


2. GET /messages/with-id [UNSECURED]
    <br><br>
    Link:   https://not-io-practice-task.herokuapp.com/messages/with-id

     
    METHOD: GET
   
    Return: the same as previous, but including an IDs of the messages; returns status code 200

    Response example: [{"id_message":1,"body":"11","counter":6},{"id_message":2,"body":"How is the weather today?","counter":1},{"id_message":3,"body":"Night sky is such a mystery","counter":2}]

3. GET /messages/{id_message} [UNSECURED]
    <br><br>
    Link: this link should be appended with ID of the message you want to retrieve https://not-io-practice-task.herokuapp.com/messages


    METHOD: GET

    Returns: single message in JSON format along with status code 200, or status code 404 if the message was not found
  
    Request example: https://not-io-practice-task.herokuapp.com/messages/3

    Response example: {"body":"Night sky is such a mystery","counter":1} 

4. POST /messages [SECURED] ( needs authentication to impact the data )
returns status code 401 if user is not authenticated
   <br><br>
    Link: https://not-io-practice-task.herokuapp.com/messages/


    METHOD: POST

    Accepts in body: POST request with JSON form in body to add new message. Form should be as follows
              {
                 "body" : "[YOUR MESSAGE]"
              }
              otherwise it will be rejected.
   
    Performs: validates the input and creates an instance of a message with a unique id and its own counter
               if validation passed. Body should be between 1 and 160 characters.

    Returns: status code 201 and a small piece of information about the created message, or status code 404 if message with the id doesn't exist

    Request example: {
                          "body" : "How is it going?"
                      }

    Response example:  "message with id 4 has been created"

5. PUT /messages/{id_message} [SECURED] ( needs authentication to impact the data ) 
   returns status code 401 if user is not authenticated
    <br><br>
    Link: this link should be appended with ID of the message you want to update https://not-io-practice-task.herokuapp.com/messages/   

    
    METHOD: PUT    

    Accepts in body: PUT request with JSON form in body to update new message. Form should be as follows
                  {
                     "body" : "[YOUR MESSAGE]"
                  }
                  otherwise it will be rejected.
   
    Performs: validates the input and updates the instance of a message with
               if validation passed. Body should be between 1 and 160 characters.

    Returns: status code 204 and a small piece of information about the updated message, or status code 404 if message with the id doesn't exist

    Request example: https://not-io-practice-task.herokuapp.com/messages/4
                      {
                          "body" : "Want some changes"
                      }

    Response example:  {"detail":"message with the id 4 has been modified","message":{"body":"Want some changes","counter":0}}
   


6.  DELETE /messages/{id_message} [SECURED] ( needs authentication to impact the data ) 
   returns status code 401 if user is not authenticated
    <br><br>
    Link: this link should be appended with ID of the message you want to delete https://not-io-practice-task.herokuapp.com/messages/   
    

    METHOD: PUT

    Returns: status code 204 and a small smail piece of information, or status code 404 if message with the id doesn't exist

    Request example: https://not-io-practice-task.herokuapp.com/messages/4

    Response example:  {"details":"success"}
    