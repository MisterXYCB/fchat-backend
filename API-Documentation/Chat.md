# Chat

### Create chat

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **POST** | `api/chat/create` | {sessionToken: String, chatInfo: Object} | {status: String} |

```js
chatInfo = {
    name: String,
    description: String,
    profilePicture: String,
    users: Array<String>,
    admins: Array<String>
}
```

### Update chat

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/chat/update` | {sessionToken: String, chatInfo: Object} | {status: String} |

```js
chatInfo = {
    chatId: String,
    name: String,
    description: String,
    profilePicture: String,
    users: Array<String>,
    admins: Array<String>
}
```

### add user

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/chat/admin-user` | {sessionToken: String, chatId: String, userId: String} | {status: String} |

### add admin

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/chat/add-admin` | {sessionToken: String, chatId: String, userId: String} | {status: String} |

### remove user

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/chat/remove-user` | {sessionToken: String, chatId: String, userId: String} | {status: String} |

### remove admin

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/chat/remove-admin` | {sessionToken: String, chatId: String, userId: String} | {status: String} |

### delete chat

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **DELETE** | `api/chat/delete` | {sessionToken: String, chatId: String} | {status: String} |