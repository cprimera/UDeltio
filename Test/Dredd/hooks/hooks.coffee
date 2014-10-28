{before, after} = require 'hooks'
{beforeAll, afterAll} = require 'hooks'
{spawn} = require 'child_process'

token = ""

beforeAll (done) ->
	reset = spawn './scripts/reset_db.sh'
	reset.on 'close', (code) ->
		done()

after "OAuth > Access Token > Get Access Token", (transaction) ->
	token = 'Bearer ' + JSON.parse(transaction.real.body).access_token

before "Board > Board > Get Board", (transaction) ->
	transaction.request.headers.Authorization = token

before "Board > Board > Update Board", (transaction) ->
	transaction.request.headers.Authorization = token

before "Board > Board > Delete Board", (transaction) ->
	transaction.request.headers.Authorization = token

before "Board > Board's Posts > List All Posts", (transaction) ->
	transaction.request.headers.Authorization = token

before "Board > Boards Collection > List all Boards", (transaction) ->
	transaction.request.headers.Authorization = token

before "Board > Boards Collection > Create a Board", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User > Get User", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User > Update User", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User > Delete User", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User's Posts > List All Posts", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User Collection > Retrieve All Users", (transaction) ->
	transaction.request.headers.Authorization = token

before "User > User Collection > Create new User", (transaction) ->
	transaction.request.headers.Authorization = token

before "Post > Post > Get Post", (transaction) ->
	transaction.request.headers.Authorization = token

before "Post > Post > Update Post", (transaction) ->
	transaction.request.headers.Authorization = token

before "Post > Post > Delete Post", (transaction) ->
	# Skip this transaction since the post will have already been
	# deleted by the User/Board deletion
	transaction.skip = true
	# transaction.request.headers.Authorization = token

before "Post > Posts Collection > List All Posts", (transaction) ->
	transaction.request.headers.Authorization = token

before "Post > Posts Collection > Create a Post", (transaction) ->
	transaction.request.headers.Authorization = token

before "Tag > Tag > Get Tag", (transaction) ->
	transaction.request.headers.Authorization = token

before "Tag > Tag > Delete Tag", (transaction) ->
	transaction.request.headers.Authorization = token

before "Tag > Tag Collection > Retrieve All Tags", (transaction) ->
	transaction.request.headers.Authorization = token

before "Tag > Tag Collection > Create new Tag", (transaction) ->
	transaction.request.headers.Authorization = token

afterAll (done) ->
	reset = spawn './scripts/reset_db.sh'
	reset.on 'close', (code) ->
		done()
