# List calendarGroups

Get the user's calendar groups.
### Prerequisites
One of the following **scopes** is required to execute this API: 
*Calendars.Read; Calendars.ReadWrite*
### HTTP request
<!-- { "blockType": "ignored" } -->
```http
GET /users/<objectId>/calendarGroups
GET /users/<userPrincipalName>/calendarGroups
```
### Optional query parameters
|Name|Value|Description|
|:---------------|:--------|:-------|
|$count|none|The count of related entities can be requested by specifying the $count query option.|
|$expand|string|Comma-separated list of relationships to expand and include in the response. See relationships table of [CalendarGroup](../resources/calendargroup.md) for supported names. |
|$filter|string|Filter string that lets you filter the response based on a set of criteria.|
|$orderby|string|Comma-separated list of properties that are used to sort the order of items in the response collection.|
|$select|string|Comma-separated list of properties to include in the response.|
|$skip|int|The number of items to skip in a result set.|
|$skipToken|string|Paging token that is used to get the next set of results.|
|$top|int|The number of items to return in a result set.|

### Request headers
| Header       | Value |
|:---------------|:--------|
| Authorization  | Bearer %token%  |
| Content-Type  | application/json  |

### Request body
Do not supply a request body for this method.
### Response
If successful, this method returns a `200 OK` response code and collection of [CalendarGroup](../resources/calendargroup.md) objects in the response body.
### Example
##### Request
Here is an example of the request.
<!-- {
  "blockType": "request",
  "name": "get_calendargroups"
}-->
```http
GET https://graph.microsoft.com/v1.0/users/<objectId>/calendarGroups
```
##### Response
Here is an example of the response.
<!-- {
  "blockType": "response",
  "truncated": false,
  "@odata.type": "microsoft.graph.calendargroup",
  "isCollection": true
} -->
```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "value": [
    {
      "id": "id-value",
      "name": "My Calendars",
      "classId": "0006f0b7-0000-0000-c000-000000000046",
      "changeKey": "TEeu8sNApk+MdJFYEFB/9wABwoTe4A=="
    },
    {
      "id": "AAMkADA...PAAA=",
      "name": "Other Calendars",
      "classId": "0006f0b8-0000-0000-c000-000000000046",
      "changeKey": "TEeu8sNApk+MdJFYEFB/9wABwoTe4g=="
    }
  ]
}
```

<!-- uuid: 8fcb5dbc-d5aa-4681-8e31-b001d5168d79
2015-10-25 14:57:30 UTC -->
<!-- {
  "type": "#page.annotation",
  "description": "List calendarGroups",
  "keywords": "",
  "section": "documentation",
  "tocPath": ""
}-->