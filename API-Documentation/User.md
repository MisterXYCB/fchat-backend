# User

### Register user

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **POST** | `api/user/register` | {username: String, email: String, password: String} | {status: String} |

```js
new DB_User = {
    "username": String,
    "email": String,
    "password": String,
    "profilePicture": String,
    "bio": String
}
```

### Login

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **POST** | `api/user/login` | {username: String, password: String} | {sessionToken: String} |

### Logout

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **POST** | `api/user/logout` | {sessionToken: String} | {status: String} |

### Update user info

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/user/update` | {sessionToken: String, userInfo: Object} | {status: String} |

```js
userInfo = {
    username: String,
    email: String,
    password: String,
    profilePicture: String,
    bio: String,
}
```
### Get user info

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **GET** | `api/user/get` | {sessionToken: String} | {userInfo: Object} |

```js
userInfo = {
    username: String,
    email: String,
    profilePicture: String,
    bio: String,
}
```

### Delete user

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **DELETE** | `api/user/delete` | {sessionToken: String} | {status: String} |