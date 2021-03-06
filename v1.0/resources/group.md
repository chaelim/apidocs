# group resource type

Represents an Azure Active Directory Group. Inherits from [DirectoryObject](directoryobject.md).

### JSON representation

Here is a JSON representation of the resource

<!-- {
  "blockType": "resource",
  "optionalProperties": [
    "acceptedSenders",
    "appRoleAssignments",
    "calendar",
    "calendarView",
    "conversations",
    "createdOnBehalfOf",
    "drive",
    "events",
    "memberOf",
    "members",
    "owners",
    "photo",
    "rejectedSenders",
    "threads"
  ],
  "@odata.type": "microsoft.graph.group"
}-->

```json
{
  "acceptedSenders": [
    {
      "@odata.type": "microsoft.graph.directoryobject"
    }
  ],
  "accessType": "String-value",
  "allowExternalSenders": true,
  "appRoleAssignments": [
    {
      "@odata.type": "microsoft.graph.approleassignment"
    }
  ],
  "autoSubscribeNewMembers": true,
  "calendar": {
    "@odata.type": "microsoft.graph.calendar"
  },
  "calendarView": [
    {
      "@odata.type": "microsoft.graph.event"
    }
  ],
  "conversations": [
    {
      "@odata.type": "microsoft.graph.conversation"
    }
  ],
  "createdOnBehalfOf": {
    "@odata.type": "microsoft.graph.directoryobject"
  },
  "creationOptions": [
    "String-value"
  ],
  "deletionTimestamp": "String (timestamp)",
  "description": "String-value",
  "dirSyncEnabled": true,
  "displayName": "String-value",
  "drive": {
    "@odata.type": "microsoft.graph.drive"
  },
  "emailAddress": "String-value",
  "events": [
    {
      "@odata.type": "microsoft.graph.event"
    }
  ],
  "groupTypes": [
    "String-value"
  ],
  "isFavorite": true,
  "isPublic": true,
  "isSubscribedByMail": true,
  "lastDirSyncTime": "String (timestamp)",
  "mail": "String-value",
  "mailEnabled": true,
  "mailNickname": "String-value",
  "memberOf": [
    {
      "@odata.type": "microsoft.graph.directoryobject"
    }
  ],
  "members": [
    {
      "@odata.type": "microsoft.graph.directoryobject"
    }
  ],
  "objectId": "String-value (identifier)",
  "objectType": "String-value",
  "onPremisesSecurityIdentifier": "String-value",
  "owners": [
    {
      "@odata.type": "microsoft.graph.directoryobject"
    }
  ],
  "photo": {
    "@odata.type": "microsoft.graph.photo"
  },
  "provisioningErrors": [
    {
      "@odata.type": "microsoft.graph.provisioningerror"
    }
  ],
  "proxyAddresses": [
    "String-value"
  ],
  "rejectedSenders": [
    {
      "@odata.type": "microsoft.graph.directoryobject"
    }
  ],
  "securityEnabled": true,
  "threads": [
    {
      "@odata.type": "microsoft.graph.conversationthread"
    }
  ],
  "unseenCount": 1024
}

```
### Properties
| Property	   | Type	|Description|
|:---------------|:--------|:----------|
|accessType|String| Possible values are: `None`, `Private`, `Secret`, `Public`.|
|allowExternalSenders|Boolean||
|autoSubscribeNewMembers|Boolean||
|creationOptions|String collection||
|deletionTimestamp|DateTimeOffset|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: `'2014-01-01T00:00:00Z'`.Read-only. |
|description|String|An optional description for the group. |
|dirSyncEnabled|Boolean|**true** if this object is synced from an on-premises directory; **false** if this object was originally synced from an on-premises directory but is no longer synced; **null** if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter.|
|displayName|String|The display name for the group. This property is required when a group is created and it cannot be cleared during updates. Supports $filter and $orderby.|
|emailAddress|String||
|groupTypes|String collection||
|isFavorite|Boolean||
|isPublic|Boolean||
|isSubscribedByMail|Boolean||
|lastDirSyncTime|DateTimeOffset|Indicates the last time at which the object was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: `'2014-01-01T00:00:00Z'`. Read-only. Supports $filter.|
|mail|String|The SMTP address for the group, for example, "serviceadmins@contoso.onmicrosoft.com". Read-only. Supports $filter.|
|mailEnabled|Boolean|Specifies whether the group is mail-enabled. If the **securityEnabled** property is also **true**, the group is a mail-enabled security group; otherwise, the group is a Microsoft Exchange distribution group. Only (pure) security groups can be created using Microsoft Graph. For this reason, the property must be set **false** when creating a group and it cannot be updated using Microsoft Graph.|
|mailNickname|String|The mail alias for the group. This property must be specified when a group is created. Supports $filter.|
|objectId|String|The unique identifier for the group. Inherited from [DirectoryObject](directoryobject.md). Key. Not nullable. Read-only.|
|onPremisesSecurityIdentifier|String|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Read-only. |
|provisioningErrors|[ProvisioningError](provisioningerror.md) collection|A collection of error details that are preventing this group from being provisioned successfully. Read-only. Not nullable.            |
|proxyAddresses|String collection| The **any** operator is required for filter expressions on multi-valued properties. Read-only. Not nullable. Supports $filter. |
|securityEnabled|Boolean|Specifies whether the group is a security group. If the mailEnabled property is also true, the group is a mail-enabled security group; otherwise it is a security group. Only (pure) security groups can be created using Microsoft Graph. For this reason, the property must be set **true** when creating a group. Supports $filter.|
|unseenCount|Int32||

### Relationships
| Relationship | Type	|Description|
|:---------------|:--------|:----------|
|acceptedSenders|[DirectoryObject](directoryobject.md) collection| Read-only. Nullable.|
|calendar|[Calendar](calendar.md)| Read-only.|
|calendarView|[Event](event.md) collection| Read-only. Nullable.|
|conversations|[Conversation](conversation.md) collection| Read-only. Nullable.|
|createdOnBehalfOf|[DirectoryObject](directoryobject.md)| Read-only.|
|drive|[drive](drive.md)| Read-only.|
|events|[Event](event.md) collection| Read-only. Nullable.|
|memberOf|[DirectoryObject](directoryobject.md) collection|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|
|members|[DirectoryObject](directoryobject.md) collection| Users, contacts, and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|
|owners|[DirectoryObject](directoryobject.md) collection|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|
|photo|[Photo](photo.md)| Read-only.|
|rejectedSenders|[DirectoryObject](directoryobject.md) collection| Read-only. Nullable.|
|threads|[ConversationThread](conversationthread.md) collection| Read-only. Nullable.|

### Methods

| Method		   | Return Type	|Description|
|:---------------|:--------|:----------|
|[Get group](../api/group_get.md) | [group](group.md) |Read properties and relationships of group object.|
|[Create acceptedSender](../api/group_post_acceptedsenders.md) |[DirectoryObject](directoryobject.md)| Create a new acceptedSender by posting to the acceptedSenders collection.|
|[List acceptedSenders](../api/group_list_acceptedsenders.md) |[DirectoryObject](directoryobject.md) collection| Get a acceptedSender object collection.|
|[Create Event](../api/group_post_calendarview.md) |[Event](event.md)| Create a new Event by posting to the calendarView collection.|
|[List calendarView](../api/group_list_calendarview.md) |[Event](event.md) collection| Get a Event object collection.|
|[Create Conversation](../api/group_post_conversations.md) |[Conversation](conversation.md)| Create a new Conversation by posting to the conversations collection.|
|[List conversations](../api/group_list_conversations.md) |[Conversation](conversation.md) collection| Get a Conversation object collection.|
|[Create Event](../api/group_post_events.md) |[Event](event.md)| Create a new Event by posting to the events collection.|
|[List events](../api/group_list_events.md) |[Event](event.md) collection| Get a Event object collection.|
|[List memberOf](../api/group_list_memberof.md) |[DirectoryObject](directoryobject.md) collection| Get the groups that this group is a direct member of from the memberOf navigation property.|
|[Create member](../api/group_post_members.md) |[DirectoryObject](directoryobject.md)| Add a user, contact, or group to this group by posting to the members navigation property (supported for security groups and mail-enabled security groups only).|
|[List members](../api/group_list_members.md) |[DirectoryObject](directoryobject.md) collection| Get the users, contacts, and groups that are members of this group from the members navigation property.|
|[Create owner](../api/group_post_owners.md) |[DirectoryObject](directoryobject.md)| Create a new owner for the group by posting to the owners navigation property (supported for security groups and mail-enabled security groups only).|
|[List owners](../api/group_list_owners.md) |[DirectoryObject](directoryobject.md) collection| Get the owners of the group from the owners navigation property.|
|[Create rejectedSender](../api/group_post_rejectedsenders.md) |[DirectoryObject](directoryobject.md)| Create a new rejectedSender by posting to the rejectedSenders collection.|
|[List rejectedSenders](../api/group_list_rejectedsenders.md) |[DirectoryObject](directoryobject.md) collection| Get a rejectedSender object collection.|
|[Create thread](../api/group_post_threads.md) |[ConversationThread](conversationthread.md)| Create a new thread by posting to the threads collection.|
|[List threads](../api/group_list_threads.md) |[ConversationThread](conversationthread.md) collection| Get a thread object collection.|
|[Update](../api/group_update.md) | [group](group.md)	|Update group object. |
|[Delete](../api/group_delete.md) | None |Delete group object. |
|[addFavorite](../api/group_addfavorite.md)|None||
|[checkMemberGroups](../api/group_checkmembergroups.md)|String collection|Check for membership in a list of groups. The check is transitive.|
|[getMemberGroups](../api/group_getmembergroups.md)|String collection|Return all the groups that the group is a member of. The check is transitive.|
|[getMemberObjects](../api/group_getmemberobjects.md)|String collection|Return all of the groups that the group is a member of. The check is transitive. |
|[removeFavorite](../api/group_removefavorite.md)|None||
|[resetUnseenCount](../api/group_resetunseencount.md)|None||
|[subscribeByMail](../api/group_subscribebymail.md)|None||
|[unsubscribeByMail](../api/group_unsubscribebymail.md)|None||

<!-- uuid: 8fcb5dbc-d5aa-4681-8e31-b001d5168d79
2015-10-25 14:57:30 UTC -->
<!-- {
  "type": "#page.annotation",
  "description": "group resource",
  "keywords": "",
  "section": "documentation",
  "tocPath": ""
}-->