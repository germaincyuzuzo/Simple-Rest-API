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
