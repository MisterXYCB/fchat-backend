# FChat Backend API Documentation

Apis we need:

- [ ] User
    - [ ] Register
    - [ ] Login -> Session token
    - [ ] Logout -> Delete session token
    - [ ] Update user info
    - [ ] Get user info
    - [ ] Delete user
- [ ] Chat
    - [ ] Create chat
    - [ ] add user to chat
    - [ ] add admin to chat
    - [ ] remove user from chat
    - [ ] remove admin from chat
    - [ ] delete chat
- [ ] Message
    - [ ] Send message
    - [ ] Get messages
    - [ ] Delete message
    - [ ] Edit message

## User

### Register

Username + Email + Password
->
Username, email, password, UserId
add to DB

### Login

Username / Email + Password
->
temporary session token

### Logout

Session token
->
Delete session token

### Update user info

Session token + new info
->
Updated user info

```js
userinfo = {
    username: String,
    email: String,
    password: String,
    profilePicture: String,
    bio: String,
}

```
### Get user info

Username / Email / UserId
->
Public user info

```js
userinfo = {
    username: String,
    email: String,
    profilePicture: String,
    bio: String,
}

```

### Delete user

Session token
->
Delete user from DB