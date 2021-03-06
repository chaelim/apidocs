# Get page

Retrieve the properties and relationships of a [page](../resources/page.md) object.

**Getting page content**

You can use the page's `content` endpoint to get the HTML content of a page:

```
GET /me/notes/pages/<id>/content[?includeIDs=true]
```

The `includeIDs=true` query option is used to [update pages](../api/page_update.md).

### Prerequisites
One of the following **scopes** is required to execute this API:  
Notes.Read, Notes.ReadWrite.CreatedByApp, Notes.ReadWrite, Notes.Read.All, or Notes.ReadWrite.All
### HTTP request
<!-- { "blockType": "ignored" } -->
```http
GET /me/notes/pages/<id>
GET /users/<mail>/notes/pages/<id>
GET /users/<objectId>/notes/pages/<id>
GET /groups/<objectId>/notes/pages/<id>
```
### Optional query parameters
|Name|Value|Description|
|:---------------|:--------|:-------|
|$expand|string|Comma-separated list of relationships to expand and include in the response. The default response expands `parentSection` and selects the section's `id`, `name`, and `self` properties. Valid values for pages are `parentNotebook` and `parentSection`.|
|$select|string|Comma-separated list of properties to include in the response.|

### Request headers
| Name       | Type | Description|
|:-----------|:------|:----------|
| Authorization  | string  | `Bearer <token>` A valid OAuth token provided to the app based on the user credentials and the user having authorized access. |
| Accept | string | `application/json` |

### Request body
Do not supply a request body for this method.
### Response
If successful, this method returns a `200 OK` response code and the [page](../resources/page.md) object in the response body.
### Example
##### Request
Here is an example of the request.
<!-- {
  "blockType": "request",
  "name": "get_page"
}-->
```http
GET https://graph.microsoft.com/beta/users/<objectId>/notes/pages/<id>
Authorization: Bearer <token>
Accept: application/json
```
##### Response
Here is an example of the response.
<!-- {
  "blockType": "response",
  "truncated": false,
  "@odata.type": "microsoft.graph.page"
} -->
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 391
...

{
  "title": "title-value",
  "createdByAppId": "createdByAppId-value",
  "links": {
    "oneNoteClientUrl": {
      "href": "href-value"
    },
    "oneNoteWebUrl": {
      "href": "href-value"
    }
  },
  "contentUrl": "contentUrl-value",
  "content": "content-value",
  "lastModifiedTime": "datetime-value",
  "id": "id-value",
  "self": "self-value",
  "createdTime": "datetime-value",
  "parentSection": {
    "id": "parentSection-id-value",
    "name": "parentSection-name-value",
    "self": "parentSection-self-value"
  }
}
```

<!-- uuid: 8fcb5dbc-d5aa-4681-8e31-b001d5168d79
2015-10-25 14:57:30 UTC -->
<!-- {
  "type": "#page.annotation",
  "description": "Get page",
  "keywords": "",
  "section": "documentation",
  "tocPath": ""
}-->