# Delete contact

Delete contact.
### Prerequisites
The following **scopes** are required to execute this API: 
*Contacts.ReadWrite*
### HTTP request
<!-- { "blockType": "ignored" } -->
```http
DELETE /me/contacts/<id>
DELETE /users/<objectId>/contacts/<id>
DELETE /users/<userPrincipalName>/contacts/<id>
DELETE /me/contactFolders/<contactFolderId>/contacts/<id>
DELETE /users/<objectId>/contactFolders/<contactFolderId>/contacts/<id>
DELETE /users/<userPrincipalName>/contactFolders/<contactFolderId>/contacts/<id>

```
### Request headers
| Header       | Value |
|:---------------|:--------|
| Authorization  | Bearer %token%  |

### Request body
Do not supply a request body for this method.


### Response
If successful, this method returns `204, No Content` response code. It does not return anything in the response body.

### Example
##### Request
Here is an example of the request.
<!-- {
  "blockType": "request",
  "name": "delete_contact"
}-->
```http
DELETE https://graph.microsoft.com/v1.0/users/<objectId>/contacts/<id>
```
##### Response
Here is an example of the response.
<!-- {
  "blockType": "response",
  "truncated": false
} -->
```http
HTTP/1.1 204 No Content
```

<!-- uuid: 8fcb5dbc-d5aa-4681-8e31-b001d5168d79
2015-10-25 14:57:30 UTC -->
<!-- {
  "type": "#page.annotation",
  "description": "Delete contact",
  "keywords": "",
  "section": "documentation",
  "tocPath": ""
}-->