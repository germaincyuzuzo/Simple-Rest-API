My simple rest API using Python and Flask

This API is designed such that a user manually makes a request to either of two endpoints.

- If the user makes a request to POST/users: then the inserted data will be stored as json data in an in-memory storage
- If the user makes a request to GET/users/user_id: then the specified user id will be located in the in-memory storage
and it returns the data associated with that very user_id.

If at somepoint the user makes a wrong request, the validations will have to return an error to the user.
Wrong requests include:

- Trying to insert a user with a missing credential, the app will return an error informing the user the mistake in their requesr.
- Trying to access data that is not yet in the in-memory storage. The program immediately returns the 404 error telling the user that the request has reached the
server but the data they are trying to access is not found.

Example Demo (Using Curl)

INSERTING USER USING THE POST ENDPOINT (Instantly shows the inserted data upon success)

germain@fedora:~/Works/python/projects/Simple-Rest-API$ curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Germain", "email": "germain@gmail.com"}'
{
  "email": "germain@gmail.com",
  "id": "f2ab35f8-7417-4af2-85f8-996814ffa210",
  "name": "Germain"
}

TRYING TO INSERT USER WITH SOME MISSING CREDENTIALS (RETURNS AN ERROR)

germain@fedora:~/Works/python/projects/Simple-Rest-API$ curl -X POST http://localhost:5000/users      -H "Content-Type: application/json"      -d '{"name": "Alice"}'
{
  "error": "Missing 'name' or 'email' in request"
}


GETTING USER USING THE GET ENDPOINT

germain@fedora:~/Works/python/projects/Simple-Rest-API$ curl http://localhost:5000/users/f2ab35f8-7417-4af2-85f8-996814ffa210
{
  "email": "germain@gmail.com",
  "id": "f2ab35f8-7417-4af2-85f8-996814ffa210",
  "name": "Germain"
}

TRYING TO GET A USER WITH AN ID THAT DOESN'T EXIST (RETURNS AN ERROR)

germain@fedora:~/Works/python/projects/Simple-Rest-API$ curl http://localhost:5000/users/f2ab35f8-7417-4af2-85f8-996814ffa210f
{
  "error": "User is not found"
}
