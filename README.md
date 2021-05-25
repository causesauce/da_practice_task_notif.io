# da_practice_task_notif.io

### description
 The API basically works on link:https://not-io-practice-task.herokuapp.com/
 
 To open visual interface based on SWAGGER and Open API you should add /docs 
 to the root url ( or click on this link https://not-io-practice-task.herokuapp.com/docs )
 
 The API is protected and uses API Key to authenticate those who have to have 
 access to number of features

 The key is provided here: ed049313-16eb-4fc1-aa36-398d21255f76112d
 ( in case you want to use it please make sure you paste it in the place specified bellow without 
  preceding and succeeding WHITESPACES ). 
 
 To access secured endpoints please provide the given key either within a header or specifying it in the
 url. Examples:

        - Header: add such a header to your http request ![img_1.png](img_1.png)
        where instead of [YOUR API KEY] provide your API Key ( the key from the upper section for example  )
        
        - Query Parameter / URL: add you key to the end of your URL in your HTTP request as show here
        https://not-io-practice-task.herokuapp.com/messages/111?access_token=[YOUR API KEY]
        where instead of [YOUR API KEY] provide your API Key ( the key from the upper section for example )

 