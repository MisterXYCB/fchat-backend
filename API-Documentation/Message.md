# Message

### Send message

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **POST** | `api/message/send` | {sessionToken: String, chatId: String, messageObject: Object} | {status: String} |

```js
messageObject = {
    chatId: String,
    userId: String,
    message: String,
    timestamp: Number,
    edited: Boolean, 
    responseTo: String | null
}
```

### Get messages

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **GET** | `api/message/get` | {sessionToken: String, chatId: String} | {messageObjects: Array\<Object>} |

### Delete message

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **DELETE** | `api/message/delete` | {sessionToken: String, messageId: String} | {status: String} |

### Edit message

| Methode | URL | Payload | Response |
| --- | --- | --- | --- |
| **PUT** | `api/message/edit` | {sessionToken: String, chatId: String, messageId: String, messageObject: Object} | {status: String} |

```js
messageObject = {
    chatId: String,
    userId: String,
    message: String,
    timestamp: Number,
    edited: Boolean, 
    responseTo: String | null
}
```