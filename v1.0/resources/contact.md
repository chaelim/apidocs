# contact resource type

A contact is an item in Outlook where you can organize and save information about the people and organizations you communicate with. Contacts are contained in contact folders.


### JSON representation

Here is a JSON representation of the resource

<!-- {
  "blockType": "resource",
  "optionalProperties": [
    "photo"
  ],
  "@odata.type": "microsoft.graph.contact"
}-->

```json
{
  "assistantName": "String-value",
  "birthday": "String (timestamp)",
  "businessAddress": {
    "@odata.type": "microsoft.graph.physicaladdress"
  },
  "businessHomePage": "String-value",
  "businessPhones": [
    "String-value"
  ],
  "categories": [
    "String-value"
  ],
  "changeKey": "String-value",
  "children": [
    "String-value"
  ],
  "companyName": "String-value",
  "createdDateTime": "String (timestamp)",
  "department": "String-value",
  "displayName": "String-value",
  "emailAddresses": [
    {
      "@odata.type": "microsoft.graph.emailaddress"
    }
  ],
  "fileAs": "String-value",
  "generation": "String-value",
  "givenName": "String-value",
  "homeAddress": {
    "@odata.type": "microsoft.graph.physicaladdress"
  },
  "homePhones": [
    "String-value"
  ],
  "id": "String-value (identifier)",
  "imAddresses": [
    "String-value"
  ],
  "initials": "String-value",
  "jobTitle": "String-value",
  "lastModifiedDateTime": "String (timestamp)",
  "manager": "String-value",
  "middleName": "String-value",
  "mobilePhone1": "String-value",
  "nickName": "String-value",
  "officeLocation": "String-value",
  "otherAddress": {
    "@odata.type": "microsoft.graph.physicaladdress"
  },
  "parentFolderId": "String-value",
  "personalNotes": "String-value",
  "photo": {
    "@odata.type": "microsoft.graph.photo"
  },
  "profession": "String-value",
  "spouseName": "String-value",
  "surname": "String-value",
  "title": "String-value",
  "yomiCompanyName": "String-value",
  "yomiGivenName": "String-value",
  "yomiSurname": "String-value"
}

```
### Properties
| Property	   | Type	|Description|
|:---------------|:--------|:----------|
|assistantName|String|The name of the contact's assistant.|
|birthday|DateTimeOffset|The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: `'2014-01-01T00:00:00Z'`|
|businessAddress|[PhysicalAddress](physicaladdress.md)|The contact's business address.|
|businessHomePage|String|The business home page of the contact.|
|businessPhones|String collection|The contact's business phone numbers.|
|categories|String collection|The categories associated with the contact.|
|changeKey|String|Identifies the version of the contact. Every time the contact is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object.|
|children|String collection|The names of the contact's children.|
|companyName|String|The name of the contact's company.|
|createdDateTime|DateTimeOffset|The time the contact was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: `'2014-01-01T00:00:00Z'`|
|department|String|The contact's department.|
|displayName|String|The contact's display name.|
|emailAddresses|[EmailAddress](emailaddress.md) collection|The contact's email addresses.|
|fileAs|String|The name the contact is filed under.|
|generation|String|The contact's generation.|
|givenName|String|The contact's given name.|
|homeAddress|[PhysicalAddress](physicaladdress.md)|The contact's home address.|
|homePhones|String collection|The contact's home phone numbers.|
|id|String|The contact's unique identifier. Read-only.|
|imAddresses|String collection|The contact's instant messaging (IM) addresses.|
|initials|String|The contact's initials.|
|jobTitle|String|The contact’s job title.|
|lastModifiedDateTime|DateTimeOffset|The time the contact was modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: `'2014-01-01T00:00:00Z'`|
|manager|String|The name of the contact's manager.
|middleName|String|The contact's middle name.|
|mobilePhone1|String|The contact's mobile phone number.|
|nickName|String|The contact's nickname.|
|officeLocation|String|The location of the contact's office.|
|otherAddress|[PhysicalAddress](physicaladdress.md)|Other addresses for the contact.|
|parentFolderId|String|The ID of the contact's parent folder.|
|personalNotes|String|The user's notes about the contact.|
|profession|String|The contact's profession.|
|spouseName|String|The name of the contact's spouse.|
|surname|String|The contact's surname.|
|title|String|The contact's title.|
|yomiCompanyName|String|The phonetic Japanese company name of the contact.|
|yomiGivenName|String|The phonetic Japanese given name (first name) of the contact.|
|yomiSurname|String|The phonetic Japanese surname (last name)  of the contact.|

### Relationships
| Relationship | Type	|Description|
|:---------------|:--------|:----------|
|photo|[Photo](photo.md)| Optional contact picture. You can get or set a photo for a contact.|

### Methods

| Method		   | Return Type	|Description|
|:---------------|:--------|:----------|
|[Get contact](../api/contact_get.md) | [contact](contact.md) |Read properties and relationships of contact object.|
|[Create](../api/user_post_contacts.md) | [contact](contact.md) |Add a contact to the root Contacts folder or to the contacts endpoint of another contact folder.|
|[Update](../api/contact_update.md) | [contact](contact.md)	|Update contact object. |
|[Delete](../api/contact_delete.md) | None |Delete contact object. |

<!-- uuid: 8fcb5dbc-d5aa-4681-8e31-b001d5168d79
2015-10-25 14:57:30 UTC -->
<!-- {
  "type": "#page.annotation",
  "description": "contact resource",
  "keywords": "",
  "section": "documentation",
  "tocPath": ""
}-->